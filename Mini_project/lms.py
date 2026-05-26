# from Book import Book
# from Library import Book
# from Book import Book

import csv
import os
from datetime import datetime, timedelta

book_fields = ['BookID', 'Title', 'Author', 'Quantity']
members_fields = ['MemberID', 'Name', 'Contact']
assignment_fields = ['AssignmentID', 'MemberID', 'BookID', 'IssueDate', 'DueDate', 'Returned']

Book_file_name = 'Mini_project/books.csv'
Member_file_name = 'Mini_project/members.csv'
Assignment_file_name = 'Mini_project/assignments.csv'

def initialize_file(filename, headers):
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
        print("File didn't exist. So it has been created")

    else:
        print("File Already exists so doing nothing")

initialize_file(Book_file_name, book_fields)
initialize_file(Member_file_name, members_fields)
initialize_file(Assignment_file_name, assignment_fields)


def get_list_of_dictionaries(FILE_NAME):
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    return rows

def update_file(FILE_NAME, fields, list_of_dictionaries:list):
    with open(FILE_NAME, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(list_of_dictionaries)

def remove(FILE_NAME:str,column_name:str, fieldvalue_to_remove:str, fields:list):

    # rows = []
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.DictReader(file)

        # for row in reader:
        #     if row[column_name] == fieldvalue_to_remove:
        #         continue
        #     rows.append(row)

        # above code using list comprehension
        rows = [row for row in reader if row[column_name] != fieldvalue_to_remove]

        #using filter
        # rows = list(filter(lambda d: d.get(column_name) != fieldvalue_to_remove, reader))

        #using map
        # rows = list(map(lambda d: d.get(column_name) != fieldvalue_to_remove, reader))
    print(f'{fieldvalue_to_remove} entry is deleted')
    update_file(FILE_NAME = FILE_NAME, fields = fields,list_of_dictionaries = rows)

class Book:
    def __init__(self,book_Id, title, author, quantity:int):
        self._book_Id = book_Id
        self.title = title
        self.author = author
        self._quantity = int(quantity)
        self.add_book()

    @property
    def quantity(self):
        return self._quantity

    @property
    def is_available(self):
        return self._quantity > 0

    def increase_quantity(self, amount=1):
        self._quantity += amount

    def decrease_quantity(self, amount=1):
        if self._quantity - amount < 0:
            raise BookUnavailableError("Book quantity cannot go below 0")

        self._quantity -= amount

    def add_book(self):
        '''Appends the new book record'''

        with open(Book_file_name, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=book_fields)
            writer.writerow({
                "Book_Id": self._book_Id,
                "Title": self.title,
                "Author": self.author,
                "Quantity": self.quantity
            })

    def update_book(self, bookID,  new_title, new_author, new_quantity):
        updated = False

        rows = get_list_of_dictionaries(Book_file_name)
        for row in rows:
            if row["BookID"] == bookID:
                row["Title"] = new_title
                row["Author"] = new_author
                row["Quantity"] = str(new_quantity)
                updated = True

        if not updated:
            raise BookNotFoundError("Book not found")
        
        update_file(Book_file_name, book_fields,rows)

    
    def delete_book(self,bookID):
        remove(FILE_NAME= Book_file_name, column_name= "Book_Id",fieldvalue_to_remove = bookID,fields= book_fields)
        del self

    def display_books(self,rows):
        """rows is list of dictionaries"""
        for row in rows:
            print(f'BookID: {row["BookID"]}\t Title:{row["Title"]}\t Author:{row["Author"]} Quantity:{row["Quantity"]} ')

    def display_all_available_books(self):
        # new_row = []
        rows = get_list_of_dictionaries(Book_file_name)
        # for row in rows:
        #     if not int(row["Quantity"]) > 0:
        #         continue
        #     new_row.append(row)
        new_row = list(filter(lambda d: int(d.get('Quantity')) > 0, rows))
        self.display_books(new_row)

    def display_all_books(self):
        rows = get_list_of_dictionaries(Book_file_name)
        self.display_books(rows)
       
class Member:
    def __init__(self, member_ID, name, contact):
        self._member_ID = member_ID
        self.name = name
        self.contact = contact
        
    def add_member(self):
        '''Appends the new member record'''

        with open(Member_file_name, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames = members_fields)
            writer.writerow({
                "MemberID": self._member_ID,
                "Name": self.name,
                "Contact": self.contact
            })

    def delete_member(self,memID):
        remove(FILE_NAME= Member_file_name, column_name= "MemberID",fieldvalue_to_remove = memID,fields= members_fields)

class Assignment(Book, Member):
    def __init__(self,assignment_ID, member_ID, book_ID, 
                 issue_Date = (datetime.today()).strftime("%Y-%m-%d"), 
                 returned = False,
                #  due_Date,
                #   returned_Date = None
                ): 
        self.assignment_ID = assignment_ID
        self.member_ID = member_ID
        self.book_ID = book_ID
        self.issue_Date = issue_Date
        self.returned = returned

        with open(Assignment_file_name, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames = assignment_fields)

            writer.writerow({
                "AssignmentID": assignment_ID,
                "MemberID": member_ID,
                "BookID": book_ID,
                "IssueDate": self.issue_Date,
                "DueDate": self.due_Date,
                "Returned": returned
            })

    @property
    def due_Date(self):
        return(datetime.strptime(self.issue_Date, "%Y-%m-%d") + timedelta(days=14)).strftime("%Y-%m-%d")
    @property
    def remaining_days(self):
        due = datetime.strptime(self.due_date, "%Y-%m-%d")
        today = datetime.today()

        return (due - today).days

    def mark_returned(self):
        self.returned = True

class App:
    def book_menu(self):
        while True:
            print("\n========== BOOK MENU ==========")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. Display Books")
            print("5. Display Unassigned Books")
            print("6. Back")

            choice = input("Enter choice: ")
            try:  
                match choice:
                    case "1":
                        Book.add_book()
                    
                    case "2":
                        Book.update_book()
                    
                    case "3":
                        Book.delete_book()
                    
                    case "4":
                        Book.add_book()
                    
                    case "5":
                        Book.add_book()

                    case 6:
                        break
                    case _:
                        print("Invalid Choice. Try Again")
                        continue
            except Exception as e:
                    print(f"Error: {e}")

    def member_menu(self):
        while True:
            print("\n========== MEMBER MENU ==========")
            print("1. Add Member")
            print("2. Update Member")
            print("3. Remove Member")
            print("4. Display Members")
            print("5. Back")

            choice = input("Enter choice: ")
            try:
                match choice:

                    case "5":
                        break
                    case _:
                            print("Invalid Choice. Try Again")
            except Exception as e:
                    print(f"Error: {e}")
    
    def assignment_menu(self):
        pass

    def run(self):

        while True:
            print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
            print("1. Book Management")
            print("2. Member Management")
            print("3. Book Assignment")
            print("4. Exit")

            choice = input("Enter choice: ")
            match choice:

                case "1":
                    self.book_menu()

                case "2":
                    self.member_menu()

                case "3":
                    self.assignment_menu()

                case "4":
                    print("Exiting program...")
                    break

                case _:
                    print("Invalid choice.")

class LibraryError(Exception):
    pass

class BookNotFoundError(LibraryError):
    pass

class MemberNotFoundError(LibraryError):
    pass

class BookUnavailableError(LibraryError):
    pass

class AssignmentNotFoundError(LibraryError):
    pass