import random
import time

class minesweeper:
    def __init__(self):
        self.need_tutorial = False
        self.difficulty_level = ""
        self.gameboard = []
        self.gameboard_for_player = []
        self.height = 0
        self.width = 0
        self.num_mines = 0
        self.tutorial_board = False
        self.num_non_mine_tiles = 0
        
    def print_gameboard(self):
        for i in self.gameboard:
            print(i)
        return
    
    def print_gameboard_player(self):
        for i in self.gameboard_for_player:
            print(i)
        return
    
    def setup_gameboard(self,custom_height, custom_width, custom_mines):
        if self.need_tutorial == True: #The tutorial borad will be a rigged 3 x 3 board so need to set some flags to prevent mines being set randomly
            self.height = 3
            self.width = 3
            self.num_mines = 1
            self.need_tutorial = False #Need to remove flag or the board will always be the tutorial one
            self.tutorial_board = True
            self.difficulty_level = 5
        
        self.difficulty_level = int(self.difficulty_level)
        if self.difficulty_level == 1:
            self.height = 5
            self.width = 5
            self.num_mines = 5
        elif self.difficulty_level == 2:
            self.height = 8
            self.width = 8
            self.num_mines = 16
        elif self.difficulty_level == 3:
            self.height = 10
            self.width = 10
            self.num_mines = 20
        elif self.difficulty_level == 4:
            self.height = int(custom_height)
            self.width = int(custom_width)
            self.num_mines = int(custom_mines)
        else:
            print("Loading tutorial...")
        
        for height_i in range(self.height):
            new_row = []
            new_row_2 = []
            for width_j in range(self.width):
                new_row.append("0")
                new_row_2.append("U")
            self.gameboard.append(new_row)
            self.gameboard_for_player.append(new_row_2)
   
        for x in range(self.num_mines):
            if self.tutorial_board == False:
                random_height_for_mine = random.randint(0,(self.height - 1))
                random_width_for_mine = random.randint(0,(self.width - 1))
            else:
                random_height_for_mine = 1
                random_width_for_mine = 2
                self.tutorial_board = False
            if self.gameboard[random_height_for_mine][random_width_for_mine] == "x":
                x = x - 1
            else:
                self.gameboard[random_height_for_mine][random_width_for_mine] = "x"
                if (not random_height_for_mine == 0) and (random_height_for_mine != (self.height - 1)) and (not random_width_for_mine == 0) and (random_width_for_mine != (self.width - 1)):
                    print(1)
                    for i in range (-1, 2):
                        for j in range (-1, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_height_for_mine == 0) and ((not random_width_for_mine == 0) and (not random_width_for_mine == self.width - 1)):
                    print(2)
                    for i in range (-1, 2):
                        for j in range (0, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)     
                elif (random_height_for_mine == (self.height - 1)) and ((not random_width_for_mine == 0) and (not random_width_for_mine == self.width - 1)):
                    print(3)
                    for i in range (-1, 2):
                        for j in range (-1, 1):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == 0) and ((not random_height_for_mine == 0) and (not random_height_for_mine == self.height - 1)):
                    print(4)
                    for i in range (0, 2):
                        for j in range (-1, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == 0) and ((not random_height_for_mine == 0) and (not random_height_for_mine == self.height - 1)):
                    print(5)
                    for i in range (0, 2):
                        for j in range (-1, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == (self.width - 1)) and ((not random_height_for_mine == 0) and (not random_height_for_mine == self.height - 1)):
                    print(6)
                    for i in range (-1, 1):
                        for j in range (-1, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == 0) and (random_height_for_mine == 0):
                    print(7)
                    for i in range (0, 2):
                        for j in range (0, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == (self.width - 1)) and (random_height_for_mine == 0):
                    print(8)
                    for i in range (-1, 1):
                        for j in range (0, 2):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == 0) and (random_height_for_mine == (self.height - 1)):
                    print(9)
                    for i in range (0, 2):
                        for j in range (-1, 1):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                elif (random_width_for_mine == (self.width - 1)) and (random_height_for_mine == (self.height - 1)):
                    print(10)
                    for i in range (-1, 1):
                        for j in range (-1, 1):
                            if self.gameboard[random_height_for_mine + j][random_width_for_mine + i] != "x":
                                self.gameboard[random_height_for_mine + j][random_width_for_mine + i] = str(int(self.gameboard[random_height_for_mine + j][random_width_for_mine + i]) + 1)
                self.print_gameboard()
        print("\n")
        self.print_gameboard_player()
        return self.gameboard
            
            
    def run_tutorial(self):
        print("--------------------------------------------")
        print("Tutorial")
        print("In minesweeper, you goal is to uncover all the tiles on the gameboard that do not contain a mine")
        time.sleep(5)
        print("To do this, you will reveal tiles on the board and use the numbers that are revealed to help locate mines")
        time.sleep(5)
        print("Here is an example board")
        self.print_gameboard_player()
        print("Here, we have a 3 x 3 board where U represents unrevealed tiles")
        time.sleep(5)
        print("To start, type in the position of the tile you would like to reveal, in this case, lets chose row 2, column 2 by typing 2 when asked for the row and 2 when asked for the column")
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
        print("When making a choice, you may chose to mark a tile instaed of revealing one.")
        time.sleep(3)
        print("This will not do anything gameplay wise, but might help you keep track of your thoughts on possible mine locations")
        time.sleep(3)
        print("marked tiles are represented with a F (for flag), lets mark row 1, column 3")
        self.gameboard_for_player[0][2] = "F"
        self.print_gameboard_player()
        time.sleep(5)
        print("If you choose the location of a mine....")
        self.gameboard_for_player[1][2] = "m"
        self.print_gameboard_player()
        time.sleep(5)
        print("You will lose.")
        time.sleep(3)
        print("Hopefully, this has helped. Hope you enjoy the game!!!! :D")
        self.gameboard = []
        self.gameboard_for_player = []
        return

    def lose_game(self):
        self.print_gameboard()
        time.sleep(5)
        print("YOU LOSE")
        print("GAME OVER")
        return
    
    def play_game(self):
        self.num_non_mine_tiles = (((self.width) * (self.height)) - self.num_mines)
        expected_inputs = ["mark","reveal"]
        print(self.num_non_mine_tiles)
        while self.num_non_mine_tiles > 0:
            self.print_gameboard_player()
            player_move = "no"
            while not str(player_move).lower() in expected_inputs:
                player_move = input("Please make a move (type mark or reveal): ")
                if not str(player_move).lower() in expected_inputs:
                    print("Please make a valid move \n")
                    self.print_gameboard_player()
            
            chosen_row = (self.height + 1)
            chosen_column = (self.width + 1)
            if str(player_move).lower() == "mark":
                while (int(chosen_row) - 1) >= int(self.height):
                    chosen_row = input("Please input the row of the tile you wish to chose: ")
                    if ((int(chosen_row) - 1) > int(self.height)) or ((int(chosen_row)) <= 0):
                        print("You have chosen a row that does not exist")
                while (int(chosen_column) - 1) >= int(self.width):
                    chosen_column = input(" Please input the column of the tile you wish to chose: ")
                    if ((int(chosen_column) - 1) > int(self.width)) or ((int(chosen_column)) <= 0):
                        print("You have chosen a column that does not exist")

                chosen_row = int(chosen_row)
                chosen_column = int(chosen_column)
                
                if self.gameboard_for_player[chosen_row - 1][chosen_column - 1] != "F":
                    self.gameboard_for_player[chosen_row - 1][chosen_column - 1] = "F"
                else:
                    self.gameboard_for_player[chosen_row - 1][chosen_column - 1] = "U"
            
            elif str(player_move).lower() == "reveal":
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
                    print("Pick a space you have not revealed")
                elif self.gameboard[chosen_row - 1][chosen_column - 1] == "x":
                    self.lose_game()
                    exit()
                else:
                    self.gameboard_for_player[chosen_row - 1][chosen_column - 1] = self.gameboard[chosen_row - 1][chosen_column - 1]
                    self.num_non_mine_tiles -= 1
        self.print_gameboard()
        print("Congratulations, you have won!!!!!")
        print("Thank you for playing!!!")
        return

    def setup_game(self):
        self.difficulty_level = int(self.difficulty_level)
        custom_height = 0
        custom_width = 0
        custom_mine = 0
        if self.difficulty_level == 4:
            custom_height = "no"
            custom_width = "no"
            custom_mine = -1
            
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
                if (int(custom_mine) >= int(custom_height) * int(custom_width)):
                    custom_mine = -1
                    print("You have put more mines on the board than spaces (or an equal amount)")
            print("\n")
        self.gameboard = self.setup_gameboard(custom_height,custom_width,custom_mine)
        self.play_game()
        return

    def introduction(self):
        synonyms = ["yes","true"]
        
        print("Hello, welcome to minesweeper!")
        tutorial = input("Do you need a tutorial for how the game works? (yes/no): ")
        
        if str(tutorial).lower() in synonyms:
            self.need_tutorial = True
            self.setup_gameboard(0,0,0)
            self.run_tutorial()
            self.difficulty_level = "no"
        
        print("The game has four different difficulty levels \n1.easy (5 x 5 grid, 5 mines) \n2.normal (8 x 8, 16 mines) \n3.Hard (10 x 10 grid, 25 mines) \n4.Custom settings")
        
        while not (str(self.difficulty_level).isnumeric()):
            self.difficulty_level = input("Please input the number associated with the difficulty you wish to choose: ")
            if (str(self.difficulty_level).isnumeric()) and ((int(self.difficulty_level) > 4) or (int(self.difficulty_level) < 0)):
                self.difficulty_level = "no"
                print("Please chose a number from 1 to 4")
                
                
        print("You have chosen difficulty " +str(self.difficulty_level) + ". Thank you, and have fun.")
        self.setup_game()
        return
        
minesweeper_game = minesweeper()
minesweeper_game.introduction()