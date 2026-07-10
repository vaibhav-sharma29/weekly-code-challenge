# Custom Exception
class BorrowLimitExceeded(Exception):
    pass

# Base Class
class Member:
    def __init__(self, member_id, name, membership_type):
        self.member_id = member_id
        self.name = name
        self.membership_type = membership_type
        # Private attribute for encapsulation
        self.__borrowed_books = 0 

    # Getter
    def get_borrowed_books(self):
        return self.__borrowed_books

    # Setter
    def set_borrowed_books(self, count):
        self.__borrowed_books = count

    def borrow_book(self, count):
        pass # To be implemented by child classes

    def return_book(self, count):
        if count < 0:
            print("Cannot return a negative number of books.")
            return
        if count > self.__borrowed_books:
            print("Cannot return more books than currently borrowed.")
            return
        self.__borrowed_books -= count

    def display_details(self):
        pass # To be implemented by child classes

# Derived Class 1
class RegularMember(Member):
    def borrow_book(self, count):
        if self.get_borrowed_books() + count > 3:
            raise BorrowLimitExceeded("Regular Member can borrow a maximum of 3 books.")
        self.set_borrowed_books(self.get_borrowed_books() + count)

    def display_details(self):
        remaining = 3 - self.get_borrowed_books()
        print("\n----------- MEMBER DETAILS -----------")
        print(f"Member ID        : {self.member_id}")
        print(f"Name             : {self.name}")
        print(f"Membership Type  : {self.membership_type}")
        print(f"Books Borrowed   : {self.get_borrowed_books()}")
        print(f"Remaining Limit  : {remaining}")
        print("--------------------------------------\n")

# Derived Class 2
class PremiumMember(Member):
    def borrow_book(self, count):
        if self.get_borrowed_books() + count > 10:
            raise BorrowLimitExceeded("Premium Member can borrow a maximum of 10 books.")
        self.set_borrowed_books(self.get_borrowed_books() + count)

    def display_details(self):
        remaining = 10 - self.get_borrowed_books()
        print("\n----------- MEMBER DETAILS -----------")
        print(f"Member ID        : {self.member_id}")
        print(f"Name             : {self.name}")
        print(f"Membership Type  : {self.membership_type}")
        print(f"Books Borrowed   : {self.get_borrowed_books()}")
        print(f"Remaining Limit  : {remaining}")
        print("--------------------------------------\n")


# Execution / Testing based on Sample Input
if __name__ == "__main__":
    members = []
    
    # Simulating the Input process
    num_members = int(input("Enter number of members: "))
    
    for i in range(1, num_members + 1):
        print(f"\nMember {i}")
        m_id = input("Member ID: ")
        m_name = input("Name: ")
        m_type = input("Membership Type (Regular/Premium): ")
        
        if m_type.lower() == "regular":
            member = RegularMember(m_id, m_name, "Regular")
        else:
            member = PremiumMember(m_id, m_name, "Premium")
            
        b_count = int(input("Books to Borrow: "))
        
        try:
            member.borrow_book(b_count)
        except BorrowLimitExceeded as e:
            print(f"\nBorrowLimitExceeded: {e}")
            
        # Optional return logic based on sample input for Member 3
        r_count_input = input("Books to Return (Press Enter to skip): ")
        if r_count_input:
            member.return_book(int(r_count_input))
            
        members.append(member)

    # Demonstrating Polymorphism
    for member in members:
        # Since we already printed exceptions during creation, 
        # we will only display details if they didn't exceed limits on their initial borrow.
        # (Or you can choose to display all depending on strict platform requirements)
        if member.get_borrowed_books() > 0 or member.membership_type:
            member.display_details()