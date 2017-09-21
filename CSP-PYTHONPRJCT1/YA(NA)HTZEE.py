#roll 1 = 1 die
#roll 2 = 2 dices
#roll 3 = 3 dices
#roll 4 = 4 dices
#roll 5 = you get the point
import random as rnd

yahzee = []
input1 = str.lower(raw_input("1st Roll, Type Roll"))
if("roll" in input1):
    r1 = rnd.randint(1,6)
    print r1
    yahzee.append(r1)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
while(True):
else:
    print "Please Type Roll"
input2 = str.lower(raw_input("2nd Roll,Type the desired amount of dice to be rolled (1-5)"))
if("5" in input2):
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
elif("4" in input2):
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6 )
elif("3" in input2):
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
elif("2" in input2):
    print rnd.randint(1,6)
    print rnd.randint(1,6)
elif("1" in input2):
    print rnd.randint(1,6)
else:
    print "Please Type the desired amount of dice to be rolled (1-5)"
input3 = str.lower(raw_input("Final Roll, type the desired amount of dice to be rolled (1-5)"))
if("5" in input3):
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
elif("4" in input3):
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6 )
elif("3" in input3):
    print rnd.randint(1,6)
    print rnd.randint(1,6)
    print rnd.randint(1,6)
elif("2" in input3):
    print rnd.randint(1,6)
    print rnd.randint(1,6)
elif("1" in input3):
    print rnd.randint(1,6)
else:
    print "Please Type the desired amount of dice to be rolled (1-5)"