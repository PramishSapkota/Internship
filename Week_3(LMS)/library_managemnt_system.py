# Simple Library Management System
import csv
import os
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

book_fields = ['BookID', 'Title', 'Author', 'Quantity']
members_fields = ['MemberID', 'Name', 'Contact']
assignment_fields = ['AssignmentID', 'MemberID', 'BookID', 'IssueDate', 'DueDate', 'Returned']

Book_file_name = 'Week_3(LMS)/csv_records/books.csv'
Member_file_name = 'Week_3(LMS)/csv_records/members.csv'
Assignment_file_name = 'Week_3(LMS)/csv_records/assignments.csv'

# custom error classes should be written in 1st
class LibraryError(Exception): pass
# id not found errors
class BookNotFoundError(LibraryError): pass
class MemberNotFoundError(LibraryError): pass
class AssignmentNotFoundError(LibraryError): pass

# not enough books
class BookUnavailableError(LibraryError): pass

class Book:
    def __init__(self,  title:str, author:str, quantity:int, book_id:str =None):
        self._book_id = book_id if book_id else self.set_ID()
        self.title = title
        self.author = author
        self._quantity = int(quantity)

    def set_ID(self):
        b = BookManager()
        ID = f'B_{b.length_of_dictionary()}'
        return ID

    # @property
    # def quantity(self):
    #     return self.quantity

    @property
    def _quantity(self):
        return self.quantity

    @_quantity.setter
    def _quantity(self,a):
        if a < 0:
            print("Quantity cannot be negative")
            raise ValueError
        else:
            self.quantity = a
        # return self.quantity

    @property
    def is_available(self):
        return self._quantity > 0

    @property
    def book_id(self) -> str:
        return self._book_id
    
    def increase_quantity(self, amount=1):
        self._quantity += amount

    def decrease_quantity(self, amount=1):
        if self._quantity - amount < 0:
            raise BookUnavailableError("Book quantity cannot go below 0")

        self._quantity -= amount

    def to_dict(self) -> dict:
        return {
            "BookID": self._book_id,
            "Title": self.title,
            "Author": self.author,
            "Quantity": self._quantity,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        '''Gives a BOOK object '''
        return cls(title = data["Title"], author = data["Author"], quantity = data["Quantity"], book_id=data["BookID"])

    def __str__(self):
        status = "Available" if self.is_available else "Unavailable"
        return f"[{self.book_id}] | {self.title} | {self.author} | Qty: {self._quantity} | {status} \n{'--'*30} |"
          
class Member:
    def __init__(self, name:str , contact:str, member_id:str = None):
        self._member_id = member_id if member_id else self.set_ID()
        self.name = name
        self.contact = contact
        
    def set_ID(self):
        '''Used to set the member ID'''
        m = MemberManager()
        ID = f'M_{m.length_of_dictionary()}'
        return ID

    @property
    def member_id(self) -> str:
        return self._member_id

    def to_dict(self) -> dict:
        return {
            "MemberID": self._member_id,
            "Name": self.name,
            "Contact": self.contact,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Member":
        '''Gives a Member object '''
        return cls(data["Name"], data["Contact"], data["MemberID"])

    def __str__(self):
        return f"[{self.member_id}] | {self.name} | Contact: {self.contact} |\n{'--'*25} |"

class Assignment:
    def __init__(self, member_ID:str, book_ID:str, 
                 issue_Date = (datetime.today()).strftime("%Y-%m-%d"), 
                 returned:str = "False",
                 dueDate = None,
                #   returned_Date = None
                assignment_id:str = None
                ): 
        self.assignment_ID = assignment_id if assignment_id else self.set_ID()
        self.member_ID = member_ID
        self.book_ID = book_ID
        self.issue_Date = issue_Date
        self.returned = returned
        self._issue_Date = None  # Internal storage variable
        self.issue_Date = issue_Date  # This calls the setter

        self.due_date = dueDate if dueDate else (datetime.strptime(self.issue_Date, "%Y-%m-%d") + timedelta(days=14)).strftime("%Y-%m-%d")
    #     self.due_Date()        
    
    # def due_Date(self):
    #     if self.due_date == None:
    #         self.due_date = (datetime.strptime(self.issue_Date, "%Y-%m-%d") + timedelta(days=14)).strftime("%Y-%m-%d")
            
    def set_ID(self):
        a = AssignmentManager()
        ID = f'A_{a.length_of_dictionary()}'
        return ID

    @property
    def issue_Date(self):
        return self._issue_Date
    
    @issue_Date.setter
    def issue_Date(self, issue):
        try:
            # datetime.strptime(issue, "%Y-%-m-%-d")
            # python doesnt support -m and -d format  to remove leading zeros.  It always expects/writes leading zeros.

            # Validate the date format
            datetime.strptime(issue, "%Y-%m-%d")             
            self._issue_Date = issue  # Store in internal variable, not the property!

        except (ValueError, TypeError) as e:
            print(f"Invalid date '{issue}': {e}")
            print("Using today's date instead.")
            self._issue_Date = datetime.today().strftime("%Y-%m-%d")

    @property
    def remaining_days(self):
        due = datetime.strptime(self.due_date, "%Y-%m-%d")
        today = datetime.today()

        return (due - today).days

    @property
    def is_overdue(self) -> bool:
        '''Tells if the book is returned within deadline or not'''
        return self.returned == 'False' and self.remaining_days < 0

    def mark_returned(self):
        self.returned = "True"

    def to_dict(self):
        return{
            "AssignmentID":self.assignment_ID ,
            'MemberID': self.member_ID,
            'BookID': self.book_ID,
            'IssueDate' : self._issue_Date,
            'DueDate' : self.due_date,
            'Returned' : self.returned,
        }
    
    @classmethod
    def from_dict(cls,data: dict):
        '''Gives an Assignment object '''
        return cls(
            assignment_id = data['AssignmentID'],
            member_ID = data['MemberID'],
            book_ID = data['BookID'],
            issue_Date = data['IssueDate'],
            returned = data['Returned'],
            dueDate = data['DueDate']
        )
    
    def __str__(self):
        if self.returned == "True":
            status = "Returned"
        elif self.is_overdue:
            status = f"OVERDUE by {abs(self.remaining_days)} day(s)"
        else:
            status = f"{self.remaining_days} day(s) remaining"
        return (
            f"| [{self.assignment_ID}] | Member:{self.member_ID} |"
            f"| Book:{self.book_ID} | Due:{self.due_date} | {status} |"
            f"\n{'--'*50}|"
        )

# Abstract Base Class
class CSV_Handling(ABC):
    def __init__(self, filepath: str, fieldnames: list):
        self.filepath = filepath
        self.fieldnames = fieldnames
        self._records: dict = {}  # { id : domain_object }
        self._ensure_file()
        self._load()

    @abstractmethod
    def _from_dict(self, data: dict):
        ...

    @abstractmethod
    def _get_id(self, obj) -> str: 
        ...

    def _ensure_file(self):
        #make folder
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        # make file
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", newline="") as f:
                csv.DictWriter(f, fieldnames=self.fieldnames).writeheader()

    def _load(self):
        with open(self.filepath, "r", newline="") as f:
            for row in csv.DictReader(f):
                obj = self._from_dict(row)
                self._records[self._get_id(obj)] = obj

    def _overwrite(self):
        with open(self.filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(obj.to_dict() for obj in self._records.values())

    def add(self, obj):
        '''Add new obj to dictionary and also append the record on file '''
        key = self._get_id(obj)
        if key in self._records:
            raise LibraryError(f"ID '{key}' already exists.")
        self._records[key] = obj
        with open(self.filepath, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames = self.fieldnames)
            writer.writerow(obj.to_dict())

    def get(self, id_: str):
        '''Get the object'''
        return self._records.get(id_)

    def update(self, obj):
        '''Update the obj and also overwrite the file'''
        key = self._get_id(obj)
        if key not in self._records:
            raise LibraryError(f"ID '{key}' not found — cannot update.")
        self._records[key] = obj
        self._overwrite()

    def delete(self, id_: str):
        if id_ not in self._records:
            raise LibraryError(f"ID '{id_}' not found — cannot delete.")
        del self._records[id_]
        self._overwrite()

    def all(self) -> list:
        '''Returns list of objects'''
        return list(self._records.values())
    
    def length_of_dictionary(self):
        '''To help automatic assignment of bookID'''
        return (len(self._records))

class BookManager(CSV_Handling):
    def __init__(self): 
        super().__init__(filepath= Book_file_name, fieldnames = book_fields)

    def _from_dict(self, data): return Book.from_dict(data)
    def _get_id(self, obj): return obj.book_id

    def available(self) -> list:
        """Return only books that have quantity > 0."""
        return [b for b in self.all() if b.is_available]


class MemberManager(CSV_Handling):
    def __init__(self):
        super().__init__(filepath = Member_file_name, fieldnames = members_fields)

    def _from_dict(self, data): return Member.from_dict(data)
    def _get_id(self, obj): return obj.member_id


class AssignmentManager(CSV_Handling):
    def __init__(self):
        super().__init__(filepath = Assignment_file_name, fieldnames = assignment_fields)

    def _from_dict(self, data): return Assignment.from_dict(data)
    def _get_id(self, obj): return obj.assignment_ID

    def active_for_member(self, member_id: str) -> list:
        """All unreturned assignments for a specific id."""
        return [a for a in self.all() if a.member_ID == str(member_id) and a.returned == 'False']
    
    def active_for_book(self, id: str) -> list:
        """All unreturned assignments for a specific bookID."""
        return [a for a in self.all() if a.book_ID == str(id) and a.returned == 'False']

    def all_active(self) -> list:
        """All assignments that have not been returned yet."""
        return [a for a in self.all() if a.returned == 'False']
    
    def history_for_member(self, member_id: str) -> list:
        """Full assignment history (returned + active) for one member."""
        return [a for a in self.all() if a.member_ID == str(member_id)]

    def has_active_assignment(self, member_id: str, book_id: str) -> bool:
        """Check if this member already has this specific book unreturned."""
        for a in self.all():
            if a.member_ID == str(member_id) and a.book_ID == str(book_id) and a.returned == "False":
                return True
           
        return False #returns None which python treats as False if not specified 
       

class LibraryService:
    def __init__(self):
        self.books = BookManager()
        self.members = MemberManager()
        self.assignments = AssignmentManager()

    @staticmethod
    def is_empty(a_value):
        '''Checks if the field is empty'''
        if not a_value:
            raise ValueError#("Field value cannot be empty")
    
    def add_book(self):
        while 1:
            try:
                # book_id = input("\tEnter book id: ")
                title = input("\tEnter title: ")
                self.is_empty(title)
                author = input("\tEnter author: ")
                self.is_empty(author)
                quantity = int(input("\tEnter quantity: "))
                # if quantity < 0 :
                #     print("Quantity cannot be negative")
                #     raise ValueError
                book = Book(title=title, author= author, quantity= quantity)
                break

            except ValueError:
                print("Please enter a valid data")
                continue
        
        # book = Book(title=title, author= author, quantity= quantity)
        self.books.add(book) # write in file
        print(f'{title} by {author} added successfully')

    def update_book(self):
        while 1:
            try:
                book_id = input("\tEnter book id to update: ")
                # get the required object
                book = self.books.get(book_id)
                if not book:
                    raise BookNotFoundError(f"Book '{book_id}' not found.")

                new_title = input("\tEnter title: ")
                self.is_empty(new_title)
                new_author = input("\tEnter author: ")
                self.is_empty(new_author)
                new_quantity = int(input("\tEnter quantity: "))
                # if new_quantity < 0:
                #     print("Quantity can't be -ve")
                #     raise ValueError
                book.title = new_title
                book.author = new_author
                book._quantity = new_quantity
                self.books.update(book)
                break
            except ValueError:
                print("Please enter a valid data")
                continue

            except BookNotFoundError as e:
                print(f" Error: {e}")
                return

        
        print(f"Book '{book_id}' updated.")

    def delete_book(self):
        try:
            book_id = input("\tEnter Book id to delete: ")
            if not self.books.get(book_id):
                raise BookNotFoundError(f"Book '{book_id}' not found.")
                
            # don't delete if book is currently issued
            if  self.assignments.active_for_book(book_id):
                raise LibraryError (f"Cannot delete Book '{book_id}' — it is currently issued.")

        except Exception as e:
            print(f" Error: {e}") 
            return    

        self.books.delete(book_id)
        print(f"Book '{book_id}' deleted.")

    def display_all_books(self):
        books = self.books.all()
        if not books:
            print("No books in the library.")
            return
        print(f"\n{'─'*60}")
        for book in books:
            print(book)
        print(f"{'─'*60}")

    def display_available_books(self):
        books = self.books.available()
        if not books:
            print("No books currently available.")
            return
        print(f"\n{'─'*60}")
        for b in books:
            print(b)
        print(f"{'─'*60}")

    # ── member operations ────────────────────────────────────────
    def add_member(self):
        while 1:
            try:
                # member_id = input("\tEnter member id: ")
                # self.is_empty(member_id)

                name = input("\tEnter member's name: ")
                self.is_empty(name)

                contact = input("\tEnter contact number: ")
                if len(contact) < 10:
                    raise TypeError("Contact Numbers must be of 10 digits")
                break
                
            except ValueError:
                print("Please enter a valid number")
                continue

            except TypeError as e:
                print(f" Error: {e}")
                continue

        member = Member(name= name, contact=contact)
        self.members.add(member)
        print(f"Member '{name}' added successfully.")

    def update_member(self):
        
        while 1:
            try:
                member_id = input("\tEnter member id to update: ")
                member = self.members.get(member_id)
                if not member:
                    raise MemberNotFoundError(f"Member '{member_id}' not found.")
            
                name = input("\tEnter member's name: ")
                self.is_empty(name)

                contact = input("\tEnter contact number: ")
                if len(contact) != 10:
                    raise TypeError("Contact Numbers must be of 10 digits")
                break
                
            except ValueError:
                print("Please enter a valid number")
                continue

            except Exception as e:
                print(f" Error: {e}")
                continue

        member.name = name
        member.contact = contact
        self.members.update(member)
        print(f"Member '{member_id}' updated.")

    def delete_member(self):
        try:
            member_id = input("\tEnter member id to delete: ")
            if not self.members.get(member_id):
                raise MemberNotFoundError(f"Member '{member_id}' not found.")
            if self.assignments.active_for_member(member_id):
                raise LibraryError(
                    f"Cannot remove Member '{member_id}' — they have unreturned books."
                )
        except Exception as e:
            print(f" Error: {e}") 
            return 
         
        self.members.delete(member_id)
        print(f"Member '{member_id}' removed.")


    def display_all_members(self):
        members = self.members.all()
        if not members:
            print("No members registered.")
            return
        print(f"\n{'─'*60}")
        for m in members:
            print(m)
        print(f"{'─'*60}")

    # ── assignment operations ────────────────────────────────────
    def assign_book(self):
        # Validate member
        try:
            # assignment_id = input("\tAssignment ID: ")
            # self.is_empty(assignment_id)

            member_id = input("\tMember ID: ")
            member = self.members.get(member_id)
            if not member:
                raise MemberNotFoundError(f"Member '{member_id}' not found.")
            
            book_id = input("\tBook ID: ")
            # Validate book
            book = self.books.get(book_id)
            if not book:
                raise BookNotFoundError(f"Book '{book_id}' not found.")
            if not book.is_available:
                raise BookUnavailableError(f"'{book.title}' has no copies available right now.")
            
            if self.assignments.has_active_assignment(member_id, book_id):
                raise LibraryError(f"'{member.name}' already has '{book.title}' and hasn't returned it yet."
            )
            
        except Exception as e:
            print(f" Error: {e}")
            return

        # Create assignment, deduct one copy
        choice = input("\tIs issue date different from today?(Y/N): ").lower()
        if choice == 'y' or choice == 'yes':
            while 1:
                try:
                    y = int(input("\tEnter year: "))
                    m = int(input("\tEnter month: "))
                    d = int(input("\tEnter date: "))
                    break
                
                except ValueError:
                    print("Please enter a number")
                    continue
            date = f'{y}-{m}-{d}'#.strftime("%Y-%m-%d")
            assignment = Assignment( member_ID=member_id, book_ID=book_id,issue_Date = date)
        else:
            assignment = Assignment( member_ID=member_id, book_ID=book_id)

        self.assignments.add(assignment)

        book.decrease_quantity()
        self.books.update(book)

        print(f"Book '{book.title}' assigned to '{member.name}'. Due Date: {assignment.due_date}")
        # return assignment

    def return_book(self):
        assignment_id = input("\tEnter assignment_id: ")
        assignment = self.assignments.get(assignment_id)
        if not assignment:
            raise AssignmentNotFoundError(f"Assignment '{assignment_id}' not found.")
        if assignment.returned == "True":
            raise LibraryError("This book is already marked as returned.")

        assignment.mark_returned()
        self.assignments.update(assignment)

        book = self.books.get(assignment.book_ID)
        if book:
            book.increase_quantity()
            self.books.update(book)

        print(f"Assignment '{assignment_id}' marked as returned.")
        # return assignment

    # ── reporting ────────────────────────────────────────────────
    def display_all_issued_books(self):
        active = self.assignments.all_active()
        if not active:
            print("No books currently issued.")
            return
        print(f"\n{'─'*60}")
        print(f"{'CURRENTLY ISSUED BOOKS':^60}")
        print(f"{'─'*60}")
        for a in active:
            print(a)
        print(f"{'─'*60}")

    def member_report(self):
        member_id = input("\tEnter 'MEMBERID' to see their report: ")
        member = self.members.get(member_id)
        if not member:
            raise MemberNotFoundError(f"Member '{member_id}' not found.")

        history = self.assignments.history_for_member(member_id)
        active = [a for a in history if a.returned == "False"]

        print(f"\n{'═'*40}")
        print(f"  MEMBER REPORT: {member.name} ({member_id})")
        print(f"  Contact: {member.contact}")
        print(f"{'═'*40}")
        print(f"  Total books ever issued : {len(history)}")
        print(f"  Currently holding       : {len(active)}")
        print(f"{'─'*40}")

        if active:
            print("  Active Assignments:")
            for a in active:
                book = self.books.get(a.book_ID)
                book_title = book.title if book else a.book_ID
                overdue_flag = " *** OVERDUE ***" if a.is_overdue else ""
                if not overdue_flag:
                    print(
                        f"    [{a.assignment_ID}] '{book_title}' | "
                        f"Due Date: {a.due_date} | "
                        f"Remaining: {a.remaining_days} day(s)"
                    )

                else:
                    print(
                        f"    [{a.assignment_ID}] | '{book_title}' | "
                        f"Due Date: {a.due_date} | "
                        f"Overdue by: {-1*a.remaining_days} day(s){overdue_flag}"
                    )
        else:
            print("  No active assignments.")
        print(f"{'═'*60}")

    def list_unassigned_books(self):
        """Books with quantity > 0 that are currently not fully issued."""
        self.display_available_books()

class App:

    def __init__(self):
        self.service = LibraryService()

    def book_menu(self):
        while True:
            print("\n========== BOOK MENU ==========")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. Display ALL Books")
            print("5. Display Unassigned Books")
            print("6. Back")

            choice = input("\tEnter choice: ")
            try:  
                match choice:
                    case "1":
                        self.service.add_book()
                    
                    case "2":
                        self.service.update_book()
                    
                    case "3":
                        self.service.delete_book()
                    
                    case "4":
                        self.service.display_all_books()
                    
                    case "5":
                        self.service.display_available_books()

                    case "6":
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

            choice = input("\tEnter choice: ")
            
            match choice:

                case "1":
                    self.service.add_member()

                case "2":
                    self.service.update_member()

                case "3":
                    self.service.delete_member()

                case "4":
                    self.service.display_all_members()

                case "5":
                    break
                case _:
                        print("Invalid Choice. Try Again")
            
    
    def assignment_menu(self):
        while True:
            print("\n========== ASSIGNMENT MENU ==========")
            print("1. Assign Book to Member")
            print("2. Return Book")
            print("3. View All Issued Books")
            print("4. Member Report")
            print("5. List Unassigned / Available Books")
            print("6. Back")
            choice = input("\tEnter choice: ").strip()

            try:
                match choice:
                    case "1":
                        self.service.assign_book()
                    case "2":
                        self.service.return_book()
                    case "3":
                        self.service.display_all_issued_books()
                    case "4":
                        self.service.member_report()
                    case "5":
                        self.service.list_unassigned_books()
                    case "6":
                        break
                    case _:
                        print("Invalid choice. Try again.")
            except LibraryError as e:
                print(f"  Error: {e}")

    def run(self):

        while True:
            print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
            print("1. Book Management")
            print("2. Member Management")
            print("3. Book Assignment")
            print("4. Exit")

            choice = input("\tEnter choice: ")
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

a = App()
a.run()