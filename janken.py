import random

class Hand:
    
    def __init__(self,num):
        self.value = num
        if(num == 0):
            self.name = "グー"
        elif(num == 1):
            self.name = "チョキ"
        else:
            self.name = "パー"
    
    def getString(self):
        return self.name

    @staticmethod
    def getConcllusion(Ahand,Bhand):
        if(Ahand.value == Bhand.value):
            return ['引き分け',0]
        else:
            if(Ahand.value < BHand.value):
                if(Ahand.value == 0 and BHand.value == 2):
                    return ['Bの勝ち',1]
                else:
                    return ['Aの勝ち',-1]
            else:
                if(Ahand.value == 2 and Bhand.value == 0):
                    return ['Aの勝ち',-1]
                else:
                    return ['Bの勝ち',1]                    
            
        
class Person:
    
    def getHand():
        return Hand(random.randint(0,2))
    

A = Person
B = Person
ACount = 0
BCount = 0
for i in range(3):
    AHand = A.getHand()
    BHand = B.getHand()
    concllusion = Hand.getConcllusion(AHand,BHand)
    print("Aの手：" + AHand.getString() + "v.s. Bの手：" + BHand.getString() + "->" + concllusion[0])
    if(concllusion[1] == -1):
        ACount += 1
    elif(concllusion[1] == 1):
        BCount += 1

if(ACount > BCount):
    print("Aの勝ち")
elif(BCount > ACount):
    print("Bの勝ち")        
else:
    print("引き分け")