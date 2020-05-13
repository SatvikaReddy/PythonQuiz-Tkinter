class CurrentAffairs:
    def __init__(self):
        self.name=input("Enter you name ")
    def questions(self):
        queslist=["Question1.\nWhich country has decided to launch world’s first national 5G networks?\na)South Korea\nb)Japan\nc)China\nd)France\n",
                  "Question2.\nWhich South American nation has recently joined International Solar Alliance(ISA)?\na)Ecuador\nb)Colombia\nc)Uruguay\nd)Bolivia\n",
                  "Question3.\nAccording to the world airport traffic rankings 2018 by Airports Council International(ACI),which Indian airport became the 12th busiest aiport in the world?\na)Chhatrapati Shivaji Maharaj International Airport\nb)Indira Gandhi International Airport\nc)Rajiv Gandhi International Airport\nd)None of the above\n",
                  "Question4.\nWho was appointed as the 24th Chief of naval staff of India?\na)Robin K Dhowan\nb)Devendra Kumar Joshi\nc)Karambir Singh\nd)Nirmal Kumar Verma\n",
                  "Question5.\nWho became the First Indian to join top 10 richest billionaire list of Hurun Research?\na)Pallonji Mistry\nb)Lakshmi Mittal\nc)Azim Premji\nd)Mukesh Ambani\n",
                  "Question6.\nWhere is the world's largest e-waste recycling plant inaugurated?\na)Bengaluru Industrial Park,India\nb)Dubai Industrial Park,Dubai\nc)Kuala Lumpur Industrial Park,Malaysia\nd)London Industrial Park,London\n",
                  "Question7.\nWhich city is set to host Olympic and Paralympic Games in the year 2020?\na)Tokyo,Japan\nb)Beijing,China\nc)Osaka,Japan\nd)None of the above\n",
                  "Question8.\nWhich two countries signed Statement of Guiding Principles(SGP) on triangular cooperation for global development in Asia and Africa?\na)Russia and US\nb)India and china\nc)India and US\nd)China and Japan\n",
                  "Question9.\nAs per the report titled 'OpenSignal's hottest city for 4G Availability',which city topped in India?\na)Nashik\nb)Nagpur\nc)Jamshedpur\nd)Dhanbad\n",
                  "Question10.\nWho was the first Indian President to visit Croatia?\na)Abdul Kalam\nb)Pratibha Patil\nc)Pranab Mukherjee\nd)Ram Nath Kovind\n"]
        anslist=['a','d','b','c','d','b','a','c','d','d']
        factlist=["South Korea would be launching the world's 1st fully-fledged 5G mobile network on 5/4/2019.The superfast communications heralded by 5G wireless technology will bring smartphones near-instantaneous connectivity-20 times faster than the existing 4G.",
                  "On March 28,President Ram Nath Kovind became the 1st ever Indian President to visit Bolivia.Both the countries have agreed to facilitate Bolivian supplies of lithium carbonate  to India and foster joint ventures for cell production plants in India.This move will make Bolivia one of the major provider of metal for India's e-mobility and e-storage needs.",
                  "In accordance with the preliminary world airport traffic rankings for 2018 released by Airports Council International(ACI),the Indira Gandhi International Airport (IGIA) of New Delhi has elevated 4 ranks to reach at 12th spot in terms of busiest airport as compared to 2017’s 16 spot. The list of world’s busiest airports by passenger traffic ranking has been topped by Hartsfield–Jackson Atlanta International Airport (US) followed by Beijing Capital International Airport(China) and Dubai International Airport(UAE).In 2018,India has followed US and China to become the world’s third-largest aviation market in terms of passenger throughput.",
                  "On 23rd March 2019,Vice Admiral Karambir Singh has been appointed as the next(24th) chief of naval staff.He will succeed present Chief of Naval Staff Admiral Sunil Lanba who retires on May 2019.At present,he is a Flag Officer Commanding in Chief of the Eastern Naval Command in Visakhapatnam.He was commissioned into the Indian Navy in July 1980 and after two years he earned his wings as a helicopter pilot.During his 39 years of service, he has flying experience of the HAL Chetak and Kamov Ka-25 helicopters and commanded numerous ships including ICGS Chand Bibi,INS Vijaydurg,INS Rana and INS Delhi.He has been honored with the Param Vishisht Seva Medal(PVSM) and the Ati Vishisht Seva Medal(AVSM).",
                  "Reliance Industries Chairman and Managing Director Mukesh Ambani became the first Indian and the only Asian to enter the Global top 10 richest billionaire list compiled by Hurun Research, China after a USD 9 billion or 20% surge in his wealth to USD 54 billion. India is at 5th spot with 104 billionaires. Last year, the country had added 32 billionaires, but this year it lost 28.Mumbai and New Delhi are the billionaire capitals of the country.",
                  "The world’s largest e-waste recycling plant has been opened in Dubai Industrial Park, Dubai by ‘Enviroserve’ company with a total cost of $5 million.It will recycle Waste Electrical and Electronic Equipment(WEEE),IT asset disposition(ITAD),refrigerant gas and specialized waste.The processing capacity of this recycling hub is 100,000 tonnes of total integrated waste(per year),of which 39,000 tonnes is e-waste. The project is supported by the Swiss Government Export Finance Agency.",
                  "On September 7, 2013 at the 125th IOC Session in Buenos Aires, Tokyo won their bid to host the games. Tokyo previously hosted the 1964 Summer Olympics. On August 3, 2016 it was reported that the IOC approved the addition of five sports to the program of the 2020 Olympics including the return of baseball and softball.",
                  "India and the United States on March 29, 2019 signed the first amendment to the Statement of Guiding Principles (SGP) on triangular cooperation for global development.The Amendment was signed by Devyani Khobragade, Joint Secretary in the External Affairs Ministry’s Development Partnership Administration -II Division and Mark Anthony White, Mission Director for the United States Agency for International Development (USAID) in India.",
                  "On 29th March 2019, Dhanbad, the coal capital of India scored 95.3 percent and become the number one city in terms of highest 4G availability in India by the report name ‘OpenSignal’s hottest city for 4G Availability’. Ranchi which has 95% of 4G Availability, ranked second and Srinagar ranked third with the score of 94.9% on the list with 4G Availability. Raipur and Patna ranked fourth and fifth place with a score of 94.8% and 94.5% respectively.",
                  "President Ram Nath Kovind has been honoured with Croatia's highest civilian award the Grand Order of the King of Tomislav.The Indian President was honoured during his visit to Croatia to strengthen the bilateral ties.The award is awarded to the heads of state for their important contribution towards the development of state relations between Croatia and their respective countries."]
        score=0    
        for i in range(len(queslist)):
            a=str(input(queslist[i]))
            if a==anslist[i]:
                score+=3
                print("Correct answer")
                print(factlist[i])
                print("\n")
            else:
                score-=0.5
                print("Wrong answer.\nCorrect answer is",anslist[i],"\n",factlist[i])
                print("\n")
        print("You scored",score,"out of 30.")
        print("THANK YOU!")
obj=CurrentAffairs()
obj.questions()
