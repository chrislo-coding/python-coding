剪刀石頭布遊戲
import random
computer=random.randint(1,3)
player=input("1.剪刀  2.石頭  3.布\n請出拳： ")
while True:
    if (computer==1):
        print("電腦出：剪刀")
    elif (computer==2):
        print("電腦出：石頭")
    else:
        print("電腦出：布")
    try:
        player=int(player)
    except ValueError:
        print("格式錯誤！請輸入正確數字")
        continue

    if (player!=1) and (player!=2) and (player!=3):
        print("請輸入正確數字！")
        continue

    if (player==computer):
        print("平手")
        continue
    elif (player==1 and computer==3)or(player==2 and computer==1)or(player==3 and computer==2):
         print("你贏了！")
          break
    else:
        print("你輸了")
        break 



        
