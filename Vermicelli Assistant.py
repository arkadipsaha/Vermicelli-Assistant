#the purpose of this program is to assist Vermicelli test scorers by having a
#uniform platform on which they can score adjustments for both front paws as well
#as have a built-in timer function. Ideally, with one function, the values for
#the above parameters will reset such that the scorer and continue onto the next
#mouse or trial. -- Arkadip Saha 9/7/16 2:05 PM

import time #helpful for creating the timer function

def newTrial():
    timer = False
    running = False
    LeftAdjustment = 0
    RightAdjustment = 0
    TimeElapsed = 0
    Dropped = 0
    BatonTwirl = 0
    Broke = 0
    OneHanded = 0

    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome to 'Vermicelli Assistant!'\nControls are as follow:\n   a = left paw adjustment \n   s = right paw adjustment \n   d, f = decreases the left, right count by 1 \n   2 = pause timer \n   1 = exit \n   q = dropped pasta \n   w = baton twirl \n   e = broke pasta \n   r = ate one-handed \n"
    speed = input("What speed are you viewing the video at?") #in case you're watching the video at half speed
    #let's start the timer
    while running == False:
        if raw_input("Press '2' to start the timer.") == "2":
                start = time.time()
                running = True
                print "The timer is now running. You may begin scoring. Please press enter after every command."
    #overall scoring cases
    while running == True:
        answer = raw_input()
        #pause function
        if answer == "2":
            end = time.time() #identify when to stop the timer
            running = False
            TimeElapsed += (end-start) #adds the elapsed time so far to the cumulative time
            while running == False: #forcing the user to resume the timer if they want to proceed
                if raw_input("press '2' to resume timer") == "2":
                    start = time.time()
                    running = True
        elif running == False: #if user tries to resume without starting the timer
            print "You must resume the timer!"
        elif answer == "a": #left
            LeftAdjustment += 1
        elif answer == "s": #right
            RightAdjustment += 1
        elif answer == "d": #undo left
            LeftAdjustment -= 1
        elif answer == "f": #undo right
            RightAdjustment -= 1
        elif answer == "q": #dropped
            Dropped += 1
        elif answer == "w": #baton twirl
            BatonTwirl += 1
        elif answer == "e": #broke pasta
            Broke += 1
        elif answer == "r": #ate one-handed
            OneHanded += 1
        elif answer == "1": #exiting the script
            end = time.time()
            break
        else: #if the user inputted something that wasn't an option
            print "Invalid entry. Please enter 'a' or 'b' for the paw adjustment."
    print "Your statistics are as follows: \n   Left Paw: %s \n   Right Paw: %s \n   Dropped Pasta: %s \n   Baton Twirled: %s \n   Broke Pasta: %s \n   Ate One-Handed: %s" % (LeftAdjustment, RightAdjustment, Dropped, BatonTwirl, Broke, OneHanded)
    TimeElapsed += (end-start)
    print "   Time elapsed: " + str(round(TimeElapsed, 2)*speed) + " seconds."
    #establishing whether the user wants to reset
    reset = raw_input("If you would like to reset the counters, please enter 'r' > ")
    while reset != "r": #forcing the user to reset if they want to continue
        reset = raw_input("If you would like to reset the counters, please enter 'r' > ")
    newTrial()
newTrial() #obligatory call to the function so it starts when the script is initially run
