import sys
import pprint

def load_file(filename):
    
    inData = open(filename, "r")

    board = []
    
    count = 0
    for line in inData.readlines():
        count += 1
        dimension = line.split()
        
        if len(dimension) != 9:
            print("Incorrect input: Not 9 numbers in the row")
            exit()

        try:
            board.append(list(map(int, dimension)))
        except ValueError as e:
            print("Incorrect input: Unable to convert input to integer")
            exit()

    if count != 9:
        print("Incorrect input: Number of rows is not equal to 9")
        exit()

    return board

def assert_nums(board):

    for row in board:
        for num in row:
            if num < 0 or num > 9:
                print("Incorrect input: Input numbers are not between 0 and 9")
                exit()

    return True

def generate(board):

    while not solved(board):
        pass





#Checks:
def check_row(board, row_num):

    check_set = set()
    
    #Can use simple set since we assert input is between 0 and 9 and
    # our code will only generate proper numbers between 1 and 9
    for num in board[row_num]:
        if num not in check_set:
            check_set.add(num)
        else:
            return False

    return True

def check_column(board, col_num):

    check_set = set()

    #Could hardcode loop sizes but that is bad    
    for row in board:
        for x in range(len(board[row])):
            if x == col_num:
                if board[row][x] not in check_set:
                    return check_set.add(board[row][x])
                else:
                    return False

    return True

def check_square(board, sq_num):

    pass


def main():
    
    filename = sys.argv[1]

    board = load_file(filename)
    assert_nums(board)

    pprint.pprint(board)

if __name__ == "__main__":
    main()


