# print("hello python")
# print("baby")
# num1=float(input("enter the num1:"))
# num2=float(input("enter the num2:"))
# print("the value of num1=",num1)
# print("the value of num2=",num2)
# total=num1+num2
# print("enter total:",total)

# mydiect={
#     "name":"karthick",
#     "age":20,
#     "course": "python",
#     "time":10.30,
#     23.89:89,
#     90.9:False,
#     "place":"chennai"
# } 
# print(mydiect,type(mydiect))
# print(mydiect["age"])
# mydiect["age"]=24
# print(mydiect[90.9])
# print(mydiect["course"])

# a=800
# b=800
# c=78
# print(a,type(a),id(a))
# print(b,type(b),id(b))
# print(c,type(c),id(c))

# c=(30,40,50,60,70)
# d=(30,40,67,60,70)
# print(c,type(c),id(c))
# print(d,type(d),id(d))

# e=[20,40,60,80]
# f=[20,40,60,80]
# print(e,type(e),id(e))
# print(f,type(f),id(f))

# a=[10,30,40,50]
# b=a
# c=[10,30,40,50]
# print(a is b,b!=c)          # is and is not discribe location of value .like true or false
# print(c is not b,a is c)
# print(b==a)

# b=5
# while b>0:
#     print(b)
#     b-=1
# print("Blast off!")
# row=int(input("enter a row number"))
# cloumn=int(input("enter a cloumn number"))



#constuctor and destructors
class student:
    def __init__(self,name,age,city):
        print("constructor calling")
        print("student data")
        self.name=name
        self.age=age
        self.city=city

    def __del__(self):
        print("destructors calling")

student_baby=student("baby",20,"chennai")
print(student_baby.name)
print(student_baby.age)
print(student_baby.city)
del student_baby
print("----------------")
student_karthi=student("karthi",26,"erode")     
print(f"{student_karthi.name}\n{student_karthi.age}\n{student_karthi.city}")
print("----------------")
student_priya=student("priya",23,"delhi") 
print(f"{student_priya.name}\n{student_priya.age}\n{student_priya.city}")
print("----------------")








