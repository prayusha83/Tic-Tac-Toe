class TicTacToe:

    # constructor
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.initialize_board()
    

    def initialize_board(self):
        pos = 0

        for i in range(3):
            for j in range(3):
                pos+=1
                self.board[i][j] = str(pos)


    def display_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end="")
                if(j<2):
                    print("|", end="")
            
            if(i<2):
                print()
                print("------")
    

    def make_move(self, pos):
        row = (pos-1)//3
        col = (pos-1)%3

        if self.board[row][col] in ['X', 'O']:
            print("Girl, that cell's taken. Try again.")
            return False

        self.board[row][col] = self.current_player
        return True


    def check_win(self):
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)):
                return True
            if all(self.board[j][i] == self.current_player for j in range(3)):
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)):
            return True    
        
        return False
    

    def is_draw(self):
        for row in self.board:
            for col in row:
                if col not in ['X', 'O']:
                    return False
                
        return True
    

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'


    def get_current_player(self):
        return self.current_player
    


def main():
    game = TicTacToe()

    while True:
        game.display_board()

        try:
            move = int(input(f"\nPlayer {game.get_current_player()}, enter position (1-9): "))

        except ValueError:
            print("Please enter a number")
            continue

        if move < 1 or move > 9:
            print("Please enter a valid move.")
            continue

        game.make_move(move)

        if game.check_win():
            game.display_board()
            print(f"Player {game.get_current_player()} CONGRATULATIONS")
            break

        if game.is_draw():
            game.display_board()
            print("Oops, it's a draw")
            break

        game.switch_player()


if __name__ == "__main__":
    main()