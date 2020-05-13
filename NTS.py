class NTS:
    def __init__(self):
        self.name=input("Enter Your Name: ")
        self.score=0
    def Choice(self):
        self.choice=input("Which is the correct answer? ")
    def Score(self,n):
        if self.choice==n:
            self.score=self.score+3
        else:
            self.score=self.score-0.5
    def questions(self):
        print("\nQuestion Number 1")
        print("Vogue, Material Girl, Music")
        print("1)Madonna\n2)AC/DC\n3)Rihanna\n4)the doors")
        self.Choice()
        self.Score('1')
        print("\nThe correct answer is 1!") 

        print("\n\nQuestion Number 2")
        print("Rolling in the Deep, Chasing Pavements, Rumour Has It")
        print("1)Rihanna\n2)Adele\n3)Britney Spears\n4)hill up")
        self.Choice()
        self.Score('2')
        print("\nThe correct answer is 2!\n")

        print("\n\nQuestion Number 3")
        print("No Woman No Cry, Redemption Song, I Shot the Sheriff")
        print("1)the who\n2)journey\n3)Spice girls\n4)Bob Marley")
        self.Choice()
        self.Score('4')
        print("\nThe correct anser is 4!")

        print("\n\nQuestion Number 4")
        print("I'm Eighteen, School's Out, Under my Wheels")
        print("1)Pink Floyd\n2)Pistols\n3)Alice Coper\n4)Bruno Mars\n")
        self.Choice()
        self.Score('3')
        print("\nThe correct answer is 3!")

        print("\n\nQuestion Number 5")
        print("White Flag, Thank You, Life for Rent")
        print("1)Dido\n2)Eminem\n3)Britney Spears\n4)Loyd")
        self.Choice()
        self.Score('1')
        print("\nThe correct answer is 1!")

        print("\n\nQuestion Number 6")
        print("Viva Forever, Wannabe, Too Much")
        print("1)Spice Girls\n2)Pistols\n3)Alice Cooper\n4)Britney Spears")
        self.Choice()
        self.Score('1')
        print("\nThe correct answer is 1!")

        print("\n\nQuestion Number 7")
        print("The Lazy Song, Grenade, Marry You")
        print("1)Bruno Mars\n2)Alice cooper\n3)Eminem\n4)Dido")
        self.Choice()
        self.Score('1')
        print("\nThe correct answer is 1!")

        print("\nQuestion Number 8")
        print("Wonderwall, Champagne Supernova, Don't Look Back in Anger")
        print("1)Oasis\n2)Dido\n3)Nirvana\n4)Green day\n")
        self.Choice()
        self.Score('1')
        print("\nThe Correct Answer is 1!")

        print("\nQuestion Number 9")
        print(" Kiss, Little Red Corvette, When Doves Cry")
        print("1)Eminem\n2)Dido\n3)Prince\n4)Kiss")
        self.Choice()
        self.Score('3')
        print("\nThe correct answer is 3!")

        print("\n\nQuestion Number 10")
        print("This Kiss, Breathe, The Way You Love Me")
        print("1)Faith Hill\n2)Dido\n3)Eminem\n4)\nAdele")
        self.Choice()
        self.Score('1')
        print("\nThe correct answer is 1!")


        print("Your Final Score is ",self.score)


Obj=NTS()
Obj.questions()
