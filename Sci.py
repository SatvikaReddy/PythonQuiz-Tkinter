class SciTech: 
    def __init__(self): 
        self.name=input("Enter Your Name: ") 
        self.score=0 
    def Choice(self): 
        self.choice=int(input("Which is the correct answer? ")) 
    def Score(self,n): 
        if self.choice==n:
            self.score=self.score+3 
        else: 
            self.score=self.score-0.5 
    def questions(self): 
        print("\nQuestion Number 1") 
        print("What was the name of the space shuttle that landed man on the moon?") 
        print("1) Columbia \n2) Challenger\n3) Apollo\n4) Explorer") 
        self.Choice() 
        self.Score(3) 
        print("\nThe correct answer is 3!")  
 
        print("\n\nQuestion Number 2") 
        print("What is supernova?") 
        print("1) A black hole\n2) A dying star\n3) An asteroid\n4) A comet") 
        self.Choice() 
        self.Score(2) 
        print("\nThe correct answer is 2!") 
 
        print("\n\nQuestion Number 3") 
        print("INS ‘Virat’ serves the Indian Navy. It is a?") 
        print("1) Submarine\n2) Gunboat\n3) Aircraft carrier\n4) Freighter") 
        self.Choice() 
        self.Score(3) 
        print("\nThe correct answer is 3!") 
 
        print("\n\nQuestion Number 4") 
        print("Of the following Indian satellites, which on is intended for long distance telecommunications for transmitting TV programmes?") 
        print("1) INSAT – A\n2) Aryabhatta\n3) Bhaskara\n4) Rohini") 
        self.Choice() 
        self.Score(1) 
        print("\nThe correct answer is 1!") 
 
        print("\n\nQuestion Number 5") 
        print("What is the range of Agni III, the long range ballistic missile, test-fired by India? ") 
        print("1) 2250 Km\n2) 3500 Km\n3) 5000 Km\n4) 1000 Km") 
        self.Choice() 
        self.Score(2) 
        print("\nThe correct answer is 2!") 
 
        print("\n\nQuestion Number 6") 
        print("Nuclear explosive devices were tested in India at…") 
        print("1) Sriharikota \n2) Bangalore\n3) Pokharan\n4) Kanchipuram") 
        self.Choice() 
        self.Score(3) 
        print("\n\nThe correct answer is 3!") 
 
        print("\n\nQuestion Number 7") 
        print("The first ever robot spacecraft to probe planet venus was named?") 
        print("1)Challenger\n2)Newton\n3)Magellan\n4)Galileo") 
        self.Choice() 
        self.Score(3) 
        print("\nThe correct answer is 3!") 
 
        print("\n\nQuestion Number 8") 
        print("Which one of the following correctly described AGNI?") 
        print("1)Long-range Gun\n2)Fighter Plane \n3)Versatile Tank\n4) Long-range Missile ") 
        self.Choice() 
        self.Score(4) 
        print("\nThe Correct Answer is 4!") 
 
        print("\n\nQuestion Number 9") 
        print("The Which of the following is not true for a Geostationary Satellite?") 
        print("1) it is fixed in space \n2)Revolves from west to east \n3) Its time period is 24 hrs \n4)Angular speed is equal to that of Earth") 
        self.Choice() 
        self.Score(1) 
        print("\nThe correct answer is 1") 
 
        print("\n\nQuestion Number 10") 
        print("Which of the following is a stealth aircraft virtually undetectable even by radar?") 
        print("1)B-2 Spirit\n2)B1-B Lancer\n3)FA-18 Homets\n4)B-52 Stratofortrees") 
        self.Choice() 
        self.Score(4) 
        print("\nThe correct answer is 4!") 


        print("\n\nYour Final Score is ",self.score)

obj=SciTech()
obj.questions()
