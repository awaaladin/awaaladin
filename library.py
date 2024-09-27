class library():
    def __init__(self, shelfname, shelfnumber):
        self.shelfname = shelfname
        self.shelfnumber = shelfnumber
        shelfname = input("name :")
        shelfnumber = input("number :")



class books(library):
   def __init__(self, number):
    self.booknumber = number
    def number():
     number = input("number: ")
     if is_valid(number):
      print("Valid")
     else:
      print("Invalid")
    def is_valid(s):
     for number in range(10):
      return True


       
    
class member():
    def __init__(self, name, idnumber, address, phonenumber):
        self.name = name
        self.idnumber = idnumber
        self.address = address
        self.phonenumber = phonenumber
        name = input("name :")
        phonenumber = input("phonenumber :")
        address = input("address :")
        idnumber = input("idnumber :")
        p1 = member("john" , 234 , "ikl" , 123 )
        if p1.name == name :
           print("valid")
        elif p1.phonenumber == phonenumber :
           print("valid")
        elif p1.address == address :
           print("valid")
        elif p1.idnumber == idnumber :
           print("valid")
        else:
           print("invalid")


shelf = member("name", "idnumber", "address", "phonenumber")



print(shelf)



















