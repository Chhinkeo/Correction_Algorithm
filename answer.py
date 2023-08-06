# S7
# EX1
# text=str(input())
# sum=0
# is_seven_number=False
# for i in range(len(text)):	
#     if int(text[i]) !=7 and is_seven_number==False :
#         sum=sum+int(text[i])
#     else:
# 	    is_seven_number=True
# print(sum)
#other way
# text = input()
# i = 0
# res = 0
# while text[i] != "7" and i < len(text):
#     res += int(text[i])
#     i+=1
# print(res)


#EX2
# text=input()
# result=0
# is_seven_number=True
# for i in range(len(text)):
#     if text[i]=="7" and is_seven_number:
#         is_seven_number=False
#     elif is_seven_number==False:
#         result=result+int(text[i])
# print(result)


# EX3
# text=input()
# result=0
# i=0
# while i<len(text):
#     if text[i]=="a" and text[i+1]=="b":
#         result=result+1
#     i=i+1
# print(result)
#///////////////////////////////////////////////////////

# S8
# EX1
# number = int(input("input here: "))
# result = ''
# for i in range(number):
#     result += str(number-i) + " "
# print(result)


# EX2
# text = input()
# res = "No"
# i = 0
# while i < len(text):
#     if text[i]=="R" and text[i+1]=="a" and text[i+2]=="d" and text[i+3]=="y":
#         res = "yes"
#     i += 1
# print(res)
#/////////////////////////////////////////////////////////////


# S9
# EX1
# text = input()
# result = ""
# is_finished = True
# for i in range(len(text)):
#     if i > 0:
#         if text[i] > text[i-1] and is_finished == True:
#             result = "SORTED"
#         else:
#             result = "NOT SORTED"
#             is_finished = False
# print(result)



# EX2
# text = input()
# count = 0
# for i in range(len(text)):
#     count += 1
#     if  i>0 :
#         if count==3 and text[i]=="c" and text[i-1]=="b" and text[i-2]=="a":
#             count = 0
#             res = "OK"
#         else:
#             res = "WORNG"
# print(res)
# other way
# t = input()
# for i in range(len(t)-2):
#     if t[i]=="a" and t[i+1]=="b" and t[i+2]=="c":
#         r= "ok"
#     else:
#         r = "wrong"
# print(r)




# EX3
# text = input()
# is_wrong_display =False
# result =''
# for i in range(len(text)):
#     if text[i] =='x':
#         result = 'OK'
#     elif i+1<len(text) and text[i] == '[' and text[i+1] == 'y':
#         result ='OK'
#     elif i+1<len(text) and text[i] == 'y' and (text[i+1] ==']' or text[i+1] =='y') and i !=0 and text[i-1] !='x':
#         result ='OK'
#     elif text[i] ==']' and text[i-1] =='y':
#         result ='OK'
#     else:
#         is_wrong_display = True
# if is_wrong_display:
#     print("WRONG")
# else:
#     print(result)
#////////////////////////////////////////////////////////////////////////////////////////////


# S10
# EX1
# text = input()
# res = 0
# i = 0
# while i<len(text):
#     if i+1<len(text)-1:
#         if text[i]=="a" and text[i+1]=="b" and text[i+2]=="c":
#             res += 1
#     i += 1
# print(res)


# EX2
# text = input()
# res = 1
# is_finished_six = True
# is_have_number_six = False
# for i in range(len(text)):
#     if not is_have_number_six:
#         if text[i] != "6" and is_finished_six:
#             res *= int(text[i])
#         else:
#             is_finished_six = False
# print(res)


#EX3
# n=int(input())
# res=0
# for i in range(n):
#     res = 1+i
#     print(res, end=" ")
#/////////////////////////////////////////////////////////////////////////



# S11
# EX1
#srul te tver klun eng


# Ex2
# text = input()
# result = True
# for i in range(len(text)):
#     if text[i]!="A":
#         result=False
# print(result)


# EX3
# text = ""
# result = ""
# while text != "end":
#     text = input()
#     if text != "end" and int(text)%2 == 0:
#         result +=text+":"
# print(result[:-1])


# EX4
# text = input()
# result = -1
# for index in range(len(text)-1):
#     letter = text[index]
#     if letter == "K" and text[index + 1] == "K":
#         result = index
# print(result) 


# EX5
# text = input()
# isfound = False
# result1 = ""
# result2 = ""
# result = 0
# for i in range(len(text)):
#     if text[i] != ";" and not isfound :
#         result1 += text[i]
#     else:
#         isfound = True
#         if isfound and text[i] != ";":
#             result2 += text[i]
# if isfound and True:
#     result += int(result1) + int(result2)
#     print(result)
# else:
#     print("wrong format")
