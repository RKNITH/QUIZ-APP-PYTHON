
from question_model import Question
from question_brain import QuestionBrain
from data import question_data


question_bank =[]
for data in question_data:
     q_text= data["text"]
     q_ans =data["answer"]
     new_question =Question(q_text, q_ans)
     question_bank.append(new_question)


quiz =QuestionBrain(question_bank)

while quiz.still_has_question():
     quiz.next_question()
     
    
   
