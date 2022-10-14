from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

qb = []

for i in question_data:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    newq = Question(question_text, question_answer)
    qb.append(newq)

q = QuizBrain(qb)
while q.qnsrem():
    q.nextquestion()

print("Final score", q.score, "/", q.qno)
