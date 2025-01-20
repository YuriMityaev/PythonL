# n = 5.5

# print(type(n))


# a = 5
# b = 5.54
# c = "Hello"5

# print(f"{a} - {b} - {c}")

# print("{} - {} - {}".format(a,b,c))

# print("Input first number")
# a = int(input())
# b = int(input("Please input second numb10er:"))

# print(a, "+", b, "=", a + b)

# # c = 1
# # print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# a = 1.2441241
# b = 5.43543545
# print(round(a*b, 3))

# Задач №1. Семинар 1. 

# n = int(input("Fill first number:"))
# m = int(input("Fill second number:"))

# print((m + n - 1)//n)

# Задача №2 Семинар 1.

# a = int(input())
# b = int(input())
# c = int(input())

# print(((a + 1)//2) + ((b + 1)//2) + ((c+1)//2))

# Задача 3 семинар 2.

# i = int(input())
# j = int(input())

# if i - j == 0:
#     print(-1)
# else:
#     print ( i+j - 1)

# n = int(input())

# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print("yes")   
# else:
#     print("no")

# HW

# ex1.

n = int(input("Введите трехзначное число:"))
if 100 <= n <= 999:
    print (n[0] + n [1] + n [2])
else:
    print ("Введено не трехзначное число повторите заново")