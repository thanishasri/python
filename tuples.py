# student = ("venu","sugain","harshini","thanisha")
# print(student)


# numbers = (10,20,30,40)
# print(numbers)

# student = ("venu","sugain","harshini","thanisha")
# # print(student [3])

# # numbers = (10,20,30,40)
# # print(numbers [-2])

# # # data=(1,2,3,3)
# # # data[0]=100
# # # print(data)

# # X= (1,2,3,4,5,6,6,7,6,6,7)
# # print(X.count(6))

# X=("venu","venu","thanisha","thanisha")
# print(X.count("thanisha"))

# # X=("venu","venu","thanisha","thanisha")
# # print(X [-1])

# # num=(10,20,30,40,50)
# # print(num[1:4])

# # x={1,2,3,1,1,1}
# # print(x)

# a={1,2,3}
# b={2,3,4}
# print(a|b)


# a={1,2,3}
# b={2,3,4}
# print(a&b)

# def add():
#     return 10+20
# result=add()
# # print(result)

# def add(a,b):
#     print(a+b)
# add(10,20)

# def add(*numbers):
#     print(numbers)
# add(10,20,30,40,50,60)

# def add(*num):
#     total=0
#     for i in num:
#         total +=i
#     print(total)
# # add(10,20,30,40,50,60)

# def add(*numbers):
#     print(numbers)
# add(10,20,30,40,50,60)

# def add(*num):
#     total=0
#     for i in num:
#         total +=i
#     print(total)
# add(10,20,30,40,50,60)

# def student(**details):
#     print(details)
#     student(
#         name="mv",
#         age=21,
# #         job="sales",
# #     )

# def student(**details):
#     print(details)

#     student(
#         name="divya",
#         age=22,
#         job="sales",
#     )
#     print(student)

# def student (**details):
#     print("name:" , details["name"])
#     print("age:" , details["age"])
#     print("job:" , details["job"])
# student(
#         name="divya", 
#         age="22",
# #         job="sales"
# #     )

# def student(**details):
#     print(details)

#     student(
#         name="divya",
#         age=22,
#         job="sales",
#     )
#     print(student)

# def student (**details):
#     print("name:" , details["name"])
#     print("age:" , details["age"])
#     print("job:" , details["job"])
# student(
#         name="divya", 
#         age="22",
#         job="sales"
#     )


# odd_even=lambda n: "even" if n% 2 ==0 else "odd"
# # print(odd_even(4))

# file=open("student.txt","w")
# file.write("hello")
# file.close()

# print("data written successfully")

# file=open("student.txt","r")
# data=file.read()
# print(data)
# file.close

# file=open("student.txt" , "a")
# file.write("\nhello student")
# file.close()

# print("data appended successfully")

# file=open("student.txt","r")
# print(file.read())

# try:
#     a=int(input("enter A:"))
#     b=int(input("enter B:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("enter only numbers")
# try:
#     print(10/2)
# except:
#     print("error")
# else:
#     print("success")