print("1.華氏轉攝氏\n2.攝氏轉華氏")
d=eval(input("請輸入數字代碼:"))
if(d==1):
    d1=eval(input("請輸入華氏溫度:"))
    print((d1-32)*5/9,"度C")
elif(d==2):
    d2=eval(input("請輸入攝氏溫度:"))
    print(9/5*d2+32,"度F")
