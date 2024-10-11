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

personNum = 3
A = Person
B = Person
C = Person
Persons = []
Hands = []
HandValues = []
Counts = []
for i in range(personNum):
    Persons.append(Person)
    Hands.append(Persons[i].getHand())
    HandValues.append(Hands[i].getValue())
    Counts.append(0)
    print("人" + str(i) + "の手：" + Hands[i].getString(),end='')
    if(i != personNum - 1):
        print(" v.s. ",end='')
    else:
        print()

print('結果')
if ((0 in HandValues and 1 in HandValues and 2 in HandValues) or (HandValues.count(0) == personNum) or (HandValues.count(1) == personNum) or (HandValues.count(2) == personNum)):
    print("引き分け")
else:
    for i in range(personNum):
        for j in range(i + 1,personNum):
            conclusion = Hand.getConcllusion(Hands[i],Hands[j])
            if(conclusion == 1):
                Counts[j] += 1
            elif(conclusion == -1):
                Counts[i] += 1#