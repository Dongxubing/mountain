#!/usr/bin/env python
# coding: utf-8

# # Tic-Tac-Toe
# ## Xubin Dong, Zhiyong Zhou, Xie Li, Xin Liu
# ### Oct 13 ,2022

# In[1]:


#replace numbers with x or o
def replaceNumber(number, playerName, basicList):
    #Determine whether the number is included (does not include continuing to ask for the correct number)
    while (not str(number) in basicList):
        if playerName == "player1":
            number = input("please input correct number【player1: O】: ");   
        else:
            number = input("please input correct number【player2: X】: ");   
    #The input value is compared with the value in the array to replace X and O
    if (int(number) == int(basicList[int(number)-1])):
        if playerName == "player1":
            basicList[int(number)-1] = "O";
        else:
            basicList[int(number)-1] = "X";
    return number;

#arrList=["1","2","3","4","5","6","7","8","9"];
#number = input("please input number: ");   
#replaceNumber(number,"player2")


# In[2]:


#Determine whether it is successful (as long as the player's list has it)
def isWinner(playerList):
    #all possibilities
    toWin = [("1","2","3"),("4","5","6"),("7","8","9"),("1","4","7"),("2","5","8"),("3","6","9"),("1","5","9"),("3","5","7")];
    # If the possibility has a set of three numbers in the player array, win
    if(len(playerList) >= 3):
        for t in range(len(toWin)): 
             if(toWin[t][0] in playerList and toWin[t][1] in playerList and toWin[t][2] in playerList):
                return True;
    return False;

player1 = ["5","1","7","3"];          
print(isWinner(player1))

    


# In[3]:


#show
def show(arrList):
    print("       __"+arrList[0]+"_|_"+arrList[1]+"_|_"+arrList[2]+"__");
    print("       __"+arrList[3]+"_|_"+arrList[4]+"_|_"+arrList[5]+"__");
    print("         "+arrList[6]+" | "+arrList[7]+" | "+arrList[8]);
    print("- player1:O;     player2:X");


# In[4]:


import random;
print("- welcome to game");
#Checkerboard
basicList=["1","2","3","4","5","6","7","8","9"];
show(basicList);
#player1 array
player1=[];
#player2 array
player2=[];
#Determine whether to jump out of the loop If someone wins, jump out of the loop
win = False;
#First and then (random)
count = random.randint(0,1);



#cycle
while(not win):
    # draw
    if len(player1) + len(player2) == 9:
        print("draw!!!");
        break;
    if(count%2 == 0):
        # start input
        number = input("please input number【player1: O】: ");
        # replace the dial and put the entered numbers into the player's array
        player1.append(replaceNumber(number,"player1", basicList));
        # Determine if it is successful
        win = isWinner(player1);
        if (win == True):
            print("congratulation! player1 is winner");
            show(basicList);
            break;
    elif(count%2 == 1):
        number = input("please input number【player2: X】: ");
        player2.append(replaceNumber(number,"player2", basicList));
        win = isWinner(player2);
        if (win == True):
            print("congratulation! player2 is winner"); 
            show(basicList);
            break;
    count+=1;
    show(basicList);

