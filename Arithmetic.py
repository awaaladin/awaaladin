#from interpreter import calculator
#number = 12345
#print(number)
#for num in range(2,10):
 #    print(num)

#user_name = "marvel"
#for char in user_name :
 #   print(char)


#fruits =["banana", "orange", "apple", "mango"]
#for fruit in fruits :
 #   print(fruit ,"start with the letter", fruit [0])




#i = 1
#while i == 1: 
 #   print(i)
  #  i += 1
    #break 

#i = 2
#while i < 10:
 #   print(i)
  #  i += 2



class Library:
    def _init_(self, shelf_name=None, shelf_number=None):
        # Initialize shelf name and number with inputs if not provided
        self.shelf_name = shelf_name or input("Shelf name: ")
        self.shelf_number = shelf_number or input("Shelf number: ")

class Books(Library):
    def _init_(self, book_number=None, shelf_name=None, shelf_number=None):
        # Initialize the parent class (Library) and book number
        super()._init_(shelf_name, shelf_number)
        self.book_number = book_number or input("Book number: ")

    def is_valid(self):
        # Check if book number is a valid digit
        return self.book_number.isdigit()

class Member():
    def _init_(self, name=None, id_number=None, address=None, phone_number=None):
        # Initialize member attributes with input values if not provided
        self.name = name or input("Name: ")
        self.id_number = id_number or input("ID number: ")
        self.address = address or input("Address: ")
        self.phone_number = phone_number or input("Phone number: ")

    def validate_member(self, name, id_number, address, phone_number):
        # Validate member details
        if self.name == name and self.id_number == id_number and self.address == address and self.phone_number == phone_number:
            print("Member details are valid")
        else:
            print("Invalid member details")

# Testing the concept
member1 = Member("John", "234", "IKL", "123456789")
member1.validate_member("John", "234", "IKL", "123456789")

shelf = Books("101", "Fiction", "2")
if shelf.is_valid():
  print("Book number is valid")
else:
    print("Book number is invalid")




















