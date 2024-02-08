from tkinter import *
from tkinter import messagebox

import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

# Import additional modules
import pandas as pd
from tkcalendar import Calendar
import datetime  # Import the datetime module at the top of your code

from tkcalendar import DateEntry  # Import the DateEntry widget



def login():
    user=username.get()
    code=password.get()
    
    if user == "Arish" and code =="1234":
        screen.destroy()
        # root=Toplevel(screen)
        # root.title("Warehouse Management System")
        # root.geometry("1280x720+150+80")
        # screen.configure(bg="#d7dae2")
        # root.resizable(False, False)
        
        #connection for phpmyadmin
        def connection():
            conn = pymysql.connect(
                host='localhost',
                user='root', 
                password='',
                db='products_db',
            )
            return conn

        def refreshTable():
            for data in my_tree.get_children():
                my_tree.delete(data)

            for array in read():
                my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

            my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
            my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

        root = Tk()
        root.title("Ware Housing System")
        #root.geometry("1600x1000")
        #root.attributes('-fullscreen', True) press+ alt f4
        root.state('zoomed')


        my_tree = ttk.Treeview(root)

        #placeholders for entry
        ph1 = tk.StringVar()
        ph2 = tk.StringVar()
        ph3 = tk.StringVar()
        ph4 = tk.StringVar()
        ph5 = tk.StringVar()

        #placeholder set value function
        def setph(word,num):
            if num ==1:
                ph1.set(word)
            if num ==2:
                ph2.set(word)
            if num ==3:
                ph3.set(word)
            if num ==4:
                ph4.set(word)
            if num ==5:
                ph5.set(word)

        # def read():
        #     conn = connection()
        #     cursor = conn.cursor()
        #     cursor.execute("SELECT * FROM products")
        #     results = cursor.fetchall()
        #     conn.commit()
        #     conn.close()
        #     return results



        # def add():
        #     global date 
        #     id = str(idEntry.get())
        #     prod_name = str(prod_nameEntry.get())
        #     price = str(priceEntry.get())
        #     quantity = str(quantityEntry.get())
        #     company_contact = str(company_contactEntry.get())
        #     date = date.get()

        #     if not date:
        #         messagebox.showerror("Error", "Please select a date.")
        #         return

        #     # Add the new data to the Treeview
        #     my_tree.insert("", "end", values=(id, prod_name, price, quantity, company_contact, date))

        #     try:
        #         conn = connection()
        #         cursor = conn.cursor()
        #         cursor.execute("INSERT INTO products (id, prod_name, price, quantity, company_contact, Date) VALUES (%s, %s, %s, %s, %s, %s)",
        #                     (id, prod_name, price, quantity, company_contact, date))
        #         conn.commit()
        #         conn.close()
        #     except:
        #         messagebox.showerror("Error", "Failed to add data to the database.")

        #     if (id == "" or id.isspace()) or (prod_name == "" or prod_name.isspace()) or (price == "" or price.isspace()) or (quantity == "" or quantity.isspace()) or (company_contact == "" or company_contact.isspace()):
        #         messagebox.showinfo("Error", "Please fill up all the blank entries.")
        #         return
        #     # Check if price and quantity are valid positive numbers
        #     try:
        #         price = float(price)
        #         quantity = int(quantity)

        #         if price < 0 or quantity < 0:
        #             messagebox.showinfo("Error", "Price and quantity must be non-negative.")
        #             return
        #     except ValueError:
        #         messagebox.showinfo("Error", "Price and quantity must be valid numbers.")
        #         return

        #     try:
        #         conn = connection()
        #         cursor = conn.cursor()
        #         cursor.execute("INSERT INTO products VALUES ('"+id+"','"+prod_name+"','"+str(price)+"','"+str(quantity)+"','"+company_contact+"')")
        #         conn.commit()
        #         conn.close()
        #         refreshTable()
        #     except:
        #         messagebox.showinfo("Error", "Product ID already exists.")
        


# ... (existing code) ...

        def add():
            id = str(idEntry.get())
            prod_name = str(prod_nameEntry.get())
            price = str(priceEntry.get())
            quantity = str(quantityEntry.get())
            company_contact = str(company_contactEntry.get())
            
            if (id == "" or id.isspace()) or (prod_name == "" or prod_name.isspace()) or (price == "" or price.isspace()) or (quantity == "" or quantity.isspace()) or (company_contact == "" or company_contact.isspace()):
                messagebox.showinfo("Error", "Please fill up all the blank entries.")
                return

            # Check if price and quantity are valid positive numbers
            try:
                price = float(price)
                quantity = int(quantity)

                if price < 0 or quantity < 0:
                    messagebox.showinfo("Error", "Price and quantity must be non-negative.")
                    return
            except ValueError:
                messagebox.showinfo("Error", "Price and quantity must be valid numbers.")
                return
            try:
                conn = connection()
                cursor = conn.cursor()
                # Use the formatted date in "YYYY-MM-DD" format for inserting into the database
                cursor.execute("INSERT INTO products (id, prod_name, price, quantity, company_contact, date) VALUES (%s, %s, %s, %s, %s, %s)",
                            (id, prod_name, price, quantity, company_contact, date_str))
                conn.commit()
                conn.close()
            except:
                pass


            date_str = dateEntry.get_date().strftime("%Y-%m-%d")  # Convert to YYYY-MM-DD format for database
            if not date_str:
                messagebox.showerror("Error", "Please select a date.")
                return

            # Add the new data to the Treeview with the formatted date
            my_tree.insert("", "end", values=(id, prod_name, price, quantity, company_contact, date_str))

            try:
                conn = connection()
                cursor = conn.cursor()
                # Use the formatted date in "YYYY-MM-DD" format for inserting into the database
                cursor.execute("INSERT INTO products (id, prod_name, price, quantity, company_contact, date) VALUES (%s, %s, %s, %s, %s, %s)",
                            (id, prod_name, price, quantity, company_contact, date_str))
                conn.commit()
                conn.close()
            except:
                messagebox.showerror("Error", "Failed to add data to the database. Id already exists")
                

            refreshTable()

# ... (existing code) ...

        def read():
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            results = cursor.fetchall()
            conn.commit()
            conn.close()

            formatted_results = []
            for result in results:
                # Convert the date from the database's format (YYYY-MM-DD) to "DD-MM-YY" format for displaying
                formatted_date = datetime.datetime.strptime(str(result[-1]), "%Y-%m-%d").strftime("%d-%m-%Y")
                formatted_result = list(result)
                formatted_result[-1] = formatted_date
                formatted_results.append(formatted_result)

            return formatted_results
        
        # def reset():
        #     decision = messagebox.askquestion("Warning!!", "Delete all data?")
        #     if decision != "yes":
        #         return 
        #     else:
        #         try:
        #             conn = connection()
        #             cursor = conn.cursor()
        #             cursor.execute("DELETE FROM products")
        #             conn.commit()
        #             conn.close()
        #         except:
        #             messagebox.showinfo("Error", "Sorry an error occured")
        #             return

        #         refreshTable()

        def reset():
    # Clear all input data fields
            idEntry.delete(0, 'end')
            prod_nameEntry.delete(0, 'end')
            priceEntry.delete(0, 'end')
            quantityEntry.delete(0, 'end')
            company_contactEntry.delete(0, 'end')
            
            

        def delete():
            decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
            if decision != "yes":
                return 
            else:
                selected_item = my_tree.selection()[0]
                deleteData = str(my_tree.item(selected_item)['values'][0])
                try:
                    conn = connection()
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM products WHERE id='"+str(deleteData)+"'")
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Error", "Sorry an error occurred")
                    return

                refreshTable()
                
                

        def select():
            try:
                selected_item = my_tree.selection()[0]
                id = str(my_tree.item(selected_item)['values'][0])
                prod_name = str(my_tree.item(selected_item)['values'][1])
                price = str(my_tree.item(selected_item)['values'][2])
                quantity = str(my_tree.item(selected_item)['values'][3])
                company_contact = str(my_tree.item(selected_item)['values'][4])

                setph(id,1)
                setph(prod_name,2)
                setph(price,3)
                setph(quantity,4)
                setph(company_contact,5)
            except:
                messagebox.showinfo("Error", "Please select a data row")
                
                

        def search():
            id = str(idEntry.get())
            conn = connection()
            cursor = conn.cursor()

            try:
                cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
                result = cursor.fetchall()

                if not result:
                    messagebox.showinfo("Error", "No data found")
                else:
                    # Assuming setph takes two arguments (value and index)
                    for num, value in enumerate(result[0]):
                        # Assuming there are 5 fields in the table (id, prod_name, price, quantity, company_contact)
                        if num == 0:
                            idEntry.delete(0, 'end')
                            idEntry.insert(0, value)
                        elif num == 1:
                            prod_nameEntry.delete(0, 'end')
                            prod_nameEntry.insert(0, value)
                        elif num == 2:
                            priceEntry.delete(0, 'end')
                            priceEntry.insert(0, value)
                        elif num == 3:
                            quantityEntry.delete(0, 'end')
                            quantityEntry.insert(0, value)
                        elif num == 4:
                            company_contactEntry.delete(0, 'end')
                            company_contactEntry.insert(0, value)

            except Exception as e:
                print("Error:", e)
                messagebox.showinfo("Error", "An error occurred while fetching data.")

            finally:
                conn.close()
                
       

        def update():
            selectedid = ""

            try:
                selected_item = my_tree.selection()[0]
                selectedid = str(my_tree.item(selected_item)['values'][0])
            except:
                messagebox.showinfo("Error", "Please select a data row")
                return

            id = str(idEntry.get())
            prod_name = str(prod_nameEntry.get())
            price = str(priceEntry.get())
            quantity = str(quantityEntry.get())
            company_contact = str(company_contactEntry.get())

            if (id == "" or id.isspace()) or (prod_name == "" or prod_name.isspace()) or (price == "" or price.isspace()) or (quantity == "" or quantity.isspace()) or (company_contact == "" or company_contact.isspace()):
                messagebox.showinfo("Error", "Please fill up all the blank entries.")
                return

            # Check if price and quantity are valid positive numbers
            try:
                price = float(price)
                quantity = int(quantity)

                if price < 0 or quantity < 0:
                    messagebox.showinfo("Error", "Price and quantity must be non-negative.")
                    return
            except ValueError:
                messagebox.showinfo("Error", "Price and quantity must be valid numbers.")
                return

            try:
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE products SET id='"+
                            id+"', prod_name='"+
                            prod_name+"', price='"+
                            str(price)+"', quantity='"+
                            str(quantity)+"', company_contact='"+
                            company_contact+"' WHERE id='"+
                            selectedid+"' ")
                conn.commit()
                conn.close()
                refreshTable()
            except:
                messagebox.showinfo("Error", "Product ID already exists.")
        
        # ... (existing code) ...

        def show_date_picker_start():
            def on_date_select_start():
                selected_date_start = cal_start.get_date()
                date_input_start.delete(0, tk.END)
                date_input_start.insert(0, selected_date_start)
                date_popup_start.destroy()

            date_input_start.config(state="normal")
            date_popup_start = tk.Toplevel(root)
            cal_start = Calendar(date_popup_start, selectmode="day", date_pattern="dd-mm-yyyy")
            cal_start.pack(pady=20)
            ok_button = ttk.Button(date_popup_start, text="OK", command=on_date_select_start)
            ok_button.pack(pady=10)

        def show_date_picker_end():
            def on_date_select_end():
                selected_date_end = cal_end.get_date()
                date_input_end.delete(0, tk.END)
                date_input_end.insert(0, selected_date_end)
                date_popup_end.destroy()

            date_input_end.config(state="normal")
            date_popup_end = tk.Toplevel(root)
            cal_end = Calendar(date_popup_end, selectmode="day", date_pattern="dd-mm-yyyy")
            cal_end.pack(pady=20)
            ok_button = ttk.Button(date_popup_end, text="OK", command=on_date_select_end)
            ok_button.pack(pady=10)

        # ... (existing code) ...

        # # Create date picker buttons for start and end dates
        # date_input_start = ttk.Entry(root, width=10, font=("Arial", 15))
        # date_input_start.grid(row=2, column=0, padx=1, pady=5)
        # date_input_start.config(state="readonly")
        # date_button_start = ttk.Button(root, text="Select Start Date", command=show_date_picker_start)
        # date_button_start.grid(row=2, column=1, padx=1, pady=5,sticky="w")

        # date_input_end = ttk.Entry(root, width=10, font=("Arial", 15))
        # date_input_end.grid(row=2, column=2, padx=2, pady=5,sticky="w")
        # date_input_end.config(state="readonly")
        # date_button_end = ttk.Button(root, text="Select End Date", command=show_date_picker_end)
        # date_button_end.grid(row=2, column=3, padx=2, pady=5,sticky="w")

        # new code 
        date_frame_start = Frame(root)
        date_frame_start.grid(row=2, column=0, padx=1, pady=5)

        date_input_start = ttk.Entry(date_frame_start, width=10, font=("Arial", 15))
        date_input_start.pack(side="left")
        date_input_start.config(state="readonly")

        date_button_start = ttk.Button(date_frame_start, text="Select Start Date", command=show_date_picker_start)
        date_button_start.pack(side="left", padx=5)

        # Create a Frame to hold the date input box and "Select End Date" button together
        date_frame_end = Frame(root)
        date_frame_end.grid(row=2, column=2, padx=1, pady=5)

        date_input_end = ttk.Entry(date_frame_end, width=10, font=("Arial", 15))
        date_input_end.pack(side="left")
        date_input_end.config(state="readonly")

        date_button_end = ttk.Button(date_frame_end, text="Select End Date", command=show_date_picker_end)
        date_button_end.pack(side="left", padx=5)


        def export_filtered_data_to_excel():
            start_date = date_input_start.get()
            end_date = date_input_end.get()

            if not start_date or not end_date:
                messagebox.showerror("Error", "Please select both start and end dates.")
                return

            try:
                # Convert the date from the date picker's format (DD-MM-YYYY) to "YYYY-MM-DD" format for database query
                start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y").strftime("%Y-%m-%d")
                end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y").strftime("%Y-%m-%d")

                conn = connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products WHERE Date BETWEEN %s AND %s", (start_date, end_date))
                data = cursor.fetchall()
                conn.close()
            except:
                messagebox.showerror("Error", "Failed to fetch data from the database.")
                return

            if not data:
                messagebox.showinfo("No Data", "No data found for the selected date range.")
                return

            columns = ["Product ID", "Product Name", "Price", "Quantity", "Company Contact", "Date"]
            df = pd.DataFrame(data, columns=columns)

            # Convert the date from "YYYY-MM-DD" format to "DD-MM-YYYY" format for the Excel file
            df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%d-%m-%Y")

            df.to_excel("warehouse_data_filtered.xlsx", index=False)
            messagebox.showinfo("Export", "Filtered data exported to 'warehouse_data_filtered.xlsx'")


# ... (existing code) ...

        # def show_date_picker():
        #     def on_date_select():
        #         selected_date = cal.get_date()
        #         date_input.delete(0, tk.END)
        #         date_input.insert(0, selected_date)
        #         date_popup.destroy()

        #     date_input.config(state="normal")
        #     date_popup = tk.Toplevel(root)
        #     cal = Calendar(date_popup, selectmode="day")
        #     cal.pack(pady=20)
        #     ok_button = ttk.Button(date_popup, text="OK", command=on_date_select)
        #     ok_button.pack(pady=10)

# Create the export button for filtered data
        export_filtered_button = ttk.Button(root, text="Export Filtered Data", command=export_filtered_data_to_excel)
        export_filtered_button.grid(row=2, column=7, padx=5, pady=5)

# ... (existing code) ...
        #         # Create the date input field for adding new data
        # date_input = ttk.Entry(root, width=20, font=("Arial", 15))
        # date_input.grid(row=2, column=6, padx=5, pady=5)
        # date_input.config(state="readonly")
        # date_button = ttk.Button(root, text="Select Date", command=show_date_picker)
        # date_button.grid(row=2, column=7, padx=5, pady=5)
        
            
        # # Create a Date picker column using a Date Entry widget with the "DD-MM-YY" format
        # dateLabel = Label(root, text="Date", font=('Arial', 15))
        # dateLabel.grid(row=2, column=4, columnspan=1, padx=5, pady=5, sticky= "w")

        # dateEntry = DateEntry(root, width=10, bd=5, font=('Arial', 15), date_pattern="dd-mm-yyyy")
        # dateEntry.grid(row=2, column=5, columnspan=1, padx=2, pady=5, sticky = "w")
        
        # new code 
        # Create "Date" label
        dateLabel = Label(root, text="Date", font=('Arial', 15))
        dateLabel.grid(row=2, column=4, padx=(5, 2), pady=5, sticky="e")  # Use "padx=(5, 2)" to specify different padding for the left and right sides

        # Create the date picker using DateEntry widget
        dateEntry = DateEntry(root, width=10, bd=5, font=('Arial', 15), date_pattern="dd-mm-yyyy")
        dateEntry.grid(row=2, column=5, padx=(2, 5), pady=5, sticky="w")  # Use "padx=(2, 5)" to specify different padding for the left and right sides

                

        label = Label(root, text="Ware Housing System", font=('Arial Bold', 30))
        label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

        # Label for description of products on the left hand side 
        idLabel = Label(root, text="Product ID", font=('Arial', 15))
        prod_nameLabel = Label(root, text="Product Name", font=('Arial', 15))
        priceLabel = Label(root, text="Price", font=('Arial', 15))
        quantityLabel = Label(root, text="Quantity", font=('Arial', 15))
        company_contactLabel = Label(root, text="Company Contact", font=('Arial', 15))

        idLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
        prod_nameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
        priceLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
        quantityLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
        company_contactLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

        idEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
        prod_nameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
        priceEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
        quantityEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
        company_contactEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)

        idEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
        prod_nameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
        priceEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
        quantityEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
        company_contactEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

        addBtn = Button(
            root, text="Add", padx=65, pady=25, width=10,
            bd=5, font=('Arial', 15), bg="#84F894", command=add)
        updateBtn = Button(
            root, text="Update", padx=65, pady=25, width=10,
            bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
        deleteBtn = Button(
            root, text="Delete", padx=65, pady=25, width=10,
            bd=5, font=('Arial', 15), bg="#FF9999", command=delete)
        searchBtn = Button(
             root, text="Search", padx=65, pady=25, width=10,
             bd=5, font=('Arial', 15), bg="#F4FE82", command=search)
        resetBtn = Button(
            root, text="Reset", padx=65, pady=25, width=10,
            bd=5, font=('Arial', 15), bg="#F398FF", command=reset) 
        selectBtn = Button(
            root, text="Select", padx=65, pady=25, width=10,
            bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)

        addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
        updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
        deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
        searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
        resetBtn.grid(row=13, column=5, columnspan=1, rowspan=2)
        selectBtn.grid(row=11, column=5, columnspan=1, rowspan=2)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial Bold', 15))

        my_tree['columns'] = ("Product ID","Product Name","Price","Quantity","company_contact", "date")

        # code for displaying the data , location = bottom 
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Product ID", anchor=W, width=150)
        my_tree.column("Product Name", anchor=W, width=150)
        my_tree.column("Price", anchor=W, width=150)
        my_tree.column("Quantity", anchor=W, width=180)
        my_tree.column("company_contact", anchor=W, width=180)
        my_tree.column("date", anchor=tk.W, width=150)  # New Date column


        my_tree.heading("Product ID", text="Product ID", anchor=CENTER)
        my_tree.heading("Product Name", text="Product Name", anchor=CENTER)
        my_tree.heading("Price", text="Price", anchor=CENTER)
        my_tree.heading("Quantity", text="Quantity", anchor=CENTER)
        my_tree.heading("company_contact", text="Company Contact", anchor=CENTER)
        my_tree.heading("date", text="date", anchor=tk.CENTER)  # New Date column header


        refreshTable()


    #all alerts when someone try to enter wrong username and password
    elif user=="" and code=="":
        messagebox.showerror("Invalid", "Please enter username and password")
        
    elif user=="":
        messagebox.showerror("Invalid", "username is required")
        
    elif code=="":
        messagebox.showerror("Invalid", "username is required")
        
    elif user!="Arish" and code!=1234:
        messagebox.showerror("Invalid", "username and password")
        
    elif user!="Arish":
        messagebox.showerror("Invalid", "Please enter a valid username")
    
    elif code!="1234":
        messagebox.showerror("Invalid", "Please enter a valid pasword")
    

    
def main_screen():
    
    global screen
    global username
    global password
    
    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")
    
    #image_icon = PhotoImage(file="login.png")
    #screen.iconphoto(False, image_icon)
    screen.title("Login")
    
    lblTitle=Label(text="Login", font=("arial", 50, 'bold'), fg="black", bg="#d7dae2")
    lblTitle.pack(pady=50)
    
    bordercolor=Frame(screen, bg="black", width=800, height=400)
    bordercolor.pack()
    
    mainframe=Frame(bordercolor, bg="#d7dae2", width=800, height=400)
    mainframe.pack(padx=20, pady=20)

    Label(mainframe, text="Username", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="Password", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)
    
    username=StringVar()
    password=StringVar()
    
    entry_username=Entry(mainframe, textvariable=username, width=12,bd=2,font=("arial", 30))
    entry_username.place(x=400,y=50)
    entry_password=Entry(mainframe, textvariable=password, width=12,bd=2,font=("arial", 30), show="*")
    entry_password.place(x=400,y=150)
    
    
    def reset():
        entry_username.delete(0, END)
        entry_password.delete(0, END)
    
    
    Button(mainframe, text="login", height="2", width=23, bg= "#ed3833", fg="white", bd=0, command=login).place(x=100,y=250)
    Button(mainframe, text="Reset", height="2", width=23, bg= "#1089ff", fg="white", bd=0,command=reset).place(x=300,y=250)
    Button(mainframe, text="Exit", height="2", width=23, bg= "#00bd56", fg="white", bd=0, command=screen.destroy).place(x=500,y=250)
    
    
    screen.mainloop()
main_screen()