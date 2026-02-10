import pandas as pd
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='delli5',database='hackathon')
mycursor=conn.cursor()

while True:
    print("***************Welcome To Quiz Management***************")
    print("Please select the category : ")
    print("1 Registration")
    print("2 Start")
    print("3 Exit")
    print()
    input1=int(input("Enter your choice:"))

    if input1==1:
        while True:
            print("*********************Registration*********************")
            print("1 New registration")
            print("2 View registration")
            print("3 Exit")
            print()
            input2=int(input("Enter your choice:"))

            if input2==1:
                print("*****************New Registration*********************")
                Registration_ID=input("Registration Id: ")
                Name=input("Name = ")
                Age=input("Age: ")
                Occupation=input("Occupation: ")
                Language=input("Language =")
                Mobile=input("Mobile: ")
                Email_id=input("Email: ")
                print()
                mycursor.execute("Insert into registration_detail values('"+Registration_ID+"','"+Name+"','"+Age+"',"+Occupation+"',"+Language+"','"+Mobile+"','"+Email_id+"');")
                conn.commit()
                print("Print your registration is successful")
                print()      

            elif input2==2:
                Quiz="select * from registration_detail;"
                old=pd.read_sql(registration_detail,conn)
                print()
                print(old)

            elif input2==3:
                print("Thank you visit again")
                break

    if input1==2:
        while True:
            print("*********************Choose topic*********************")
            print("Please select the topic : ")
            print("1 Formation of constitution")
            print("2 Addition and deletion of law")
            print("3 Justice process")
            print("4 Duties")
            print("5 Rights")
            print("6 Laws")
            print("7 Exit")
            print()
            input3=int(input("Enter your choice:"))

            if input3==1:
                while True:
                    Registration_ID=input("Registration Id: ")
                    Name=input("Name: ")
                    print("************************Formation of constitution************************")
                    print("1. Consider the following statements regarding the constituent assembly ")
                    print("i. The final session of the constitution assembly was held on 24th january 1950")
                    print("ii. Dr Rajendra prasad was declared to be duly elected to the office of president of India in this final session. ")
                    print("a. i is incorrect and ii is coorect")
                    print("b. i is correct and ii is incorrect")
                    print("c. Both are incorrect")
                    print("d. Both are correct")
                    Gk_Q1_ans=input("Enter your choice:")

                    if Gk_Q1_ans=="a" or Gk_Q1_ans=="A" or Gk_Q1_ans=="b" or Gk_Q1_ans=="B" or Gk_Q1_ans=="c" or Gk_Q1_ans=="C":
                        print("Sorry Your Answer Is Incorrect")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input5=int(input("Enter your choice: "))

                    elif Gk_Q1_ans=="d" or Gk_Q1_ans=="D":
                        print("Congratulation Your answer is correct")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input5=int(input("Enter your choice:"))

                    if input5==2:
                        print("Thank you visit again")

                    elif input5==1:
                        print()
                        print("2. In the indian constitution the section of citizenship draws inspiration from which country's constitution ?")
                        print("a. USA")
                        print("b. Uk")
                        print("c. Australia")
                        print("d. More than one of them")
                        Gk_Q2_ans=input("Enter your choice: ")

                        if Gk_Q2_ans=="a" or Gk_Q2_ans=="A" or Gk_Q2_ans=="c" or Gk_Q2_ans=="C" or Gk_Q2_ans=="d" or Gk_Q2_ans=="D":
                            print("Sorry your answer is incorrect")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input7=int(input("Enter your choice: "))

                        elif Gk_Q2_ans=="b" or Gk_Q2_ans=="B":
                            print("Congratulations your answer is correct")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input7=int(input("Enter your choice: "))

                        if input7==2:
                            print("Thank you visit again")

                        elif input7==1:
                            print()
                            print("3. The Indian constitution was adopted by the Constitute assembly on ")
                            print("a. 26th November 1949")
                            print("b. 28th November 1949")
                            print("c. 28th November 1950")
                            print("d. 26th November 1950")
                            Gk_Q3_ans=input("Enter your choice: ")

                            if Gk_Q3_ans=="a" or Gk_Q3_ans=="A":
                                print("Congratulations your answer is correct")
                                print()
                                print("Please select the category: ")
                                print("1. Continue")
                                print("2. Exit")
                                input9=int(input("Enter your choice: "))

                            elif Gk_Q3_ans=="b" or Gk_Q3_ans=="B" or Gk_Q3_ans=="c" or Gk_Q3_ans=="C" or Gk_Q3_ans=="d" or Gk_Q3_ans=="D":
                                print("Sorry your answer is incorrect")
                                print()
                                print("Please select the category: ")
                                print("1. Continue")
                                print("2. Exit")
                                input9=int(input("Enter your choice: "))

                            if input9==2:
                                print("Thank you visit again")
                                break

                            elif input9==1:
                                print()
                                print("4. When did the Constitution of India came into force? ")
                                print("a. 15th January 1950")
                                print("b. 26th January 1950")
                                print("c. 15th August 1950")
                                print("d. 26th August 1950")
                                Gk_Q4_ans=input("Enter your choice:")

                                if Gk_Q4_ans=="a" or Gk_Q4_ans=="A" or Gk_Q4_ans=="c" or Gk_Q4_ans=="C" or Gk_Q4_ans=="d" or Gk_Q4_ans=="D":
                                    print("Sorry Your Answer Is Incorrect")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input11=int(input("Enter your choice:"))

                                elif Gk_Q4_ans=="b" or Gk_Q4_ans=="B":
                                    print("Congratulation Your answer is correct")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input11=int(input("Enter your choice:"))

                                if input11==2:
                                    print("Thank you visit again")

                                elif input11==1:
                                    print()
                                    print("5. Who prepared the intital draft of the Indian Constitution ?")
                                    print("a. Shyama Prasad Mukherjee")
                                    print("b. Beohar Rammanohar Sinha")
                                    print("c. Benegal Narsing Rau")
                                    print("d. More than one of the above")
                                    Gk_Q5_ans=input("Enter your choice:")


                                if Gk_Q5_ans=="a" or Gk_Q5_ans=="A" or Gk_Q5_ans=="b" or Gk_Q5_ans=="B" or Gk_Q5_ans=="d" or Gk_Q5_ans=="D":
                                    print("Sorry Your Answer Is Incorrect")
                                    print()
                                    print("Thank you visit again")
                                    break

                                elif Gk_Q5_ans=="c" or Gk_Q5_ans=="C":
                                    print("Congratulation Your answer is correct")
                                    print()
                                    print("Thank you visit again")
                                    break

                                    mycursor.execute("Insert into formation_of_constitution values('"+Registration_ID+"','"+Name+"','"+Gk_Q1_ans+"','"+Gk_Q2_ans+"','"+Gk_Q3_ans+"','"+Gk_Q4_ans+"','"+Gk_Q5_ans+"');")
                                    conn.commit()
                                            
            elif input3==2:
                while True:
                    Registration_ID=input("Registration Id: ")
                    Name=input("Name: ")
                    print("***************************************Addition and deletion of law**************************************")
                    print("1. When was article 370 abolished")
                    print("a. 30 October 2019")
                    print("b. 30 July 2019")
                    print("c. 15 October 2019")
                    print("d. 7 July 2017")
                    GS_Q1_ans=input("Enter your choice:")

                    if GS_Q1_ans=="a" or GS_Q1_ans=="A":
                        print("Congratulation Your answer is correct")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input14=int(input("Enter your choice:"))

                    elif GS_Q1_ans=="b" or GS_Q1_ans=="B" or GS_Q1_ans=="c" or GS_Q1_ans=="C" or GS_Q1_ans=="d" or GS_Q1_ans=="D":
                        print("Sorry Your Answer Is Incorrect")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input14=int(input("Enter your choice:"))

                    if input14==2:
                        print("Thank you visit again")
                        break

                    elif input14==1:
                        print()
                        print("2. When was commercial court act implemented")
                        print("a. 2013")
                        print("b. 2015")
                        print("c. 2017")
                        print("d. 2019")
                        GS_Q2_ans=input("Enter your choice:")
                            
                        if GS_Q2_ans=="a" or GS_Q2_ans=="A" or GS_Q2_ans=="c" or GS_Q2_ans=="C" or GS_Q2_ans=="d" or GS_Q2_ans=="D":
                            print("Sorry Your Answer Is Incorrect")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input16=int(input("Enter your choice:"))

                        elif GS_Q2_ans=="b" or GS_Q2_ans=="B":
                            print("Congratulation Your answer is correct")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input16=int(input("Enter your choice:"))

                        if input16==2:
                            print("Thank you visit again")
                            break

                        elif input16==1:
                            print()
                            print("3. in 2016, the supreme court has clarified that the 'The third Gender ")
                            print("a. Bisexual")
                            print("b. Gays and lesbian")
                            print("c. Transgender")
                            print("d. None of the above")
                            GS_Q3_ans=input("Enter your choice:")

                            if GS_Q3_ans=="a" or GS_Q3_ans=="A" or GS_Q3_ans=="d" or GS_Q3_ans=="D" or GS_Q3_ans=="c" or GS_Q3_ans=="C":
                                print("Sorry Your Answer Is Incorrect")
                                print()
                                print("Please select the category : ")
                                print("1 Continue")
                                print("2 Exit")
                                input18=int(input("Enter your choice:"))

                            elif GS_Q3_ans=="b" or GS_Q3_ans=="B":
                                print("Congratulation Your answer is correct")
                                print()
                                print("Please select the category : ")
                                print("1 Continue")
                                print("2 Exit")
                                input18=int(input("Enter your choice:"))

                            if input18==2:
                                print("Thank you visit again")
                                break

                            elif input18==1:
                                print()
                                print("4.The principal of rule of law is enshrined in which part of the Indian constitution ")
                                print("a.Fundamental rights")
                                print("b.Preamble ")
                                print("c.Union and state territories ")
                                print("d.Directive principles ")
                                GS_Q4_ans=input("Enter your choice:")

                                if GS_Q4_ans=="a" or GS_Q4_ans=="A" or GS_Q4_ans=="c" or GS_Q4_ans=="C" or GS_Q4_ans=="d" or GS_Q4_ans=="D":
                                    print("Sorry Your Answer Is Incorrect")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input20=int(input("Enter your choice:"))

                                elif GS_Q4_ans=="b" or GS_Q4_ans=="B":
                                    print("Congratulation Your answer is correct")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input20=int(input("Enter your choice:"))

                                if input20==2:
                                    print("Thank you visit again")
                                    break

                                elif input20==1:
                                    print()
                                    print("5. The primary source of law in India is? ")
                                    print("a.Customary Law ")
                                    print("b.Case law ")
                                    print("c.Religious law ")
                                    print("d.Statutory Law")
                                    GS_Q5_ans=input("Enter your choice:")

                                    if GS_Q5_ans=="a" or GS_Q5_ans=="A" or GS_Q5_ans=="b" or GS_Q5_ans=="B" or GS_Q5_ans=="c" or GS_Q5_ans=="C":
                                        print("Sorry Your Answer Is Incorrect")
                                        print()
                                        print("Thank you visit again")
                                        break

                                    elif GS_Q5_ans=="d" or GS_Q5_ans=="D":
                                        print("Congratulation Your answer is correct")
                                        print()
                                        print("Thank you visit again")
                                        break

                                        mycursor.execute("Insert into addition_and_deletion values('"+Registration_ID+"','"+Name+"','"+GS_Q1_ans+"','"+GS_Q2_ans+"','"+GS_Q3_ans+"','"+GS_Q4_ans+"','"+GS_Q5_ans+"');")
                                        conn.commit()
                                                        
            elif input3==3:
                while True:
                    Registration_ID=input("Registration Id: ")
                    Name=input("Name: ")
                    print("************************Justice process***********************")
                    print("1. Which of the acts And regulatioms cannot be declared unconstitutional by high courts and supreme court")
                    print("a. Acts and regulations concerning persons from scheduled castes and schedule tribes")
                    print("b. Acts and regulations concerning parliament and its members")
                    print("c. Acts and regulations enlisted in schedule 7 of the constitution")
                    print("d. Acts and regulations enlisted in schedule 9 of the constitution")
                    SS_Q1_ans=input("Enter your choice:")

                    if SS_Q1_ans=="a" or SS_Q1_ans=="A" or SS_Q1_ans=="b" or SS_Q1_ans=="B" or SS_Q1_ans=="c" or SS_Q1_ans=="C":
                        print("Sorry Your Answer Is Incorrect")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input14=int(input("Enter your choice:"))

                    elif SS_Q1_ans=="d" or SS_Q1_ans=="D":
                        print("Congratulation Your answer is correct")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input14=int(input("Enter your choice:"))

                    if input14==2:
                        print("Thank you visit again")
                        break

                    elif input14==1:
                        print()
                        print("2. ")
                        print("a. ")
                        print("b. ")
                        print("c. ")
                        print("d. ")
                        SS_Q2_ans=input("Enter your choice:")

                        if SS_Q2_ans=="a" or SS_Q2_ans=="A":
                            print("Congratulation Your answer is correct")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input16=int(input("Enter your choice:"))

                        elif SS_Q2_ans=="b" or SS_Q2_ans=="B" or SS_Q2_ans=="c" or SS_Q2_ans=="C" or SS_Q2_ans=="d" or SS_Q2_ans=="D":
                            print("Sorry Your Answer Is Incorrect")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input16=int(input("Enter your choice:"))

                        if input16==2:
                            print("Thank you visit again")
                            break

                        elif input16==1:
                            print()
                            print("3. Fundamental Duties are contained within which Article of the Constitution of India?")
                            print("a. Article 492")
                            print("b. Article 50A")
                            print("c. Article 44")
                            print("d. Article 51A")
                            SS_Q3_ans=input("Enter your choice:")

                                
                            if SS_Q3_ans=="a" or SS_Q3_ans=="A" or SS_Q3_ans=="b" or SS_Q3_ans=="B" or SS_Q3_ans=="c" or SS_Q3_ans=="C":
                                print("Sorry Your Answer Is Incorrect")
                                print()
                                print("Please select the category : ")
                                print("1 Continue")
                                print("2 Exit")
                                input18=int(input("Enter your choice:"))

                            elif SS_Q3_ans=="d" or SS_Q3_ans=="D":
                                print("Congratulation Your answer is correct")
                                print()
                                print("Please select the category : ")
                                print("1 Continue")
                                print("2 Exit")
                                input18=int(input("Enter your choice:"))

                            if input18==2:
                                print("Thank you visit again")
                                break

                            elif input18==1:
                                print()
                                print("4. All the ______ countries likely to have Constitution.")
                                print("a. democratic")
                                print("b. oligarchic")
                                print("c. communist")
                                print("d. totalitarian")
                                SS_Q4_ans=input("Enter your choice:")
                                            
                                if SS_Q4_ans=="a" or SS_Q4_ans=="A":
                                    print("Congratulation Your answer is correct")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input20=int(input("Enter your choice:"))

                                elif SS_Q4_ans=="b" or SS_Q4_ans=="B" or SS_Q4_ans=="c" or SS_Q4_ans=="C" or SS_Q4_ans=="d" or SS_Q4_ans=="D":
                                    print("Sorry Your Answer Is Incorrect")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input20=int(input("Enter your choice:"))

                                if input20==2:
                                    print("Thank you visit again")
                                    break

                                elif input20==1:
                                    print()
                                    print("5. Which of the following combinations is NOT correct?")
                                    print("a. Wular lake - Kashmir")
                                    print("b. Naini lake - Uttarakhand")
                                    print("c. Vembanad lake - Maharashtra")
                                    print("d. Chilika lake - Odisha")
                                    SS_Q5_ans=input("Enter your choice:")

                                if SS_Q5_ans=="a" or SS_Q5_ans=="A" or SS_Q5_ans=="b" or SS_Q5_ans=="B" or SS_Q5_ans=="d" or SS_Q5_ans=="D":
                                    print("Sorry Your Answer Is Incorrect")
                                    print()
                                    print("Thank you visit again")
                                    break

                                elif SS_Q5_ans=="c" or SS_Q5_ans=="C":
                                    print("Congratulation Your answer is correct")
                                    print()
                                    print("Thank you visit again")
                                    break

                                    mycursor.execute("Insert into justic_process values('"+Registration_ID+"','"+Name+"','"+SS_Q1_ans+"','"+SS_Q2_ans+"','"+SS_Q3_ans+"','"+SS_Q4_ans+"','"+SS_Q5_ans+"');")
                                    conn.commit()
                                    
            elif input3==4:
                while True:
                    Registration_ID=input("Registration Id: ")
                    Name=input("Name: ")
                    print("************************Duties***********************")
                    print("3. Fundamental Duties are contained within which Article of the Constitution of India?")
                    print("a. Article 492")
                    print("b. Article 50A")
                    print("c. Article 44")
                    print("d. Article 51A")
                    M_Q1_ans=input("Enter your choice:")

                    if M_Q1_ans=="a" or M_Q1_ans=="A"or M_Q1_ans=="c" or M_Q1_ans=="C" or M_Q1_ans=="d" or M_Q1_ans=="D":
                        print("Sorry Your Answer Is Incorrect")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input23=int(input("Enter your choice:"))
                        
                    elif M_Q1_ans=="b" or M_Q1_ans=="B":
                        print("Congratulation Your answer is correct")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input23=int(input("Enter your choice:"))

                    if input23==2:
                        print("Thank you visit again")
                        break

                    elif input23==1:
                        print()
                        print("2. According to 4A of Indian Constitution who is a parent or guardian has a duty to provide opportunities for education to his child or as the case may be ward between the age of ")
                        print("a. 2 - 6")
                        print("b. 6 - 12")
                        print("c. 6 - 14")
                        print("d. more than one of the above")
                        M_Q2_ans=input("Enter your choice:")

                        if M_Q2_ans=="a" or M_Q2_ans=="A" or M_Q2_ans=="b" or M_Q2_ans=="B" or M_Q2_ans=="d" or M_Q2_ans=="D":
                            print("Sorry Your Answer Is Incorrect")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input25=int(input("Enter your choice:"))
                                    
                        elif M_Q2_ans=="c" or M_Q2_ans=="C":
                            print("Congratulation Your answer is correct")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input25=int(input("Enter your choice:"))

                        if input25==2:
                            print("Thank you visit again")
                            break

                        elif input25==1:
                            print()
                            print("3. Which of the following is not a fundamental duty of an Indian citizen")
                            print("a. To value and preserve the rich heritage of our compositie culture")
                            print("b. To safeguard public property and to abjure violence")
                            print("c. To vote in public elections")
                            print("d. None of them")
                            M_Q3_ans=input("Enter your choice:")

                            if M_Q3_ans=="a" or M_Q3_ans=="A" or M_Q3_ans=="b" or M_Q3_ans=="B" or M_Q3_ans=="d" or M_Q3_ans=="D":
                                print("Sorry Your Answer Is Incorrect")
                                print()
                                print("Please select the category : ")
                                print("1 Continue")
                                print("2 Exit")
                                input27=int(input("Enter your choice:"))

                            elif M_Q3_ans=="c" or M_Q3_ans=="C":
                                print("Congratulation Your answer is correct")
                                print()
                                print("Please select the category : ")
                                print("1 Continue")
                                print("2 Exit")
                                input27=int(input("Enter your choice:"))

                            if input27==2:
                                print("Thank you visit again")
                                break 

                            elif input27==1:
                                print()
                                print("4. Original Constitution did not mention any fundamental duty because")
                                print("a. It was expected that the citizens of the country would perform their duties willingly")
                                print("b. it was that the citizen of the country would perform their duties forcefully")
                                print("c. initially fundamental duties were punishable as per the constitution")
                                print("d. intially fundamental duties were not expected to be performed ")
                                M_Q4_ans=input("Enter your choice:")

                                if M_Q4_ans=="a" or M_Q4_ans=="A":
                                    print("Congratulation Your answer is correct")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input29=int(input("Enter your choice:"))
                                            
                                elif M_Q4_ans=="b" or M_Q4_ans=="B" or M_Q4_ans=="c" or M_Q4_ans=="C" or M_Q4_ans=="d" or M_Q4_ans=="D":
                                    print("Sorry Your Answer Is Incorrect")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input29=int(input("Enter your choice:"))

                                if input29==2:
                                    print("Thank you visit again")
                                    break

                                elif input29==1:
                                    print()
                                    print("5. To uphold and protect the Sovereignty, unity and integrity of Indian id a provision made in the ")
                                    print("a.Preamble of the Consitution ")
                                    print("b. Fundamental duties ")
                                    print("c. Fundamental Rights")
                                    print("d. Directive principles of state policy")
                                    M_Q5_ans=input("Enter your choice:")

                                    if M_Q5_ans=="a" or M_Q5_ans=="A" or M_Q5_ans=="c" or M_Q5_ans=="C" or M_Q5_ans=="d" or M_Q5_ans=="D":
                                        print("Sorry Your Answer Is Incorrect")
                                        print()
                                        print("Thank you visit again")
                                        break

                                    elif M_Q5_ans=="b" or M_Q5_ans=="B":
                                        print("Congratulation Your answer is correct")
                                        print()
                                        print("Thank you visit again")
                                        break

                                        mycursor.execute("Insert into duties values('"+Registration_ID+"','"+Name+"','"+M_Q1_ans+"','"+M_Q2_ans+"','"+M_Q3_ans+"','"+M_Q4_ans+"','"+M_Q5_ans+"');")
                                        conn.commit()
                                        break

                    
            elif input3==5:
                while True:
                    Registration_ID=input("Registration Id: ")
                    Name=input("Name: ")
                    print("************************Rights***********************")
                    print("1. What are the duties of Indian citizens ?")
                    print("a. To abide by the constitution and respect its ideals and institutions, the National Flag and the National Anthem. ")
                    print("b. To cherish and follow the noble ideals which insipred our national struggle for freedom. ")
                    print("c. To uphold and protect the soverignty, unity and intergrity of Indian")
                    print("d. All of these")
                    R_Q1_ans=input("Enter your choice:")

                    if R_Q1_ans=="a" or R_Q1_ans=="A"or R_Q1_ans=="c" or R_Q1_ans=="C" or R_Q1_ans=="b" or R_Q1_ans=="B":
                        print("Sorry Your Answer Is Incorrect")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input23=int(input("Enter your choice:"))
                        
                    elif R_Q1_ans=="d" or R_Q1_ans=="D":
                        print("Congratulation Your answer is correct")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input23=int(input("Enter your choice:"))

                    if input23==2:
                        print("Thank you visit again")
                        break

                    elif input23==1:
                        print()
                        print("2. The citizenship Act, 1955 doesnot deal with")
                        print("a. acquistion")
                        print("b. termination")
                        print("c. election.")
                        print("d. determination")
                        R_Q2_ans=input("Enter your choice:")

                        if R_Q2_ans=="a" or R_Q2_ans=="A" or R_Q2_ans=="b" or R_Q2_ans=="B" or R_Q2_ans=="d" or R_Q2_ans=="D":
                            print("Sorry Your Answer Is Incorrect")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input25=int(input("Enter your choice:"))
                                    
                        elif R_Q2_ans=="c" or R_Q2_ans=="C":
                            print("Congratulation Your answer is correct")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input25=int(input("Enter your choice:"))

                        if input25==2:
                            print("Thank you visit again")
                            break

                        elif input25==1:
                            print()
                            print("3. Which of the following is are consumer rights")
                            print("a. Right to information")
                            print("b. Right to safety ")
                            print("c. Right to seek redressal")
                            print("d. More than one of the above")
                            R_Q3_ans=input("Enter your choice:")

                            if R_Q3_ans=="a" or R_Q3_ans=="A" or R_Q3_ans=="b" or R_Q3_ans=="B" or R_Q3_ans=="c" or R_Q3_ans=="C":
                                print("Sorry Your Answer Is Incorrect")
                                print()
                                print("Please select the category : ")
                                print("1 Continue")
                                print("2 Exit")
                                input27=int(input("Enter your choice:"))

                            elif R_Q3_ans=="d" or R_Q3_ans=="D":
                                print("Congratulation Your answer is correct")
                                print()
                                print("Please select the category : ")
                                print("1 Continue")
                                print("2 Exit")
                                input27=int(input("Enter your choice:"))

                            if input27==2:
                                print("Thank you visit again")
                                break 

                            elif input27==1:
                                print()
                                print("4. As part of the fundamental rights, the Constitution of Indian gurantees the right to ")
                                print("a. Divorce")
                                print("b. Equality")
                                print("c. Travel")
                                print("d. Marriage")
                                R_Q4_ans=input("Enter your choice:")

                                if R_Q4_ans=="a" or R_Q4_ans=="A":
                                    print("Congratulation Your answer is correct")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input29=int(input("Enter your choice:"))
                                            
                                elif R_Q4_ans=="b" or R_Q4_ans=="B" or R_Q4_ans=="c" or R_Q4_ans=="C" or R_Q4_ans=="d" or R_Q4_ans=="D":
                                    print("Sorry Your Answer Is Incorrect")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input29=int(input("Enter your choice:"))

                                if input29==2:
                                    print("Thank you visit again")
                                    break

                                elif input29==1:
                                    print()
                                    print("5. Right to freedom as under Article 19 is automatically suspended when a proclamation of emergency is made under which of the following grounds")
                                    print("a. Armed rebellion")
                                    print("b. War or external aggression")
                                    print("c. Loss of election")
                                    print("d. Internal disturbance")
                                    R_Q5_ans=input("Enter your choice:")

                                    if R_Q5_ans=="a" or R_Q5_ans=="A" or R_Q5_ans=="c" or R_Q5_ans=="C" or R_Q5_ans=="d" or R_Q5_ans=="D":
                                        print("Sorry Your Answer Is Incorrect")
                                        print()
                                        print("Thank you visit again")
                                        break

                                    elif R_Q5_ans=="b" or R_Q5_ans=="B":
                                        print("Congratulation Your answer is correct")
                                        print()
                                        print("Thank you visit again")
                                        break

                                        mycursor.execute("Insert into r values('"+Registration_ID+"','"+Name+"','"+R_Q1_ans+"','"+R_Q2_ans+"','"+R_Q3_ans+"','"+R_Q4_ans+"','"+R_Q5_ans+"');")
                                        conn.commit()
                                        break


            elif input3==6:
                while True:
                    Registration_ID=input("Registration Id: ")
                    Name=input("Name: ")
                    print("************************Laws***********************")
                    print("1. Which provision of the Constitution of India abolished 'Untouchability, and forbids its in any form ?")
                    print("a. Article 18")
                    print("b. Article 17")
                    print("c. Article 16")
                    print("d. Article 15")
                    L_Q1_ans=input("Enter your choice:")

                    if L_Q1_ans=="a" or L_Q1_ans=="A"or L_Q1_ans=="c" or L_Q1_ans=="C" or L_Q1_ans=="d" or L_Q1_ans=="D":
                        print("Sorry Your Answer Is Incorrect")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input23=int(input("Enter your choice:"))
                        
                    elif L_Q1_ans=="b" or L_Q1_ans=="B":
                        print("Congratulation Your answer is correct")
                        print()
                        print("Please select the category : ")
                        print("1 Continue")
                        print("2 Exit")
                        input23=int(input("Enter your choice:"))

                    if input23==2:
                        print("Thank you visit again")
                        break

                    elif input23==1:
                        print()
                        print("2. How many parts are there in Indian constituiton?")
                        print("a.22 ")
                        print("b.28 ")
                        print("c.18 ")
                        print("d.25 ")
                        L_Q2_ans=input("Enter your choice:")

                        if L_Q2_ans=="a" or L_Q2_ans=="A" or L_Q2_ans=="b" or L_Q2_ans=="B" or L_Q2_ans=="d" or L_Q2_ans=="D":
                            print("Sorry Your Answer Is Incorrect")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input25=int(input("Enter your choice:"))
                                    
                        elif L_Q2_ans=="c" or L_Q2_ans=="C":
                            print("Congratulation Your answer is correct")
                            print()
                            print("Please select the category : ")
                            print("1 Continue")
                            print("2 Exit")
                            input25=int(input("Enter your choice:"))

                        if input25==2:
                            print("Thank you visit again")
                            break

                        elif input25==1:
                            print()
                            print("3.What is the longest chapter in the Indian constitution? ")
                            print("a.Fundamental rights  ")
                            print("b.Union and state territories ")
                            print("c.Constitution of India ")
                            print("d.Directive principles of state policy ")
                            L_Q3_ans=input("Enter your choice:")

                            if L_Q3_ans=="a" or L_Q3_ans=="A" or L_Q3_ans=="b" or L_Q3_ans=="B" or L_Q3_ans=="c" or L_Q3_ans=="C":
                                print("Sorry Your Answer Is Incorrect")
                                print()
                                print("Please select the category : ")
                                print("1 Continue")
                                print("2 Exit")
                                input27=int(input("Enter your choice:"))

                            elif L_Q3_ans=="d" or L_Q3_ans=="D":
                                print("Congratulation Your answer is correct")
                                print()
                                print("Please select the category : ")
                                print("1 Continue")
                                print("2 Exit")
                                input27=int(input("Enter your choice:"))

                            if input27==2:
                                print("Thank you visit again")
                                break 

                            elif input27==1:
                                print()
                                print("4.Which artical of Indian constitution deals with right to equality ")
                                print("a.Article 14 ")
                                print("b.Article 15 ")
                                print("c.Article 16 ")
                                print("d.Article 17 ")
                                L_Q4_ans=input("Enter your choice:")

                                if L_Q4_ans=="a" or L_Q4_ans=="A":
                                    print("Congratulation Your answer is correct")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input29=int(input("Enter your choice:"))
                                            
                                elif L_Q4_ans=="b" or L_Q4_ans=="B" or L_Q4_ans=="c" or L_Q4_ans=="C" or L_Q4_ans=="d" or L_Q4_ans=="D":
                                    print("Sorry Your Answer Is Incorrect")
                                    print()
                                    print("Please select the category : ")
                                    print("1 Continue")
                                    print("2 Exit")
                                    input29=int(input("Enter your choice:"))

                                if input29==2:
                                    print("Thank you visit again")
                                    break

                                elif input29==1:
                                    print()
                                    print("5.Which article of the Indian constitution deals with the right to freedom of speech and expression? ")
                                    print("a.Article 18 ")
                                    print("b.Article 19 ")
                                    print("c.Article 20 ")
                                    print("d.Article 21 ")
                                    L_Q5_ans=input("Enter your choice:")

                                    if L_Q5_ans=="a" or L_Q5_ans=="A" or L_Q5_ans=="c" or L_Q5_ans=="C" or L_Q5_ans=="d" or L_Q5_ans=="D":
                                        print("Sorry Your Answer Is Incorrect")
                                        print()
                                        print("Thank you visit again")
                                        break

                                    elif L_Q5_ans=="b" or L_Q5_ans=="B":
                                        print("Congratulation Your answer is correct")
                                        print()
                                        print("Thank you visit again")
                                        break

                                        mycursor.execute("Insert into law values('"+Registration_ID+"','"+Name+"','"+L_Q1_ans+"','"+L_Q2_ans+"','"+L_Q3_ans+"','"+L_Q4_ans+"','"+L_Q5_ans+"');")
                                        conn.commit()
                                        break

    elif input1==3:
        print("Thank you visit again")
        break

                
            
