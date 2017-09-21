#roll 1 = 1 die
#roll 2 = 2 dices
#roll 3 = 3 dices 
#roll 4 = 4 dices
#roll 5 = you get the point
import random as rnd

    input = str.lower(raw_input("Type Roll"))
if("roll5" in input):
      print rnd.randint(1,6)  
      print rnd.randint(1,6)
      print rnd.randint(1,6)  
      print rnd.randint(1,6)
      print rnd.randint(1,6)  
elif("roll4" in input):
      print rnd.randint(1,6)  
      print rnd.randint(1,6)
      print rnd.randint(1,6)
      print rnd.randint(1,6)  
elif("roll3" in input):
      print rnd.randint(1,6)  
      print rnd.randint(1,6)
      print rnd.randint(1,6)  
elif("roll2" in input):
      print rnd.randint(1,6)  
      print rnd.randint(1,6)
elif("roll1" in input):
      print rnd.randint(1,6)
    else:
      print "Please Type Roll"
        
