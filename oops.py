'''
Oop's are real world entities add in our programming language
class , object , abstraction , encapsulation , inheritence , polymorphism
abstraction , encapsulation are use to secure data
inheritence , polymorphism are use to reuseability 
Defination of class :- class is a blue print of an object where we define property and action 
                       / behaviour of an object
Defination of object :- object is a instense of class
properties are represent by variables
action / behaviours are represent by methods
SYNTAX OF CLASS IN PYTHON
class class_name:
       "Doc.String"
       Property(Variables)
       Action (Methods)
Types of variables:- [instance variable, local variable, static variable]
Types of Methods  :- [instance method, local method, static method]
'''
# class without constructor 
class student:
      stu_university="BARKATULLAH UNIVERSITY"
      stu_college="BHOPAL SCHOOL OF SOCIAL SCIENCE {BSSS}"
      stu_qulification="B.com Computer Application"
      def stu_detail(self,name,age):
             print("stu_University :-",student.stu_university)
             print("stu_college :-",student.stu_college)
             print("Stu_NAME :- ",name)
             print("Stu_age :- ",age)
             print("stu_Qulification :- ",student.stu_qulification)
obj=student()
obj.stu_detail("ADNAN",23)
print(obj.__doc__)
print(obj.__dict__)
print(dir(student))
# # class with constructor's
class Student:
       stu_qulification="BCA"
       def __init__(self) :
              print("Constructer Called")
obj=Student() # paranthesis are responsible to call a constructor 
print(obj)

'''variables in python 
1 instance variable , 2 local variables , 3 statics variables
'''
class student:
       "THIS IS FOR DOC STRING TESTING"
       def __init__(self,Name,age):
              self.Name=Name # instance variables
              self.age=age   # instance variables
              print(id(self))
       def stu_details(self):
           print(id(self))
           print(self.Name)
           print(self.age)
obj=student("ADNAN FAROOQUI",24)
print(id(obj))
obj.stu_details()
print(obj.Name)
print(obj.age)
#   Self can hold the reference of current object of current class   
class stu:
    quli="B.com computer" # stastic variable
    def __init__(self,name):
        self.name=name # instance variable
    def display(self):
            age=24 # local variable
            print("NAME : ",self.name)
            print("AGE :",age)
            print("Qulification :",stu.quli)
obj=stu("ADNAN FAROOQUI")
obj.display()           
'''
how we declare instance variable
through costructor
through instance method
through object 
'''
# using instance method in instance variable 
class s:
     def display(self,name):
          self.name=name
     def show(self):
          print("NAME :- ",self.name)
obj=s()
obj.display("ADNAN FAROOQUI")
obj.show()
class S:
     def __init__(self,name):
          self.name=name # through constructor
     def display(self,age):
          self.age=age
     def show(self): # through instance method
          print("Name :-",self.name)
          print("Age :- ", self.age)
          print("Qulification :- ",self.quli)
obj=S("ADNAN")
obj.display(24)
obj.quli='MCA' # through object
obj.show()
'''
how to access instance variable 
inside the class
outside class
'''
# stastic variable
class student:
     quli="B.com computer application" # stastic variable declare inside the class
     def __init__(self,name,age):
         self.name=name
         self.age=age
         student.school="BHOPAL SCHOOL OF SOCIAL SCIENCE {BSSS}"# stastic variable declare inside the constructor
     def display(self):
           student.gread="Batchlour's"# stastic variable declar inside the instance variable
           print("NAME :-",self.name)
           print("AGE :-",self.age)
           print("Qulification :-",student.quli)#Stastic variable access inside the class through class name
           print("College :-",student.school) #Stastic variable access inside the class through class name
           print("Gread :-",student.gread)#Stastic variable access inside the class through class name
      #      print("Achivement :-",student.achivement)#Stastic variable access inside the class through class name
obj=student("ADNAN FAROOQUI",24)
student.achvement="GATE-QULIFIED"#Stastic variable declare outside of the class
print("Access through class_name :-",student.quli)#Stastic variable access outside the class through class name
print("Access through object :-",obj.quli)#Stastic variable access outside the class through object
obj.display()
print("Access through class_name :-",student.gread) #Stastic variable access outside the class through class name
print("Access through class_name :-",student.school)#Stastic variable access outside the class through class name
# print("Access through class_name :-",student.achivement)#Stastic variable access outside the class through class name
obj.display()
print(dir(student))
print(student.__dict__)
print(obj.__dict__)
#  local variable
'''local 
 ''' 
class student:
      def display(self):
            global q
            q=10 # local variable
            print("val of q :-",q)
      def show(self):
            print("val of q :-",q)
      def new():
            print("val of q :-",q)
obj=student()
obj.display()
obj.show()
student.new()# if we not use self then we call the variable through classname.method()
print("val of q :-",q)
'''
methods
types of methods  instance method , class method , local method 
'''
#   instance method call
class Student:
      def display(self,name):
            self.name=name
            print("NAME :-",self.name)
      def show(self,age):
            self.age=age
            self.display()
            print("AGE :-",self.age)
obj=Student()
obj.display("ADNAN FAROOQUI")
obj.show(24)
Student.display("ADNAN FAROOQUI") # this is not possible we use instance method            
#  class method
'''
stastic variable of class variable value change we use class method
@ classmethod
instead of self, here we use cls
'''
class book:
      price=1000
      def book_detail(self,name,author):
            self.name=name
            self.author=author
      @classmethod 
      def update_price(cls,price):
            cls.price=price
      def show_detail(self,page):
            self.page=page
            print("Book_Name :-",self.name)
            print("Book_Author :-",self.author)
            print("Book_Price :-",book.price)
            print("Pages :-",page)
obj=book()
obj.book_detail('Python Full Stack','ADNAN FAROOQUI')
obj.update_price(1500)
obj.show_detail(110)
# stastic method
'''
syntax of stastic method
@ stastic method
'''
class Students:
   @ staticmethod
   def greet():
      print("welcome to python class") 
   def greet1():
      print("Thanks for visit to python class")
obj=Students()
obj.greet()
Students.greet()
obj.greet1()
# Students.greet1()
obj.greet1()