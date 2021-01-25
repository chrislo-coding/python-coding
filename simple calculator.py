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
    
  
#0125 add use "class" to do
class calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def cal_plus(self):
        print(self.n1,"+",self.n2,"=",self.n1+self.n2)
    def cal_minus(self):
        print(self.n1,"-",self.n2,"=",self.n1-self.n2) 
    def cal_mul(self):
        print(self.n1,"*",self.n2,"=",self.n1*self.n2)
    def cal_div(self):
        print(self.n1,"/",self.n2,"=",self.n1/self.n2)
        
n1=eval(input("請輸入第一個數字: "))
n2=eval(input("請輸入第二個數字: "))
cal=eval(input("1.加\n2.減\n3.乘\n4.除\n請輸入四則運算代碼: "))

if (cal==1):
    data=calculator(n1,n2).cal_plus()
elif (cal==2):
    data=calculator(n1,n2).cal_minus()
elif (cal==3):
    data=calculator(n1,n2).cal_mul()
elif (cal==4):
    data=calculator(n1,n2).cal_div()
