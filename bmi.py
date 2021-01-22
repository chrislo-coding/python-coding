h=eval(input("請輸入身高(cm): "))
w=eval(input("請輸入體重(kg): "))
bmi=w/(h/100)**2
w1=w-(24*(h/100)**2) #w1過重 要用bmi最大24作為範圍
w2=(18.5*(h/100)**2)-w #w2過瘦 要用bmi最小18.5作為範圍
print("您的BMI值是:{:.1f}".format(bmi))
if (bmi>=24):
    print("過重,距離標準體重還須減少:{:.1f}公斤".format(w1))
elif (bmi<=18.5):
    print("過瘦,距離標準體重還需增加:{:.1f}公斤".format(w2))
else:
    print("適中")       