#THIS IS THE WIN FUNCTIONS MODULE. IT CONTAINS ALL THE FUNCTIONS THAT DICTATE THE  X WINS, O WIN AND SCENARIOS OF THE GAME
import doctest # import the doctest library
import random  # import the random library
from tkinter import *  # import tkinter
from tkinter import messagebox  # import messagebox from tkinter
import buttons_only as bo  # import buttons_only module

Listwin = [0, 0, 0, 0, 0, 0, 0, 0,
           0]  # Create a new list Listwin of 9 values representing each of the smaller boards that determines who wins the ultimate game


def win():  # Define a win function
    """
This function determines who wins board one of the nine three by three smaller tic tac toe boards using if/else
statements. If X turns three blank buttons into X boxes in a row, X wins the board. If O turns three blank buttons into
O boxes in a row, O wins the board. If there are no winners after all 9 buttons are clicked, the game is a tie.
                        """
    global winner  # Create a global variable winner
    global count1  # Create a global variable count1
    winner = False  # Set winner equal to false
    count1 = 0  # Set count1 equal to 0
    # Checking for X wins
    if bo.b1["text"] == "X" and bo.b2["text"] == "X" and bo.b3["text"] == "X":  # If button 1, 2, and 3 all equal X
        bo.b1.config(bg="green")  # Turn button one green
        bo.b2.config(bg="green")  # Turn button one green
        bo.b3.config(bg="green")  # Turn button one green
        bo.b4.config(bg="green")  # Turn button one green
        bo.b5.config(bg="green")  # Turn button one green
        bo.b6.config(bg="green")  # Turn button one green
        bo.b7.config(bg="green")  # Turn button one green
        bo.b8.config(bg="green")  # Turn button one green
        bo.b9.config(bg="green")  # Turn button one green
        winner = True  # Change winner to true
        Listwin[0] = 1  # Change the first value of Listwin to 1, because X won the first box.
        # This general pattern repeats for all win functions
    elif bo.b4["text"] == "X" and bo.b5["text"] == "X" and bo.b6["text"] == "X":
        bo.b1.config(bg="green")
        bo.b2.config(bg="green")
        bo.b3.config(bg="green")
        bo.b4.config(bg="green")
        bo.b5.config(bg="green")
        bo.b6.config(bg="green")
        bo.b7.config(bg="green")
        bo.b8.config(bg="green")
        bo.b9.config(bg="green")
        winner = True
        Listwin[0] = 1
       
    elif bo.b7["text"] == "X" and bo.b8["text"] == "X" and bo.b9["text"] == "X":
        bo.b1.config(bg="green")
        bo.b2.config(bg="green")
        bo.b3.config(bg="green")
        bo.b4.config(bg="green")
        bo.b5.config(bg="green")
        bo.b6.config(bg="green")
        bo.b7.config(bg="green")
        bo.b8.config(bg="green")
        bo.b9.config(bg="green")
        winner = True
        Listwin[0] = 1
       
    elif bo.b1["text"] == "X" and bo.b4["text"] == "X" and bo.b7["text"] == "X":
        bo.b1.config(bg="green")
        bo.b2.config(bg="green")
        bo.b3.config(bg="green")
        bo.b4.config(bg="green")
        bo.b5.config(bg="green")
        bo.b6.config(bg="green")
        bo.b7.config(bg="green")
        bo.b8.config(bg="green")
        bo.b9.config(bg="green")
        winner = True
        Listwin[0] = 1
       
    elif bo.b2["text"] == "X" and bo.b5["text"] == "X" and bo.b8["text"] == "X":
        bo.b1.config(bg="green")
        bo.b2.config(bg="green")
        bo.b3.config(bg="green")
        bo.b4.config(bg="green")
        bo.b5.config(bg="green")
        bo.b6.config(bg="green")
        bo.b7.config(bg="green")
        bo.b8.config(bg="green")
        bo.b9.config(bg="green")
        winner = True
        Listwin[0] = 1
      

    elif bo.b3["text"] == "X" and bo.b6["text"] == "X" and bo.b9["text"] == "X":
        bo.b1.config(bg="green")
        bo.b2.config(bg="green")
        bo.b3.config(bg="green")
        bo.b4.config(bg="green")
        bo.b5.config(bg="green")
        bo.b6.config(bg="green")
        bo.b7.config(bg="green")
        bo.b8.config(bg="green")
        bo.b9.config(bg="green")
        winner = True
        Listwin[0] = 1
        

    elif bo.b1["text"] == "X" and bo.b5["text"] == "X" and bo.b9["text"] == "X":
        bo.b1.config(bg="green")
        bo.b2.config(bg="green")
        bo.b3.config(bg="green")
        bo.b4.config(bg="green")
        bo.b5.config(bg="green")
        bo.b6.config(bg="green")
        bo.b7.config(bg="green")
        bo.b8.config(bg="green")
        bo.b9.config(bg="green")
        winner = True
        Listwin[0] = 1
        

    elif bo.b3["text"] == "X" and bo.b5["text"] == "X" and bo.b7["text"] == "X":
        bo.b1.config(bg="green")
        bo.b2.config(bg="green")
        bo.b3.config(bg="green")
        bo.b4.config(bg="green")
        bo.b5.config(bg="green")
        bo.b6.config(bg="green")
        bo.b7.config(bg="green")
        bo.b8.config(bg="green")
        bo.b9.config(bg="green")
        winner = True
        Listwin[0] = 1
        

    # Checking for O wins
    if bo.b1["text"] == "O" and bo.b2["text"] == "O" and bo.b3["text"] == "O":
        bo.b1.config(bg="blue")
        bo.b2.config(bg="blue")
        bo.b3.config(bg="blue")
        bo.b4.config(bg="blue")
        bo.b5.config(bg="blue")
        bo.b6.config(bg="blue")
        bo.b7.config(bg="blue")
        bo.b8.config(bg="blue")
        bo.b9.config(bg="blue")
        winner = True
        Listwin[0] = 2
        
    elif bo.b4["text"] == "O" and bo.b5["text"] == "O" and bo.b6["text"] == "O":
        bo.b1.config(bg="blue")
        bo.b2.config(bg="blue")
        bo.b3.config(bg="blue")
        bo.b4.config(bg="blue")
        bo.b5.config(bg="blue")
        bo.b6.config(bg="blue")
        bo.b7.config(bg="blue")
        bo.b8.config(bg="blue")
        bo.b9.config(bg="blue")
        winner = True
        Listwin[0] = 2
      
    elif bo.b7["text"] == "O" and bo.b8["text"] == "O" and bo.b9["text"] == "O":
        bo.b1.config(bg="blue")
        bo.b2.config(bg="blue")
        bo.b3.config(bg="blue")
        bo.b4.config(bg="blue")
        bo.b5.config(bg="blue")
        bo.b6.config(bg="blue")
        bo.b7.config(bg="blue")
        bo.b8.config(bg="blue")
        bo.b9.config(bg="blue")
        winner = True
        Listwin[0] = 2
        
    elif bo.b1["text"] == "O" and bo.b4["text"] == "O" and bo.b7["text"] == "O":
        bo.b1.config(bg="blue")
        bo.b2.config(bg="blue")
        bo.b3.config(bg="blue")
        bo.b4.config(bg="blue")
        bo.b5.config(bg="blue")
        bo.b6.config(bg="blue")
        bo.b7.config(bg="blue")
        bo.b8.config(bg="blue")
        bo.b9.config(bg="blue")
        winner = True
        Listwin[0] = 2
        
    elif bo.b2["text"] == "O" and bo.b5["text"] == "O" and bo.b8["text"] == "O":
        bo.b1.config(bg="blue")
        bo.b2.config(bg="blue")
        bo.b3.config(bg="blue")
        bo.b4.config(bg="blue")
        bo.b5.config(bg="blue")
        bo.b6.config(bg="blue")
        bo.b7.config(bg="blue")
        bo.b8.config(bg="blue")
        bo.b9.config(bg="blue")
        winner = True
        Listwin[0] = 2
       

    elif bo.b3["text"] == "O" and bo.b6["text"] == "O" and bo.b9["text"] == "O":
        bo.b1.config(bg="blue")
        bo.b2.config(bg="blue")
        bo.b3.config(bg="blue")
        bo.b4.config(bg="blue")
        bo.b5.config(bg="blue")
        bo.b6.config(bg="blue")
        bo.b7.config(bg="blue")
        bo.b8.config(bg="blue")
        bo.b9.config(bg="blue")
        winner = True
        Listwin[0] = 2
      

    elif bo.b1["text"] == "O" and bo.b5["text"] == "O" and bo.b9["text"] == "O":
        bo.b1.config(bg="blue")
        bo.b2.config(bg="blue")
        bo.b3.config(bg="blue")
        bo.b4.config(bg="blue")
        bo.b5.config(bg="blue")
        bo.b6.config(bg="blue")
        bo.b7.config(bg="blue")
        bo.b8.config(bg="blue")
        bo.b9.config(bg="blue")
        winner = True
        Listwin[0] = 2
        

    elif bo.b3["text"] == "O" and bo.b5["text"] == "O" and bo.b7["text"] == "O":
        bo.b1.config(bg="blue")
        bo.b2.config(bg="blue")
        bo.b3.config(bg="blue")
        bo.b4.config(bg="blue")
        bo.b5.config(bg="blue")
        bo.b6.config(bg="blue")
        bo.b7.config(bg="blue")
        bo.b8.config(bg="blue")
        bo.b9.config(bg="blue")
        winner = True
        Listwin[0] = 2

    if bo.b1["text"] != "" and bo.b2["text"] != "" and bo.b3["text"] != "" and bo.b4["text"] != "" and bo.b5[
        "text"] != "" and bo.b6["text"] != "" and bo.b7["text"] != "" and bo.b8["text"] != "" and bo.b9[
        "text"] != "" and winner == False:
        bo.b1.config(bg="red")
        bo.b2.config(bg="red")
        bo.b3.config(bg="red")
        bo.b4.config(bg="red")
        bo.b5.config(bg="red")
        bo.b6.config(bg="red")
        bo.b7.config(bg="red")
        bo.b8.config(bg="red")
        bo.b9.config(bg="red")
        Listwin[0] = 3
        winner = True

    if winner == True:
        count1 = 1


def win2():
    """
This function determines who wins board two of the nine three by three smaller tic tac toe boards using if/else
statements. If X turns three blank buttons into X boxes in a row, X wins the board. If O turns three blank buttons into
O boxes in a row, O wins the board. If there are no winners after all 9 buttons are clicked, the game is a tie.
                        """
    global winner
    global count2
    winner = False
    count2 = 0
    # Checking for X wins
    if bo.b10["text"] == "X" and bo.b11["text"] == "X" and bo.b12["text"] == "X":
        bo.b10.config(bg="green")
        bo.b11.config(bg="green")
        bo.b12.config(bg="green")
        bo.b13.config(bg="green")
        bo.b14.config(bg="green")
        bo.b15.config(bg="green")
        bo.b16.config(bg="green")
        bo.b17.config(bg="green")
        bo.b18.config(bg="green")
        winner = True
        
    elif bo.b13["text"] == "X" and bo.b14["text"] == "X" and bo.b15["text"] == "X":
        bo.b10.config(bg="green")
        bo.b11.config(bg="green")
        bo.b12.config(bg="green")
        bo.b13.config(bg="green")
        bo.b14.config(bg="green")
        bo.b15.config(bg="green")
        bo.b16.config(bg="green")
        bo.b17.config(bg="green")
        bo.b18.config(bg="green")
        winner = True
        Listwin[1] = 1
        
    elif bo.b16["text"] == "X" and bo.b17["text"] == "X" and bo.b18["text"] == "X":
        bo.b10.config(bg="green")
        bo.b11.config(bg="green")
        bo.b12.config(bg="green")
        bo.b13.config(bg="green")
        bo.b14.config(bg="green")
        bo.b15.config(bg="green")
        bo.b16.config(bg="green")
        bo.b17.config(bg="green")
        bo.b18.config(bg="green")
        winner = True
        Listwin[1] = 1
       
    elif bo.b10["text"] == "X" and bo.b13["text"] == "X" and bo.b16["text"] == "X":
        bo.b10.config(bg="green")
        bo.b11.config(bg="green")
        bo.b12.config(bg="green")
        bo.b13.config(bg="green")
        bo.b14.config(bg="green")
        bo.b15.config(bg="green")
        bo.b16.config(bg="green")
        bo.b17.config(bg="green")
        bo.b18.config(bg="green")
        winner = True
        Listwin[1] = 1
        
    elif bo.b11["text"] == "X" and bo.b14["text"] == "X" and bo.b17["text"] == "X":
        bo.b10.config(bg="green")
        bo.b11.config(bg="green")
        bo.b12.config(bg="green")
        bo.b13.config(bg="green")
        bo.b14.config(bg="green")
        bo.b15.config(bg="green")
        bo.b16.config(bg="green")
        bo.b17.config(bg="green")
        bo.b18.config(bg="green")
        winner = True
        Listwin[1] = 1
        

    elif bo.b12["text"] == "X" and bo.b15["text"] == "X" and bo.b18["text"] == "X":
        bo.b10.config(bg="green")
        bo.b11.config(bg="green")
        bo.b12.config(bg="green")
        bo.b13.config(bg="green")
        bo.b14.config(bg="green")
        bo.b15.config(bg="green")
        bo.b16.config(bg="green")
        bo.b17.config(bg="green")
        bo.b18.config(bg="green")
        winner = True
        Listwin[1] = 1
       

    elif bo.b10["text"] == "X" and bo.b14["text"] == "X" and bo.b18["text"] == "X":
        bo.b10.config(bg="green")
        bo.b11.config(bg="green")
        bo.b12.config(bg="green")
        bo.b13.config(bg="green")
        bo.b14.config(bg="green")
        bo.b15.config(bg="green")
        bo.b16.config(bg="green")
        bo.b17.config(bg="green")
        bo.b18.config(bg="green")
        winner = True
        Listwin[1] = 1
      

    elif bo.b12["text"] == "X" and bo.b14["text"] == "X" and bo.b16["text"] == "X":
        bo.b10.config(bg="green")
        bo.b11.config(bg="green")
        bo.b12.config(bg="green")
        bo.b13.config(bg="green")
        bo.b14.config(bg="green")
        bo.b15.config(bg="green")
        bo.b16.config(bg="green")
        bo.b17.config(bg="green")
        bo.b18.config(bg="green")
        winner = True
        Listwin[1] = 1
       

    # Checking for O wins
    if bo.b10["text"] == "O" and bo.b11["text"] == "O" and bo.b12["text"] == "O":
        bo.b10.config(bg="blue")
        bo.b11.config(bg="blue")
        bo.b12.config(bg="blue")
        bo.b13.config(bg="blue")
        bo.b14.config(bg="blue")
        bo.b15.config(bg="blue")
        bo.b16.config(bg="blue")
        bo.b17.config(bg="blue")
        bo.b18.config(bg="blue")
        winner = True
        Listwin[1] = 2
       
    elif bo.b13["text"] == "O" and bo.b14["text"] == "O" and bo.b15["text"] == "O":
        bo.b10.config(bg="blue")
        bo.b11.config(bg="blue")
        bo.b12.config(bg="blue")
        bo.b13.config(bg="blue")
        bo.b14.config(bg="blue")
        bo.b15.config(bg="blue")
        bo.b16.config(bg="blue")
        bo.b17.config(bg="blue")
        bo.b18.config(bg="blue")
        winner = True
        Listwin[1] = 2
       
    elif bo.b16["text"] == "O" and bo.b17["text"] == "O" and bo.b18["text"] == "O":
        bo.b10.config(bg="blue")
        bo.b11.config(bg="blue")
        bo.b12.config(bg="blue")
        bo.b13.config(bg="blue")
        bo.b14.config(bg="blue")
        bo.b15.config(bg="blue")
        bo.b16.config(bg="blue")
        bo.b17.config(bg="blue")
        bo.b18.config(bg="blue")
        winner = True
        Listwin[1] = 2
       
    elif bo.b10["text"] == "O" and bo.b13["text"] == "O" and bo.b16["text"] == "O":
        bo.b10.config(bg="blue")
        bo.b11.config(bg="blue")
        bo.b12.config(bg="blue")
        bo.b13.config(bg="blue")
        bo.b14.config(bg="blue")
        bo.b15.config(bg="blue")
        bo.b16.config(bg="blue")
        bo.b17.config(bg="blue")
        bo.b18.config(bg="blue")
        winner = True
        Listwin[1] = 2
       
    elif bo.b11["text"] == "O" and bo.b14["text"] == "O" and bo.b17["text"] == "O":
        bo.b10.config(bg="blue")
        bo.b11.config(bg="blue")
        bo.b12.config(bg="blue")
        bo.b13.config(bg="blue")
        bo.b14.config(bg="blue")
        bo.b15.config(bg="blue")
        bo.b16.config(bg="blue")
        bo.b17.config(bg="blue")
        bo.b18.config(bg="blue")
        winner = True
        Listwin[1] = 2
        

    elif bo.b12["text"] == "O" and bo.b15["text"] == "O" and bo.b18["text"] == "O":
        bo.b10.config(bg="blue")
        bo.b11.config(bg="blue")
        bo.b12.config(bg="blue")
        bo.b13.config(bg="blue")
        bo.b14.config(bg="blue")
        bo.b15.config(bg="blue")
        bo.b16.config(bg="blue")
        bo.b17.config(bg="blue")
        bo.b18.config(bg="blue")
        winner = True
        Listwin[1] = 2
        

    elif bo.b10["text"] == "O" and bo.b14["text"] == "O" and bo.b18["text"] == "O":
        bo.b10.config(bg="blue")
        bo.b11.config(bg="blue")
        bo.b12.config(bg="blue")
        bo.b13.config(bg="blue")
        bo.b14.config(bg="blue")
        bo.b15.config(bg="blue")
        bo.b16.config(bg="blue")
        bo.b17.config(bg="blue")
        bo.b18.config(bg="blue")
        winner = True
        Listwin[1] = 2
        

    elif bo.b12["text"] == "O" and bo.b14["text"] == "O" and bo.b16["text"] == "O":
        bo.b10.config(bg="blue")
        bo.b11.config(bg="blue")
        bo.b12.config(bg="blue")
        bo.b13.config(bg="blue")
        bo.b14.config(bg="blue")
        bo.b15.config(bg="blue")
        bo.b16.config(bg="blue")
        bo.b17.config(bg="blue")
        bo.b18.config(bg="blue")
        winner = True
        Listwin[1] = 2
       

    if bo.b10["text"] != "" and bo.b11["text"] != "" and bo.b12["text"] != "" and bo.b13["text"] != "" and bo.b14[
        "text"] != "" and bo.b15["text"] != "" and bo.b16["text"] != "" and bo.b17["text"] != "" and bo.b18[
        "text"] != "" and winner == False:
        bo.b10.config(bg="red")
        bo.b11.config(bg="red")
        bo.b12.config(bg="red")
        bo.b13.config(bg="red")
        bo.b14.config(bg="red")
        bo.b15.config(bg="red")
        bo.b16.config(bg="red")
        bo.b17.config(bg="red")
        bo.b18.config(bg="red")
        Listwin[1] = 3
        winner = True

    if winner == True:
        count2 = 1


def win3():
    """
This function determines who wins board three of the nine three by three smaller tic tac toe boards using if/else
statements. If X turns three blank buttons into X boxes in a row, X wins the board. If O turns three blank buttons into
O boxes in a row, O wins the board. If there are no winners after all 9 buttons are clicked, the game is a tie.
                        """
    global winner
    winner = False
    global count3
    count3 = 0
    # Checking for X wins
    if bo.b19["text"] == "X" and bo.b20["text"] == "X" and bo.b21["text"] == "X":
        bo.b19.config(bg="green")
        bo.b20.config(bg="green")
        bo.b21.config(bg="green")
        bo.b22.config(bg="green")
        bo.b23.config(bg="green")
        bo.b24.config(bg="green")
        bo.b25.config(bg="green")
        bo.b26.config(bg="green")
        bo.b27.config(bg="green")

        winner = True
        Listwin[2] = 1
        
    elif bo.b22["text"] == "X" and bo.b23["text"] == "X" and bo.b24["text"] == "X":
        bo.b19.config(bg="green")
        bo.b20.config(bg="green")
        bo.b21.config(bg="green")
        bo.b22.config(bg="green")
        bo.b23.config(bg="green")
        bo.b24.config(bg="green")
        bo.b25.config(bg="green")
        bo.b26.config(bg="green")
        bo.b27.config(bg="green")
        winner = True
        Listwin[2] = 1
        
    elif bo.b25["text"] == "X" and bo.b26["text"] == "X" and bo.b27["text"] == "X":
        bo.b19.config(bg="green")
        bo.b20.config(bg="green")
        bo.b21.config(bg="green")
        bo.b22.config(bg="green")
        bo.b23.config(bg="green")
        bo.b24.config(bg="green")
        bo.b25.config(bg="green")
        bo.b26.config(bg="green")
        bo.b27.config(bg="green")
        winner = True
        Listwin[2] = 1

       
    elif bo.b19["text"] == "X" and bo.b22["text"] == "X" and bo.b25["text"] == "X":
        bo.b19.config(bg="green")
        bo.b20.config(bg="green")
        bo.b21.config(bg="green")
        bo.b22.config(bg="green")
        bo.b23.config(bg="green")
        bo.b24.config(bg="green")
        bo.b25.config(bg="green")
        bo.b26.config(bg="green")
        bo.b27.config(bg="green")
        winner = True
        Listwin[2] = 1

        
    elif bo.b20["text"] == "X" and bo.b23["text"] == "X" and bo.b26["text"] == "X":
        bo.b19.config(bg="green")
        bo.b20.config(bg="green")
        bo.b21.config(bg="green")
        bo.b22.config(bg="green")
        bo.b23.config(bg="green")
        bo.b24.config(bg="green")
        bo.b25.config(bg="green")
        bo.b26.config(bg="green")
        bo.b27.config(bg="green")
        winner = True
        Listwin[2] = 1

        

    elif bo.b21["text"] == "X" and bo.b24["text"] == "X" and bo.b27["text"] == "X":
        bo.b19.config(bg="green")
        bo.b20.config(bg="green")
        bo.b21.config(bg="green")
        bo.b22.config(bg="green")
        bo.b23.config(bg="green")
        bo.b24.config(bg="green")
        bo.b25.config(bg="green")
        bo.b26.config(bg="green")
        bo.b27.config(bg="green")
        winner = True
        Listwin[2] = 1

       

    elif bo.b19["text"] == "X" and bo.b23["text"] == "X" and bo.b27["text"] == "X":
        bo.b19.config(bg="green")
        bo.b20.config(bg="green")
        bo.b21.config(bg="green")
        bo.b22.config(bg="green")
        bo.b23.config(bg="green")
        bo.b24.config(bg="green")
        bo.b25.config(bg="green")
        bo.b26.config(bg="green")
        bo.b27.config(bg="green")
        winner = True
        Listwin[2] = 1

        

    elif bo.b21["text"] == "X" and bo.b23["text"] == "X" and bo.b25["text"] == "X":
        bo.b19.config(bg="green")
        bo.b20.config(bg="green")
        bo.b21.config(bg="green")
        bo.b22.config(bg="green")
        bo.b23.config(bg="green")
        bo.b24.config(bg="green")
        bo.b25.config(bg="green")
        bo.b26.config(bg="green")
        bo.b27.config(bg="green")
        winner = True
        Listwin[2] = 1
       

    # Checking for O wins
    if bo.b19["text"] == "O" and bo.b20["text"] == "O" and bo.b21["text"] == "O":
        bo.b19.config(bg="blue")
        bo.b20.config(bg="blue")
        bo.b21.config(bg="blue")
        bo.b22.config(bg="blue")
        bo.b23.config(bg="blue")
        bo.b24.config(bg="blue")
        bo.b25.config(bg="blue")
        bo.b26.config(bg="blue")
        bo.b27.config(bg="blue")
        winner = True
        Listwin[2] = 2
       
    elif bo.b22["text"] == "O" and bo.b23["text"] == "O" and bo.b24["text"] == "O":
        bo.b19.config(bg="blue")
        bo.b20.config(bg="blue")
        bo.b21.config(bg="blue")
        bo.b22.config(bg="blue")
        bo.b23.config(bg="blue")
        bo.b24.config(bg="blue")
        bo.b25.config(bg="blue")
        bo.b26.config(bg="blue")
        bo.b27.config(bg="blue")
        winner = True
        Listwin[2] = 2
        
    elif bo.b25["text"] == "O" and bo.b26["text"] == "O" and bo.b27["text"] == "O":
        bo.b19.config(bg="blue")
        bo.b20.config(bg="blue")
        bo.b21.config(bg="blue")
        bo.b22.config(bg="blue")
        bo.b23.config(bg="blue")
        bo.b24.config(bg="blue")
        bo.b25.config(bg="blue")
        bo.b26.config(bg="blue")
        bo.b27.config(bg="blue")
        winner = True
        Listwin[2] = 2
   

    elif bo.b19["text"] == "O" and bo.b22["text"] == "O" and bo.b25["text"] == "O":
        bo.b19.config(bg="blue")
        bo.b20.config(bg="blue")
        bo.b21.config(bg="blue")
        bo.b22.config(bg="blue")
        bo.b23.config(bg="blue")
        bo.b24.config(bg="blue")
        bo.b25.config(bg="blue")
        bo.b26.config(bg="blue")
        bo.b27.config(bg="blue")
        winner = True
        Listwin[2] = 2
    
    elif bo.b20["text"] == "O" and bo.b23["text"] == "O" and bo.b26["text"] == "O":
        bo.b19.config(bg="blue")
        bo.b20.config(bg="blue")
        bo.b21.config(bg="blue")
        bo.b22.config(bg="blue")
        bo.b23.config(bg="blue")
        bo.b24.config(bg="blue")
        bo.b25.config(bg="blue")
        bo.b26.config(bg="blue")
        bo.b27.config(bg="blue")
        winner = True
        Listwin[2] = 2
       

    elif bo.b21["text"] == "O" and bo.b24["text"] == "O" and bo.b27["text"] == "O":
        bo.b19.config(bg="blue")
        bo.b20.config(bg="blue")
        bo.b21.config(bg="blue")
        bo.b22.config(bg="blue")
        bo.b23.config(bg="blue")
        bo.b24.config(bg="blue")
        bo.b25.config(bg="blue")
        bo.b26.config(bg="blue")
        bo.b27.config(bg="blue")
        winner = True
        Listwin[2] = 2
        

    elif bo.b19["text"] == "O" and bo.b23["text"] == "O" and bo.b27["text"] == "O":
        bo.b19.config(bg="blue")
        bo.b20.config(bg="blue")
        bo.b21.config(bg="blue")
        bo.b22.config(bg="blue")
        bo.b23.config(bg="blue")
        bo.b24.config(bg="blue")
        bo.b25.config(bg="blue")
        bo.b26.config(bg="blue")
        bo.b27.config(bg="blue")
        winner = True
        Listwin[2] = 2
        

    elif bo.b21["text"] == "O" and bo.b23["text"] == "O" and bo.b25["text"] == "O":
        bo.b19.config(bg="blue")
        bo.b20.config(bg="blue")
        bo.b21.config(bg="blue")
        bo.b22.config(bg="blue")
        bo.b23.config(bg="blue")
        bo.b24.config(bg="blue")
        bo.b25.config(bg="blue")
        bo.b26.config(bg="blue")
        bo.b27.config(bg="blue")
        winner = True
        Listwin[2] = 2

    if bo.b19["text"] != "" and bo.b20["text"] != "" and bo.b21["text"] != "" and bo.b22["text"] != "" and bo.b23[
        "text"] != "" and bo.b24["text"] != "" and bo.b25["text"] != "" and bo.b26["text"] != "" and bo.b27[
        "text"] != "" and winner == False:
        bo.b19.config(bg="red")
        bo.b20.config(bg="red")
        bo.b21.config(bg="red")
        bo.b22.config(bg="red")
        bo.b23.config(bg="red")
        bo.b24.config(bg="red")
        bo.b25.config(bg="red")
        bo.b26.config(bg="red")
        bo.b27.config(bg="red")
        Listwin[2] = 3
        winner = True
    if winner == True:
        count3 = 1


def win4():
    """
This function determines who wins board four of the nine three by three smaller tic tac toe boards using if/else
statements. If X turns three blank buttons into X boxes in a row, X wins the board. If O turns three blank buttons into
O boxes in a row, O wins the board. If there are no winners after all 9 buttons are clicked, the game is a tie.
                        """
    global winner
    winner = False
    global count4
    count4 = 0

    # Checking for X wins
    if bo.b28["text"] == "X" and bo.b29["text"] == "X" and bo.b30["text"] == "X":
        bo.b28.config(bg="green")
        bo.b29.config(bg="green")
        bo.b30.config(bg="green")
        bo.b31.config(bg="green")
        bo.b32.config(bg="green")
        bo.b33.config(bg="green")
        bo.b34.config(bg="green")
        bo.b35.config(bg="green")
        bo.b36.config(bg="green")

        winner = True
        Listwin[3] = 1
       
    elif bo.b31["text"] == "X" and bo.b32["text"] == "X" and bo.b33["text"] == "X":
        bo.b28.config(bg="green")
        bo.b29.config(bg="green")
        bo.b30.config(bg="green")
        bo.b31.config(bg="green")
        bo.b32.config(bg="green")
        bo.b33.config(bg="green")
        bo.b34.config(bg="green")
        bo.b35.config(bg="green")
        bo.b36.config(bg="green")
        winner = True
        Listwin[3] = 1
        messagebox.showinfo("tic tac toe", "Player X won the game!")
       
    elif bo.b34["text"] == "X" and bo.b35["text"] == "X" and bo.b36["text"] == "X":
        bo.b28.config(bg="green")
        bo.b29.config(bg="green")
        bo.b30.config(bg="green")
        bo.b31.config(bg="green")
        bo.b32.config(bg="green")
        bo.b33.config(bg="green")
        bo.b34.config(bg="green")
        bo.b35.config(bg="green")
        bo.b36.config(bg="green")
        winner = True
        Listwin[3] = 1
       
    elif bo.b28["text"] == "X" and bo.b31["text"] == "X" and bo.b34["text"] == "X":
        bo.b28.config(bg="green")
        bo.b29.config(bg="green")
        bo.b30.config(bg="green")
        bo.b31.config(bg="green")
        bo.b32.config(bg="green")
        bo.b33.config(bg="green")
        bo.b34.config(bg="green")
        bo.b35.config(bg="green")
        bo.b36.config(bg="green")
        winner = True
        Listwin[3] = 1
       
    elif bo.b29["text"] == "X" and bo.b32["text"] == "X" and bo.b35["text"] == "X":
        bo.b28.config(bg="green")
        bo.b29.config(bg="green")
        bo.b30.config(bg="green")
        bo.b31.config(bg="green")
        bo.b32.config(bg="green")
        bo.b33.config(bg="green")
        bo.b34.config(bg="green")
        bo.b35.config(bg="green")
        bo.b36.config(bg="green")
        winner = True
        Listwin[3] = 1
       

    elif bo.b30["text"] == "X" and bo.b33["text"] == "X" and bo.b36["text"] == "X":
        bo.b28.config(bg="green")
        bo.b29.config(bg="green")
        bo.b30.config(bg="green")
        bo.b31.config(bg="green")
        bo.b32.config(bg="green")
        bo.b33.config(bg="green")
        bo.b34.config(bg="green")
        bo.b35.config(bg="green")
        bo.b36.config(bg="green")
        winner = True
        Listwin[3] = 1
       

    elif bo.b28["text"] == "X" and bo.b32["text"] == "X" and bo.b36["text"] == "X":
        bo.b28.config(bg="green")
        bo.b29.config(bg="green")
        bo.b30.config(bg="green")
        bo.b31.config(bg="green")
        bo.b32.config(bg="green")
        bo.b33.config(bg="green")
        bo.b34.config(bg="green")
        bo.b35.config(bg="green")
        bo.b36.config(bg="green")
        winner = True
        Listwin[3] = 1
       

    elif bo.b30["text"] == "X" and bo.b32["text"] == "X" and bo.b34["text"] == "X":
        bo.b28.config(bg="green")
        bo.b29.config(bg="green")
        bo.b30.config(bg="green")
        bo.b31.config(bg="green")
        bo.b32.config(bg="green")
        bo.b33.config(bg="green")
        bo.b34.config(bg="green")
        bo.b35.config(bg="green")
        bo.b36.config(bg="green")
        winner = True
        Listwin[3] = 1
       

    # Checking for O wins
    if bo.b28["text"] == "O" and bo.b29["text"] == "O" and bo.b30["text"] == "O":
        bo.b28.config(bg="blue")
        bo.b29.config(bg="blue")
        bo.b30.config(bg="blue")
        bo.b31.config(bg="blue")
        bo.b32.config(bg="blue")
        bo.b33.config(bg="blue")
        bo.b34.config(bg="blue")
        bo.b35.config(bg="blue")
        bo.b36.config(bg="blue")
        winner = True
        Listwin[3] = 2
       
    elif bo.b31["text"] == "O" and bo.b32["text"] == "O" and bo.b33["text"] == "O":
        bo.b28.config(bg="blue")
        bo.b29.config(bg="blue")
        bo.b30.config(bg="blue")
        bo.b31.config(bg="blue")
        bo.b32.config(bg="blue")
        bo.b33.config(bg="blue")
        bo.b34.config(bg="blue")
        bo.b35.config(bg="blue")
        bo.b36.config(bg="blue")
        winner = True
        Listwin[3] = 2
       
    elif bo.b34["text"] == "O" and bo.b35["text"] == "O" and bo.b36["text"] == "O":
        bo.b28.config(bg="blue")
        bo.b29.config(bg="blue")
        bo.b30.config(bg="blue")
        bo.b31.config(bg="blue")
        bo.b32.config(bg="blue")
        bo.b33.config(bg="blue")
        bo.b34.config(bg="blue")
        bo.b35.config(bg="blue")
        bo.b36.config(bg="blue")
        winner = True
        Listwin[3] = 2
       
    elif bo.b28["text"] == "O" and bo.b31["text"] == "O" and bo.b34["text"] == "O":
        bo.b28.config(bg="blue")
        bo.b29.config(bg="blue")
        bo.b30.config(bg="blue")
        bo.b31.config(bg="blue")
        bo.b32.config(bg="blue")
        bo.b33.config(bg="blue")
        bo.b34.config(bg="blue")
        bo.b35.config(bg="blue")
        bo.b36.config(bg="blue")
        winner = True
        Listwin[3] = 2
       
    elif bo.b29["text"] == "O" and bo.b32["text"] == "O" and bo.b35["text"] == "O":
        bo.b28.config(bg="blue")
        bo.b29.config(bg="blue")
        bo.b30.config(bg="blue")
        bo.b31.config(bg="blue")
        bo.b32.config(bg="blue")
        bo.b33.config(bg="blue")
        bo.b34.config(bg="blue")
        bo.b35.config(bg="blue")
        bo.b36.config(bg="blue")
        winner = True
        Listwin[3] = 2
       

    elif bo.b30["text"] == "O" and bo.b33["text"] == "O" and bo.b36["text"] == "O":
        bo.b28.config(bg="blue")
        bo.b29.config(bg="blue")
        bo.b30.config(bg="blue")
        bo.b31.config(bg="blue")
        bo.b32.config(bg="blue")
        bo.b33.config(bg="blue")
        bo.b34.config(bg="blue")
        bo.b35.config(bg="blue")
        bo.b36.config(bg="blue")
        winner = True
        Listwin[3] = 2
       

    elif bo.b28["text"] == "O" and bo.b32["text"] == "O" and bo.b36["text"] == "O":
        bo.b28.config(bg="blue")
        bo.b29.config(bg="blue")
        bo.b30.config(bg="blue")
        bo.b31.config(bg="blue")
        bo.b32.config(bg="blue")
        bo.b33.config(bg="blue")
        bo.b34.config(bg="blue")
        bo.b35.config(bg="blue")
        bo.b36.config(bg="blue")
        winner = True
        Listwin[3] = 2
       

    elif bo.b30["text"] == "O" and bo.b32["text"] == "O" and bo.b34["text"] == "O":
        bo.b28.config(bg="blue")
        bo.b29.config(bg="blue")
        bo.b30.config(bg="blue")
        bo.b31.config(bg="blue")
        bo.b32.config(bg="blue")
        bo.b33.config(bg="blue")
        bo.b34.config(bg="blue")
        bo.b35.config(bg="blue")
        bo.b36.config(bg="blue")
        winner = True
        Listwin[3] = 2

    if bo.b28["text"] != "" and bo.b29["text"] != "" and bo.b30["text"] != "" and bo.b31["text"] != "" and bo.b32[
        "text"] != "" and bo.b33["text"] != "" and bo.b34["text"] != "" and bo.b35["text"] != "" and bo.b36[
        "text"] != "" and winner == False:
        bo.b28.config(bg="red")
        bo.b29.config(bg="red")
        bo.b30.config(bg="red")
        bo.b31.config(bg="red")
        bo.b32.config(bg="red")
        bo.b33.config(bg="red")
        bo.b34.config(bg="red")
        bo.b35.config(bg="red")
        bo.b36.config(bg="red")
        Listwin[3] = 3
        winner = True

    if winner == True:
        count4 = 1


def win5():
    """
This function determines who wins board five of the nine three by three smaller tic tac toe boards using if/else
statements. If X turns three blank buttons into X boxes in a row, X wins the board. If O turns three blank buttons into
O boxes in a row, O wins the board. If there are no winners after all 9 buttons are clicked, the game is a tie.
                        """
    global winner
    winner = False
    global count5
    count5 = 0

    # Checking for X wins
    if bo.b37["text"] == "X" and bo.b38["text"] == "X" and bo.b39["text"] == "X":
        bo.b37.config(bg="green")
        bo.b38.config(bg="green")
        bo.b39.config(bg="green")
        bo.b40.config(bg="green")
        bo.b41.config(bg="green")
        bo.b42.config(bg="green")
        bo.b43.config(bg="green")
        bo.b44.config(bg="green")
        bo.b45.config(bg="green")
        winner = True
        Listwin[4] = 1

    elif bo.b40["text"] == "X" and bo.b41["text"] == "X" and bo.b42["text"] == "X":
        bo.b37.config(bg="green")
        bo.b38.config(bg="green")
        bo.b39.config(bg="green")
        bo.b40.config(bg="green")
        bo.b41.config(bg="green")
        bo.b42.config(bg="green")
        bo.b43.config(bg="green")
        bo.b44.config(bg="green")
        bo.b45.config(bg="green")
        winner = True
        Listwin[4] = 1

    elif bo.b43["text"] == "X" and bo.b44["text"] == "X" and bo.b45["text"] == "X":
        bo.b37.config(bg="green")
        bo.b38.config(bg="green")
        bo.b39.config(bg="green")
        bo.b40.config(bg="green")
        bo.b41.config(bg="green")
        bo.b42.config(bg="green")
        bo.b43.config(bg="green")
        bo.b44.config(bg="green")
        bo.b45.config(bg="green")
        winner = True
        Listwin[4] = 1

    elif bo.b37["text"] == "X" and bo.b40["text"] == "X" and bo.b43["text"] == "X":
        bo.b37.config(bg="green")
        bo.b38.config(bg="green")
        bo.b39.config(bg="green")
        bo.b40.config(bg="green")
        bo.b41.config(bg="green")
        bo.b42.config(bg="green")
        bo.b43.config(bg="green")
        bo.b44.config(bg="green")
        bo.b45.config(bg="green")
        winner = True
        Listwin[4] = 1
    ## #disable_all_buttons()
    elif bo.b38["text"] == "X" and bo.b41["text"] == "X" and bo.b44["text"] == "X":
        bo.b37.config(bg="green")
        bo.b38.config(bg="green")
        bo.b39.config(bg="green")
        bo.b40.config(bg="green")
        bo.b41.config(bg="green")
        bo.b42.config(bg="green")
        bo.b43.config(bg="green")
        bo.b44.config(bg="green")
        bo.b45.config(bg="green")
        winner = True
        Listwin[4] = 1
    ## #disable_all_buttons()

    elif bo.b39["text"] == "X" and bo.b42["text"] == "X" and bo.b45["text"] == "X":
        bo.b37.config(bg="green")
        bo.b38.config(bg="green")
        bo.b39.config(bg="green")
        bo.b40.config(bg="green")
        bo.b41.config(bg="green")
        bo.b42.config(bg="green")
        bo.b43.config(bg="green")
        bo.b44.config(bg="green")
        bo.b45.config(bg="green")
        winner = True
        Listwin[4] = 1
    ## #disable_all_buttons()

    elif bo.b37["text"] == "X" and bo.b41["text"] == "X" and bo.b45["text"] == "X":
        bo.b37.config(bg="green")
        bo.b38.config(bg="green")
        bo.b39.config(bg="green")
        bo.b40.config(bg="green")
        bo.b41.config(bg="green")
        bo.b42.config(bg="green")
        bo.b43.config(bg="green")
        bo.b44.config(bg="green")
        bo.b45.config(bg="green")
        winner = True
        Listwin[4] = 1
    ## #disable_all_buttons()

    elif bo.b39["text"] == "X" and bo.b41["text"] == "X" and bo.b43["text"] == "X":
        bo.b37.config(bg="green")
        bo.b38.config(bg="green")
        bo.b39.config(bg="green")
        bo.b40.config(bg="green")
        bo.b41.config(bg="green")
        bo.b42.config(bg="green")
        bo.b43.config(bg="green")
        bo.b44.config(bg="green")
        bo.b45.config(bg="green")
        winner = True
        Listwin[4] = 1
    ## #disable_all_buttons()

    # Checking for O wins
    # Checking for O wins
    if bo.b37["text"] == "O" and bo.b38["text"] == "O" and bo.b39["text"] == "O":
        bo.b37.config(bg="blue")
        bo.b38.config(bg="blue")
        bo.b39.config(bg="blue")
        bo.b40.config(bg="blue")
        bo.b41.config(bg="blue")
        bo.b42.config(bg="blue")
        bo.b43.config(bg="blue")
        bo.b44.config(bg="blue")
        bo.b45.config(bg="blue")
        winner = True
        Listwin[4] = 2
    ## #disable_all_buttons()
    elif bo.b40["text"] == "O" and bo.b41["text"] == "O" and bo.b42["text"] == "O":
        bo.b37.config(bg="blue")
        bo.b38.config(bg="blue")
        bo.b39.config(bg="blue")
        bo.b40.config(bg="blue")
        bo.b41.config(bg="blue")
        bo.b42.config(bg="blue")
        bo.b43.config(bg="blue")
        bo.b44.config(bg="blue")
        bo.b45.config(bg="blue")
        winner = True
        Listwin[4] = 2
    ## #disable_all_buttons()
    elif bo.b43["text"] == "O" and bo.b44["text"] == "O" and bo.b45["text"] == "O":
        bo.b37.config(bg="blue")
        bo.b38.config(bg="blue")
        bo.b39.config(bg="blue")
        bo.b40.config(bg="blue")
        bo.b41.config(bg="blue")
        bo.b42.config(bg="blue")
        bo.b43.config(bg="blue")
        bo.b44.config(bg="blue")
        bo.b45.config(bg="blue")
        winner = True
        Listwin[4] = 2
    ## #disable_all_buttons()
    elif bo.b37["text"] == "O" and bo.b40["text"] == "O" and bo.b43["text"] == "O":
        bo.b37.config(bg="blue")
        bo.b38.config(bg="blue")
        bo.b39.config(bg="blue")
        bo.b40.config(bg="blue")
        bo.b41.config(bg="blue")
        bo.b42.config(bg="blue")
        bo.b43.config(bg="blue")
        bo.b44.config(bg="blue")
        bo.b45.config(bg="blue")
        winner = True
        Listwin[4] = 2
    ## #disable_all_buttons()
    elif bo.b38["text"] == "O" and bo.b41["text"] == "O" and bo.b44["text"] == "O":
        bo.b37.config(bg="blue")
        bo.b38.config(bg="blue")
        bo.b39.config(bg="blue")
        bo.b40.config(bg="blue")
        bo.b41.config(bg="blue")
        bo.b42.config(bg="blue")
        bo.b43.config(bg="blue")
        bo.b44.config(bg="blue")
        bo.b45.config(bg="blue")
        winner = True
        Listwin[4] = 2
    ## #disable_all_buttons()

    elif bo.b39["text"] == "O" and bo.b42["text"] == "O" and bo.b45["text"] == "O":
        bo.b37.config(bg="blue")
        bo.b38.config(bg="blue")
        bo.b39.config(bg="blue")
        bo.b40.config(bg="blue")
        bo.b41.config(bg="blue")
        bo.b42.config(bg="blue")
        bo.b43.config(bg="blue")
        bo.b44.config(bg="blue")
        bo.b45.config(bg="blue")
        winner = True
        Listwin[4] = 2
    ## #disable_all_buttons()

    elif bo.b37["text"] == "O" and bo.b41["text"] == "O" and bo.b45["text"] == "O":
        bo.b37.config(bg="blue")
        bo.b38.config(bg="blue")
        bo.b39.config(bg="blue")
        bo.b40.config(bg="blue")
        bo.b41.config(bg="blue")
        bo.b42.config(bg="blue")
        bo.b43.config(bg="blue")
        bo.b44.config(bg="blue")
        bo.b45.config(bg="blue")
        winner = True
        Listwin[4] = 2
    ## #disable_all_buttons()

    elif bo.b39["text"] == "O" and bo.b41["text"] == "O" and bo.b43["text"] == "O":
        bo.b37.config(bg="blue")
        bo.b38.config(bg="blue")
        bo.b39.config(bg="blue")
        bo.b40.config(bg="blue")
        bo.b41.config(bg="blue")
        bo.b42.config(bg="blue")
        bo.b43.config(bg="blue")
        bo.b44.config(bg="blue")
        bo.b45.config(bg="blue")
        winner = True
        Listwin[4] = 2

    if bo.b37["text"] != "" and bo.b38["text"] != "" and bo.b39["text"] != "" and bo.b40["text"] != "" and bo.b41[
        "text"] != "" and bo.b42["text"] != "" and bo.b43["text"] != "" and bo.b44["text"] != "" and bo.b45[
        "text"] != "" and winner == False:
        bo.b37.config(bg="red")
        bo.b38.config(bg="red")
        bo.b39.config(bg="red")
        bo.b40.config(bg="red")
        bo.b41.config(bg="red")
        bo.b42.config(bg="red")
        bo.b43.config(bg="red")
        bo.b44.config(bg="red")
        bo.b45.config(bg="red")
        Listwin[4] = 3
        winner = True

    if winner == True:
        count5 = 1


def win6():
    """
This function determines who wins board six of the nine three by three smaller tic tac toe boards using if/else
statements. If X turns three blank buttons into X boxes in a row, X wins the board. If O turns three blank buttons into
O boxes in a row, O wins the board. If there are no winners after all 9 buttons are clicked, the game is a tie.
                        """
    global winner
    winner = False
    global count6
    count6 = 0

    # Checking for X wins
    if bo.b46["text"] == "X" and bo.b47["text"] == "X" and bo.b48["text"] == "X":
        bo.b46.config(bg="green")
        bo.b47.config(bg="green")
        bo.b48.config(bg="green")
        bo.b49.config(bg="green")
        bo.b50.config(bg="green")
        bo.b51.config(bg="green")
        bo.b52.config(bg="green")
        bo.b53.config(bg="green")
        bo.b54.config(bg="green")
        winner = True
        Listwin[5] = 1
    # #disable_all_buttons()
    elif bo.b49["text"] == "X" and bo.b50["text"] == "X" and bo.b51["text"] == "X":
        bo.b46.config(bg="green")
        bo.b47.config(bg="green")
        bo.b48.config(bg="green")
        bo.b49.config(bg="green")
        bo.b50.config(bg="green")
        bo.b51.config(bg="green")
        bo.b52.config(bg="green")
        bo.b53.config(bg="green")
        bo.b54.config(bg="green")
        winner = True
        Listwin[5] = 1
    # #disable_all_buttons()
    elif bo.b52["text"] == "X" and bo.b53["text"] == "X" and bo.b54["text"] == "X":
        bo.b46.config(bg="green")
        bo.b47.config(bg="green")
        bo.b48.config(bg="green")
        bo.b49.config(bg="green")
        bo.b50.config(bg="green")
        bo.b51.config(bg="green")
        bo.b52.config(bg="green")
        bo.b53.config(bg="green")
        bo.b54.config(bg="green")
        winner = True
        Listwin[5] = 1
    # #disable_all_buttons()
    elif bo.b46["text"] == "X" and bo.b49["text"] == "X" and bo.b52["text"] == "X":
        bo.b46.config(bg="green")
        bo.b47.config(bg="green")
        bo.b48.config(bg="green")
        bo.b49.config(bg="green")
        bo.b50.config(bg="green")
        bo.b51.config(bg="green")
        bo.b52.config(bg="green")
        bo.b53.config(bg="green")
        bo.b54.config(bg="green")
        winner = True
        Listwin[5] = 1
    # #disable_all_buttons()
    elif bo.b47["text"] == "X" and bo.b50["text"] == "X" and bo.b53["text"] == "X":
        bo.b46.config(bg="green")
        bo.b47.config(bg="green")
        bo.b48.config(bg="green")
        bo.b49.config(bg="green")
        bo.b50.config(bg="green")
        bo.b51.config(bg="green")
        bo.b52.config(bg="green")
        bo.b53.config(bg="green")
        bo.b54.config(bg="green")
        winner = True
        Listwin[5] = 1
    # #disable_all_buttons()

    elif bo.b48["text"] == "X" and bo.b51["text"] == "X" and bo.b54["text"] == "X":
        bo.b46.config(bg="green")
        bo.b47.config(bg="green")
        bo.b48.config(bg="green")
        bo.b49.config(bg="green")
        bo.b50.config(bg="green")
        bo.b51.config(bg="green")
        bo.b52.config(bg="green")
        bo.b53.config(bg="green")
        bo.b54.config(bg="green")
        winner = True
        Listwin[5] = 1
    # #disable_all_buttons()

    elif bo.b46["text"] == "X" and bo.b50["text"] == "X" and bo.b54["text"] == "X":
        bo.b46.config(bg="green")
        bo.b47.config(bg="green")
        bo.b48.config(bg="green")
        bo.b49.config(bg="green")
        bo.b50.config(bg="green")
        bo.b51.config(bg="green")
        bo.b52.config(bg="green")
        bo.b53.config(bg="green")
        bo.b54.config(bg="green")
        winner = True
        Listwin[5] = 1
    # #disable_all_buttons()

    elif bo.b48["text"] == "X" and bo.b50["text"] == "X" and bo.b52["text"] == "X":
        bo.b46.config(bg="green")
        bo.b47.config(bg="green")
        bo.b48.config(bg="green")
        bo.b49.config(bg="green")
        bo.b50.config(bg="green")
        bo.b51.config(bg="green")
        bo.b52.config(bg="green")
        bo.b53.config(bg="green")
        bo.b54.config(bg="green")
        winner = True
        Listwin[5] = 1
    # #disable_all_buttons()

    # Checking for O wins
    if bo.b46["text"] == "O" and bo.b47["text"] == "O" and bo.b48["text"] == "O":
        bo.b46.config(bg="blue")
        bo.b47.config(bg="blue")
        bo.b48.config(bg="blue")
        bo.b49.config(bg="blue")
        bo.b50.config(bg="blue")
        bo.b51.config(bg="blue")
        bo.b52.config(bg="blue")
        bo.b53.config(bg="blue")
        bo.b54.config(bg="blue")
        winner = True
        Listwin[5] = 2
    # #disable_all_buttons()
    elif bo.b49["text"] == "O" and bo.b50["text"] == "O" and bo.b51["text"] == "O":
        bo.b46.config(bg="blue")
        bo.b47.config(bg="blue")
        bo.b48.config(bg="blue")
        bo.b49.config(bg="blue")
        bo.b50.config(bg="blue")
        bo.b51.config(bg="blue")
        bo.b52.config(bg="blue")
        bo.b53.config(bg="blue")
        bo.b54.config(bg="blue")
        winner = True
        Listwin[5] = 2
    # #disable_all_buttons()
    elif bo.b52["text"] == "O" and bo.b53["text"] == "O" and bo.b54["text"] == "O":
        bo.b46.config(bg="blue")
        bo.b47.config(bg="blue")
        bo.b48.config(bg="blue")
        bo.b49.config(bg="blue")
        bo.b50.config(bg="blue")
        bo.b51.config(bg="blue")
        bo.b52.config(bg="blue")
        bo.b53.config(bg="blue")
        bo.b54.config(bg="blue")
        winner = True
        Listwin[5] = 2
    # #disable_all_buttons()
    elif bo.b46["text"] == "O" and bo.b49["text"] == "O" and bo.b52["text"] == "O":
        bo.b46.config(bg="blue")
        bo.b47.config(bg="blue")
        bo.b48.config(bg="blue")
        bo.b49.config(bg="blue")
        bo.b50.config(bg="blue")
        bo.b51.config(bg="blue")
        bo.b52.config(bg="blue")
        bo.b53.config(bg="blue")
        bo.b54.config(bg="blue")
        winner = True
        Listwin[5] = 2
    # #disable_all_buttons()
    elif bo.b47["text"] == "O" and bo.b50["text"] == "O" and bo.b53["text"] == "O":
        bo.b46.config(bg="blue")
        bo.b47.config(bg="blue")
        bo.b48.config(bg="blue")
        bo.b49.config(bg="blue")
        bo.b50.config(bg="blue")
        bo.b51.config(bg="blue")
        bo.b52.config(bg="blue")
        bo.b53.config(bg="blue")
        bo.b54.config(bg="blue")
        winner = True
        Listwin[5] = 2
    # #disable_all_buttons()

    elif bo.b48["text"] == "O" and bo.b51["text"] == "O" and bo.b54["text"] == "O":
        bo.b46.config(bg="blue")
        bo.b47.config(bg="blue")
        bo.b48.config(bg="blue")
        bo.b49.config(bg="blue")
        bo.b50.config(bg="blue")
        bo.b51.config(bg="blue")
        bo.b52.config(bg="blue")
        bo.b53.config(bg="blue")
        bo.b54.config(bg="blue")
        winner = True
        Listwin[5] = 2
    # #disable_all_buttons()

    elif bo.b46["text"] == "O" and bo.b50["text"] == "O" and bo.b54["text"] == "O":
        bo.b46.config(bg="blue")
        bo.b47.config(bg="blue")
        bo.b48.config(bg="blue")
        bo.b49.config(bg="blue")
        bo.b50.config(bg="blue")
        bo.b51.config(bg="blue")
        bo.b52.config(bg="blue")
        bo.b53.config(bg="blue")
        bo.b54.config(bg="blue")
        winner = True
        Listwin[5] = 2
    # #disable_all_buttons()

    elif bo.b48["text"] == "O" and bo.b50["text"] == "O" and bo.b52["text"] == "O":
        bo.b46.config(bg="blue")
        bo.b47.config(bg="blue")
        bo.b48.config(bg="blue")
        bo.b49.config(bg="blue")
        bo.b50.config(bg="blue")
        bo.b51.config(bg="blue")
        bo.b52.config(bg="blue")
        bo.b53.config(bg="blue")
        bo.b54.config(bg="blue")
        winner = True
        Listwin[5] = 2

    # #disable_all_buttons()
    if bo.b46["text"] != "" and bo.b47["text"] != "" and bo.b48["text"] != "" and bo.b49["text"] != "" and bo.b50[
        "text"] != "" and bo.b51["text"] != "" and bo.b52["text"] != "" and bo.b53["text"] != "" and bo.b54[
        "text"] != "" and winner == False:
        bo.b46.config(bg="red")
        bo.b47.config(bg="red")
        bo.b48.config(bg="red")
        bo.b49.config(bg="red")
        bo.b50.config(bg="red")
        bo.b51.config(bg="red")
        bo.b52.config(bg="red")
        bo.b53.config(bg="red")
        bo.b54.config(bg="red")
        Listwin[5] = 3
        winner = True

    if winner == True:
        count6 = 1


def win7():
    """
This function determines who wins board seven of the nine three by three smaller tic tac toe boards using if/else
statements. If X turns three blank buttons into X boxes in a row, X wins the board. If O turns three blank buttons into
O boxes in a row, O wins the board. If there are no winners after all 9 buttons are clicked, the game is a tie.
                        """
    global winner
    winner = False
    global count7
    count7 = 0
    # Checking for X wins
    if bo.b55["text"] == "X" and bo.b56["text"] == "X" and bo.b57["text"] == "X":
        bo.b55.config(bg="green")
        bo.b56.config(bg="green")
        bo.b57.config(bg="green")
        bo.b58.config(bg="green")
        bo.b59.config(bg="green")
        bo.b60.config(bg="green")
        bo.b61.config(bg="green")
        bo.b62.config(bg="green")
        bo.b63.config(bg="green")
        winner = True
        Listwin[6] = 1
        # disable_all_buttons()
    elif bo.b58["text"] == "X" and bo.b59["text"] == "X" and bo.b60["text"] == "X":
        bo.b55.config(bg="green")
        bo.b56.config(bg="green")
        bo.b57.config(bg="green")
        bo.b58.config(bg="green")
        bo.b59.config(bg="green")
        bo.b60.config(bg="green")
        bo.b61.config(bg="green")
        bo.b62.config(bg="green")
        bo.b63.config(bg="green")
        winner = True
        Listwin[6] = 1

        # disable_all_buttons()
    elif bo.b61["text"] == "X" and bo.b62["text"] == "X" and bo.b63["text"] == "X":
        bo.b55.config(bg="green")
        bo.b56.config(bg="green")
        bo.b57.config(bg="green")
        bo.b58.config(bg="green")
        bo.b59.config(bg="green")
        bo.b60.config(bg="green")
        bo.b61.config(bg="green")
        bo.b62.config(bg="green")
        bo.b63.config(bg="green")
        winner = True
        Listwin[6] = 1

        # disable_all_buttons()
    elif bo.b55["text"] == "X" and bo.b58["text"] == "X" and bo.b61["text"] == "X":
        bo.b55.config(bg="green")
        bo.b56.config(bg="green")
        bo.b57.config(bg="green")
        bo.b58.config(bg="green")
        bo.b59.config(bg="green")
        bo.b60.config(bg="green")
        bo.b61.config(bg="green")
        bo.b62.config(bg="green")
        bo.b63.config(bg="green")
        winner = True
        Listwin[6] = 1

        # disable_all_buttons()
    elif bo.b56["text"] == "X" and bo.b59["text"] == "X" and bo.b62["text"] == "X":
        bo.b55.config(bg="green")
        bo.b56.config(bg="green")
        bo.b57.config(bg="green")
        bo.b58.config(bg="green")
        bo.b59.config(bg="green")
        bo.b60.config(bg="green")
        bo.b61.config(bg="green")
        bo.b62.config(bg="green")
        bo.b63.config(bg="green")
        winner = True
        Listwin[6] = 1
        # disable_all_buttons()

    elif bo.b57["text"] == "X" and bo.b60["text"] == "X" and bo.b63["text"] == "X":
        bo.b55.config(bg="green")
        bo.b56.config(bg="green")
        bo.b57.config(bg="green")
        bo.b58.config(bg="green")
        bo.b59.config(bg="green")
        bo.b60.config(bg="green")
        bo.b61.config(bg="green")
        bo.b62.config(bg="green")
        bo.b63.config(bg="green")
        winner = True
        Listwin[6] = 1
        # disable_all_buttons()

    elif bo.b55["text"] == "X" and bo.b59["text"] == "X" and bo.b63["text"] == "X":
        bo.b55.config(bg="green")
        bo.b56.config(bg="green")
        bo.b57.config(bg="green")
        bo.b58.config(bg="green")
        bo.b59.config(bg="green")
        bo.b60.config(bg="green")
        bo.b61.config(bg="green")
        bo.b62.config(bg="green")
        bo.b63.config(bg="green")
        winner = True
        Listwin[6] = 1


    elif bo.b57["text"] == "X" and bo.b59["text"] == "X" and bo.b61["text"] == "X":
        bo.b55.config(bg="green")
        bo.b56.config(bg="green")
        bo.b57.config(bg="green")
        bo.b58.config(bg="green")
        bo.b59.config(bg="green")
        bo.b60.config(bg="green")
        bo.b61.config(bg="green")
        bo.b62.config(bg="green")
        bo.b63.config(bg="green")
        winner = True
        Listwin[6] = 1

    # Checking for O wins
    # Checking for O wins
    if bo.b55["text"] == "O" and bo.b56["text"] == "O" and bo.b57["text"] == "O":
        bo.b55.config(bg="blue")
        bo.b56.config(bg="blue")
        bo.b57.config(bg="blue")
        bo.b58.config(bg="blue")
        bo.b59.config(bg="blue")
        bo.b60.config(bg="blue")
        bo.b61.config(bg="blue")
        bo.b62.config(bg="blue")
        bo.b63.config(bg="blue")
        winner = True
        Listwin[6] = 2
        # disable_all_buttons()
    elif bo.b58["text"] == "O" and bo.b59["text"] == "O" and bo.b60["text"] == "O":
        bo.b55.config(bg="blue")
        bo.b56.config(bg="blue")
        bo.b57.config(bg="blue")
        bo.b58.config(bg="blue")
        bo.b59.config(bg="blue")
        bo.b60.config(bg="blue")
        bo.b61.config(bg="blue")
        bo.b62.config(bg="blue")
        bo.b63.config(bg="blue")
        winner = True
        Listwin[6] = 2
        # disable_all_buttons()
    elif bo.b61["text"] == "O" and bo.b62["text"] == "O" and bo.b63["text"] == "O":
        bo.b55.config(bg="blue")
        bo.b56.config(bg="blue")
        bo.b57.config(bg="blue")
        bo.b58.config(bg="blue")
        bo.b59.config(bg="blue")
        bo.b60.config(bg="blue")
        bo.b61.config(bg="blue")
        bo.b62.config(bg="blue")
        bo.b63.config(bg="blue")
        winner = True
        Listwin[6] = 2
        # disable_all_buttons()
    elif bo.b55["text"] == "O" and bo.b58["text"] == "O" and bo.b61["text"] == "O":
        bo.b55.config(bg="blue")
        bo.b56.config(bg="blue")
        bo.b57.config(bg="blue")
        bo.b58.config(bg="blue")
        bo.b59.config(bg="blue")
        bo.b60.config(bg="blue")
        bo.b61.config(bg="blue")
        bo.b62.config(bg="blue")
        bo.b63.config(bg="blue")
        winner = True
        Listwin[6] = 2
        # disable_all_buttons()
    elif bo.b56["text"] == "O" and bo.b59["text"] == "O" and bo.b62["text"] == "O":
        bo.b55.config(bg="blue")
        bo.b56.config(bg="blue")
        bo.b57.config(bg="blue")
        bo.b58.config(bg="blue")
        bo.b59.config(bg="blue")
        bo.b60.config(bg="blue")
        bo.b61.config(bg="blue")
        bo.b62.config(bg="blue")
        bo.b63.config(bg="blue")
        winner = True
        Listwin[6] = 2
        # disable_all_buttons()

    elif bo.b57["text"] == "O" and bo.b60["text"] == "O" and bo.b63["text"] == "O":
        bo.b55.config(bg="blue")
        bo.b56.config(bg="blue")
        bo.b57.config(bg="blue")
        bo.b58.config(bg="blue")
        bo.b59.config(bg="blue")
        bo.b60.config(bg="blue")
        bo.b61.config(bg="blue")
        bo.b62.config(bg="blue")
        bo.b63.config(bg="blue")
        winner = True
        Listwin[6] = 2
        # disable_all_buttons()

    elif bo.b55["text"] == "O" and bo.b59["text"] == "O" and bo.b63["text"] == "O":
        bo.b55.config(bg="blue")
        bo.b56.config(bg="blue")
        bo.b57.config(bg="blue")
        bo.b58.config(bg="blue")
        bo.b59.config(bg="blue")
        bo.b60.config(bg="blue")
        bo.b61.config(bg="blue")
        bo.b62.config(bg="blue")
        bo.b63.config(bg="blue")
        winner = True
        Listwin[6] = 2
        # disable_all_buttons()

    elif bo.b57["text"] == "O" and bo.b59["text"] == "O" and bo.b61["text"] == "O":
        bo.b55.config(bg="blue")
        bo.b56.config(bg="blue")
        bo.b57.config(bg="blue")
        bo.b58.config(bg="blue")
        bo.b59.config(bg="blue")
        bo.b60.config(bg="blue")
        bo.b61.config(bg="blue")
        bo.b62.config(bg="blue")
        bo.b63.config(bg="blue")
        winner = True
        Listwin[6] = 2

        # disable_all_buttons()
    if bo.b55["text"] != "" and bo.b56["text"] != "" and bo.b57["text"] != "" and bo.b58["text"] != "" and bo.b59[
        "text"] != "" and bo.b60["text"] != "" and bo.b61["text"] != "" and bo.b62["text"] != "" and bo.b63[
        "text"] != "" and winner == False:
        bo.b55.config(bg="red")
        bo.b56.config(bg="red")
        bo.b57.config(bg="red")
        bo.b58.config(bg="red")
        bo.b59.config(bg="red")
        bo.b60.config(bg="red")
        bo.b61.config(bg="red")
        bo.b62.config(bg="red")
        bo.b63.config(bg="red")
        Listwin[6] = 3
        winner = True
    if winner == True:
        count7 = 1


def win8():
    """
This function determines who wins board eight of the nine three by three smaller tic tac toe boards using if/else
statements. If X turns three blank buttons into X boxes in a row, X wins the board. If O turns three blank buttons into
O boxes in a row, O wins the board. If there are no winners after all 9 buttons are clicked, the game is a tie.
                        """
    global winner
    winner = False
    global count8
    count8 = 0

    # Checking for X wins
    if bo.b64["text"] == "X" and bo.b65["text"] == "X" and bo.b66["text"] == "X":
        bo.b64.config(bg="green")
        bo.b65.config(bg="green")
        bo.b66.config(bg="green")
        bo.b67.config(bg="green")
        bo.b68.config(bg="green")
        bo.b69.config(bg="green")
        bo.b70.config(bg="green")
        bo.b71.config(bg="green")
        bo.b72.config(bg="green")
        winner = True
        Listwin[7] = 1
        # disable_all_buttons()
    elif bo.b67["text"] == "X" and bo.b68["text"] == "X" and bo.b69["text"] == "X":
        bo.b64.config(bg="green")
        bo.b65.config(bg="green")
        bo.b66.config(bg="green")
        bo.b67.config(bg="green")
        bo.b68.config(bg="green")
        bo.b69.config(bg="green")
        bo.b70.config(bg="green")
        bo.b71.config(bg="green")
        bo.b72.config(bg="green")
        winner = True
        Listwin[7] = 1
        # disable_all_buttons()
    elif bo.b70["text"] == "X" and bo.b71["text"] == "X" and bo.b72["text"] == "X":
        bo.b64.config(bg="green")
        bo.b65.config(bg="green")
        bo.b66.config(bg="green")
        bo.b67.config(bg="green")
        bo.b68.config(bg="green")
        bo.b69.config(bg="green")
        bo.b70.config(bg="green")
        bo.b71.config(bg="green")
        bo.b72.config(bg="green")
        winner = True
        Listwin[7] = 1
        # disable_all_buttons()
    elif bo.b64["text"] == "X" and bo.b67["text"] == "X" and bo.b70["text"] == "X":
        bo.b64.config(bg="green")
        bo.b65.config(bg="green")
        bo.b66.config(bg="green")
        bo.b67.config(bg="green")
        bo.b68.config(bg="green")
        bo.b69.config(bg="green")
        bo.b70.config(bg="green")
        bo.b71.config(bg="green")
        bo.b72.config(bg="green")
        winner = True
        Listwin[7] = 1
        # disable_all_buttons()
    elif bo.b65["text"] == "X" and bo.b68["text"] == "X" and bo.b71["text"] == "X":
        bo.b64.config(bg="green")
        bo.b65.config(bg="green")
        bo.b66.config(bg="green")
        bo.b67.config(bg="green")
        bo.b68.config(bg="green")
        bo.b69.config(bg="green")
        bo.b70.config(bg="green")
        bo.b71.config(bg="green")
        bo.b72.config(bg="green")
        winner = True
        Listwin[7] = 1
        # disable_all_buttons()

    elif bo.b66["text"] == "X" and bo.b69["text"] == "X" and bo.b72["text"] == "X":
        bo.b64.config(bg="green")
        bo.b65.config(bg="green")
        bo.b66.config(bg="green")
        bo.b67.config(bg="green")
        bo.b68.config(bg="green")
        bo.b69.config(bg="green")
        bo.b70.config(bg="green")
        bo.b71.config(bg="green")
        bo.b72.config(bg="green")
        winner = True
        Listwin[7] = 1
        # disable_all_buttons()

    elif bo.b64["text"] == "X" and bo.b68["text"] == "X" and bo.b72["text"] == "X":
        bo.b64.config(bg="green")
        bo.b65.config(bg="green")
        bo.b66.config(bg="green")
        bo.b67.config(bg="green")
        bo.b68.config(bg="green")
        bo.b69.config(bg="green")
        bo.b70.config(bg="green")
        bo.b71.config(bg="green")
        bo.b72.config(bg="green")
        winner = True
        Listwin[7] = 1
        # disable_all_buttons()

    elif bo.b66["text"] == "X" and bo.b68["text"] == "X" and bo.b70["text"] == "X":
        bo.b64.config(bg="green")
        bo.b65.config(bg="green")
        bo.b66.config(bg="green")
        bo.b67.config(bg="green")
        bo.b68.config(bg="green")
        bo.b69.config(bg="green")
        bo.b70.config(bg="green")
        bo.b71.config(bg="green")
        bo.b72.config(bg="green")
        winner = True
        Listwin[7] = 1
        # disable_all_buttons()

    # Checking for O wins
    # Checking for O wins
    if bo.b64["text"] == "O" and bo.b65["text"] == "O" and bo.b66["text"] == "O":
        bo.b64.config(bg="blue")
        bo.b65.config(bg="blue")
        bo.b66.config(bg="blue")
        bo.b67.config(bg="blue")
        bo.b68.config(bg="blue")
        bo.b69.config(bg="blue")
        bo.b70.config(bg="blue")
        bo.b71.config(bg="blue")
        bo.b72.config(bg="blue")
        winner = True
        Listwin[7] = 2
        # disable_all_buttons()
    elif bo.b67["text"] == "O" and bo.b68["text"] == "O" and bo.b69["text"] == "O":
        bo.b64.config(bg="blue")
        bo.b65.config(bg="blue")
        bo.b66.config(bg="blue")
        bo.b67.config(bg="blue")
        bo.b68.config(bg="blue")
        bo.b69.config(bg="blue")
        bo.b70.config(bg="blue")
        bo.b71.config(bg="blue")
        bo.b72.config(bg="blue")
        winner = True
        Listwin[7] = 2
        # disable_all_buttons()
    elif bo.b70["text"] == "O" and bo.b71["text"] == "O" and bo.b72["text"] == "O":
        bo.b64.config(bg="blue")
        bo.b65.config(bg="blue")
        bo.b66.config(bg="blue")
        bo.b67.config(bg="blue")
        bo.b68.config(bg="blue")
        bo.b69.config(bg="blue")
        bo.b70.config(bg="blue")
        bo.b71.config(bg="blue")
        bo.b72.config(bg="blue")
        winner = True
        Listwin[7] = 2
        # disable_all_buttons()
    elif bo.b64["text"] == "O" and bo.b67["text"] == "O" and bo.b70["text"] == "O":
        bo.b64.config(bg="blue")
        bo.b65.config(bg="blue")
        bo.b66.config(bg="blue")
        bo.b67.config(bg="blue")
        bo.b68.config(bg="blue")
        bo.b69.config(bg="blue")
        bo.b70.config(bg="blue")
        bo.b71.config(bg="blue")
        bo.b72.config(bg="blue")
        winner = True
        Listwin[7] = 2
        # disable_all_buttons()
    elif bo.b65["text"] == "O" and bo.b68["text"] == "O" and bo.b71["text"] == "O":
        bo.b64.config(bg="blue")
        bo.b65.config(bg="blue")
        bo.b66.config(bg="blue")
        bo.b67.config(bg="blue")
        bo.b68.config(bg="blue")
        bo.b69.config(bg="blue")
        bo.b70.config(bg="blue")
        bo.b71.config(bg="blue")
        bo.b72.config(bg="blue")
        winner = True
        Listwin[7] = 2
        # disable_all_buttons()

    elif bo.b66["text"] == "O" and bo.b69["text"] == "O" and bo.b72["text"] == "O":
        bo.b64.config(bg="blue")
        bo.b65.config(bg="blue")
        bo.b66.config(bg="blue")
        bo.b67.config(bg="blue")
        bo.b68.config(bg="blue")
        bo.b69.config(bg="blue")
        bo.b70.config(bg="blue")
        bo.b71.config(bg="blue")
        bo.b72.config(bg="blue")
        winner = True
        Listwin[7] = 2
        # disable_all_buttons()

    elif bo.b64["text"] == "O" and bo.b68["text"] == "O" and bo.b72["text"] == "O":
        bo.b64.config(bg="blue")
        bo.b65.config(bg="blue")
        bo.b66.config(bg="blue")
        bo.b67.config(bg="blue")
        bo.b68.config(bg="blue")
        bo.b69.config(bg="blue")
        bo.b70.config(bg="blue")
        bo.b71.config(bg="blue")
        bo.b72.config(bg="blue")
        winner = True
        Listwin[7] = 2
        # disable_all_buttons()

    elif bo.b66["text"] == "O" and bo.b68["text"] == "O" and bo.b70["text"] == "O":
        bo.b64.config(bg="blue")
        bo.b65.config(bg="blue")
        bo.b66.config(bg="blue")
        bo.b67.config(bg="blue")
        bo.b68.config(bg="blue")
        bo.b69.config(bg="blue")
        bo.b70.config(bg="blue")
        bo.b71.config(bg="blue")
        bo.b72.config(bg="blue")
        winner = True
        Listwin[7] = 2

        # disable_all_buttons()but
    if bo.b64["text"] != "" and bo.b65["text"] != "" and bo.b66["text"] != "" and bo.b67["text"] != "" and bo.b68[
        "text"] != "" and bo.b69["text"] != "" and bo.b70["text"] != "" and bo.b71["text"] != "" and bo.b72[
        "text"] != "" and winner == False:
        bo.b64.config(bg="red")
        bo.b65.config(bg="red")
        bo.b66.config(bg="red")
        bo.b67.config(bg="red")
        bo.b68.config(bg="red")
        bo.b69.config(bg="red")
        bo.b70.config(bg="red")
        bo.b71.config(bg="red")
        bo.b72.config(bg="red")
        Listwin[7] = 3
        winner = True

    if winner == True:
        count8 = 1


def win9():
    """
This function determines who wins board nine of the nine three by three smaller tic tac toe boards using if/else
statements. If X turns three blank buttons into X boxes in a row, X wins the board. If O turns three blank buttons into
O boxes in a row, O wins the board. If there are no winners after all 9 buttons are clicked, the game is a tie.
                        """
    global winner
    winner = False
    global count9
    count9 = 0
    # Checking for X wins
    if bo.b73["text"] == "X" and bo.b74["text"] == "X" and bo.b75["text"] == "X":
        bo.b73.config(bg="green")
        bo.b74.config(bg="green")
        bo.b75.config(bg="green")
        bo.b76.config(bg="green")
        bo.b77.config(bg="green")
        bo.b78.config(bg="green")
        bo.b79.config(bg="green")
        bo.b80.config(bg="green")
        bo.b81.config(bg="green")
        winner = True
        Listwin[8] = 1
        # disable_all_buttons()
    elif bo.b76["text"] == "X" and bo.b77["text"] == "X" and bo.b78["text"] == "X":
        bo.b73.config(bg="green")
        bo.b74.config(bg="green")
        bo.b75.config(bg="green")
        bo.b76.config(bg="green")
        bo.b77.config(bg="green")
        bo.b78.config(bg="green")
        bo.b79.config(bg="green")
        bo.b80.config(bg="green")
        bo.b81.config(bg="green")
        winner = True
        Listwin[8] = 1
    # disable_all_buttons()

    elif bo.b79["text"] == "X" and bo.b80["text"] == "X" and bo.b81["text"] == "X":
        bo.b73.config(bg="green")
        bo.b74.config(bg="green")
        bo.b75.config(bg="green")
        bo.b76.config(bg="green")
        bo.b77.config(bg="green")
        bo.b78.config(bg="green")
        bo.b79.config(bg="green")
        bo.b80.config(bg="green")
        bo.b81.config(bg="green")
        winner = True
        Listwin[8] = 1
    # disable_all_buttons()
    elif bo.b73["text"] == "X" and bo.b76["text"] == "X" and bo.b79["text"] == "X":
        bo.b73.config(bg="green")
        bo.b74.config(bg="green")
        bo.b75.config(bg="green")
        bo.b76.config(bg="green")
        bo.b77.config(bg="green")
        bo.b78.config(bg="green")
        bo.b79.config(bg="green")
        bo.b80.config(bg="green")
        bo.b81.config(bg="green")
        winner = True
        Listwin[8] = 1
    # disable_all_buttons()
    elif bo.b74["text"] == "X" and bo.b77["text"] == "X" and bo.b80["text"] == "X":
        bo.b73.config(bg="green")
        bo.b74.config(bg="green")
        bo.b75.config(bg="green")
        bo.b76.config(bg="green")
        bo.b77.config(bg="green")
        bo.b78.config(bg="green")
        bo.b79.config(bg="green")
        bo.b80.config(bg="green")
        bo.b81.config(bg="green")
        winner = True
        Listwin[8] = 1

    # disable_all_buttons()

    elif bo.b75["text"] == "X" and bo.b78["text"] == "X" and bo.b81["text"] == "X":
        bo.b73.config(bg="green")
        bo.b74.config(bg="green")
        bo.b75.config(bg="green")
        bo.b76.config(bg="green")
        bo.b77.config(bg="green")
        bo.b78.config(bg="green")
        bo.b79.config(bg="green")
        bo.b80.config(bg="green")
        bo.b81.config(bg="green")
        winner = True
        Listwin[8] = 1
    # disable_all_buttons()

    elif bo.b73["text"] == "X" and bo.b77["text"] == "X" and bo.b81["text"] == "X":
        bo.b73.config(bg="green")
        bo.b74.config(bg="green")
        bo.b75.config(bg="green")
        bo.b76.config(bg="green")
        bo.b77.config(bg="green")
        bo.b78.config(bg="green")
        bo.b79.config(bg="green")
        bo.b80.config(bg="green")
        bo.b81.config(bg="green")
        winner = True
        Listwin[8] = 1
        # disable_all_buttons()

    elif bo.b75["text"] == "X" and bo.b77["text"] == "X" and bo.b79["text"] == "X":
        bo.b73.config(bg="green")
        bo.b74.config(bg="green")
        bo.b75.config(bg="green")
        bo.b76.config(bg="green")
        bo.b77.config(bg="green")
        bo.b78.config(bg="green")
        bo.b79.config(bg="green")
        bo.b80.config(bg="green")
        bo.b81.config(bg="green")
        winner = True
        Listwin[8] = 1
        # disable_all_buttons()

    # Checking for O wins
    # Checking for O wins
    if bo.b73["text"] == "O" and bo.b74["text"] == "O" and bo.b75["text"] == "O":
        bo.b73.config(bg="blue")
        bo.b74.config(bg="blue")
        bo.b75.config(bg="blue")
        bo.b76.config(bg="blue")
        bo.b77.config(bg="blue")
        bo.b78.config(bg="blue")
        bo.b79.config(bg="blue")
        bo.b80.config(bg="blue")
        bo.b81.config(bg="blue")
        winner = True
        Listwin[8] = 2
        # disable_all_buttons()
    elif bo.b76["text"] == "O" and bo.b77["text"] == "O" and bo.b78["text"] == "O":
        bo.b73.config(bg="blue")
        bo.b74.config(bg="blue")
        bo.b75.config(bg="blue")
        bo.b76.config(bg="blue")
        bo.b77.config(bg="blue")
        bo.b78.config(bg="blue")
        bo.b79.config(bg="blue")
        bo.b80.config(bg="blue")
        bo.b81.config(bg="blue")
        winner = True
        Listwin[8] = 2
        # disable_all_buttons()
    elif bo.b79["text"] == "O" and bo.b80["text"] == "O" and bo.b81["text"] == "O":
        bo.b73.config(bg="blue")
        bo.b74.config(bg="blue")
        bo.b75.config(bg="blue")
        bo.b76.config(bg="blue")
        bo.b77.config(bg="blue")
        bo.b78.config(bg="blue")
        bo.b79.config(bg="blue")
        bo.b80.config(bg="blue")
        bo.b81.config(bg="blue")
        winner = True
        Listwin[8] = 2
        # disable_all_buttons()
    elif bo.b73["text"] == "O" and bo.b76["text"] == "O" and bo.b79["text"] == "O":
        bo.b73.config(bg="blue")
        bo.b74.config(bg="blue")
        bo.b75.config(bg="blue")
        bo.b76.config(bg="blue")
        bo.b77.config(bg="blue")
        bo.b78.config(bg="blue")
        bo.b79.config(bg="blue")
        bo.b80.config(bg="blue")
        bo.b81.config(bg="blue")
        winner = True
        Listwin[8] = 2
        # disable_all_buttons()
    elif bo.b74["text"] == "O" and bo.b77["text"] == "O" and bo.b80["text"] == "O":
        bo.b73.config(bg="blue")
        bo.b74.config(bg="blue")
        bo.b75.config(bg="blue")
        bo.b76.config(bg="blue")
        bo.b77.config(bg="blue")
        bo.b78.config(bg="blue")
        bo.b79.config(bg="blue")
        bo.b80.config(bg="blue")
        bo.b81.config(bg="blue")
        winner = True
        Listwin[8] = 2
        # disable_all_buttons()

    elif bo.b75["text"] == "O" and bo.b78["text"] == "O" and bo.b81["text"] == "O":
        bo.b73.config(bg="blue")
        bo.b74.config(bg="blue")
        bo.b75.config(bg="blue")
        bo.b76.config(bg="blue")
        bo.b77.config(bg="blue")
        bo.b78.config(bg="blue")
        bo.b79.config(bg="blue")
        bo.b80.config(bg="blue")
        bo.b81.config(bg="blue")
        winner = True
        Listwin[8] = 2
        # disable_all_buttons()

    elif bo.b73["text"] == "O" and bo.b77["text"] == "O" and bo.b81["text"] == "O":
        bo.b73.config(bg="blue")
        bo.b74.config(bg="blue")
        bo.b75.config(bg="blue")
        bo.b76.config(bg="blue")
        bo.b77.config(bg="blue")
        bo.b78.config(bg="blue")
        bo.b79.config(bg="blue")
        bo.b80.config(bg="blue")
        bo.b81.config(bg="blue")
        winner = True
        Listwin[8] = 2
        # disable_all_buttons()

    elif bo.b75["text"] == "O" and bo.b77["text"] == "O" and bo.b79["text"] == "O":
        bo.b73.config(bg="blue")
        bo.b74.config(bg="blue")
        bo.b75.config(bg="blue")
        bo.b76.config(bg="blue")
        bo.b77.config(bg="blue")
        bo.b78.config(bg="blue")
        bo.b79.config(bg="blue")
        bo.b80.config(bg="blue")
        bo.b81.config(bg="blue")
        winner = True
        Listwin[8] = 2

       
    if bo.b73["text"] != "" and bo.b74["text"] != "" and bo.b75["text"] != "" and bo.b76["text"] != "" and bo.b77[
        "text"] != "" and bo.b78["text"] != "" and bo.b79["text"] != "" and bo.b80["text"] != "" and bo.b81[
        "text"] != "" and winner == False:
        bo.b73.config(bg="red")
        bo.b74.config(bg="red")
        bo.b75.config(bg="red")
        bo.b76.config(bg="red")
        bo.b77.config(bg="red")
        bo.b78.config(bg="red")
        bo.b79.config(bg="red")
        bo.b80.config(bg="red")
        bo.b81.config(bg="red")
        Listwin[8] = 3
        winner = True

    if winner == True:  # If the winner is true
        count9 = 1  # Set the variable count9 to 1


def finalwin():  # Define the function finalwin
    """
This function determines who wins the game of ultimate tic tac toe by using if/else statements to determine which
combinations of outcomes of the three by three tic tac toe boards lead to which end result of the ultimate tic tac toe
game. If X wins three boards arranged in a row, X wins the game. If O wins three boards arranged in a row, O wins the
game. If after all 9 boards are played there are no winners, or if after 7 boards are tied there are no winners, the
game is determined to be a tie.
                        """
    global finalwinner  # Create the global variable finalwin
    finalwinner = False  # Set the variable finalwin to false

    if Listwin[0] == 1 and Listwin[4] == 1 and Listwin[8] == 1:  # If X won box 1, 5, and 9
        finalwinner = True  # Change finalwinner to true
        messagebox.showinfo("tic tac toe",
                            "Player X won the game!")  # Display a message saying that player X won the game.
        bo.disable_all_buttons()  # Disable all buttons
    elif Listwin[0] == 1 and Listwin[1] == 1 and Listwin[2] == 1:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player X won the game!")
        bo.disable_all_buttons()
    elif Listwin[0] == 1 and Listwin[3] == 1 and Listwin[6] == 1:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player X won the game!")
        bo.disable_all_buttons()
    elif Listwin[3] == 1 and Listwin[4] == 1 and Listwin[5] == 1:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player X won the game!")
        bo.disable_all_buttons()
    elif Listwin[6] == 1 and Listwin[7] == 1 and Listwin[8] == 1:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player X won the game!")
        bo.disable_all_buttons()
    elif Listwin[1] == 1 and Listwin[4] == 1 and Listwin[7] == 1:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player X won the game!")
        bo.disable_all_buttons()
    elif Listwin[2] == 1 and Listwin[5] == 1 and Listwin[8] == 1:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player X won the game!")
        bo.disable_all_buttons()
    elif Listwin[2] == 1 and Listwin[4] == 1 and Listwin[6] == 1:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player X won the game!")
        bo.disable_all_buttons()
        # O final wins
    elif Listwin[0] == 2 and Listwin[4] == 2 and Listwin[8] == 2:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player O won the game!")
        bo.disable_all_buttons()
    elif Listwin[0] == 2 and Listwin[1] == 2 and Listwin[2] == 2:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player O won the game!")
        bo.disable_all_buttons()
    elif Listwin[0] == 2 and Listwin[3] == 2 and Listwin[6] == 2:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player O won the game!")
        bo.disable_all_buttons()
    elif Listwin[3] == 2 and Listwin[4] == 2 and Listwin[5] == 2:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player O won the game!")
        bo.disable_all_buttons()
    elif Listwin[6] == 2 and Listwin[7] == 2 and Listwin[8] == 2:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player O won the game!")
        bo.disable_all_buttons()
    elif Listwin[1] == 2 and Listwin[4] == 2 and Listwin[7] == 2:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player O won the game!")
        bo.disable_all_buttons()
    elif Listwin[2] == 2 and Listwin[5] == 2 and Listwin[8] == 2:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player O won the game!")
        bo.disable_all_buttons()
    elif Listwin[2] == 2 and Listwin[4] == 2 and Listwin[6] == 2:
        finalwinner = True
        messagebox.showinfo("tic tac toe", "Player O won the game!")
        bo.disable_all_buttons()

    if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 and count5 == 1 and count6 == 1 and count7 == 1 and count8 == 1 and count9 == 1 and finalwinner == False:  # If the all of the 9 boards are played without a final winner
        messagebox.showinfo("tic tac toe", "ITS A TIE")  # Display a message that the final game is a tie
        bo.disable_all_buttons()  # Disable all buttons

    if Listwin[0] == 3 and Listwin[1] == 3 and Listwin[2] == 3 and Listwin[3] == 3 and Listwin[4] == 3 and Listwin[
        5] == 3 and Listwin[6] == 3:  # If the first 7 boxes are tied
        messagebox.showinfo("tic tac toe",
                            "ITS A TIE")  # Display a message that the final game is a tie, because there is no possibility for anyone to win.
        bo.disable_all_buttons()  # Disable all buttons
