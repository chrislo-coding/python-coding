#lambda 匿名函數

def buyticket (num):
    total=lambda price:price*num
    return total     #回傳值＝lambda price:price*num

#myticket=buyticket(num) #呼叫buyticket(16)，傳入參數num=16
#print("總共：",myticket(price),"元") #印出匿名函數，傳入參數price=100


num=eval(input("每一張票100元\n請輸入購買張數： "))
myticket=buyticket(num)
print("總共：",myticket(100),"元")