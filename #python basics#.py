#python basics#
#name = "anna"
#print(name)
#age = int(input("enter the age:"))
#if(age>18):
    #print("can drive")
#else:
   # print("cant drive")
# num = (1,2,3,4,5,6,7,8,9,10)
# i = 0
# while(i<(num)):
#     print(num[i])
#     i+=1
# print("end")
# for i in range(1,6):
#     print("number:",i)
# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
#     return(sum)
# calculate_sum(2,10)
class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am robot {self.name}")

r1 = Robot("Robo1")
r1.introduce()