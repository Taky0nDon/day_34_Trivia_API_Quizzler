import data
from quiz_brain import QuizBrain
import ui


quiz = QuizBrain(data.give_questions_to_user(category_id=None))
quiz_ui = ui.QuizInterface(quiz)  # passing the QuizBrain instance to the quiz_ui
