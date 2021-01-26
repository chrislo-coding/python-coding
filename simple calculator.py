def cal_plus(n1,n2):
    result=n1+n2
    return result
def cal_minus(n1,n2):
    result=n1-n2
    return result
def cal_mul(n1,n2):
    result=n1*n2
    return result
def cal_div(n1,n2):
    result=n1/n2
    return result

n1=eval(input("請輸入第一個數字： "))
n2=eval(input("請輸入第二個數字： "))
cal=eval(input("四則運算代碼 1.加法  2.減法  3.乘法  4.除法\n請輸入代碼："))
if (cal==1):
    print(cal_plus(n1,n2))
elif (cal==2):
    print(cal_minus(n1,n2))
elif (cal==3):
    print(cal_mul(n1,n2))
elif(cal==4):
    print(cal_div(n1,n2))
else:
    print("四則運算代碼輸入錯誤")

#0126 use class 

class calculator:
    def __init__(self,fun):
        self.fun=fun
    def calculator(self,x,y):
        if (self.fun=="1"):
            print(x,"+",y,"=",x+y)
        elif (self.fun=="2"):
            print(x,"-",y,"=",x-y)
        elif (self.fun=="3"):
            print(x,"*",y,"=",x*y)
        elif (self.fun=="4"):
            print(x,"/",y,"=",x/y)
        else:
            print("輸入錯誤")
oper=input("1. 加 2.減 3.乘 4.除\n輸入代碼： ")
x=eval(input("輸入第一個數字： "))
y=eval(input("輸入第二個數字： "))
data=calculator(oper)
data.calculator(x,y)