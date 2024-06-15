# inheritence in python
'''
Syntax of inheritence
class parent:
      {Variables}
      {method}
    class child(parent):
    access of parent class variables & methods
Types of inheritence {Single_level , multi_level , multiple_inheritece} 
'''
# code of single level inheritence
# class Q:
#     name = "ADNAN FAROOQUI"
#     def m1(self):
#         return"This is m1 method"
# class U(Q):
#     def m2(self):
#         print("NAME :-",Q.name)
#         print("M1 :-",self.m1())
# obj=U()
# obj.m2()
# # # multilevel inheritence 
# class A:
#     name = "ADNAN FAROOQUI"
#     def m1(self):
#         return"This is m1 method"
# class B(A):
#     age=24
#     def m2(self):
#         print("NAME :-",A.name)
#         print("M1 :-",self.m1())
# class C(B):
#      def m3(self):
#       print("AGE :-",B.age)
#       self.m2()
# obj=C()
# obj.m3()
# # # multiple level inheritence
# class parent1:
#     def m1(self):
#         print("parent1 method is called")
# class parent2:
#     def m2(self):
#         print("parent2 method is called")
# class child(parent1,parent2):
#     def m3(self):
#         self.m1()
#         self.m2()
# obj=child()
# obj.m3()
# class A:
#     def m1(self):
#         print("m1 method is called from A class")
# class B(A):
#     def m1(self):
#         print("m1 method is called from B class")
#         super().m1()
# obj=B()
# obj.m1()
'''
polymorphism
poly means many
morph means form
polymorphism means one object that perform multiple task 
real world meaning like a man who perform a role of father , husband and teacher.
categories of polymorphism 
{overloading , overriding}
method overloading :- 1 class have same method but different parameter are known as method overloading
python doesn't support over load but python support override method
'''
#method overloading example

class X:
    def old(self,a,b):
        print (a+b)
    def new(self,x,y,z):
        print(x+y+z)
obj=X()
obj.new(12,9,8)
obj.old(8,5)
# default argument set the method overloading 
class X:
    def new(self,x=0,y=0,z=0):
        return x+y+z
    def new(self,x,y,z):
        print(x+y+z)
obj=X()
obj.new(12,9,8)
obj.new(8,5,6)
from multipledispatch import dispatch
class A:
    @dispatch(int,int)
    def add(self,a,b):
       print(a+b)
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)
obj=A()
obj.add(10,8)
obj.add(8,7,4)
class Q:
    def add(self,a,b):
        print("Output from parent class")
class S(Q):
    def add(self,x,y):
        print("Output from child class")
        super().add(12,9)
obj=S()
obj.add(12,7)
    