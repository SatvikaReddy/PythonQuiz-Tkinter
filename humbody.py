class HB:
    def __init__(self):
        self.name=input("Enter Your Name: ")
        self.score=0
    def Choice(self):
        self.choice=int(input("Which is the correct answer? "))
    def Score(self,n):
        if self.choice ==n:
            self.score=self.score+3
        else:
            self.score=self.score-0.5
    def questions(self):
        print("\nQuestion Number 1")
        print("How many litres of blood is pumped by human heart during the average life time?")
        print("1)182\n2)172\n3)162\n4)152")
        self.Choice()
        self.Score(1)
        print("\nThe correct answer is 1!") 

        print("\n\nQuestion Number 2")
        print("How many times human bones are stronger than steel?")
        print("1)15\n2)10\n3)5\n4)3")
        self.Choice()
        self.Score(3)
        print("\nThe correct answer is 3!")

        print("\n\nQuestion Number 3")
        print("On an average,how many words does a person speak in 24hours?")
        print("1)8400\n2)4800\n3)2400\n4)4200")
        self.Choice()
        self.Score(2)
        print("\nThe correct anser is 2!")

        print("\n\nQuestion Number 4")
        print("How many musles does a person uses whike smiling")
        print("1)19\n2)18\n3)17\n4)16")
        self.Choice()
        self.Score(3)
        print("\nThe correct answer is 3!")

        print("Question Number 5")
        print("How many bones does an infant body has?")
        print("1)206\n2)300\n3)306\n4)307")
        self.Choice()
        self.Score(2)
        print("The correct answer is 2!")

        print("\n\nQuestion Number 6")
        print("An adult heart weights upto?")
        print("1)220-260grams\n2)240-280grams\n3)320-360grams\n4)200-260grams")
        self.Choice()
        self.Score(1)
        print("\nThe correct answer is 1!")

        print("\n\nQuestion Number 7")
        print("How much percentage of DNA does humans share with chimpanzees?")
        print("1)99.9%\n2)98.9%\n3)98.4%\n4)100%")
        self.Choice()
        self.Score(3)
        print("\nThe correct answer is 3!")

        print("\n\nQuestion Number 8")
        print("How much percentage of our brain is filled with water?")
        print("1)80%\n2)90%\n3)50%\n4)40%")
        self.Choice()
        self.Score(1)
        print("\nThe Correct Answer is 1!")

        print("\n\nQuestion Number 9")
        print("How many different scents can our nose remember?")
        print("1)80000\n2)40000\n3)50000\n4)70000")
        self.Choice()
        self.Score(3)
        print("\nThe correct answer is 3!")

        print("\n\nQuestion Number 10")
        print("How many times does a person laugh in a day?")
        print("1)6\n2)5\n3)10\n4)15\n")
        self.Choice()
        self.Score(4)
        print("\nThe correct answer is 4!")
        

        print("\n\nYour Final Score is ",self.score)


obj=HB()
obj.questions()
