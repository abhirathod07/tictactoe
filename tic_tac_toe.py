def tic_tac_toe_pat():
    choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9 = " "," "," "," "," "," "," "," "," ",
    choice='X'
    count=0
    print("\n")
    print("Welcome to Pattern Based Tic Tac Toe Game!!!")
    print("---------------------------------------")
    print("NOTE: THE ROWS & COLUMNS STARTS WITH 1")
    print("--------------------------------------- \n")
    play1 = input("Please enter the name of the first player ")
    play2 = input("Please enter the name of the second player ")
    print("\n")
    print("{} is X and {} is O".format(play1, play2))
    while(count!=9):
        row = int(input("Please select which row "))
        column = int(input("Please select which column "))
        if (row>=4 or column>=4):
            print("Please enter proper rows/columns ")
            continue
        else:
            if row==1 and column==1:
                choice1 = choice
            elif row==1 and column==2:
                choice2 = choice
            elif row==1 and column==3:
                choice3 = choice
            elif row==2 and column==1:
                choice4 = choice
            elif row==2 and column==2:
                choice5 = choice
            elif row==2 and column==3:
                choice6 = choice
            elif row==3 and column==1:
                choice7 = choice
            elif row==3 and column==2:
                choice8 = choice
            else:
                choice9 = choice

            print(" 1    2    3")
            print(" ---"*3)
            print("1|  {}|  {}|  {}|".format(choice1, choice2, choice3))
            print(" ---"*3)
            print("2|  {}|  {}|  {}|".format(choice4, choice5, choice6))
            print(" ---"*3)
            print("3|  {}|  {}|  {}|".format(choice7, choice8, choice9))
            print(" ---"*3)
            if (choice1 == choice and choice2 == choice and choice3 == choice) or \
            (choice1 == choice and choice4 == choice and choice7 == choice) or \
            (choice1 == choice and choice5 == choice and choice9 == choice) or \
            (choice2 == choice and choice5 == choice and choice8 == choice) or \
            (choice3 == choice and choice5 == choice and choice7 == choice) or \
            (choice3 == choice and choice6 == choice and choice9 == choice) or \
            (choice4 == choice and choice5 == choice and choice6 == choice) or \
            (choice7 == choice and choice8 == choice and choice9 == choice):
                if choice == 'X':
                    print("{} won :)".format(play1))
                    return True
                else:
                    print("{} won :)".format(play2))
                    return True
            count +=1
            if count%2==0:
                choice = 'X'
            else:
                choice = 'O'
                
            if count==9:
                conti = input("Position over, Do you want to play again, Enter Y for Continue and N for Exit ")
                if conti in ["Y", "y"]:
                    tic_tac_toe()
                else:
                    break
        
    print("It's a Draw :(")
                
def tic_tac_toe_num():
    choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9 = 0,0,0,0,0,0,0,0,0
    choice=0
    count=0
    print("\n")
    print("Welcome to Number Based Tic Tac Toe Game!!!")
    print("---------------------------------------")
    print("NOTE: THE ROWS & COLUMNS STARTS WITH 1")
    print("--------------------------------------- \n")
    print("Rules: The numbers are to be entered from 1 to 9 \n")
    play1 = input("Please enter the name of the first player \n")
    play2 = input("Please enter the name of the second player \n")
    print("\n")
    print("{} will enter Odd Numbers and {} will enter Even Numbers \n".format(play1, play2))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while(count!=9):
        row = int(input("Please select which row \n"))
        column = int(input("Please select which column \n"))
        value = int(input("Please enter the value \n"))
        if value>=10:
            print("Please enter value between 1 to 9 \n")
            continue
        if count%2==0 and value%2==0:
            print("Please enter the Odd Number \n")
            continue
        elif count%2!=0 and value%2!=0:
            print("Please enter the Even Number \n")
            continue
        if value not in nums:
            print("Duplicate number or Please enter the proper number \n")
            continue
        else:
            nums.remove(value)
        if (row>=4 or column>=4):
            print("Please enter proper rows/columns \n")
            continue
        else:
            if row==1 and column==1:
                choice1 = value
            elif row==1 and column==2:
                choice2 = value
            elif row==1 and column==3:
                choice3 = value
            elif row==2 and column==1:
                choice4 = value
            elif row==2 and column==2:
                choice5 = value
            elif row==2 and column==3:
                choice6 = value
            elif row==3 and column==1:
                choice7 = value
            elif row==3 and column==2:
                choice8 = value
            else:
                choice9 = value

            print(" 1    2    3")
            print(" ---"*3)
            print("1|  {}|  {}|  {}|".format(choice1, choice2, choice3))
            print(" ---"*3)
            print("2|  {}|  {}|  {}|".format(choice4, choice5, choice6))
            print(" ---"*3)
            print("3|  {}|  {}|  {}|".format(choice7, choice8, choice9))
            print(" ---"*3)
            if (choice1 + choice2 + choice3 == 15) or \
            (choice1 + choice4 + choice7 == 15) or \
            (choice1 + choice5 + choice9 == 15) or \
            (choice2 + choice5 + choice8 == 15) or \
            (choice3 + choice5 + choice7 == 15) or \
            (choice3 + choice6 + choice9 == 15) or \
            (choice4 + choice5 + choice6 == 15) or \
            (choice7 + choice8 + choice9 == 15):
                if value%2 != 0:
                    print("{} won :)".format(play1))
                    return True
                else:
                    print("{} won :)".format(play2))
                    return True
            count +=1
            
            if count==9:
                conti = input("Position over, Do you want to play again, Enter Y for Continue and N for Exit ")
                if conti in ["Y", "y"]:
                    tic_tac_toe()
                else:
                    break
        
    print("It's a Draw :(")
                
def tic_tac_toe():
    print("Welcome to the world of Tic Tac Toe!!! \n")
    print(" 1    2    3")
    print(" ---"*3)
    print("1|   |   |   |")
    print(" ---"*3)
    print("2|   |   |   |")
    print(" ---"*3)
    print("3|   |   |   |")
    print(" ---"*3)
    print("Please enter the mode which you want to play ")
    mode = input("Enter 1 for Pattern Based and 2 for Number Based ")
    if int(mode) == 1:
        tic_tac_toe_pat()
    else:
        tic_tac_toe_num()
		
tic_tac_toe()