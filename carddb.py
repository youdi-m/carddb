from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Card Database")
root.geometry("650x900")
root.resizable(False, False)

#connect to databse
conn = sqlite3.connect("cards.db") # name of db

#creating cursor
c = conn.cursor()

#create table if it doesnt exist
c.execute("""CREATE TABLE IF NOT EXISTS cards (
            card_id text NOT NULL PRIMARY KEY,
            card_name text NOT NULL,
            card_rarity text NOT NULL,
            card_tcg text NOT NULL,
            card_price float NOT NULL,
            card_amount integer NOT NULL)""")

#creating submit function
def submit():
    #connect to databse
    conn = sqlite3.connect("cards.db") # name of db

    #creating cursor
    c = conn.cursor()

    #Insert into table if entry boxes are not empty
    id_value = card_id.get()
    name_value = card_name.get()
    rarity_value = card_rarity.get()
    tcg_value = card_tcg.get()
    price_value = card_price.get()
    amount_value = card_amount.get()

    #bools to check for valid types of price and int
    valid_price_bool = True
    valid_amount_bool = True

    #try for price type
    try:
        valid_price = float(price_value)
    except ValueError:
        valid_price_bool = False
    
    #try for amount type
    try:
        valid_amount = int(amount_value)
    except ValueError:
        valid_amount_bool = False
        
    if (id_value and name_value and rarity_value and tcg_value and price_value and amount_value and valid_price_bool and valid_amount_bool):
        print(id_value)
        print(name_value)
        print(rarity_value)
        print(tcg_value)
        print(price_value)
        print(amount_value)
        print(valid_price_bool)
        print(valid_amount_bool)

        c.execute("INSERT INTO cards VALUES (:card_id, :card_name, :card_rarity, :card_tcg, :card_price, :card_amount)",
                    {
                        'card_id': card_id.get(),
                        'card_name': card_name.get(),
                        'card_rarity': card_rarity.get(),
                        'card_tcg': card_tcg.get(),
                        'card_price': card_price.get(),
                        'card_amount': card_amount.get(),
                    })

        #clear the text boxes
        card_id.delete(0, END)
        card_name.delete(0, END)
        card_rarity.delete(0, END)
        card_tcg.delete(0, END)
        card_price.delete(0, END)
        card_amount.delete(0, END)

        #commit changes
        conn.commit()

        #close connection
        conn.close()
    else:

        print(id_value)
        print(name_value)
        print(rarity_value)
        print(tcg_value)
        print(price_value)
        print(amount_value)
        print(valid_price_bool)
        print(valid_amount_bool)

        #creating null entry page
        null_entry = Tk()
        null_entry.title("Invalid Entry")
        null_entry.geometry("250x150")

        #creating null entry text
        null_label = Label(null_entry, text="Fill in all the boxes!\nPrice must be float and amount must be int!")
        null_label.place(relx=0.5, rely=0.5, anchor='ce')

#defining method to bring up add record GUI
def addRecord():

    #creating text boxes
    card_id = Entry(add_record, width=40)
    card_id.grid(row=0, column=1, padx=20, pady=(10, 0))

    card_name = Entry(add_record, width=40)
    card_name.grid(row=1, column=1, padx=20, pady=3)

    card_rarity = Entry(add_record, width=40)
    card_rarity.grid(row=2, column=1, padx=20, pady=3)

    card_tcg = Entry(add_record, width=40)
    card_tcg.grid(row=3, column=1, padx=20, pady=3)

    card_price = Entry(add_record, width=40)
    card_price.grid(row=4, column=1, padx=20, pady=3)

    card_amount = Entry(add_record, width=40)
    card_amount.grid(row=5, column=1, padx=20, pady=3)

    #creating text box labels
    card_id_label = Label(add_record, text="Card ID:")
    card_id_label.grid(sticky="e", row=0, column=0, pady=(10, 0))

    card_name_label = Label(add_record, text="Card Name:")
    card_name_label.grid(sticky="e", row=1, column=0, pady=3)

    card_rarity_label = Label(add_record, text="Card Rarity:")
    card_rarity_label.grid(sticky="e", row=2, column=0, pady=3)

    card_tcg_label = Label(add_record, text="Card TCG:")
    card_tcg_label.grid(sticky="e", row=3, column=0, pady=3)

    card_price_label = Label(add_record, text="Card Price:")
    card_price_label.grid(sticky="e", row=4, column=0, pady=3)

    card_amount_label = Label(add_record, text="Card Amount:")
    card_amount_label.grid(sticky="e", row=5, column=0, pady=3)


    #creating submit button
    submit_btn = Button(add_record, text="Submit", command=submit)
    submit_btn.grid(row=6, column=1, padx=10, pady=(10,0), ipadx=87)

#creating query function
def query():
    #connect to databse
    conn = sqlite3.connect("cards.db") # name of db

    #creating cursor
    c = conn.cursor()

    #query the database
    c.execute("SELECT *, oid FROM cards")
    records = c.fetchall()
    #print(records)

    #loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_listbox = Listbox(root)
    query_listbox.place(relx=0.9, rely=0.4, anchor='ne')

    #commit changes
    conn.commit()

    #close connection
    conn.close()

#creating delete function
def delete():
    #connect to databse
    conn = sqlite3.connect("cards.db") # name of db

    #creating cursor
    c = conn.cursor()

    #query the database
    c.execute("DELETE from cards WHERE card_id=" + str(delete_box.get()))
    records = c.fetchall()


    #commit changes
    conn.commit()

    #close connection
    conn.close()

#creating a save function for update window
def save():
    #connect to databse
    conn = sqlite3.connect("cards.db") # name of db

    #creating cursor
    c = conn.cursor()

    record_id = delete_box.get()

    #updating multiple columns
    c.execute("""UPDATE cards SET
        card_id = :id,
        card_name = :name,
        card_rarity = :rarity,
        card_tcg = :tcg,
        card_price = :price,
        card_amount = :amount

        WHERE card_id = :card_id_get""",
        {
        'id': card_id_update.get(),
        'name': card_name_update.get(),
        'rarity': card_rarity_update.get(),
        'tcg': card_tcg_update.get(),
        'price': card_price_update.get(),
        'amount': card_amount_update.get(),

        'card_id_get': record_id
        })

    #commit changes
    conn.commit()

    #close connection
    conn.close()

    update.destroy()

#creating update function
def update():
    global update
    update = Tk()
    update.title("Update Record")
    update.geometry("410x230")

    #connect to databse
    conn = sqlite3.connect("cards.db") #name of db

    #creating cursor
    c = conn.cursor()

    record_id = delete_box.get()
    #query the database
    c.execute("SELECT * FROM cards WHERE card_id =" + record_id)
    records = c.fetchall()

    #creating global variables for text box names
    global card_id_update
    global card_name_update
    global card_rarity_update
    global card_tcg_update
    global card_price_update
    global card_amount_update

    #creating text boxes
    card_id_update = Entry(update, width=40)
    card_id_update.grid(row=0, column=1, padx=20, pady=(10, 0))

    card_name_update = Entry(update, width=40)
    card_name_update.grid(row=1, column=1, padx=20, pady=3)

    card_rarity_update = Entry(update, width=40)
    card_rarity_update.grid(row=2, column=1, padx=20, pady=3)

    card_tcg_update = Entry(update, width=40)
    card_tcg_update.grid(row=3, column=1, padx=20, pady=3)

    card_price_update = Entry(update, width=40)
    card_price_update.grid(row=4, column=1, padx=20, pady=3)

    card_amount_update = Entry(update, width=40)
    card_amount_update.grid(row=5, column=1, padx=20, pady=3)

    #creating text box labels
    card_id_label_update = Label(update, text="Card ID:")
    card_id_label_update.grid(row=0, column=0, pady=(10, 0))

    card_name_label_update = Label(update, text="Card Name:")
    card_name_label_update.grid(row=1, column=0, pady=3)

    card_rarity_label_update = Label(update, text="Card Rarity:")
    card_rarity_label_update.grid(row=2, column=0, pady=3)

    card_tcg_label_update = Label(update, text="Card TCG:")
    card_tcg_label_update.grid(row=3, column=0, pady=3)

    card_price_label_update = Label(update, text="Card Price:")
    card_price_label_update.grid(row=4, column=0, pady=3)

    card_amount_label_update = Label(update, text="Card Amount:")
    card_amount_label_update.grid(row=5, column=0, pady=3)

    #loop through results
    for record in records:
        card_id_update.insert(0, record[0])
        card_name_update.insert(0, record[1])
        card_rarity_update.insert(0, record[2])
        card_tcg_update.insert(0, record[3])
        card_price_update.insert(0, record[4])
        card_amount_update.insert(0, record[5])

    #create save button to save updated record
    save_btn = Button(update, text="Update Record", command=save)
    save_btn.grid(row=6, column=1, pady=10, padx=10, ipadx=79)

    #commit changes
    conn.commit()

    #close connection
    conn.close()

def refresh():
    return

#       MAIN PAGE GUI

# setup treeview
columns = ('ID', 'Name', 'Rarity', 'TCG', 'Price', 'Amount')
tree = ttk.Treeview(root, height=35, columns=columns, show='headings')
tree.grid(row=0, column=0, sticky='news')

# setup columns attributes
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor=CENTER)

# fetch data
con = sqlite3.connect("cards.db")
c = con.cursor()
c.execute('SELECT * FROM cards')

# populate data to treeview
for rec in c:
    tree.insert('', 'end', value=rec)

# scrollbar
sb = Scrollbar(root, orient=VERTICAL, command=tree.yview)
sb.grid(row=0, column=1, sticky='ns')
tree.config(yscrollcommand=sb.set)

#create submit button
submit_btn = Button(root, text="Add Record", command=addRecord, width=20, height=1)
submit_btn.place(relx=0.1, rely=0.9, anchor="sw")

#create update button
update_btn = Button(root, text="Update Record", command=update, width=20, height=1)
update_btn.place(relx=0.5, rely=0.9, anchor="s")

#create refresh button
refresh_btn = Button(root, text="Refresh Records", command=update, width=20, height=1)
refresh_btn.place(relx=0.9, rely=0.9, anchor="se")

















#creating text boxes
card_id = Entry(root, width=40)
#card_id.grid(row=0, column=1, padx=20, pady=(10, 0))

card_name = Entry(root, width=40)
#card_name.grid(row=1, column=1, padx=20, pady=3)

card_rarity = Entry(root, width=40)
#card_rarity.grid(row=2, column=1, padx=20, pady=3)

card_tcg = Entry(root, width=40)
#card_tcg.grid(row=3, column=1, padx=20, pady=3)

card_price = Entry(root, width=40)
#card_price.grid(row=4, column=1, padx=20, pady=3)

card_amount = Entry(root, width=40)
#card_amount.grid(row=5, column=1, padx=20, pady=3)

delete_box = Entry(root, width=40)
#delete_box.grid(row=9, column=1, pady=(15,0))

#creating text box labels
card_id_label = Label(root, text="Card ID:")
#card_id_label.grid(sticky="e", row=0, column=0, pady=(10, 0))

card_name_label = Label(root, text="Card Name:")
#card_name_label.grid(sticky="e", row=1, column=0, pady=3)

card_rarity_label = Label(root, text="Card Rarity:")
#card_rarity_label.grid(sticky="e", row=2, column=0, pady=3)

card_tcg_label = Label(root, text="Card TCG:")
#card_tcg_label.grid(sticky="e", row=3, column=0, pady=3)

card_price_label = Label(root, text="Card Price:")
#card_price_label.grid(sticky="e", row=4, column=0, pady=3)

card_amount_label = Label(root, text="Card Amount:")
#card_amount_label.grid(sticky="e", row=5, column=0, pady=3)

delete_box_label = Label(root, text="Select Card ID:")
#delete_box_label.grid(sticky="e", row=9, column=0, pady=(15,0))

#creating submit button
submit_btn = Button(root, text="Add Record", command=submit)
#submit_btn.grid(row=6, column=1, padx=10, pady=(10,0), ipadx=87)

#create query button
query_btn = Button(root, text="Show Records", command=query)
#query_btn.grid(row=7, column=1, padx=10, pady=10, ipadx=81)

#create delete button
delete_btn = Button(root, text="Delete Record", command=delete)
#delete_btn.grid(row=11, column=1, padx=10, pady=(10,0), ipadx=81)

#create update button
update_btn = Button(root, text="Update Record", command=update)
#update_btn.grid(row=12, column=1, padx=10, pady=10, ipadx=79)

#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()