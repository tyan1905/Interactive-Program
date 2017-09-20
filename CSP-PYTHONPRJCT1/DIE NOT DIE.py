import random as rnd
while(True):
    input = str.lower(raw_input("Type Roll"))
    if("roll" in input):
        print rnd.randint(1,20)
    else:
        print "Please Type Roll"