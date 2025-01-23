import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import os
import platform

def clrscreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_connection():
    """Create and return a database connection."""
    return mysql.connector.connect(user='root', password='123', host='localhost', database='Library')

# User Management Functions
def insertUser():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        
        mno = input("Enter Member Code : ")
        mname = input("Enter Member Name : ")
        print("Enter Date of Membership (Date/Month and Year separately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        addr = input("Enter Member Address : ")
        mob = input("Enter Member Mobile No. : ")

        qry = ("INSERT INTO Member VALUES (%s, %s, %s, %s, %s)")
        data = (mno, mname, date(YY, MM, DD), addr, mob)
        
        cursor.execute(qry, data)
        cnx.commit()
        
        print("User Record Inserted.")
    except mysql.connector.Error as err:
        handle_db_error(err)
    finally:
        cursor.close()
        cnx.close()

# Other existing functions...
def updateUser():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        
        mno = input("Enter Member Code of Member to be Updated: ")
        
        print("Enter new data")
        mname = input("Enter New Member Name : ")
        print("Enter Date of Membership (Date/Month and Year separately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        addr = input("Enter New Member Address : ")
        mob = input("Enter New Member's mobile no : ")

        qry = ("UPDATE Member SET Mname=%s, Date_of_Membership=%s, Addr=%s, Mob=%s WHERE Mno=%s")
        data = (mname, date(YY, MM, DD), addr, mob, mno)
        
        cursor.execute(qry, data)
        cnx.commit()
        
        print(cursor.rowcount,"User Record(s) Updated Successfully.")
    except mysql.connector.Error as err:
        handle_db_error(err)
    finally:
       cursor.close()
       cnx.close()

def deleteUser():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        
        mno = input("Enter Member Code to be deleted from the Library: ")
        
        qry = ("DELETE FROM Member WHERE MNO = %s")
        del_rec = (mno,)
        
        cursor.execute(qry, del_rec)
        cnx.commit()
        
        print(cursor.rowcount,"User Record(s) Deleted Successfully.")
    except mysql.connector.Error as err:
       handle_db_error(err)
    finally:
       cursor.close()
       cnx.close()

def searchUser():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        
        mno = input("Enter Member No to be Searched from the Library: ")
        
        query = ("SELECT * FROM Member WHERE MNO = %s")
        rec_srch = (mno,)
        
        cursor.execute(query, rec_srch)
        
        rec_count = 0
        for (Mno, Mname, Date_of_Membership, Addr, Mob) in cursor:
            rec_count += 1
            print("=============================================================")
            print(f"Member Code : {Mno}")
            print(f"Member Name : {Mname}")
            print(f"Date of Membership : {Date_of_Membership}")
            print(f"Address : {Addr}")
            print(f"Mobile No. of Member : {Mob}")
            print("=============================================================")

            if rec_count % 2 == 0:
                input("Press any key to continue")
                clrscreen()

            print(rec_count,"Record(s) found")
    except mysql.connector.Error as err:
       handle_db_error(err)
    finally:
       cursor.close()
       cnx.close()

# Catalog Management Functions
def insertBook():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        bno = input("Enter Book Code: ")
        bname = input("Enter Book Name: ")
        auth = input("Enter Author's Name: ")
        price = float(input("Enter Price: "))
        publ = input("Enter Publisher: ")
        
        qry = ("INSERT INTO BookRecord VALUES (%s, %s, %s, %s, %s)")
        data = (bno, bname, auth, price, publ)

        cursor.execute(qry, data)
        cnx.commit()

        print("Book Record Inserted.")
    except mysql.connector.Error as err:
       handle_db_error(err)
    finally:
       cursor.close()
       cnx.close()

def updateBook():
    try:
      cnx = get_connection()
      cursor = cnx.cursor()

      bno = input("Enter Book Code of Book to be Updated: ")

      print("Enter new data")
      bname = input("Enter New Book Name: ")
      auth = input("Enter New Author's Name: ")
      price = float(input("Enter New Price: "))
      publ = input("Enter New Publisher: ")

      qry = ("UPDATE BookRecord SET BName=%s, Auth=%s, Price=%s, Publ=%s WHERE BNO=%s")
      data = (bname, auth, price, publ, bno)

      cursor.execute(qry,data)
      cnx.commit()

      print(cursor.rowcount,"Book Record(s) Updated Successfully.")
    except mysql.connector.Error as err:
       handle_db_error(err)
    finally:
       cursor.close()
       cnx.close()

def deleteBook():
    try:
       cnx = get_connection()
       cursor = cnx.cursor()

       bno = input("Enter Book Code of Book to be deleted from the Library: ")

       qry = ("DELETE FROM BookRecord WHERE BNO=%s")
       del_rec =(bno,)
       
       cursor.execute(qry, del_rec)
       cnx.commit()

       print(cursor.rowcount,"Book Record(s) Deleted Successfully.")
    except mysql.connector.Error as err:
       handle_db_error(err)
    finally:
       cursor.close()
       cnx.close()

def searchBook():
    try:
       cnx= get_connection()
       cursor=cnx.cursor()

       bno=input("Enter Book Code to be Searched from the Library: ")

       query=("SELECT * FROM BookRecord WHERE BNO=%s")
       rec_srch=(bno,)
       
       cursor.execute(query , rec_srch)

       rec_count=0
       
       for (Bno,Bname , Author , price , publ) in cursor :
           rec_count+=1
           print("===============================")
           print(f"Book Code : {Bno}")
           print(f"Book Name : {Bname}")
           print(f"Author of Book : {Author}")
           print(f"Price of Book : {price}")
           print(f"Publisher : {publ}")
           print("===============================")

           if rec_count%2==0 :
               input("Press any key to continue")
               clrscreen()

           print(rec_count,"Record(s) found")
    except mysql.connector.Error as err:
         handle_db_error(err)
    finally:
         cursor.close()
         cnx.close()

# Fee Management Functions
def addFeeStructure():
    try:
         cnx=get_connection()
         cursor=cnx.cursor()

         fee_type=input("Enter Fee Type (e.g., Regular/Student): ")
         amount=float(input("Enter Amount for this Fee Type: "))

         qry=("INSERT INTO FeeStructure (FeeType, Amount) VALUES (%s,%s)")
         data=(fee_type , amount)

         cursor.execute(qry,data)
         cnx.commit()

         print ("Fee Structure Added Successfully.")
         
     except mysql.connector.Error as err :
          handle_db_error(err)

     finally :
          cursor.close() 
          cnx.close() 

def recordPayment():
     try :
          cnx=get_connection() 
          cursor=cnx.cursor() 

          mno=input ("Enter Member Code for Payment: ") 
          amount=float(input ("Enter Amount Paid: ")) 

          qry=("INSERT INTO Payments (MNO , Amount , PaymentDate) VALUES (%s,%s,%s)") 
          data=(mno , amount , date.today()) 

          cursor.execute(qry,data) 
          cnx.commit() 

          print ("Payment Recorded Successfully.") 

     except mysql.connector.Error as err :
          handle_db_error(err)

     finally :
          cursor.close() 
          cnx.close() 

def calculateFine(mno):
     """Calculate fine for overdue books."""
     try:
         today=date.today()
         fine_per_day=0.5  # Adjust fine per day as needed

         query=("SELECT d_o_ret FROM issue WHERE MNO=%s AND d_o_ret < %s") 
         rec_srch=(mno , today)

         # Calculate total fine based on overdue books
         with get_connection() as conn:
             with conn.cursor() as cur:
                 cur.execute(query , rec_srch)

                 total_fine=0
                 for (due_date,) in cur.fetchall():
                     days_overdue=(today - due_date).days
                     total_fine+=days_overdue * fine_per_day

                 return total_fine

     except mysql.connector.Error as err :
          handle_db_error(err)

# Dynamic Reporting Functions
def mostPopularBooks():
    try:
         cnx=get_connection() 
         cursor=cnx.cursor() 

         query="""SELECT BNO,BName,count(*) AS IssueCount 
                  FROM issue 
                  JOIN BookRecord ON issue.BNO=BookRecord.BNO 
                  GROUP BY BNO,BName 
                  ORDER BY IssueCount DESC LIMIT 5""" 

         cursor.execute(query) 

         results=cursor.fetchall() 

         if results: 
             print("\nMost Popular Books:\n") 
             for row in results: 
                 bno,bname,count=row 
                 print(f"Book Code: {bno}, Book Name: {bname}, Issued Count: {count}") 
         else: 
             print("\nNo records found.") 

     except mysql.connector.Error as err :
          handle_db_error(err)

     finally :
          cursor.close() 
          cnx.close() 

def mostActiveMembers():
     try:
         cnx=get_connection() 
         cursor=cnx.cursor() 

         query="""SELECT MNO,Mname,count(*) AS IssueCount 
                  FROM issue 
                  JOIN Member ON issue.MNO=Member.MNO 
                  GROUP BY MNO,Mname 
                  ORDER BY IssueCount DESC LIMIT 5""" 

         cursor.execute(query) 

         results=cursor.fetchall() 

         if results: 
             print("\nMost Active Members:\n") 
             for row in results: 
                 mno,mname,count=row 
                 print(f"Member Code: {mno}, Member Name: {mname}, Issued Count: {count}") 
         else: 
             print("\nNo records found.") 

     except mysql.connector.Error as err :
          handle_db_error(err)

     finally :
          cursor.close() 
          cnx.close() 

def booksIssuedLastMonth():
     try:
         today=datetime.today() 
         last_month=today - timedelta(days=30) 

         query="""SELECT BNO,BName FROM issue 
                  JOIN BookRecord ON issue.BNO=BookRecord.BNO 
                  WHERE d_o_issue >= %s""" 

         with get_connection() as conn: 
             with conn.cursor() as cur: 
                 cur.execute(query,(last_month,))
                 results=cur.fetchall() 

                 if results:  
                     print("\nBooks Issued in the Last Month:\n")  
                     for row in results:  
                         bno,bname=row  
                         print(f"Book Code: {bno}, Book Name: {bname}")  
                 else:  
                     print("\nNo records found.")  

     except mysql.connector.Error as err :
          handle_db_error(err)

# Enhanced User Interactivity Functions
def notifyUsersAboutOverdueBooks():
    """Notify users about overdue books."""
    today=date.today()
    
    query=("SELECT MNO,Mname,d_o_ret FROM issue "
           "JOIN Member ON issue.MNO=Member.MNO "
           "WHERE d_o_ret < %s")

    with get_connection() as conn:
         with conn.cursor() as cur:
             cur.execute(query,(today,))
             overdue_records=cur.fetchall()

             if overdue_records:
                 for record in overdue_records:
                     mno,mname,due_date=record
                     days_overdue=(today - due_date).days
                     fine_amount=days_overdue * 0.5  # Assuming $0.5 per day fine
                     # Here you can implement actual notification logic (e.g., email/SMS notifications)
                     print(f"Notification sent to {mname} ({mno}): You have an overdue book! Total fine is ${fine_amount:.2f}.")
             else:
                 print("\nNo overdue notifications to send.")

# Acquisition Management Functions
def addAcquisition():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        bno = input("Enter Book Code: ")
        bname = input("Enter Book Name: ")
        auth = input("Enter Author's Name: ")
        price = float(input("Enter Price: "))
        publ = input("Enter Publisher: ")

        # Insert into BookRecord first
        qry_book = ("INSERT INTO BookRecord (BNO, BName, Auth, Price, Publ) VALUES (%s, %s, %s, %s, %s)")
        data_book = (bno, bname, auth, price, publ)
        
        cursor.execute(qry_book, data_book)

        # Now insert into Acquisition record
        qry_acquisition = ("INSERT INTO Acquisitions (BNO) VALUES (%s)")
        data_acquisition = (bno,)
        
        cursor.execute(qry_acquisition, data_acquisition)
        
        cnx.commit()

        print("Acquisition Record Added Successfully.")
    except mysql.connector.Error as err:
       handle_db_error(err)
    finally:
       cursor.close()
       cnx.close()

def receiveGoods():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        bno = input("Enter Book Code for Received Goods: ")

        # Update the status in the Acquisitions table or similar logic
        qry_receive = ("UPDATE Acquisitions SET Status='Received' WHERE BNO=%s")
        
        cursor.execute(qry_receive, (bno,))
        
        cnx.commit()

        print(f"Goods for Book Code {bno} marked as received.")
    except mysql.connector.Error as err:
       handle_db_error(err)
    finally:
       cursor.close()
       cnx.close()

def processInvoice():
    try:
         cnx=get_connection() 
         cursor=cnx.cursor() 

         bno=input("Enter Book Code for Invoice Processing: ")
         invoice_number=input("Enter Invoice Number: ")
         invoice_date=input("Enter Invoice Date (YYYY-MM-DD): ")

         qry=("INSERT INTO Invoices (BNO , InvoiceNumber , InvoiceDate) VALUES (%s,%s,%s)") 
         data=(bno , invoice_number , invoice_date) 

         cursor.execute(qry,data) 
         cnx.commit() 

         print ("Invoice Processed Successfully.") 

     except mysql.connector.Error as err :
          handle_db_error(err)

     finally :
          cursor.close() 
          cnx.close() 

# Main Program Execution
if __name__ == "__main__":
     Database.DatabaseCreate()  # Assuming this function exists
     Database.TablesCreate()     # Assuming this function exists

     while True:
          clrscreen()
          print("\t\t\t Library Management\n")
          print("==============================================================")
          print("1. User Management")  
          print("2. Catalog Management")  
          print("3. Acquisition Management")  # Added option for acquisition management
          print("4. Issue/Return Book")  
          print("5. Renew a Book")  
          print("6. Fee Management")  
          print("7. Dynamic Reporting")  
          print("8. Exit")

          choice=int(input ("Enter Choice between 1 to 8 -------> : "))

          if choice == 1:
              while True:
                  clrscreen()
                  print("\t\t\t User Management\n")
                  print("===============================")
                  print ("1. Add User")
                  print ("2. Update User")
                  print ("3. Delete User")
                  print ("4. Search User")
                  print ("5. Return to Main Menu")

                  user_choice=int(input ("Choose an option (1-5): "))

                  if user_choice == 1:
                      insertUser()
                  elif user_choice == 2:
                      updateUser()
                  elif user_choice == 3:
                      deleteUser()
                  elif user_choice == 4:
                      searchUser()
                  elif user_choice == 5:
                      break
                  else:
                      print ("Invalid choice! Please select again.")

          elif choice == 2:  # Catalog Management Menu
              while True:
                  clrscreen()
                  print("\t\t\t Catalog Management\n")
                  print("===============================")
                  print ("1. Add Book")
                  print ("2. Update Book")
                  print ("3. Delete Book")
                  print ("4. Search for Books")
                  print ("5. Return to Main Menu")

                  catalog_choice=int(input ("Choose an option (1-5): "))

                  if catalog_choice == 1:
                      insertBook() 
                  elif catalog_choice == 2:
                      updateBook() 
                  elif catalog_choice == 3:
                      deleteBook() 
                  elif catalog_choice == 4:
                      searchBook() 
                  elif catalog_choice == 5:
                      break 
                  else:
                      print ("Invalid choice! Please select again.")

          elif choice == 3:  # Acquisition Management Menu
              while True:
                   clrscreen()
                   print("\t\t\t Acquisition Management\n")
                   print("===============================")
                   print ("1. Add Acquisition")
                   print ("2. Receive Goods")
                   print ("3. Process Invoice")
                   print ("4. Return to Main Menu")

                   acquisition_choice=int(input ("Choose an option (1-4): "))

                   if acquisition_choice == 1:
                       addAcquisition() 
                   elif acquisition_choice == 2:
                       receiveGoods() 
                   elif acquisition_choice == 3:  
                       processInvoice()   
                   elif acquisition_choice == 4:  
                       break   
                   else:  
                       print ("Invalid choice! Please select again.")

          elif choice == 4: 
              Menulib.MenuIssueReturn() # Assuming this function exists

          elif choice == 5: 
              renewBook()  

          elif choice == 6:  
              # Fee management code here...
              # Fee Management Menu
             while True:
                  clrscreen()
                  printf("\t\t\t Fee Management\n")
                  printf("===============================")
                  printf ("1. Add Fee Structure")
                  printf ("2. Record Payment")
                  printf ("3. Calculate Fine for a Member")
                  printf ("4. Return to Main Menu")

                  fee_choice=int(input ("Choose an option (1-4): "))

                  if fee_choice == 1:
                      addFeeStructure() 
                  elif fee_choice == 2:
                      recordPayment() 
                  elif fee_choice == 3:  
                      mno=input ("Enter Member Code to calculate fine: ")  
                      total_fine=calculateFine(mno)  
                      if total_fine > 0:  
                          printf(f"Total Fine for member {mno}: ${total_fine:.2f}")  
                      else:  
                          printf(f"No outstanding fines for member {mno}.")  
                  elif fee_choice == 4:  
                      break  
                  else:  
                      printf ("Invalid choice! Please select again.")


          elif choice == 7:  
              # Dynamic reporting code here...
              # Dynamic Reporting Menu
              while True:
                   clrscreen()
                   printf("\t\t\t Dynamic Reporting\n")
                   printf("===============================")
                   printf ("1. Most Popular Books")
                   printf ("2. Most Active Members")
                   printf ("3. Books Issued in the Last Month")
                   printf ("4. Return to Main Menu")

                   report_choice=int(input ("Choose an option (1-4): "))

                   if report_choice == 1:
                       mostPopularBooks() 
                   elif report_choice == 2:
                       mostActiveMembers()  
                   elif report_choice == 3:  
                       booksIssuedLastMonth()   
                   elif report_choice == 4:  
                       break   
                   else:  
                       printf ("Invalid choice! Please select again.")


          elif choice == 8: # Exit option
              break 

          else: # Invalid choice handling
              print ("Invalid choice! Please select again.")
