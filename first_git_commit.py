import random
COMPUTER_LETTER = 'X'
HUMAN_LETTER = 'O'

class User:
    def __init__(self, letter):
        self.letter = letter

    def user_make_move(self, position):
        g1.manipulate_board_list(position, 'X')


class Computer:
    def __init__(self, letter):
        self.letter = letter

    def computer_make_move(self):
        comp_move = random.sample(self.aval_moves())
        return comp_move

class Game:

    def __init__(self):
        self.main = []

    #responsible for choosing what letter starts
    starting_letter = random.sample(['X','O'], 1)

    def create_board_list(self):
        j = 3
        for x in range(3):
            self.main.append([i for i in range(j-3, j)])
            j += 3
        return self.main


    def user_input(self):
        user_choice = int(input("Enter a number(0-8): "))
        return user_choice

    def manipulate_board_list(self, number, letter):

        val = self.create_board_list()

        new_val = []
        count = 0
        for lists in val:
            if count < 3:
                new_val.append(lists)
            count += 1

        if number < 3:
            num_inner_list = 0
            for i in new_val[num_inner_list]:
                if i == number:
                    index = new_val[num_inner_list].index(i)
                    new_val[num_inner_list][index] = letter

        if 2 < number < 6:
            num_inner_list = 1
            for i in new_val[num_inner_list]:
                if i == number:
                    index = new_val[num_inner_list].index(i)
                    new_val[num_inner_list][index] = letter

        if 5 < number < 9:
            num_inner_list = 2
            for i in new_val[num_inner_list]:
                if i == number:
                    index = new_val[num_inner_list].index(i)
                    new_val[num_inner_list][index] = letter

        return new_val

    def aval_moves(self):
        current_board = self.manipulate_board_list(self.user_input(), 'X')
        poss_moves = []
        for lists in current_board:
            for ele in lists:
                try:
                    int(ele)
                    poss_moves.append(ele)
                except ValueError:
                    continue
        return poss_moves


    def print_board(self):
        val = self.create_board_list()
        final_list = []

        count = 0
        for lists in val:
            if count < 3:
                final_list.append(lists)
            count += 1

        first_element = True
        for row in final_list:
            first_element = True
            for ele in row:
                if first_element:
                    print(f'| {row[0]} | {row[1]} | {row[2]} |')
                    first_element = False

        return '-------------'

    def play(self, user, computer):

        print(self.print_board())
        print("Poss Moves:", self.aval_moves())
        #BRING IT OVER TO PLAYER.PY and test some some stuff
        #what happens when you define a method as a variable? Why do I get a certain number of input requests? etc

        count = 0
        while count < 8:
            print(self.print_board())
            print('Your poss moves are: ', self.aval_moves())
            count += 1


human_player = User(HUMAN_LETTER)
comp_player = Computer(COMPUTER_LETTER)
g1 = Game()
g1.play(human_player, comp_player)