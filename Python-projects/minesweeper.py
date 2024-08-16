import random #Need random in order to choose spots on the board to place mines
import time #This will be used for the text that will be displayed to the user

class minesweeper:
    def __init__(self):
        self.need_tutorial = False #Flag that will be updated if the user requests the tutorial
        self.difficulty_level = "" #Will be used to hold the difficulty requested by the player
        self.gameboard = [] #There will be 2 versions of the gameboard, the one the player can see which has spaces covered and the generated board which will be referred to by the code to check if a mine has been chosen
        self.gameboard_for_player = [] #This gameboard is the one that will be show to the player with spaces covered
        self.height = 0 #height of the gameboard initialized here
        self.width = 0 #width of the gameboard initialized here
        self.num_mines = 0 #number of mines in the gameboard initialized here
        self.tutorial_board = False #This flag will be used when the board is generated. If True, the board will be a pre-set one for the tutorial
        self.num_non_mine_tiles = 0 #This will be used to see if the player has chosen all non-mine spaces
        
    def print_gameboard(self): #Function used to display the uncovered gameboard for the player
        for i in self.gameboard:
            print(i)
        return
    
    def print_gameboard_player(self): #Function used to display the covered gameboard for the player
        for i in self.gameboard_for_player:
            print(i)
        return
    
    def setup_gameboard(self,custom_height, custom_width, custom_mines): #This function will take the inputs from the player to make the gameboard
        if self.need_tutorial == True: #The tutorial borad will be a rigged 3 x 3 board so need to set some flags to prevent mines being set randomly
            self.height = 3
            self.width = 3
            self.num_mines = 1
            self.need_tutorial = False #Need to remove flag or the board will always be the tutorial one
            self.tutorial_board = True
            self.difficulty_level = 5
        
        self.difficulty_level = int(self.difficulty_level) #need to convert the string inputted to an int
        if self.difficulty_level == 1: #if the player chose difficulty 1, set the game to the following settings
            self.height = 5
            self.width = 5
            self.num_mines = 5
        elif self.difficulty_level == 2: #if the player chose difficulty 2, set the game to the following settings
            self.height = 8
            self.width = 8
            self.num_mines = 16
        elif self.difficulty_level == 3: #if the player chose difficulty 3, set the game to the following settings
            self.height = 10
            self.width = 10
            self.num_mines = 20
        elif self.difficulty_level == 4: #if the player chose difficulty 4, set the game to the custom settings chosen by the player
            self.height = int(custom_height)
            self.width = int(custom_width)
            self.num_mines = int(custom_mines)
        else: #since the tutorial sets the difficulty to 5 in order to prevent the tutorial board being overwritten, I have included this print to prove it has worked.
            print("Loading tutorial...")
        
        for height_i in range(self.height): #The following creates the default boards (player and code versions) without any mines. It sets up the correct width and height
            new_row = [] #Create a new list representing a row in the fully revealed version of the board
            new_row_2 = [] #Create a new list representing a row in the unrevealed version of the board
            for width_j in range(self.width): #add to the list until it becomes the right width
                new_row.append("0") #the board not shown to the player will be iniliased with 0's
                new_row_2.append("U") #the board shown to the player will have U to represent "unrevealed"
            self.gameboard.append(new_row) #add the row to the board
            self.gameboard_for_player.append(new_row_2) #add the row to the board
   
        for x in range(self.num_mines): #The following adds mines to the board
            if self.tutorial_board == False: #randomly generate a space for the mine
                random_height_for_mine = random.randint(0,(self.height - 1))
                random_width_for_mine = random.randint(0,(self.width - 1))
            else: #if its the tutorial, alwyas choose the same spot
                random_height_for_mine = 1
                random_width_for_mine = 2
                self.tutorial_board = False
            if self.gameboard[random_height_for_mine][random_width_for_mine] == "x": #if the spot generated is already a mine, we need to generate aa new spot
                x = x - 1
            else:
                self.gameboard[random_height_for_mine][random_width_for_mine] = "x" #change the spot to an x representing a mine
                #The following lines adds 1 to all adjacent tiles to indicate an additional mine being within 1 tile
                #There are lots of edge cases that need to be checked hence the amount of "if" statements
                if (not random_height_for_mine == 0) and (random_height_for_mine != (self.height - 1)) and (not random_width_for_mine == 0) and (random_width_for_mine != (self.width - 1)):
                    for i in range (-1, 2):
                        for j in range (-1, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_height_for_mine == 0) and ((not random_width_for_mine == 0) and (not random_width_for_mine == self.width - 1)):
                    for i in range (-1, 2):
                        for j in range (0, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)     
                elif (random_height_for_mine == (self.height - 1)) and ((not random_width_for_mine == 0) and (not random_width_for_mine == self.width - 1)):
                    for i in range (-1, 2):
                        for j in range (-1, 1):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == 0) and ((not random_height_for_mine == 0) and (not random_height_for_mine == self.height - 1)):
                    for i in range (0, 2):
                        for j in range (-1, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == 0) and ((not random_height_for_mine == 0) and (not random_height_for_mine == self.height - 1)):
                    for i in range (0, 2):
                        for j in range (-1, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == (self.width - 1)) and ((not random_height_for_mine == 0) and (not random_height_for_mine == self.height - 1)):
                    for i in range (-1, 1):
                        for j in range (-1, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == 0) and (random_height_for_mine == 0):
                    for i in range (0, 2):
                        for j in range (0, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == (self.width - 1)) and (random_height_for_mine == 0):
                    for i in range (-1, 1):
                        for j in range (0, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == 0) and (random_height_for_mine == (self.height - 1)):
                    for i in range (0, 2):
                        for j in range (-1, 1):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == (self.width - 1)) and (random_height_for_mine == (self.height - 1)):
                    for i in range (-1, 1):
                        for j in range (-1, 1):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
        return self.gameboard #Return the fully ccompleted gameboard's. One contains the mines and all the numbers representing number of mines within 1 square and one contains a grid of unrevealed tiles
            
            
    def run_tutorial(self): #The following runs the tutorial which explains the game 
        print("--------------------------------------------")
        print("Tutorial")
        print("In minesweeper, your goal is to uncover all the tiles on the gameboard that do not contain a mine")
        time.sleep(5)
        print("To do this, you will reveal tiles on the board and use the numbers that are revealed to help locate mines")
        time.sleep(5)
        print("Here is an example board")
        self.print_gameboard_player()
        print("Here, we have a 3 x 3 board where U represents unrevealed tiles")
        time.sleep(5)
        print("To start, type in the position of the tile you would like to reveal, in this case, lets choose row 2, column 2 by typing 2 when asked for the row and 2 when asked for the column")
        time.sleep(6)
        self.gameboard_for_player[1][1] = "1"
        self.print_gameboard_player()
        time.sleep(5)
        print("We can see there is 1 mine within the area of the tile we uncovered (the area around tiles are the tiles 1 space away, which includes diagonals)")
        time.sleep(5)
        print("Using this information, we can attempt to uncover another tile")
        self.gameboard_for_player[1][0] = "0"
        self.print_gameboard_player()
        time.sleep(5)
        print("since this tile is 0, we know there is 1 mine on the final column")
        time.sleep(3)
        print("When making a choice, you may chose to mark a tile instead of revealing one.")
        time.sleep(3)
        print("This will not do anything gameplay wise, but might help you keep track of your thoughts on possible mine locations")
        time.sleep(3)
        print("marked tiles are represented with a F (for flag), lets mark row 1, column 3")
        self.gameboard_for_player[0][2] = "F"
        self.print_gameboard_player()
        time.sleep(5)
        print("If you choose the location of a mine....")
        self.gameboard_for_player[1][2] = "x"
        self.print_gameboard_player()
        time.sleep(5)
        print("You will lose.")
        time.sleep(3)
        print("Hopefully, this has helped. Hope you enjoy the game!!!! :D")
        self.gameboard = [] #Reset the boards after the tutorial finishes
        self.gameboard_for_player = [] 
        return

    def lose_game(self): #this function is run when a player reveals a mine
        self.print_gameboard() #show the fully revealed gameboard
        time.sleep(5) #give the player some time to look at it
        print("YOU LOSE") #print the loss to the player so they understand what happened
        print("GAME OVER")
        return
    
    def play_game(self): #This function is important as it allows the player to play the game
        self.num_non_mine_tiles = (((self.width) * (self.height)) - self.num_mines) #This counts the tiles that don't have a mine on them, the player needs to reveal all these tiles to win
        expected_inputs = ["mark","reveal"] # A list containing expected inputs, used to catch inputs from player that don't match
        while self.num_non_mine_tiles > 0: #The game is run in a while loop until the player either loses or reveals all the tiles neccesary to win
            self.print_gameboard_player() #show the player the board
            player_move = "no" #reset the player's inputed move, default is set to "no" as its not in expected inputs
            while not str(player_move).lower() in expected_inputs: #While the player has not an inputed a expected move, ask them to do so
                player_move = input("Please make a move (type mark or reveal): ")
                if not str(player_move).lower() in expected_inputs: #If they input a move that is not expected, ask them to do so
                    print("Please make a valid move \n")
                    self.print_gameboard_player()
            
            chosen_row = (self.height + 1) #reset the variable of the players chosen row. Set out of bounds so we can enter the following while loop
            chosen_column = (self.width + 1) #reset the variable of the players chosen column. Set out of bounds so we can enter the following while loop
            if str(player_move).lower() == "mark": #If the player choses to mark a spot with a flag, do the following
                while (int(chosen_row) - 1) >= int(self.height): #in while loop to catch out of bound inputs
                    chosen_row = input("Please input the row of the tile you wish to chose: ")
                    if ((int(chosen_row) - 1) > int(self.height)) or ((int(chosen_row)) <= 0): #catch out of bound inputs
                        print("You have chosen a row that does not exist")
                while (int(chosen_column) - 1) >= int(self.width): #in while loop to catch out of bound inputs
                    chosen_column = input(" Please input the column of the tile you wish to chose: ")
                    if ((int(chosen_column) - 1) > int(self.width)) or ((int(chosen_column)) <= 0): #catch out of bound inputs
                        print("You have chosen a column that does not exist")

                chosen_row = int(chosen_row)
                chosen_column = int(chosen_column)
                
                if self.gameboard_for_player[chosen_row - 1][chosen_column - 1] == "U": #If Unrevealed, mark with a flag
                    self.gameboard_for_player[chosen_row - 1][chosen_column - 1] = "F"
                elif self.gameboard_for_player[chosen_row - 1][chosen_column - 1] == "F": #else, unmark it
                    self.gameboard_for_player[chosen_row - 1][chosen_column - 1] = "U"
                else: #This prevents an exploit where the player puts a flag on a revealed tile, then removes it to turn the tile back to unrevealed so they can reveal the same tile over and over to win
                    print("This tile has already been revealed")
            
            elif str(player_move).lower() == "reveal": #If the player choses to "reveal", do the following
                #The following gets a row and column from the player and prevents out of bound answers
                while (int(chosen_row) - 1) >= int(self.height):
                    chosen_row = input("Please input the row of the tile you wish to chose: ")
                    if ((int(chosen_row) - 1) > int(self.height)) or ((int(chosen_row)) <= 0):
                        print("You have chosen a row that does not exist")
                while (int(chosen_column) - 1) >= int(self.width):
                    chosen_column = input(" Please input the column of the tile you wish to chose: ")
                    if ((int(chosen_column) - 1) > int(self.width)) or ((int(chosen_column)) <= 0):
                        print("You have chosen a column that does not exist")

                chosen_column = int(chosen_column)
                chosen_row = int(chosen_row)
                
                if (self.gameboard_for_player[chosen_row - 1][chosen_column - 1] != "U") and (self.gameboard_for_player[chosen_row - 1][chosen_column - 1] != "F"):
                    print("Pick a space you have not revealed") #prevent players from choosing spots they have already revealed
                elif self.gameboard[chosen_row - 1][chosen_column - 1] == "x": #if the player picks a mine, they lose
                    self.lose_game() #run the function made earlier
                    exit()
                else:
                    self.gameboard_for_player[chosen_row - 1][chosen_column - 1] = self.gameboard[chosen_row - 1][chosen_column - 1] #otherwise, replace the unrevealed tile with its equivalent from the revealed board
                    self.num_non_mine_tiles -= 1 #reduce the number of unrevealed tiles by one
        self.print_gameboard() #If the player wins, print the gameboard and display a win message
        print("Congratulations, you have won!!!!!")
        print("Thank you for playing!!!")
        return

    def setup_game(self): #Function used for the games setup
        self.difficulty_level = int(self.difficulty_level) #During the introfuction function, a difficulty level is gotten from the player. This turns it to an int
        custom_height = 0
        custom_width = 0
        custom_mine = 0
        if self.difficulty_level == 4: #If the player chose "4", they need to setup custom parameters. This will do that
            custom_height = "no" #these are set this way as they are not numeric so allow the code to access necessary loops
            custom_width = "no"
            custom_mine = -1 #negative iniatisation to enter the following while loop
            
            while not (str(custom_height).isnumeric()):
                custom_height = input("Please input the height of the board you would like: ")
                if not (str(custom_height).isnumeric()):
                    print("Please input a positive number")
            print("\n")
            
            while not (str(custom_width).isnumeric()):
                custom_width = input("Please input the width of the board you would like: ")
                if not (str(custom_width).isnumeric()):
                    print("Please input a positive number")
            print("\n")
            
            while (not (str(custom_mine).isnumeric())):
                custom_mine = input("Please input the number of mines you would like: ")
                if not (str(custom_mine).isnumeric()):
                    custom_mine = -1
                    print("Please input a positve number")
                if (int(custom_mine) >= int(custom_height) * int(custom_width)): #if there are more mines than board spaces (or equal amounts), prevent the player as this makes the game impossible
                    custom_mine = -1
                    print("You have put more mines on the board than spaces (or an equal amount)")
            print("\n")
        self.gameboard = self.setup_gameboard(custom_height,custom_width,custom_mine) #After the paramters have been elicited, run the setup function
        self.play_game() #play the game after setup is done
        return

    def introduction(self): #function used to intoduce the player and to get the difficulty level. Also lets the player ask for tutorial
        synonyms = ["yes","true"] #used to let the player respond in multiple ways
        
        print("Hello, welcome to minesweeper!")
        tutorial = input("Do you need a tutorial for how the game works? (yes/no): ")
        
        if str(tutorial).lower() in synonyms: #If the player asks for tutorial, set it up for them
            self.need_tutorial = True
            self.setup_gameboard(0,0,0)
            self.run_tutorial()
            self.difficulty_level = "no"
        
        print("The game has four different difficulty levels \n1.easy (5 x 5 grid, 5 mines) \n2.normal (8 x 8, 16 mines) \n3.Hard (10 x 10 grid, 25 mines) \n4.Custom settings")
        
        while not (str(self.difficulty_level).isnumeric()): #a loop used to ensure a difficulty level is chosen correctly
            self.difficulty_level = input("Please input the number associated with the difficulty you wish to choose: ")
            if (str(self.difficulty_level).isnumeric()) and ((int(self.difficulty_level) > 4) or (int(self.difficulty_level) < 0)):
                self.difficulty_level = "no" #reset this as the player may have chosen an incorrect numeric difficulty
                print("Please chose a number from 1 to 4")
                
                
        print("You have chosen difficulty " +str(self.difficulty_level) + ". Thank you, and have fun.")
        self.setup_game()
        return
        
minesweeper_game = minesweeper() #Setup an instance of the game
minesweeper_game.introduction() #Run the game
