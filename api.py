from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from models import db, Task

import pandas as pd
import numpy as np

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    tasks_list = [{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'priority': task.priority,
        'status': task.status,
        'created_date': task.created_date.isoformat()
    } for task in tasks]
    return jsonify(tasks_list), 200

@api_bp.route('/tasks', methods=['POST'])
@login_required
def add_task():
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400

    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        priority=data.get('priority', 'Medium'),
        status=data.get('status', 'Pending'),
        user_id=current_user.id
    )
    db.session.add(new_task)
    db.session.commit()

    from app import socketio
    socketio.emit('task_updated', {'message': 'New task added'}, room=None)
    
    return jsonify({
        'id': new_task.id,
        'message': 'Task created successfully'
    }), 201

@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'priority' in data:
        task.priority = data['priority']
    if 'status' in data:
        task.status = data['status']

    db.session.commit()

    from app import socketio
    socketio.emit('task_updated', {'message': 'Task updated'}, room=None)

    return jsonify({'message': 'Task updated successfully'}), 200

@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()

    from app import socketio
    socketio.emit('task_updated', {'message': 'Task deleted'}, room=None)

    return jsonify({'message': 'Task deleted successfully'}), 200

@api_bp.route('/analytics', methods=['GET'])
@login_required
def get_analytics():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    if not tasks:
        return jsonify({
            'total_tasks': 0,
            'completed_tasks': 0,
            'pending_tasks': 0,
            'completion_percentage': 0.0
        }), 200

    data = [{
        'id': task.id,
        'status': task.status
    } for task in tasks]

    # Use Pandas for Analytics
    df = pd.DataFrame(data)
    total_tasks = int(df['id'].count())
    
    # Use numpy where and sum to calculate
    df['is_completed'] = np.where(df['status'] == 'Completed', 1, 0)
    completed_tasks = int(df['is_completed'].sum())
    pending_tasks = total_tasks - completed_tasks
    
    completion_percentage = float(np.round((completed_tasks / total_tasks) * 100, 2)) if total_tasks > 0 else 0.0

    return jsonify({
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'completion_percentage': completion_percentage
    }), 200
