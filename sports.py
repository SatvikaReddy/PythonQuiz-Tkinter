class Sports:
    def __init__(self):
        self.name=input("Enter your name ")
    def Quiz(self):
        queslist=["Question1.\nWith which among the following sports, Ian Thorpe is related to?\na)Racing\nb)Athletics\nc)Boxing\nd)Swimming\n",
                    "Question2.\nHow many players are on each side of the net in beach volleyball?\na)Four\nb)Two\nc)Six\nd)Three\n",
                    "Question3.\nWhat name is given to the score 111 in cricket?\na)Nelson\nb)Triples\nc)Newton\nd)Stumps\n",

                    "Question4.\nWhich country won the inaugral Twenty20 world cup??\na)Australia\nb)India\nc)Pakistan\nd)West Indies\n",
                    "Question5.\nTill 1889 how many balls an over used to be bowled?\na)Eight\nb)Six\nc)Four\nd)Five\n",

                    "Question6.\nWhich among the following country is the host of 2018 Commonwealth Games?\na)Australia\nb)England\nc)Canada\nd)India\n",
                    "Question7.\nWhich cricketer has made the highest individual score at the World Cup ?\na)Rahul Dravid\nb)Kapil Dev\nc)Sachin Tendulkar\nd)None of the above\n",

                    "Question8.\nIn which sport can you win the Davis Cup?\na)Tennis\nb)Cricket\nc)Football\nd)Golf\n",
                    "Question9.\nSultan Azlan Shah Cup is related to which among the following Sports?\na)Badminton\nb)Hockey\nc)Table Tennis\nd)Tennis\n",
            
                    "Question10.\nWhich cricketers have the record for the highest run partnership at the World Cup ?\na)Sachin Tendulkar and Saurav Ganguly\nb)Saurav Ganguly and Rahul Dravid\nc)Saurav Ganguly and Virender Sehwag\nd)Rahul Dravid and Sachin Tendulkar\n"]

        anslist=['d','b','a','b','c','d','c','a','b','b']

        score=0

        for i in range(len(queslist)):
            a=str(input(queslist[i]))
            if a==anslist[i]:
                score+=3
                print("Correct answer")
                print("\n")
            else:
                score-=0.5
                print("Wrong answer.\nCorrect answer is",anslist[i])
                print("\n")
        print("You scored",score,"out of 30")
        print("THANK YOU!")

obj=Sports()
obj.Quiz()

