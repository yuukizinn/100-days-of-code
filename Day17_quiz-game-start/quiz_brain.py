class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, concurrent_question):
        if str.lower(answer) == str.lower(concurrent_question):
            print("nice")
            self.score += 1
        else:
            print("wrong")
        print(f"the collect answer is {answer}")
        print(f"your current score is {self.score}/{self.question_number}")

    def next_question(self):
        concurrent_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q{self.question_number}: {concurrent_question.text} select "True" or "False"\n')
        self.check_answer(answer, concurrent_question.answer)
