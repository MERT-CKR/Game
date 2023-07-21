import random

turn =0
turn2 = 0
p1_dice1=0
p1_dice2=0
p2_dice1=0
p2_dice2=0


def play(user):
    global turn2,p1_dice1,p1_dice2,p2_dice1,p2_dice2
    turn2+=1
    
    input("devam etmek için herhangi bir tuşa basın")   
    
    if user == "user1":
        print("oyun sırası kullanıcı 1 de")
        p1_dice1 = random.randint(0,6)
        print("zar1: ",p1_dice1)
        p1_dice2 = random.randint(0,6)
        print("zar2: ",p1_dice2)
        print("puan: ",p1_dice1+p1_dice2)

    elif user == "user2":
        print("oyun sırası kullanıcı 2 de")
        p2_dice1 = random.randint(0,6)
        print("zar1: ",p2_dice1)
        p2_dice2 = random.randint(0,6)
        print("zar2: ",p2_dice2)
        print("puan: ",p2_dice1+p2_dice2)
            
    else:
        print("kullanıcı seçilemedi")

    if turn2 % 2==0:
        if p1_dice1 + p1_dice2 > p2_dice1 + p2_dice2:
            print("oyuncu1 kazandı \n-------")
        elif p2_dice1 + p2_dice2 > p1_dice1 + p1_dice2:
            print("oyuncu2 kazandı \n-------")
        else:
            print("oyun berabere \n-------")



def Who_plays():
    global turn
    while True:
        
        turn+=1
        if turn %2==0:
            play("user2")
        elif turn %2==1:
            play("user1")
        if turn >=10:
            break

Who_plays()