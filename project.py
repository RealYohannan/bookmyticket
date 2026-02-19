
import pandas as pd
from tabulate import tabulate 

while True:
    print("----------Main Menu----------")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    ch= input("Enter your choice: ")
    if ch==3:
        break
    elif ch=='1':
        aduser=input("Enter Admin User: ")
        adpass=input("Enter admin password: ")
        if adpass=="ilovemovies@1234" and aduser=="TheAdmin":
            while True:
                print("="*50)
                print(""*15 + "\t*** ADMIN MOVIE MANAGEMENT MENU ***")
                print("="*50)
                print("\n\t1. Add Movie Details")
                print("\t2. Edit Movie Details")
                print("\t3. Delete Movie Details")
                print("\t4. Display All Movie Details")
                print("\t5. Display All Bookings")
                print("\t6. Exit")
                print("="*50)
                ch=int(input('Enter your choice:'))
                
                if ch==6:
                    break
                
                elif ch==1:
                    L=[]
                    mid=int(input('Enter Movie ID:'))
                    mname=input('Enter movie name:')
                    gen=input('Enter genre:')
                    lan=input('Enrer Language:')
                    dor=input('Enter date of release:')
                    mc=input('Enter main actor/actress:')
                    di=input('Enter director name:')
                    L.append([mid,mname,gen,lan,dor,mc,di,250])
                    df1=pd.DataFrame(L)
                    df1.to_csv('MOVIE_CSV.csv',mode='a',index=False,header=False)
                    print("Movie details added successfully!")
                    print()
                elif ch==2:
                    B=['Movie ID' ,'Movie Name' ,'Genre' ,'Date of Release' ,'Main Role' ,'Director','Seats Available']
                    DF=pd.read_csv('MOVIE_CSV.csv')
                    midd=int(input('Enter the movie ID'))
                    X=DF[DF['Movie ID']==midd]
                    if X.empty:
                        pass
                    else:
                        while True:
                            
                            print()
                            print('Choose the following to edit')
                            print('1.Movie name')
                            print('2.Genre')
                            print('3.Date of release')
                            print('4.Main Role')
                            print('5.Director')
                            print('6.Seats Available')
                            print('7.Exit')
                            print()
                            ch=int(input('Enter your choice:'))
                            if ch==1:
                                print(tabulate(X,headers='keys',tablefmt='fancy_grid'))
                                N=input('Enter NEW movie name:')
                                DF.loc[DF['Movie ID']==midd,'Movie Name']=N
                                DF.to_csv('MOVIE_CSV.csv',index=False,header=B)
                                print('Data is updated sucessfully')
                                df1=pd.read_csv('MOVIE_CSV.csv')
                                print(df1)
                            elif ch==2:
                                print(tabulate(X,headers='keys',tablefmt='fancy_grid'))
                                N=input('Enter NEW genre:')
                                DF.loc[DF['Movie ID']==midd,'Genre']=N
                                DF.to_csv('MOVIE_CSV.csv',index=False,header=B)
                                print('Data is updated sucessfully')
                                df1=pd.read_csv('MOVIE_CSV.csv')
                                print(df1)
                            elif ch==3:
                                print(tabulate(X,headers='keys',tablefmt='fancy_grid'))
                                N=input('Enter NEW date of release:')
                                DF.loc[DF['Movie ID']==midd,'Date of Release']=N
                                DF.to_csv('MOVIE_CSV.csv',index=False,header=B)
                                print('Data is updated sucessfully')
                                df1=pd.read_csv('MOVIE_CSV.csv')
                                print(df1)
                            elif ch==4:
                                print(tabulate(X,headers='keys',tablefmt='fancy_grid'))
                                N=input('Enter NEW main role:')
                                DF.loc[DF['Movie ID']==midd,'Main Role']=N
                                DF.to_csv('MOVIE_CSV.csv',index=False,header=B)
                                print('Data is updated sucessfully')
                                df1=pd.read_csv('MOVIE_CSV.csv')
                                print(df1)
                            elif ch==5:
                                print(tabulate(X,headers='keys',tablefmt='fancy_grid'))
                                N=input('Enter NEW Diretor:')
                                DF.loc[DF['Movie ID']==midd,'Director']=N
                                DF.to_csv('MOVIE_CSV.csv',index=False,header=B)
                                print('Data is updated sucessfully')
                                df1=pd.read_csv('MOVIE_CSV.csv')
                                print(df1)
                            elif ch==6:
                                print(tabulate(X,headers='keys',tablefmt='fancy_grid'))
                                N=int(input('Enter NEW Seats Available:'))
                                DF.loc[DF['Movie ID']==midd,'Seats Available']=N
                                DF.to_csv('MOVIE_CSV.csv',index=False,header=B)
                                print('Data is updated sucessfully')
                                df1=pd.read_csv('MOVIE_CSV.csv')
                                print(df1)
                            else:
                                break
                elif ch=='3':
                    B=['Movie ID' ,'Movie Name' ,'Genre' ,'Date of Release' ,'Main Role' ,'Director','Seats Available']
                    DF=pd.read_csv('MOVIE_CSV.csv')
                    midd=int(input('Enter the movie ID'))
                    X=DF[DF['Movie ID']==midd]
                    if X.empty:
                        pass
                    else:
                        print(X)
                        print()
                        C=input("Do you wish to delete this record?(Y/N)")
                        if C=='y' or C=='Y':
                            DF.drop(DF[DF["Movie ID"]==midd].index,inplace=True)
                            DF.to_csv("MOVIE_CSV.csv",index=False,header=B)
                            print("Data is successfully deleted")
                            df1=pd.read_csv('MOVIE_CSV.csv')
                            print(df1)
                        else:
                            pass
                elif ch==4:
                    DF=pd.read_csv('MOVIE_CSV.csv')
                    print("Details of all ongoing movies:")
                    print(tabulate(DF,headers='keys',tablefmt='fancy_grid'))
                    
                elif ch==5:
                    DF=pd.read_csv('BOOK_CSV.csv')
                    print("All Bookings Till Now:")
                    print(tabulate(DF,headers='keys',tablefmt='fancy_grid'))                    
                    
                else:
                     break
        else:
            print("Invalid admin user and password.")

    elif ch=='2':
        while True:
            print(("-----------------USER MENU------------------").center(100))
            print("1. Sign Up")
            print("2. Sign In")
            print("3. Exit")

            uch=input("Enter your choice: ")
            if uch=='3':
                break

            elif uch=='1':
                L=[]
                uname=input("Enter a username: ")
                password=input("Enter a password: ")
                L.append([uname,password])
                df1=pd.DataFrame(L)
                df1.to_csv('USER_CSV.csv',mode='a',index=False,header=False)
                print("Sign up successful!")
                print("Please sign in now!")

            elif uch== '2':
                L=[]
                username=input("Enter your username: ")
                password=input("Enter your password: ")
                df=pd.read_csv('USER_CSV.csv')

                if ((df['Username']==username)&(df['Password']==password)).all():
                    print("Sign in successful!")
                    while True:
                        print("---------------------USER MENU---------------------")
                        print("1.Check details of all ongoing movies")
                        print("2.Book a ticket")
                        print("3.Cancel a ticket")
                        print("4.Rate a movie")
                        print("5.Watch a Trailer")
                        print("6.Book a show")
                        print("7.Sort by Language")
                        print("8.Leave a movie review")
                        print("9.Exit")
                        ch=int(input('Enter your choice:'))
                        if ch==0:
                            break
                        elif ch==1:
                            DF=pd.read_csv('MOVIE_CSV.csv')
                            print("Ongoing Movies:")
                            print(DF)
                        elif ch==2:
                            amt=0
                            DF=pd.read_csv('MOVIE_CSV.csv')
                            mid=int(input('Enter the movie ID'))
                            X=DF[DF['Movie ID']==mid]
                            print(X)
                            print()
                            C=input("Do you wish to book a ticket for this movie?(Y/N)")
                            if C=='Y' or C=='y':
                                print('1.Normal Seat -> ₹179')
                                print('2.Executive Seat -> ₹199')
                                print('3.Premium Seat -> ₹229')
                                tp=int(input('Enter your preference:'))
                                if tp==1:
                                    amt=amt+179
                                elif tp==2:
                                    amt=amt+199
                                elif tp==3:
                                    amt=amt+229
                                else:
                                    print('Invalid choice!')
                                    break
                                s=int(input('Enter number of seats:'))
                                amt=amt*s
                                DF.loc[DF['Movie ID']==mid,'Seats Available']=DF.loc[DF['Movie ID']==mid,'Seats Available']-s
                                B=['Movie ID' ,'Movie Name' ,'Genre' ,'Date of Release' ,'Main Role' ,'Director','Seats Available']
                                DF.to_csv('MOVIE_CSV.csv',index=False,header=B)
                                d=input('Enter the date:')
                                sn=''
                                sn=input('Add popcorn?(Y/N):')
                                if sn=='Y' or sn=='y':
                                    amt=amt+199
                                else:
                                    pass
                                amt=amt+23.60
                                print()
                                print('**(TIP:check our socials for any new coupon codes)**')
                                print()
                                code=''
                                c=input('Do you have a coupon code?(Y/N)')
                                if c=='Y' or c=='y':
                                    code=input('Enter your coupon code:')
                                    if code=='WELCOMECINEMA':
                                        print('CONGRATS!You got ₹50 OFF')
                                        amt=amt-50
                                    else:
                                        print('SORRY!Invalid/Expired Coupon code')
                                else:
                                    pass
                                DF1=pd.read_csv('BOOK_CSV.csv')
                                b=DF1.tail(1)
                                print(b)
                                ll=b["Book ID"]
                                print(ll)
                                BID=ll.iloc[0]
                                print()
                                print()
                                print('*************BookYourCinema**************')
                                print()
                                print('*****************E-RECIPT****************')
                                print('BOOK ID:',BID+101)
                                BID=BID+101
                                print('Movie ID:',mid)
                                print('Date:',d)
                                if tp==1:
                                    print('Ticket Price:179')
                                elif tp==2:
                                    print('Ticket Price:199')
                                elif tp==3:
                                    print('Ticket Price:229')
                                print('Number of seats:',s)
                                if sn=='Yes' or sn=='yes':
                                    print('\t+Popcorn:199')
                                else:
                                    pass
                                print('\t+Convenience Fee:20')
                                amt+=23.60
                                print('\t+Integrated GST(IGST)@18%:3.60')
                                if code=='WELCOMECINEMA':
                                    print('\t-Coupon Code:50')
                                else:
                                    pass
                                print('TOTAL',amt)
                                print('*****************************************')
                                print()
                                print()
                                print('**Choose a payment meathod:**')
                                print('1.Google pay')
                                print('2.Other UPI')
                                print('3.Internet Banking')
                                print('4.Debit Card')
                                print('5.Credit Card')
                                
                                p=int(input('Enter your payment meathod:'))
                                if p==1:
                                    gpay=input('Enter your gpay UPI ID:')
                                    print('Please make payment in the app now')
                                    print()
                                    print('**Thank you**')
                                elif p==2:
                                    upi=input('Enter your UPI ID:')
                                    print('Please make payment in the app now')
                                    print()
                                    print('**Thank you**')
                                elif p==3:
                                    ib=input('Enter your Internet Banking ID:')
                                    print('Please make payment in the app/website now')
                                    print()
                                    print('**Thank you**')
                                elif p==4:
                                    no=int(input('Enter your phone number:'))
                                    print('An SMS will be send to you please click the link to make the payment')
                                    print('**Thank you**')
                                elif p==5:
                                    no=int(input('Enter your phone number:'))
                                    print('An SMS will be send to you please click the link to make the payment')
                                    print('**Thank you**')
                                else:
                                    print('invalid payment meathod')
                                    break
                                data=[]                         
                                data.append([username,BID,mid,d,s,tp,sn,amt,p])
                                df2=pd.DataFrame(data)
                                df2.to_csv('Book_CSV.csv', mode='a', index=False, header=False)
                                while True:
                                    num=input('Enter your phone number: ')
                                    if len(str(num))==10:  
                                        print('Your Ticket has been sent to', num)
                                        break  
                                    else:
                                        print('Invalid phone number. Please enter a valid 10-digit phone number.')
                                print()
                                print('Your Ticket is Booked Successfully!')
                                print('Feel Free to book another one!')

                        elif ch==3:
                            B=['Username','Book ID','Movie ID','Date','Seats','Type','Popcorn','Amount','Payment Meathod']
                            DF3=pd.read_csv('BOOK_CSV.csv')
                            bid=int(input('Enter the Book ID'))
                            Q=DF3[DF3['Book ID']==bid]
                            if Q.empty:
                                pass
                            else:
                                print(Q)
                                print()
                                C=input("Do you wish cancel this ticket?(Y/N)")
                                if C=='y' or C=='Y':
                                    DF3.drop(DF3[DF3["Book ID"]==bid].index,inplace=True)
                                    DF3.to_csv("BOOK_CSV.csv",index=False,header=B)
                                    print()
                                    print("Sucessfully cancelled the ticket")
                                    print()
                                    print("**Refund will be reflected to your account within 2-3 business days**")
                                    print()
                                else:
                                    pass
                            


                        elif ch==4:
                            P=[]
                            m=int(input('Enter Movie ID:'))
                            r=int(input('Enter your rating(1-10):'))
                            P.append([m,username,r])
                            ra=pd.DataFrame(P)
                            ra.to_csv('RATING_CSV.csv',mode='a',index=False,header=False)
                            print('Rating given sucessfully')
                            
                        elif ch==6:
                            amt = 0
                            DF = pd.read_csv('SHOW_CSV.csv')
                            print()
                            print('******Displaying available shows******')
                            print('1.Stand up comedy')
                            print('2.Music concert')
                            print('3.Open mic')
                            print('4.Show all')
                            t=int(input('Enter type of show'))
                            print()
                            if t==1:
                                a=DF.loc[DF['Type']=='Stand up comedy']
                                print(tabulate(a,headers='keys',tablefmt='fancy_grid'))
                            elif t==2:
                                a=DF.loc[DF['Type']=='Music concert']
                                print(tabulate(a,headers='keys',tablefmt='fancy_grid'))
                            elif t==3:
                                a=DF.loc[DF['Type']=='Open mic']
                                print(tabulate(a,headers='keys',tablefmt='fancy_grid'))
                            elif t==4:
                                print(tabulate(DF,headers='keys',tablefmt='fancy_grid'))
                            sid=int(input('Enter the show ID: '))
                            X=DF[DF['Show ID'] == sid]
                            
                            if X.empty:
                                print('Show ID not found.')
                                break
                            else:
                                print(X)
                                print()
                            
                                C = input("Do you wish to book a ticket for this show? (Y/N): ")
                                tp=0
                                
                                if C == 'Y' or C == 'y':
                                    if sid==2:
                                        print('1.Standing(Floor)- 5000')
                                        print('2.Seating - 3000')
                                        print('3.VIP - 35000')
                                        tp = int(input('Enter your preference: '))
                                        if tp == 1:
                                            amt += 5000
                                            print()
                                        elif tp == 3:
                                            amt += 3000
                                            print()
                                        elif tp == 3:
                                            amt += 35000
                                            print()
                                        else:
                                            print('Invalid choice!')
                                            break
                                        
                                    elif sid==1:
                                        amt +=400
                                    elif sid==3:
                                        amt +=700
                                    elif sid==4:
                                        amt +=3000
                                        
                                    s = int(input('Enter number of seats: '))
                                    amt *= s
                                    DF.loc[DF['Show ID'] == sid, 'Seats Available'] -= s
                                    DF.to_csv('SHOW_CSV.csv', index=False)
                    
                                    DF1 = pd.read_csv('SBOOK_CSV.csv')
                                    b = DF1.tail(1)
                                    ll = b["Book ID"]
                                    BID = ll.iloc[0]
                                    print()
                                    print('************* BookYourCinema **************')
                                    print('***************** E-RECIPT ****************')
                                    print('BOOK ID:', BID + 101)
                                    BID += 101                
                                    print('Show ID:', sid)
                                    if tp == 1:
                                        print('Ticket Price: ₹5000')
                                    elif tp == 2:
                                        print('Ticket Price: ₹3000')
                                    elif tp == 3:
                                        print('Ticket Price: ₹35000')
                                    elif sid == 1:
                                        print('Ticket Price: ₹400')
                                    elif sid == 3:
                                        print('Ticket Price: ₹700')
                                    elif sid == 4:
                                        print('Ticket Price: ₹3000')
                                    print('Number of seats:', s)
                                    print('\t+ Convenience Fee: ₹20')
                                    amt+=23.60
                                    print('\t+ Integrated GST (IGST) @18%: ₹3.60')
                                    print('TOTAL:', amt)
                                    print('*****************************************')
                                    print()
                                    print()
                                    print('** Choose a payment method:**')
                                    print('1. Google Pay')
                                    print('2. Other UPI')
                                    print('3. Internet Banking')
                                    print('4. Debit Card')
                                    print('5. Credit Card')
                                    p = int(input('Enter your payment method: '))
                                    if p == 1:
                                        gpay = input('Enter your Google Pay UPI ID: ')
                                        print('Please make payment in the app now')
                                        print('** Thank you **')
                                    elif p == 2:
                                        upi = input('Enter your UPI ID: ')
                                        print('Please make payment in the app now')
                                        print('** Thank you **')
                                    elif p == 3:
                                        ib = input('Enter your Internet Banking ID: ')
                                        print('Please make payment in the app/website now')
                                        print('** Thank you **')
                                    elif p == 4 or p == 5:
                                        no = input('Enter your phone number: ')
                                        print('An SMS will be sent to you; please click the link to make the payment')
                                        print('** Thank you **')
                                    else:
                                        print('Invalid payment method')
                                        break
                                    data = []
                                    data.append([username, BID, sid, s, tp, amt, p])
                                    df2 = pd.DataFrame(data)
                                    df2.to_csv('SBOOK_CSV.csv', mode='a', index=False, header=False)
                                    while True:
                                        num = input('Enter your phone number: ')
                                        if len(str(num)) == 10:
                                            print('Your ticket has been sent to', num)
                                            break
                                        else:
                                            print('Invalid phone number. Please enter a valid 10-digit phone number.')
                                            print()
                                            print('Your ticket is booked successfully!')
                                            print('Feel free to book another one!')
                        elif ch==7:
                            print('**Select from the following***')
                            print('1.Malayalam')
                            print('2.English')
                            print('3.Hindi')
                            print('4.Tamil')
                            la=input('Enter the Language'))
                            
                             
                            

                else:
                    print("Invalid username or password.")

    else:
        print()
        print('Thank you for using BookYourCinema! Visit us again anytime!')
        break


