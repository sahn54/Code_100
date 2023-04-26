from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    new_text = question['question']
    new_answer = question['correct_answer']
    new_question = Question(new_text, new_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

quiz.end_of_quiz()
