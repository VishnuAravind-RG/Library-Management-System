import cx_Oracle
from datetime import datetime
import os
import platform
import tkinter as tk
from tkinter import ttk, messagebox



# Database Connection
def get_connection():
    try:
        dsn = cx_Oracle.makedsn("10.1.67.153", 1522, service_name="orclNEW")
        return cx_Oracle.connect(user='msc23pt38', password='msc23pt38', dsn=dsn)
    except cx_Oracle.Error as err:
        print(f"Database connection error: {err}")
        return None



# Utility Functions
def clrscreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def insert_user():
    while True:
        try:
            cnx = get_connection()
            cursor = cnx.cursor()

            mno = input("Enter Member Code: ")
            mname = input("Enter Member Name: ")
            
            while True:
                try:
                    dom = input("Enter Date of Membership (YYYY-MM-DD): ")
                    dom_date = datetime.strptime(dom, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD format.")
            
            addr = input("Enter Address: ")
            mob = input("Enter Mobile Number: ")

            cursor.callproc("InsertUser", [mno, mname, dom_date, addr, mob])
            cnx.commit()
            print("User inserted successfully!")
            break
            
        except cx_Oracle.Error as err:
            print(f"Database Error: {err}")
            if "unique constraint" in str(err):
                print("Member code already exists. Please try a different code.")
            retry = input("Retry? (y/n): ").lower()
            if retry != 'y':
                break
        except ValueError as err:
            print(f"Invalid input: {err}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'cnx' in locals():
                cnx.close()

def update_user():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        mno = input("Enter Member Code to update: ")
        mname = input("Enter New Member Name: ")
        
        # Get date input with validation
        while True:
            dom = input("Enter New Date of Membership (YYYY-MM-DD): ")
            try:
                dom_date = datetime.strptime(dom, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
                
        addr = input("Enter New Address: ")
        mob = input("Enter New Mobile Number: ")

        cursor.callproc("UpdateUser", [mno, mname, dom_date, addr, mob])
        cnx.commit()
        print("User updated successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()
def delete_user():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        mno = input("Enter Member Code to delete: ")
        cursor.callproc("DeleteUser", [mno])
        cnx.commit()
        print("User deleted successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

def search_user():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        mno = input("Enter Member Code to search: ")
        ref_cursor = cursor.var(cx_Oracle.CURSOR)
        cursor.callproc("SearchUser", [mno, ref_cursor])

        result = ref_cursor.getvalue().fetchall()
        if result:
            for row in result:
                print(f"Member Code: {row[0]}, Name: {row[1]}, Date of Membership: {row[2]}, Address: {row[3]}, Mobile: {row[4]}")
        else:
            print("No user found!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

# Catalog Management
def insert_book():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        bno = input("Enter Book Code: ")
        bname = input("Enter Book Name: ")
        auth = input("Enter Author: ")
        price = float(input("Enter Price: "))
        publ = input("Enter Publisher: ")

        cursor.callproc("InsertBook", [bno, bname, auth, price, publ])
        cnx.commit()
        print("Book inserted successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

def update_book():
    while True:
        try:
            cnx = get_connection()
            cursor = cnx.cursor()

            bno = input("Enter Book Code to update: ")
            bname = input("Enter New Book Name: ")
            auth = input("Enter New Author: ")
            
            while True:
                try:
                    price = float(input("Enter New Price: "))
                    break
                except ValueError:
                    print("Invalid price. Please enter a numeric value.")
            
            publ = input("Enter New Publisher: ")

            cursor.callproc("UpdateBook", [bno, bname, auth, price, publ])
            cnx.commit()
            print("Book updated successfully!")
            break
            
        except cx_Oracle.Error as err:
            print(f"Database Error: {err}")
            retry = input("Retry? (y/n): ").lower()
            if retry != 'y':
                break
        except Exception as err:
            print(f"Error: {err}")
            retry = input("Retry? (y/n): ").lower()
            if retry != 'y':
                break
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'cnx' in locals():
                cnx.close()

def delete_book():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        bno = input("Enter Book Code to delete: ")
        cursor.callproc("DeleteBook", [bno])
        cnx.commit()
        print("Book deleted successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

def search_book():
    while True:
        try:
            cnx = get_connection()
            cursor = cnx.cursor()

            bno = input("Enter Book Code to search: ")
            ref_cursor = cursor.var(cx_Oracle.CURSOR)
            cursor.callproc("SearchBook", [bno, ref_cursor])

            result = ref_cursor.getvalue().fetchall()
            if result:
                for row in result:
                    print(f"Book Code: {row[0]}, Name: {row[1]}, Author: {row[2]}, Price: {row[3]}, Publisher: {row[4]}")
            else:
                print("No book found!")
            break
            
        except cx_Oracle.Error as err:
            print(f"Database Error: {err}")
            retry = input("Retry search? (y/n): ").lower()
            if retry != 'y':
                break
        except Exception as err:
            print(f"Error: {err}")
            retry = input("Retry search? (y/n): ").lower()
            if retry != 'y':
                break
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'cnx' in locals():
                cnx.close()

# Fee Management
def add_fee_structure():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        fee_type = input("Enter Fee Type: ")
        amount = float(input("Enter Amount: "))

        cursor.callproc("AddFeeStructure", [fee_type, amount])
        cnx.commit()
        print("Fee structure added successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

def record_payment():
    while True:
        try:
            cnx = get_connection()
            cursor = cnx.cursor()

            mno = input("Enter Member Code: ")
            
            while True:
                try:
                    amount = float(input("Enter Amount: "))
                    break
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")

            cursor.callproc("RecordPayment", [mno, amount])
            cnx.commit()
            print("Payment recorded successfully!")
            break
            
        except cx_Oracle.Error as err:
            print(f"Database Error: {err}")
            if "ORA-02291" in str(err):  # Integrity constraint violation
                print("Member does not exist. Please check the member code.")
            retry = input("Retry? (y/n): ").lower()
            if retry != 'y':
                break
        except Exception as err:
            print(f"Error: {err}")
            retry = input("Retry? (y/n): ").lower()
            if retry != 'y':
                break
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'cnx' in locals():
                cnx.close()

def calculate_fine():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        mno = input("Enter Member Code: ")
        fine = cursor.callfunc("CalculateFine", cx_Oracle.NUMBER, [mno])
        print(f"Total Fine for Member {mno}: ${fine:.2f}")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

# Dynamic Reporting
def most_popular_books():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        ref_cursor = cursor.var(cx_Oracle.CURSOR)
        cursor.callproc("MostPopularBooks", [ref_cursor])

        result = ref_cursor.getvalue().fetchall()
        if result:
            print("Most Popular Books:")
            for row in result:
                print(f"Book Code: {row[0]}, Name: {row[1]}, Issue Count: {row[2]}")
        else:
            print("No data found!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

def most_active_members():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        ref_cursor = cursor.var(cx_Oracle.CURSOR)
        cursor.callproc("MostActiveMembers", [ref_cursor])

        result = ref_cursor.getvalue().fetchall()
        if result:
            print("Most Active Members:")
            for row in result:
                print(f"Member Code: {row[0]}, Name: {row[1]}, Issue Count: {row[2]}")
        else:
            print("No data found!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()
        
        

def books_issued_last_month():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        ref_cursor = cursor.var(cx_Oracle.CURSOR)
        cursor.callproc("BooksIssuedLastMonth", [ref_cursor])

        result = ref_cursor.getvalue().fetchall()
        if result:
            print("Books Issued Last Month:")
            for row in result:
                print(f"Book Code: {row[0]}, Name: {row[1]}")
        else:
            print("No data found!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

# Notify Users About Overdue Books
def notify_overdue_books():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        cursor.callproc("NotifyOverdueBooks")
        cnx.commit()
        print("Notifications sent for overdue books!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

# Acquisition Management
def add_acquisition():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        bno = input("Enter Book Code: ")
        cursor.callproc("AddAcquisition", [bno])
        cnx.commit()
        print("Acquisition added successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

def receive_goods():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        bno = input("Enter Book Code: ")
        cursor.callproc("ReceiveGoods", [bno])
        cnx.commit()
        print("Goods received successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

def process_invoice():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        bno = input("Enter Book Code: ")
        invoice_number = input("Enter Invoice Number: ")
        invoice_date = input("Enter Invoice Date (YYYY-MM-DD): ")

        # Convert date string to Oracle DATE
        invoice_date = datetime.strptime(invoice_date, "%Y-%m-%d").date()

        cursor.callproc("ProcessInvoice", [bno, invoice_number, invoice_date])
        cnx.commit()
        print("Invoice processed successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

# Advanced Fee Management
def add_fee_waiver():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        mno = input("Enter Member Code: ")
        fee_type = input("Enter Fee Type: ")
        waiver_amount = float(input("Enter Waiver Amount: "))
        reason = input("Enter Reason for Waiver: ")
        approved_by = input("Enter Approved By (Admin ID): ")

        cursor.callproc("AddFeeWaiver", [mno, fee_type, waiver_amount, reason, approved_by])
        cnx.commit()
        print("Fee waiver added successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

def record_payment_history():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        mno = input("Enter Member Code: ")
        amount = float(input("Enter Amount: "))
        payment_method = input("Enter Payment Method: ")

        cursor.callproc("RecordPaymentHistory", [mno, amount, payment_method])
        cnx.commit()
        print("Payment history recorded successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

def process_refund():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        payment_id = int(input("Enter Payment ID: "))
        refund_amount = float(input("Enter Refund Amount: "))
        reason = input("Enter Reason for Refund: ")
        approved_by = input("Enter Approved By (Admin ID): ")

        cursor.callproc("ProcessRefund", [payment_id, refund_amount, reason, approved_by])
        cnx.commit()
        print("Refund processed successfully!")
    except cx_Oracle.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

# User Interface (GUI)
class LibraryGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Library Management System")
        self.theme = "light"  # Default theme
        self.create_login_form()

    def create_login_form(self):
        self.login_frame = ttk.Frame(self.root, padding=20)
        ttk.Label(self.login_frame, text="User ID:").grid(row=0, column=0)
        self.user_id = ttk.Entry(self.login_frame)
        self.user_id.grid(row=0, column=1)

        ttk.Label(self.login_frame, text="Password:").grid(row=1, column=0)
        self.password = ttk.Entry(self.login_frame, show="*")
        self.password.grid(row=1, column=1)

        ttk.Button(self.login_frame, text="Login", command=self.authenticate).grid(row=2, columnspan=2)
        ttk.Button(self.login_frame, text="Toggle Theme", command=self.toggle_theme).grid(row=3, columnspan=2)
        self.login_frame.pack()

    def authenticate(self):
        user_id = self.user_id.get()
        password = self.password.get()

        # Add your authentication logic here
        if user_id == "admin" and password == "password":
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def show_main_menu(self):
        self.login_frame.destroy()
        menu_frame = ttk.Frame(self.root, padding=20)
        ttk.Label(menu_frame, text="Welcome to Library Management System").grid(row=0, columnspan=2)

        ttk.Button(menu_frame, text="Search Book", command=self.search_book).grid(row=1, column=0)
        ttk.Button(menu_frame, text="Exit", command=self.root.quit).grid(row=1, column=1)
        menu_frame.pack()

    def search_book(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Book")

        ttk.Label(search_window, text="Enter Book Code:").grid(row=0, column=0)
        book_code = ttk.Entry(search_window)
        book_code.grid(row=0, column=1)

        ttk.Button(search_window, text="Search", command=lambda: self.perform_search(book_code.get())).grid(row=1, columnspan=2)

    def perform_search(self, book_code):
        try:
            cnx = get_connection()
            cursor = cnx.cursor()

            cursor.execute("SELECT * FROM BookRecord WHERE BNO = :1", (book_code,))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Search Result", f"Book Code: {result[0]}, Name: {result[1]}, Author: {result[2]}")
            else:
                messagebox.showerror("Error", "Book not found!")
        except cx_Oracle.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}")
        finally:
            cursor.close()
            cnx.close()

    def toggle_theme(self):
        if self.theme == "light":
            self.root.configure(bg="black")
            self.theme = "dark"
        else:
            self.root.configure(bg="white")
            self.theme = "light"

# Main Menu
def main():
    while True:
        clrscreen()
        print("\t\t\t Library Management System\n")
        print("==============================================================")
        print("1. User Management")
        print("2. Catalog Management")
        print("3. Fee Management")
        print("4. Dynamic Reporting")
        print("5. Notify Overdue Books")
        print("6. Acquisition Management")
        print("7. Advanced Fee Management")
        print("8. User Interface (GUI)")
        print("9. Exit")

        choice = input("Enter Choice between 1 to 9 -------> : ")

        if choice == "1":
            # User Management
            while True:
                clrscreen()
                print("\t\t\t User Management\n")
                print("==============================================================")
                print("1. Insert User")
                print("2. Update User")
                print("3. Delete User")
                print("4. Search User")
                print("5. Return to Main Menu")

                user_choice = input("Enter Choice between 1 to 5 -------> : ")

                if user_choice == "1":
                    insert_user()
                elif user_choice == "2":
                    update_user()
                elif user_choice == "3":
                    delete_user()
                elif user_choice == "4":
                    search_user()
                elif user_choice == "5":
                    break
                else:
                    print("Invalid choice! Please select again.")
                input("Press any key to continue...")

        elif choice == "2":
            # Catalog Management
            while True:
                clrscreen()
                print("\t\t\t Catalog Management\n")
                print("==============================================================")
                print("1. Insert Book")
                print("2. Update Book")
                print("3. Delete Book")
                print("4. Search Book")
                print("5. Return to Main Menu")

                catalog_choice = input("Enter Choice between 1 to 5 -------> : ")

                if catalog_choice == "1":
                    insert_book()
                elif catalog_choice == "2":
                    update_book()
                elif catalog_choice == "3":
                    delete_book()
                elif catalog_choice == "4":
                    search_book()
                elif catalog_choice == "5":
                    break
                else:
                    print("Invalid choice! Please select again.")
                input("Press any key to continue...")

        elif choice == "3":
            # Fee Management
            while True:
                clrscreen()
                print("\t\t\t Fee Management\n")
                print("==============================================================")
                print("1. Add Fee Structure")
                print("2. Record Payment")
                print("3. Calculate Fine")
                print("4. Return to Main Menu")

                fee_choice = input("Enter Choice between 1 to 4 -------> : ")

                if fee_choice == "1":
                    add_fee_structure()
                elif fee_choice == "2":
                    record_payment()
                elif fee_choice == "3":
                    calculate_fine()
                elif fee_choice == "4":
                    break
                else:
                    print("Invalid choice! Please select again.")
                input("Press any key to continue...")

        elif choice == "4":
            # Dynamic Reporting
            while True:
                clrscreen()
                print("\t\t\t Dynamic Reporting\n")
                print("==============================================================")
                print("1. Most Popular Books")
                print("2. Most Active Members")
                print("3. Books Issued Last Month")
                print("4. Return to Main Menu")

                report_choice = input("Enter Choice between 1 to 4 -------> : ")

                if report_choice == "1":
                    most_popular_books()
                elif report_choice == "2":
                    most_active_members()
                elif report_choice == "3":
                    books_issued_last_month()
                elif report_choice == "4":
                    break
                else:
                    print("Invalid choice! Please select again.")
                input("Press any key to continue...")

        elif choice == "5":
            # Notify Overdue Books
            notify_overdue_books()
            input("Press any key to continue...")

        elif choice == "6":
            # Acquisition Management
            while True:
                clrscreen()
                print("\t\t\t Acquisition Management\n")
                print("==============================================================")
                print("1. Add Acquisition")
                print("2. Receive Goods")
                print("3. Process Invoice")
                print("4. Return to Main Menu")

                acquisition_choice = input("Enter Choice between 1 to 4 -------> : ")

                if acquisition_choice == "1":
                    add_acquisition()
                elif acquisition_choice == "2":
                    receive_goods()
                elif acquisition_choice == "3":
                    process_invoice()
                elif acquisition_choice == "4":
                    break
                else:
                    print("Invalid choice! Please select again.")
                input("Press any key to continue...")

        elif choice == "7":
            # Advanced Fee Management
            while True:
                clrscreen()
                print("\t\t\t Advanced Fee Management\n")
                print("==============================================================")
                print("1. Add Fee Waiver")
                print("2. Record Payment History")
                print("3. Process Refund")
                print("4. Return to Main Menu")

                advanced_fee_choice = input("Enter Choice between 1 to 4 -------> : ")

                if advanced_fee_choice == "1":
                    add_fee_waiver()
                elif advanced_fee_choice == "2":
                    record_payment_history()
                elif advanced_fee_choice == "3":
                    process_refund()
                elif advanced_fee_choice == "4":
                    break
                else:
                    print("Invalid choice! Please select again.")
                input("Press any key to continue...")

        elif choice == "8":
            # User Interface (GUI)
            app = LibraryGUI()
            app.root.mainloop()
            

        elif choice == "9":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice! Please select again.")
            input("Press any key to continue...")

# Main Execution
if __name__ == "__main__":
    main()
