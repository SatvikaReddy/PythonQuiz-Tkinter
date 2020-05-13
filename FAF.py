class FaF:
    def __init__(self):
        self.name=input("Enter Your Name: ")
        self.score=0
    def Choice(self):
        self.choice=int(input("Which is the correct answer?"))
    def Score(self,n):
        if self.choice==n:
            self.score=self.score+3
        else:
            self.score=self.score-0.5
    def questions(self):
        print("Question Number 1")
        print("Which Bird is known to have the largest wingspan?")
        print("1)White Pelican\n2)Wandering Albatross\n3)Southern Royal Albatross\n4)Marabou Stork")
        self.Choice()
        self.Score(2)
        print("\nThe correct answer is 2!\nThe Wandering Albatross is known to have a wingspan of 3.65-3.7 meters(about 12 feet)") 

        print("\n\nQuestion Number 2")
        print("Which Animal has the largest brain?")
        print("1)Killer Whale\n2)Elephant\n3)Sperm Whale\n4)Bottlenose Dolphin")
        self.Choice()
        self.Score(3)
        print("\nThe correct answer is 3!\nA Sperm Whale's brain weighs around 8 kilograms(about 18 pounds)")

        print("\n\nQuestion Number 3")
        print("Which is the largest flower?")
        print("1)Cauliflower\n2)Water Lily\n3)Corspe Lily\n4)Hibiscus")
        self.Choice()
        self.Score(3)
        print("\nThe correct anser is 3!Corpse Lily, another name for Rafflesia Arnoldii is the largest flower known and grows upto 3 feet across!")

        print("\nQuestion Number 4")
        print("Which of the following countries do we NOT find penguins")
        print("1)South Africa\n2)Greenland\n3)Argentina\n4)Austrailia")
        self.Choice()
        self.Score(2)
        print("\n\nThe correct answer is 2!Penguins are majorly found in Antarctica, Argentina, Austrailia, Chile, New Zealand, Angola and South Africa!")

        print("\nQuestion Number 5")
        print("Which of these trees is the tallest in the world?")
        print("1)Redwood\n2)Oak\n3)Eucalyptus\n4)Fir")
        self.Choice()
        self.Score(1)
        print("\n\nThe correct answer is 1! Redwood trees(Coast Redwood in particular) are the tallest trees that grow upto 116 meters(380 feet) high!")

        print("\nQuestion Number 6")
        print("How long does it take for an emu to hatch?")
        print("1)3 weeks\n2)30 days\n3)45 days\n4)60 days")
        self.Choice()
        self.Score(4)
        print("\n\nThe correct answer is 4! It takes about 8 weeks for an emu bird to hatch!")

        print("\nQuestion Number 7")
        print("Which animal is the slowest animal in the world?")
        print("1)Three Toed Sloth\n2)Koala Bear\n3)Tortoises\n4)Starfish")
        self.Choice()
        self.Score(1)
        print("\n\nThe correct answer is 1!If a sloth decides to move, it can reach a top speed of 2 meters per minute")

        print("\nQuestion Number 8")
        print("What is a Male Rhino called?")
        print("1)Cow\n2)Father\n3)Bull\n4)Alpha")
        self.Choice()
        self.Score(3)
        print("\n\nThe Correct Answer is 3! A Male Rhino is called a Bull while a Female Rhino is called a Cow")

        print("\nQuestion Number 9")
        print("The fruit of which of these plants is found underground?")
        print("1)Potato\n2)Carrot\n3)Groundnut\n4)Onion")
        self.Choice()
        self.Score(3)
        print("\n\nThe correct answer is 3! Potato and Carrots are the roots of the plant whereas Onion is an underground stem!")

        print("\nQuestion Number 10")
        print("How many eyes does a honey bee have?")
        print("1)Two\n2)Four\n3)Five\n4)\nSix")
        self.Choice()
        self.Score(3)
        print("\n\nThe correct answer is 3! A bee has a total of 5 eyes! Three of which dicern light intensity and the other two detect movement.")

        print("\n\n**Your Final Score is ",self.score,"**")
        
        
obj=FaF()
obj.questions()
