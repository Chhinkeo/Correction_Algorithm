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
# res = "WRONG"
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
#     if text[i] == "6":
#         is_have_number_six = True
# for i in range(len(text)):
#     if is_have_number_six:
#         if text[i] != "6" and is_finished_six:
#             res *= int(text[i])
#         else:
#             is_finished_six = False
#     else:
#         res = 0
# print(res)
