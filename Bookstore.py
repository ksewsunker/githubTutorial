import sqlite3
db = sqlite3.connect('ebookstore_db')
cursor = db.cursor()
# cursor.execute ('''CREATE TABLE books
# (id INTEGER PRIMARY KEY, 
# Title TEXT,
# Author TEXT,
# Qty INTEGER)
# ''')

id1 = 3001
Title1 = 'A Tale of Two Cities'
Author1 = 'Charles Dickens' 
Qty1 = 30

id2 = 3002 
Title2 = 'Harry Potter and the Philosopher\'s Stone'
Author2 = 'J.K. Rowling'
Qty2 = 40

id3 = 3003 
Title3 = 'The Lion, the Witch and the Wardrobe'
Author3 = 'C.S. Lewis'
Qty3 = 25

id4 = 3004 
Title4 = 'The Lord of the Rings'
Author4 = 'J.R.R Tolkien'
Qty4 = 37

id5 = 3005 
Title5 = 'Alice in Wonderland'
Author5 = 'Lewis Carroll'
Qty5 = 12

id6 = 3006 
Title6 = 'A Storm of Swords'
Author6 = 'G.R.R Martins'
Qty6 = 18

# cursor.execute (f'''INSERT INTO books(id, Title, Author, Qty)
#     VALUES(:id,:Title,:Author,:Qty)''',
# {'id':id6, 'Title':Title6, 'Author':Author6, 'Qty':Qty6})
db.commit() 

Menu = input("""
1: Enter book
2: Update book
3: Delete book
4: Search books
0: Exit 
""")

userChoice = ""

while userChoice != "Exit":
    userChoice = input("What would you like to do - Enter/Update/Delete/Search/Exit?: ")

    if userChoice == "Enter":
        
        id = int(input("Enter the id of the record you want to insert: "))
        Title = input("Enter the Title of the record you want to insert: ")
        Author = input("Enter the Author name for the record: ")
        Qty = int(input("Enter the Quantity for the item: "))

        cursor.execute ('''INSERT INTO books(id, Title, Author, Qty)
        VALUES(?, ?, ?, ?)''',(id, Title, Author, Qty))
        db.commit()                 
        print ("User Entered")
        
    elif userChoice == "Update":
        
        Title = input("Enter the Title of the record you want to update: ")
        Qty = int(input("Enter the Quantity for the item you want to update: "))

        cursor.execute('''
        UPDATE books SET Qty = ? WHERE Title = ?
        ''', (Title, Qty))
        db.commit() 
        print ("User Updated")
    
    elif userChoice == "Delete":

        id = int(input("Enter the id of the record you want to delete: "))

        cursor.execute ('''DELETE FROM books WHERE id = ?''', (id,))
        db.commit() 
        print ("User Deleted")
    
    elif userChoice == "Search":

        Title = input("Enter the Title of the record you want to find: ")

        cursor.execute ('''SELECT id, Author, Qty FROM books WHERE Title = ?''',(Title,))
        ebookstore = cursor.fetchone ()
        db.commit()
        print ("Search complete")
        
    elif userChoice == "Exit":
        db.commit() 
        print ("Goodbye")

db.commit()        
db.close() 
