class ATW:
    def __init__(self):
        self.name=input("Enter Your Name:")
        self.score=0
    def Choice(self):
        self.choice=int(input("\nWhich is the correct answer? "))
    def Score(self,n):
        if self.choice==n:
            self.score=self.score+3
        else:
            self.score=self.score-0.5
    def questions(self):
        print("Question Number 1")
        print("What is Cuban Medionache ?")
        print("Options\n1)A 24 Hour Diner\n2)A Coffe Drink\n3)Squid Ink Pasta\n4)A Sandwich")
        self.Choice()
        self.Score(4)
        print("\n\nThe Correct Answer is 4")

        print("\n\nQuestion Number 2")
        print("What is the Traditional Dress of China?")
        print("Options\n1)Cheogsan\n2)Gilaki\n3)Kanzu\n4)Barong Tagalong")
        self.Choice()
        self.Score(1)
        print("\nThe Correct Answer is 1")


        print("\n\nQuestion Number 3")
        print("Which Festival in Thailand is also celebrated as Traditional New Year's Day ?")
        print("Option\n1)Loi Krathang\n2)Bro-Sang\n3)Songkram\n4)Naga-fireball")
        self.Choice()
        self.Score(3)
        print("\nThe Correct Answer is 3")

        print("\n\nQuestion Number 4")
        print("Name the World's Tallest Fountain?")
        print("Options\n1)Buckigham Fountain\n2)Trevi Fountain\n3)King Fahd's Fountain\n4)Archbald Fountain\n")
        self.Choice()
        self.Score(3)
        print("\nThe Correct Answer is 3")


        print("\n\nQuestion Number 5")
        print("Name the Largest Casino?")
        print("Options\n1)City of Dreams\n2)WinStar World Casino\n3)MGM Grand Las Vegas\n4)Sands Macao")
        self.Choice
        self.Score(2)
        print("\nThe Correct Answer is 2")

        print("\n\nQuestion Number 6")
        print("What is the Spanish word for Apple?")
        print("Options\n1)Manzanas\n2)Frigole\n3)Fourchette\n4)Citron")
        self.Choice()
        self.Score(1)
        print("\nThe Corrrect Answer is 1")


        print("\nQuestion Number 7")
        print("In which country is the Cape Town International Jazz Festival conducted?")
        print("Options\n1)Bulgaria\n2)Austria\n3)Spain\n4)South Africa")
        self.Choice()
        self.Score(4)
        print("\nThe correct answer is 4")


        print("\n\nQuestion Number 8")
        print("Name the Country where the World's Oldest University is located?")
        print("Options\n)Bologna\n2)Beijing\n3)Moscow\n4)Cairo")
        self.Choice()
        self.Score(1)
        print("\nThe Correct Answer is 1")


        print("\n\nQuestion Number 9")
        print("What si World's most Expensive Spice?")
        print("Options\n1)Turmeric\n2)Clove\n3)Saffron\n4)Vanilla")
        self.Choice()
        self.Score(3)
        print("\nThe Correct Answr is 3")


        print("\n\nQuestion Number is 10")
        print("Name is the Presidenyt of US who created most Monuments?")
        print("Options\n1)George W Bush\n2)Bill Clinton\n3)Jimmy Carter\n4)John F kennedy")
        self.Choice()
        self.Score(2)
        print("\nThe Correct Answer is 2")

        print("\n\n**Your Final Score is",self.score,"**")


obj=ATW()
obj.questions()
