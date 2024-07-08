class QuestionBrain:
    def __init__(self, q_list):
        self.q_list =q_list
        self.score=0
        self.q_number =0

    def still_has_question(self):
        if self.q_number < len(self.q_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number +=1

        user_ans =input(f"Q{self.q_number} : {current_question.q_text} (True/False)")
        correct_ans =current_question.q_ans
        self.check_ans(user_ans, correct_ans)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score +=1
            print(f"Score is {self.score}/{self.q_number}")  
            return True
        else:
            print(f"Score is {self.score}/{self.q_number}")  
            return False
            
                
