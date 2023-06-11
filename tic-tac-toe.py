a1=" "
a2=" "
a3=" "
b1=" "
b2=" "
b3=" "
c1=" "
c2=" "
c3=" "



print("tic-tac-toe ye hoş geldiniz")


def print_p():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    platform1=" ---1-----2-----3---\n"
    platform2=f"1|  {a1}  |  {a2}  |  {a3}  |\n"
    platform3=" -------------------\n"
    platform4=f"2|  {b1}  |  {b2}  |  {b3}  |\n"
    platform5=" -------------------\n"
    platform6=f"3|  {c1}  |  {c2}  |  {c3}  |\n"
    platform7=" -------------------\n"
    print(platform1+platform2+platform3+platform4+platform5+platform6+platform7)

def play(user):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    if user =="user1":
        hamle = "X"
    else:
        hamle="O"    

    x = int(input("satır"))
    y = int(input("sütun"))

    if((x == 1 and y == 1 and a1 == " ") or (x == 1 and y == 2 and a2 == " ") or (x == 1 and y == 3 and a3 == " ") or (x == 2 and y == 1 and b1 == " ") or (x == 2 and y == 2 and b2 == " ") or (x == 2 and y == 3 and b3 == " ") or (x == 3 and y == 1 and c1 == " ") or(x == 3 and y == 2 and c2 == " ") or (x == 3 and y == 3 and c3 == " ")):
        if x==1 and y ==1:
            a1= hamle
        elif x==1 and y ==2:
            a2= hamle
        elif x==1 and y ==3:
            a3= hamle
        elif x==2 and y ==1:
            b1= hamle
        elif x==2 and y ==2:
            b2= hamle
        elif x==2 and y ==3:
            b3= hamle
        elif x==3 and y ==1:
            c1= hamle
        elif x==3 and y ==2:
            c2= hamle
        elif x==3 and y ==3:
            c3= hamle

        print_p()

    else:
        print("olmadı")

def isDone():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    if (a1 == "X" and a2 == "X" and a3 == "x") or (b1 == "X" and b2 == "X" and b3 == "X") or (c1 == "X" and c2 == "X" and c3 == "X") or (a1 == "X" and b2 == "X" and c3=="X") or (a3 == "X" and b2 == "X" and c1=="X"):
        print("Kullanıcı 1 kazandı")
        print_p()
        return True
    elif (a1 == "O" and a2 == "O" and a3 == "O") or (b1 == "O" and b2 == "O" and b3 == "O") or (c1 == "O" and c2 == "O" and c3 == "O") or (a1 == "O" and b2 == "O" and c3=="O") or (a3 == "O" and b2 == "O" and c1=="O"):
        print("Kullanıcı 2 kazandı")
        print_p()
        return True
    elif ((a2 == "O" or a2 == "X") and (a2 == "O" or a2 == "X") and (a3 == "O" or a3 == "X") and (b1 == "O" or b1 == "X") and (b2 == "O" or b2 == "X") and (b3 == "O" or b3 == "X") and (c1 == "O" or c1 == "X") and (c2 == "O" or c2 == "X") and (c3 == "O" or c3 == "X")):
        print("Oyun berabere")
        print_p()
        return True
    else:
       return False

def ply_bot():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    """defense"""

    #horizon-----------

    #a1-a3 horizon
    if a1=="X" and a2 == "X" and a3==" ":
        a3="O"
        print_p()
        return a3
    elif a1=="X" and a2 == " " and a3=="X":
        a2="O"
        print_p()
        return a2
    elif a1==" " and a2 == "X" and a3=="X":
        a1="O"
        print_p()
        return a1
    #b1-b3 horizon
    elif b1=="X" and b2 == "X" and b3==" ":
        b3="O"
        print_p()
        return b3
    elif b1=="X" and b2 == " " and b3=="X":
        b2="O"
        print_p()
        return b2
    elif a1==" " and a2 == "X" and a3=="X":
        b1="O"
        print_p()
        return b1
    #c1-c3 horizon
    elif c1=="X" and c2 == "X" and c3==" ":
        c3="O"
        print_p()
        return c3
    elif b1=="X" and b2 == " " and b3=="X":
        c2="O"
        print_p()
        return c2
    elif a1==" " and a2 == "X" and a3=="X":
        c1="O"
        print_p()
        return c1

    #vertical-----------

    #a1-c1 vertical
    if a1=="X" and b1 == "X" and c1==" ":
        c1="O"
        print_p()
        return c1
    elif a1=="X" and b1 == " " and c1=="X":
        b1="O"
        print_p()
        return b1
    elif a1==" " and b1 == "X" and c1=="X":
        a1="O"
        print_p()
        return a1

    #a2-c2 vertical
    elif a2=="X" and b2 == "X" and c2==" ":
        c2="O"
        print_p()
        return c2
    elif a2=="X" and b2 == " " and c2=="X":
        b2="O"
        print_p()
        return b2
    elif a2==" " and b2 == "X" and c2=="X":
        a2="O"
        print_p()
        return a2

    #a3-c3 vertical
    elif a3=="X" and b3 == "X" and c3==" ":
        c3="O"
        print_p()
        return c3
    elif a3=="X" and b3 == " " and c3=="X":
        b3="O"
        print_p()
        return b3
    elif a3==" " and b3 == "X" and c3=="X":
        a3="O"
        print_p()
        return a3

    #cross-----------

    #cross a3-c1
    elif a3=="X" and b2 == "X" and c1==" ":
        c1="O"
        print_p()
        return c1
    
    elif a3=="X" and b2 == " " and c1=="X":
        b2="O"
        print_p()
        return c1
    
    elif a3==" " and b2 == "X" and c1=="X":
        a3="O"
        print_p()
        return c1
    
    #cross a1-c3
    elif a1=="X" and b2 == "X" and c3==" ":
        c3="O"
        print_p()
        return c3
    elif a1=="X" and b2 == " " and c3=="X":
        b2="O"
        print_p()
        return c3
    elif a1==" " and b2 == "X" and c3=="X":
        a1="O"
        print_p()
        return c3



    """Attack"""



    #a1-a3 horizon
    if a1=="O" and a2 == "O" and a3==" ":
        a3="O"
        print_p()
        return a3
    elif a1=="O" and a2 == " " and a3=="O":
        a2="O"
        print_p()
        return a2
    elif a1==" " and a2 == "O" and a3=="O":
        a1="O"
        print_p()
        return a1
    #b1-b3 horizon
    elif b1=="O" and b2 == "O" and b3==" ":
        b3="O"
        print_p()
        return b3
    elif b1=="O" and b2 == " " and b3=="O":
        b2="O"
        print_p()
        return b2
    elif a1==" " and a2 == "O" and a3=="O":
        b1="O"
        print_p()
        return b1
    #c1-c3 horizon
    elif c1=="O" and c2 == "O" and c3==" ":
        c3="O"
        print_p()
        return c3
    elif b1=="O" and b2 == " " and b3=="O":
        c2="O"
        print_p()
        return c2
    elif a1==" " and a2 == "O" and a3=="O":
        c1="O"
        print_p()
        return c1
    
    #vertical-----------

    #a1-c1 vertical
    if a1=="O" and b1 == "O" and c1==" ":
        c1="O"
        print_p()
        return c1
    elif a1=="O" and b1 == " " and c1=="O":
        b1="O"
        print_p()
        return b1
    elif a1==" " and b1 == "O" and c1=="O":
        a1="O"
        print_p()
        return a1

    #a2-c2 vertical
    elif a2=="O" and b2 == "O" and c2==" ":
        c2="O"
        print_p()
        return c2
    elif a2=="O" and b2 == " " and c2=="O":
        b2="O"
        print_p()
        return b2
    elif a2==" " and b2 == "O" and c2=="O":
        a2="O"
        print_p()
        return a2

    #a3-c3 vertical
    elif a3=="O" and b3 == "O" and c3==" ":
        c3="O"
        print_p()
        return c3
    elif a3=="O" and b3 == " " and c3=="O":
        b3="O"
        print_p()
        return b3
    elif a3==" " and b3 == "O" and c3=="O":
        a3="O"
        print_p()
        return a3

  #cross-----------

    #cross a3-c1
    elif a3=="O" and b2 == "O" and c1==" ":
        c1="O"
        print_p()
        return c1
    
    elif a3=="O" and b2 == " " and c1=="O":
        b2="O"
        print_p()
        return c1
    
    elif a3==" " and b2 == "O" and c1=="O":
        a3="O"
        print_p()
        return c1
    
    #cross a1-c3
    elif a1=="O" and b2 == "O" and c3==" ":
        c3="O"
        print_p()
        return c3
    elif a1=="O" and b2 == " " and c3=="O":
        b2="O"
        print_p()
        return c3
    elif a1==" " and b2 == "O" and c3=="O":
        a1="O"
        print_p()
        return c3



    #random
    # a1-a3
    elif a1==" ":
        a1="O"
        print_p()
        return a1
    elif a2==" ":
        a2="O"
        print_p()
        return a2
    elif a3==" ":
        a3="O"
        print_p()
        return a3

    #b1-b3
    elif b1==" ":
        b1="O"
        print_p()
        return b1
    elif b2==" ":
        b2="O"
        print_p()
        return b2
    elif b3==" ":
        b3="O"
        print_p()
        return b3

    #c1-c3
    elif c1==" ":
        c1="O"
        print_p()
        return c1
    elif c2==" ":
        c2="O"
        print_p()
        return c2
    elif c3==" ":
        c3="O"
        print_p()
        return c3
    print_p()

def tic_tac_toe():
    print("Tic-Tac-Toe'ye hoş geldiniz!")
    print_p()

    islem2 = int(input("bot ile oynamak için 1'e , iki kişilik oynamak için 2 ye basın"))
    if islem2 ==1:
       while True:
            if isDone():
                break
            print("kullanıcı 1 in hamlesi")
            play("user1")

            if isDone():
                break
            print("Bot un hamlesi")
            ply_bot()
    else:
        while True:
            if isDone():
                break
            print("kullanıcı 1 in hamlesi")
            play("user1")
            if isDone():
                break
            print("kullanıcı 2 nin hamlesi")
            play("user2")

tic_tac_toe()

