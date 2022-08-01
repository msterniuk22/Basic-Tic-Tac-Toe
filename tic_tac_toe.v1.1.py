import random


class User:
    def __init__(self, letter):
        self.letter = letter


class Computer:
    def __init__(self, letter):
        self.letter = letter


#main driver class
class Game:

    def __init__(self):
        self.default_board = []
        self.board_with_additions = []
        self.poss_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.winner = None
        self.invalid_input = False

    @staticmethod
    def starting_move():
        #picks either X or O to start
        move = random.sample(["X", "O"], 1)
        return move[0]

    def create_board_list(self):
        j = 3
        #iterates 3 times to get all 3 'rows' of the board
        for num in range(3):
            #creates the default board by iterating through 3 numbers
            #appending this, and then increasing by 3 each iteration
            #this leads to 012, +3, 345, +3, etc...
            self.default_board.append([i for i in range(j-3, j)])
            j += 3
        return self.default_board

    #takes user input, does some non-valid input handling and returns the result
    def user_input(self):
        #ask for user input. if user gives non-num input, give two chances to fix it
        #on third chance, gracefully exit program
        #if problem is non poss_move input, let program run until user resolves error
        try:
            while True:
                user_choice = int(input("Enter a new spot(0-8): "))
                if user_choice in self.poss_moves:
                    return user_choice
                print('Enter a spot that is not occupied yet.')
        except:
            try:
                print('Do not input non-numbers. You have one chance to make it right: ')
                user_choice = int(input("Enter a new NUMERIC spot(0-8): "))
                if (user_choice in self.poss_moves) and (type(user_choice) == int):
                    return user_choice
            except:
                print('Another non-numeric input. Buh bye! ')
                self.invalid_input = True
                return -1

    def manipulate_board_list(self, new_pos, letter):

        self.board_with_additions = []
        #goes through and makes sure that we only have the first
        #three 'rows' of the board queued to be printed
        num_of_sublists = 0
        for lists in self.default_board:
            if num_of_sublists < 3:
                self.board_with_additions.append(lists)
            num_of_sublists += 1

        #if the new pos is 0, 1 or 2 then it will be located
        #in the first sublist
        first_sublist = self.board_with_additions[0]
        if new_pos < 3:
            for ele in first_sublist:
                #when/if we find the ele = to new_pos
                if ele == new_pos:
                    #we take it's index and replace it with 'X'
                    ele_index = first_sublist.index(ele)
                    first_sublist[ele_index] = letter

        #same process as above but for the second sublist
        second_sublist = self.board_with_additions[1]
        if 2 < new_pos < 6:
            for ele in second_sublist:
                if ele == new_pos:
                    ele_index = second_sublist.index(ele)
                    second_sublist[ele_index] = letter

        #same O same O for third sublist
        third_sublist = self.board_with_additions[2]
        if 5 < new_pos < 9:
            for ele in third_sublist:
                if ele == new_pos:
                    ele_index = third_sublist.index(ele)
                    third_sublist[ele_index] = letter

        return self.board_with_additions

    def aval_moves(self):
        user_choice = self.user_input()
        #calls to get current board post run of manipulate function
        current_board = self.manipulate_board_list(user_choice, 'X')
        self.poss_moves.remove(user_choice)

        print('poss moves are', self.poss_moves)
        return self.poss_moves

    def print_board(self):
        #takes in the 'vanilla' board we made prev
        default_board = self.create_board_list()
        adj_default_board = []

        #iterates through and only adds to adj_board
        #if adj_board has less than 3(gets rid of extra
        #lists from excessive calls)
        num_of_sublists = 0
        for lists in default_board:
            if num_of_sublists < 3:
                adj_default_board.append(lists)
            num_of_sublists += 1

        #just goes through each row and prints it, w/ some formatting
        for row in adj_default_board:
            print(f'| {row[0]} | {row[1]} | {row[2]} |')

        return '-------------'

    def make_comp_move(self):
        #takes it's (random) pick at the poss_moves
        select_move = random.sample(self.poss_moves, 1)
        #calls manip_board on the pick(with [0] to fix list type)
        self.manipulate_board_list(select_move[0], 'O')
        self.poss_moves.remove(select_move[0])
        return 'make_comp_move was successfully run'

    def determine_winner(self):

        # determine a horizontal winner
        x_count = 0
        o_count = 0
        #adds extra list to get 1 more iteration
        self.board_with_additions.append([])
        for lists in self.board_with_additions:
            #checks to see how many x's in a sublist
            #because each horz row == a single sublist
            if x_count == 3:
                self.winner = 'X'
                self.board_with_additions.remove([])
                return self.winner
            if o_count == 3:
                self.winner = 'O'
                self.board_with_additions.remove([])
                return self.winner
            #resets the counts so one row doesn't affect the other
            x_count = 0
            o_count = 0
            #checking for X's and O's
            for ele in lists:
                if ele == 'X':
                    x_count += 1
                if ele == 'O':
                    o_count += 1

        self.board_with_additions.remove([])

        #determining a vertical winner
        cur_sublist_index = 0
        column_tracker = []
        while cur_sublist_index <= 3:
            #checks the column to see if it is all X's or O's
            if column_tracker.count('X') == 3:
                self.winner = 'X'
                return self.winner
            if column_tracker.count('O') == 3:
                self.winner = 'O'
                return self.winner
            #after we check the third list, end the loop
            if cur_sublist_index == 3:
                cur_sublist_index += 1
            #clears the column prior to a new sublist_index
            column_tracker.clear()
            #if you are in the first three lists
            if cur_sublist_index < 3:
                for lists in self.board_with_additions:
                    #it will iterate and create a column by adding
                    #the same index ele in all 3 sublists
                    column_tracker.append(lists[cur_sublist_index])
                cur_sublist_index += 1

        #determining a diagonal winner
        #turns all the sublists into one list w/ 9 eles
        cur_board = []
        for lists in self.board_with_additions:
            for ele in lists:
                cur_board.append(ele)

        #adds only the diagonal spots, L -> R
        relevant_spots = []
        relevant_spots.append(cur_board[0])
        relevant_spots.append(cur_board[4])
        relevant_spots.append(cur_board[8])

        #checks if the diagonal L->R is all X's or O's
        if relevant_spots.count('X') == 3:
            self.winner = 'X'
            return self.winner
        if relevant_spots.count('O') == 3:
            self.winner = 'O'
            return self.winner

        #clears it and changes the list to other diagonal
        relevant_spots.clear()
        relevant_spots.append(cur_board[2])
        relevant_spots.append(cur_board[4])
        relevant_spots.append(cur_board[6])

        #does the same check
        if relevant_spots.count('X') == 3:
            self.winner = 'X'
            return self.winner
        if relevant_spots.count('O') == 3:
            self.winner = 'O'
            return self.winner

        return self.winner

    def play(self, user, computer):
        try:
            if self.invalid_input == True:
                print('game over! non-number input too many times...')
                return -1

            #tries to run first move of user and computer
            print(self.print_board())
            self.aval_moves()
            self.make_comp_move()

            #runs the game while there are still
            #poss_moves to execute
            while len(self.poss_moves) > 0: # while there are still moves
                if self.invalid_input == True:
                    print('game over! non-number input too many times...')
                    return -1
                print(self.print_board())
                self.aval_moves() # indirectly calls for user input and calcs poss_moves
                self.make_comp_move()
                self.determine_winner() # checks to see if any winning patterns occurred
                if self.winner is not None: # if prev func found a winner, returns winner
                    print(self.print_board())
                    return self.winner

        except ValueError:
            #if an exception is called, it tries to
            #determine the winner and print board
            self.determine_winner()
            print(self.print_board())
            print("Thanks for playing Tic-Tac-Toe!")

###ideally I'd like to randomly choose a first move and then change
#human player to 'O' based on the roll of the die
human_player = User('X')
comp_player = Computer('O')
g1 = Game()
g1.play(human_player, comp_player)
#if a winner has been found, prints the winner
if g1.winner is not None:
    print(g1.winner, 'has won!')
if (g1.invalid_input == False) and (g1.winner == None):
    print('Draw!')
