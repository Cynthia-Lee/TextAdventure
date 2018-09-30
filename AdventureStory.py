print "Welcome to this Adventure Story Game! Type the single digit numbers for your choices!"
print "You are a scubadiver trying to look for treasure.\nYou can:\n[1]Swim deeper\n[2]Resurface"
#choice1 = int(input("Enter an integer for your choice:"))
score = 0;
ask1 = True;
ask2 = True;
ask3 = True;
ask4 = True;
playAgain = True;

def endGame(): 
    print "\nYour oxygen tank is running out. That is all the time you have for now. You head up to resurface."
    print "-End of Game-\nYour score is:",score,"\nThanks for playing!"
    
#def lastChoice(message):
    #print "\n",message
    #exitM = "\nType 'Y' to play again. Type 'N' or anything else to end game."
    #displayM = str(message) + "\n" + str(exitM)
    #lc = raw_input(displayM)
    #if lc == "Y":
        #print "\nNew game started!"
        #score = 0;
        #ask1 = True;
        #ask2 = True;
        #ask3 = True;
        #ask4 = True;
    #else:
        #playAgain = False;
        #print "Game ended."
    
choice1 = raw_input("Welcome to this Adventure Story Game! Type the single digit numbers for your choices!\nYou are a scubadiver trying to look for treasure.\n\nYou can:\n[1]Swim deeper\n[2]Resurface\nEnter an integer for your choice:")
while ask1 == True and playAgain == True:
    if choice1 == "1":
        ask1 = False;
        print "(1) was chosen"
        print "\nYou swim deeper and notice a sunken ship lying on the sea floor. The ship is tattered and covered in algae. You notice openings you can enter through."
        print "You can:\n[1]Enter through front\n[2]Leave"
        choice2 = raw_input("You swim deeper and notice a sunken ship lying on the sea floor. The ship is tattered and covered in algae. You notice openings you can enter through.\nYou can:\n[1]Enter through front\n[2]Leave")
        while ask2 == True:
            if choice2 == "1":
                ask2 = False
                print "(1) was chosen"
                print "\nYou enter what appears to be the sleeping area.\nYou can:\n[1]Go through the belongings in the room\n[2]Head towards what appears to be the kitchen\n[3]Head towards a single bedroom, which probably is the captain's room."
                choice3 = raw_input("You enter what appears to be the sleeping area.\nYou can:\n[1]Go through the belongings in the room\n[2]Head towards what appears to be the kitchen\n[3]Head towards a single bedroom, which probably is the captain's room.")
                while ask3 == True:
                    if choice3 == "1":
                        ask3 = False;
                        print "(1) was chosen" 
                        print "\nYou examine the area. Much of it is destroyed but there are 2 salvageable chests.They are very worn and tattered but you can make out some distinctions.\nYou can:\n[1]Go through the chest with the solid color\n[2]Go through the chest that has detailed markings and engravings"
                        choice4 = raw_input("You examine the area. Much of it is destroyed but there are 2 salvageable chests.They are very worn and tattered but you can make out some distinctions.\nYou can:\n[1]Go through the chest with the solid color\n[2]Go through the chest that has detailed markings and engravings")
                        while ask4 == True:
                            ask4 = False
                            if choice4 == "1":
                                score = 4
                                #lastChoice("You find around 10 different types of knives and swords.\nYour score is: 4")
                                print "\nYou find around 10 different types of knives and swords."
                                endGame()
                            elif choice4 == "2":
                                score = 3
                                #lastChoice("You find a pile of decayed fabrics which are useless. But, after rummaging around you find an ornate jeweled necklace!\nYour score is: 3")
                                print "\nYou find a pile of decayed fabrics which are useless. But, after rummaging around you find an ornate jeweled necklace!"
                                endGame()
                            else:
                                ask4 = True
                                choice4 = raw_input("Please enter a valid choice. Enter an integer for your choice:")
                    elif choice3 == "2": 
                        ask3 = False; # The Kitchen
                        print "(2) was chosen" 
                        print "\nYou examine the area. The kitchen is worn and tattered. Most of the drawers seem missing or about to fall off.\nYou can:\n[1]Go through the pantry closet\n[2]Go through the drawers"
                        choice4 = raw_input("You examine the area. The kitchen is worn and tattered. Most of the drawers seem missing or about to fall off.\nYou can:\n[1]Go through the pantry closet\n[2]Go through the drawers")
                        while ask4 == True:
                            ask4 = False
                            if choice4 == "1": # Pantry
                                score = 2
                                print "\nYou find a few knives and a box of fancy silverware."
                                endGame()
                            elif choice4 == "2": # Drawers
                                score = 1
                                print "\nSince most of the drawers are decayed, you don't find much. All you manage to find are 2 fancy dishes."
                                endGame()
                            else:
                                ask4 = True
                                choice4 = raw_input("Please enter a valid choice. Enter an integer for your choice:")
                    elif choice3 == "3":
                        ask3 = False; # The Captain's Room
                        print "(3) was chosen" 
                        print "\nYou examine the area. The bed is worn and tattered, almost unrecognizable. You notice a chest and many decayed paintings on the wall.\nYou can:\n[1]Go through the chest\n[2]Check the paintings"
                        choice4 = raw_input("You examine the area. The bed is worn and tattered, almost unrecognizable. You notice a chest and many decayed paintings on the wall.\nYou can:\n[1]Go through the chest\n[2]Check the paintings")
                        while ask4 == True:
                            ask4 = False
                            if choice4 == "1": # Chest
                                score = 6
                                print "\nYou manage to pry the chest open with all your might. You find the chest is filled with gold coins."
                                endGame()
                            elif choice4 == "2": # Paintings
                                score = 8
                                print "\nUpon closer examination you notice that there is a wooden panel behind 1 painting. You tear the painting and panel to reveal a safe. Luckliy the safe has eroded enough where you can pry it open! Inside it is filled with golden bars."
                                endGame()
                            else:
                                ask4 = True
                                choice4 = raw_input("Please enter a valid choice. Enter an integer for your choice:")
                    else:
                        choice3 = raw_input("Please enter a valid choice. Enter an integer for your choice:")
            elif choice2 == "2": #########
                ask2 = False # Entering through the side
                print "(2) was chosen"
                print "\nYou think that the area isn't safe and decide to resurface."
                endGame()
            else:
                choice2 = raw_input("Please enter a valid choice. Enter an integer for your choice:")
    elif choice1 == "2":
        ask1 = False;
        print "(2) was chosen"
        print "\nYou decide that you don't want to look for treasure right now. You swim up and resurface."
        endGame()
    else: 
        choice1 = raw_input("Please enter a valid choice. Enter an integer for your choice:")
    

