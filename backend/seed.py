from backend.app import app, db
from backend.models import Quiz, Question

def seed_data():
    with app.app_context():
        print("Using DB:", app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()

        # Prevent duplicate seeding
        if Quiz.query.count() > 0:
            print("Database already has quizzes, skipping seeding")
            return

        # Define quizzes and their Aquestions
        quizzes = [
            {
                "title": "General Knowledge Quiz",
                "questions": [
                    {
                        "question": "What is the capital of France?",
                        "options": ["Berlin", "Madrid", "Paris", "Rome"],
                        "answer": "Paris"
                    },
                    {
                        "question": "Which planet is known as the Red Planet?",
                        "options": ["Earth", "Mars", "Jupiter", "Venus"],
                        "answer": "Mars"
                    }
                ]
            },
            {
                "title": "Science Quiz",
                "questions": [
                    {
                        "question": "What is the chemical symbol for water?",
                        "options": ["O2", "H2O", "CO2", "HO"],
                        "answer": "H2O"
                    },
                    {
                        "question": "How many bones are in the adult human body?",
                        "options": ["206", "201", "210", "215"],
                        "answer": "206"
                    }
                ]
            },
            {
                "title": "Math Quiz",
                "questions": [
                    {
                        "question": "What is 7 × 8?",
                        "options": ["54", "56", "64", "49"],
                        "answer": "56"
                    },
                    {
                        "question": "What is the square root of 144?",
                        "options": ["12", "14", "16", "10"],
                        "answer": "12"
                    }
                ]
            }
        ]

        # Seed each quiz and its questions
        for qz in quizzes:
            quiz = Quiz(title=qz["title"])
            db.session.add(quiz)
            db.session.flush()  # ensures quiz.id is available

            for q in qz["questions"]:
                question = Question(
                    quiz_id=quiz.id,
                    question_text=q["question"],
                    options=q["options"],
                    correct_answer=q["answer"]
                )
                db.session.add(question)

        db.session.commit()
        print(" Database seeded with multiple quizzes and questions")

if __name__ == "__main__":
    seed_data()
