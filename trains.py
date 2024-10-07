#Defining the Function for searching Trains
def train_search():
        print("***(NOTE- While searching for trains, Please Start with Capital Letter.)***")
        print("***[--FOR EXAMPLE:- 'Your Origin:  Bilaspur']***")
        print()
        print()
        
#Provide the origin station
        user_input=input("Your Origin: ")
#Provide the destination station
        user_input1=input("Your Destination: ")
#Query to fetch trains between origin and destination
        query1= f"SELECT * FROM train_details WHERE origin='{user_input}' AND destination='{user_input1}' "
        cur.execute(query1)
        records=cur.fetchall()
        if len(records)==0:
                print("-----Enter Valid - [Origin/Destination]-----")
#Provide the Day of Travel
        else:
                user_input2=input("Day On Which You Wish to Travel: ")

                for row in records:
                        if user_input2==row[6] or user_input2==row[7] or user_input2==row[8] or user_input2==row[9] or user_input2==row[10] or user_input2==row[11] or user_input2==row[12]:
                                print("Total Number of Trains Found: ",cur.rowcount )
                                print("Train Number: ",row[0])
                                print("Train Name: ",row[1])
                                print("Origin Station: ",row[2])
                                print("Destination Station: ",row[3])
                                print("Departure Time: ",row[4])
                                print("Destination Arrival Time: ",row[5] )
                                print("On-time Efficiency: ",row[13])
                                print("Meal on Board: ",row[22])
                        else:
                                print("No Trains Available!!.. Try some Other Options [Origin/Destination/Day] ")
                                break

	

                
                        user_input3=input("In which Coach would you like to travell(Sleeper/3AC/2AC/1AC) ? : ")
                        if user_input3=='Sleeper':
                                print("Available SL seats :",row[14])
                                print("Fare for SL seat :",row[18])
                        elif user_input3=="3AC":
                                print("Available 3AC seats :", row[15])
                                print("Fare for 3AC seat : Rs. ", row[19])
                        elif user_input3=="2AC":
                                print("Available 2AC seats :", row[16])
                                print("Fare for 2AC seat : ", row[20])
                        elif user_input3=="1AC":
                                print("Available 1AC seats :", row[17])
                                print("Fare for 1AC seat : Rs. ", row[21])
                        else:
                                print("SORRY!! No seats are available of your choice")
        print()
        print("THANKYOU!! FOR USING OUR SERVICE")
        print()
#----MAIN FUNCTION----
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",password="743389")
query="use central_railways"

cur=mydb.cursor()
cur.execute(query)
while True: 
        choice=input("Do you want to search for Trains? , [ Yes/No ]:: ")
        if choice=="Yes":
                print()
                train_search()
        elif choice=="No":
                print("Thankyou! for using our service...")
                quit()
        else:
                print("INVALID SELECTION!!! Please Choose Valid Option. ")
        
        print()
        print()
