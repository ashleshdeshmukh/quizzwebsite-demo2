from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models import db, Quiz, Question

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/create', methods=['POST'])
@jwt_required()
def create_quiz():
    identity = get_jwt_identity()
    if not identity['is_admin']:
        return jsonify(message="Admins Only"), 403

    data = request.json
    new_quiz = Quiz(title=data['title'])
    db.session.add(new_quiz)
    db.session.flush()

    for q in data['questions']:
        question = Question(
            quiz_id=new_quiz.id,
            question_text=q['question'],
            options=q['options'],
            correct_answer=q['answer']
        )
        db.session.add(question)

    db.session.commit()
    return jsonify(message='Quiz created')