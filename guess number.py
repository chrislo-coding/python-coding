#基礎版 while迴圈
#自己設定密碼 
#告知使用者數字猜大一點或小一點
finalans=eval(input("請設定一個終極密碼： "))
guessnum=eval(input("猜猜密碼是多少？ "))
while (finalans!=guessnum):
    if (finalans>guessnum):
        print("猜錯了，再猜大一點")
        guessnum=eval(input("繼續猜猜密碼是多少？ "))
    elif (guessnum>finalans):
        print("猜錯了，再猜小一點")
        guessnum=eval(input("繼續猜猜密碼是多少？ "))
else:
    if (finalans==guessnum):
        print("猜對了！")


#基礎版 for迴圈
#自己設定密碼
#告知使用者數字猜大一點或小一點
#增加  設定使用者猜的次數 
import sys
times=10
finalans=eval(input("請設定一個終極密碼？ "))
for i in range(times):
    times-=1
    guessnum=eval(input("猜猜密碼是多少？ "))
    if (finalans>guessnum):
        print("猜錯了，再猜大一點！你還剩下"+str(times)+"次機會，加油！")             
    elif (finalans<guessnum):
        print("猜錯了，再猜小一點！你還剩下"+str(times)+"次機會，加油！")
    else:
        print("猜對了！")
        break
if(times==0):
    print("十次機會用完囉～下次再來！")
    sys.exit()
else:
    sys.exit()

#while 迴圈
#亂數指定密碼
#告知使用者確切數字範圍（範圍會隨著使用者輸入的數字改變）
import random
highest=1000
lowest=1
finalans=random.randint(lowest,highest)        #隨機取0~1000之間的整數
while True:
    guessnum=input("密碼範圍是："+str(lowest)+"~"+str(highest)+"\n您的答案： ")

    try:
        guessnum=int(guessnum)
    except ValueError:
        print("ˊ格式錯誤，請輸入數字")
        continue          #若辨識格式錯誤，會跳過繼續迴圈

    if (guessnum<=lowest) or (guessnum>=highest):
        print("  *注意*  您輸入的數字超出範圍囉！")
        continue          #若辨識超出範圍，會跳過繼續下個迴圈

    if(guessnum<finalans):
        lowest=guessnum
    elif(guessnum>finalans):
        highest=guessnum
    else:
        print("恭喜答對！")
        break

    
    