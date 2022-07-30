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

class Game:

    def __init__(self):
        self.main = []
        self.new_val = []
        self.poss_moves = []
        self.winner = None

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

        val = self.main

        self.new_val = []
        count = 0
        for lists in val:
            if count < 3:
                self.new_val.append(lists)
            count += 1

        if number < 3:
            num_inner_list = 0
            for i in self.new_val[num_inner_list]:
                if i == number:
                    index = self.new_val[num_inner_list].index(i)
                    self.new_val[num_inner_list][index] = letter

        if 2 < number < 6:
            num_inner_list = 1
            for i in self.new_val[num_inner_list]:
                if i == number:
                    index = self.new_val[num_inner_list].index(i)
                    self.new_val[num_inner_list][index] = letter

        if 5 < number < 9:
            num_inner_list = 2
            for i in self.new_val[num_inner_list]:
                if i == number:
                    index = self.new_val[num_inner_list].index(i)
                    self.new_val[num_inner_list][index] = letter

        return self.new_val

    def aval_moves(self):
        self.poss_moves = []
        user_choice = self.user_input()
        current_board = self.manipulate_board_list(user_choice, 'X')
        pre_filter_list = []

        for lists in current_board:
            for ele in lists:
                try:
                    int(ele)
                    pre_filter_list.append(ele)
                except ValueError:
                    continue
        for ele in pre_filter_list:
            if ele not in self.poss_moves:
                self.poss_moves.append(ele)

        return self.poss_moves


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

    def make_comp_move(self):
        select_move = random.sample(self.poss_moves, 1)
        for ele in select_move:
            comp_move = ele
        self.manipulate_board_list(comp_move, 'O')
        return 'make_comp_move was successfully run'


    def determine_winner(self):
        x_count = 0
        o_count = 0
        #determine a horizontal winner
        for lists in self.new_val:
            if x_count == 3:
                self.winner = 'X'
                return self.winner
            if o_count == 3:
                self.winner = 'O'
                return self.winner
            x_count = 0
            o_count = 0
            for ele in lists:
                if ele == 'X':
                    x_count += 1
                if ele == 'O':
                    o_count += 1

        #determining a vertical winner
        cur_index = 0
        checker_list = []
        while cur_index < 3:
            if checker_list.count('X') == 3:
                self.winner = 'X'
                return self.winner
            if checker_list.count('O') == 3:
                self.winner = 'O'
                return self.winner
            for lists in self.new_val:
                checker_list.append(lists[cur_index])
            cur_index += 1

        #determining a diagonal winner
        simple_new_val = []
        for lists in self.new_val:
            for ele in lists:
                simple_new_val.append(ele)

        relevant_spots = []
        relevant_spots.append(simple_new_val[0])
        relevant_spots.append(simple_new_val[4])
        relevant_spots.append(simple_new_val[8])

        if relevant_spots.count('X') == 3:
            self.winner = 'X'
            print('I guess diagonal worked!')
            return self.winner

        if relevant_spots.count('O') == 3:
            self.winner = 'O'
            print('I guess diagonal worked!')
            return self.winner

        relevant_spots.clear()
        relevant_spots.append(simple_new_val[2])
        relevant_spots.append(simple_new_val[4])
        relevant_spots.append(simple_new_val[6])

        if relevant_spots.count('X') == 3:
            self.winner = 'X'
            print('I guess diagonal worked!')
            return self.winner

        if relevant_spots.count('O') == 3:
            self.winner = 'O'
            print('I guess diagonal worked!')
            return self.winner

        return self.winner

    def play(self, user, computer):
        try:
            print(self.print_board())
            self.aval_moves()
            self.make_comp_move()

            count = 0
            while len(self.poss_moves) > 0:
                print(self.print_board())
                self.aval_moves()
                self.make_comp_move()
                self.determine_winner()
                count += 1
        except ValueError:
            print("Thanks for playing Tic-Tac-Toe!")

human_player = User(HUMAN_LETTER)
comp_player = Computer(COMPUTER_LETTER)
g1 = Game()
g1.play(human_player, comp_player)
print(g1.winner)
