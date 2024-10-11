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
    
    def getValue(self):
        return self.value

    def getConcllusion(Ahand,Bhand):
        if(Ahand.value == Bhand.value):
            return ['引き分け',0]
        else:
            if(int(Ahand.value) < int(Bhand.value)):
                if(Ahand.value == 0 and Bhand.value == 2):
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

    def getHand(num):
        return Hand(num)    

A = Person
B = Person
C = Person
Hands = []
ACount = 0
BCount = 0
CCount = 0
AHand = A.getHand(0)
BHand = B.getHand(2)
CHand = C.getHand(0)
Hands.append(AHand.getValue())
Hands.append(BHand.getValue())
Hands.append(CHand.getValue())
print("Aの手：" + AHand.getString() + "v.s. Bの手：" + BHand.getString() + " v.s. Cの手" + CHand.getString() + "->")

if ((0 in Hands and 1 in Hands and 2 in Hands) or (Hands.count(0) == 3) or (Hands.count(1) == 3) or (Hands.count(2) == 3)):
    print("引き分け")
else:
    concllusionAB = Hand.getConcllusion(AHand,BHand)[1]
    concllusionAC= Hand.getConcllusion(AHand,CHand)[1]
    concllusionBC = Hand.getConcllusion(BHand,CHand)[1]
    if(concllusionAB == -1):
        ACount += 1
    elif(concllusionAB == 1):
        BCount += 1
    if(concllusionAC == -1):
        ACount += 1
    elif(concllusionAC == 1):
        CCount += 1
    if(concllusionBC == -1):
        BCount += 1
    elif(concllusionBC == 1):
        CCount += 1
    
if(ACount > 0):
    print("Aの勝ち")
if(BCount > 0):
    print("Bの勝ち")
if(CCount > 0):
    print("Cの勝ち")
