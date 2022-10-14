from data import question_data


class QuizBrain:
    def __init__(self, l):
        self.qno = 0
        self.qlist = l
        self.score = 0

    def nextquestion(self):
        curr_qn = self.qlist[self.qno]
        # s += str(self.qlist[n-1])
        self.qno = self.qno + 1
        an = input(f"Q.{self.qno}. {curr_qn.text} True/False ")
        self.checker(an, curr_qn.answer)

    def qnsrem(self):
        l = len(self.qlist)
        if self.qno < l:
            return True
        else:
            return False

    def checker(self, an, c):
        if an.lower() == c.lower():
            self.score += 1
            print("Right Answer")

        else:
            print("Wrong Answer")
        print("Correct Answer was", str(c))
        print("Score currently", self.score, "/", self.qno)
        print()