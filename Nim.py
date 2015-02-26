from random import randint, random
from time import sleep


board_size = 3
board_bin=[]

def show_board(board):
    
    columnformat = "{0:5}".format
    lineformat = "\n{0:10}: {1}".format
    cols = map(columnformat, range(1, len(board) + 1))
    show_text(lineformat("column", ''.join(cols)))
    cols = map(columnformat, board)
    show_text(lineformat("pieces", ''.join(cols)))
    show_text("\n")

def show_text(s):
    print s

def calcbest(board_bin,xorsum):
    newbin=[]
    for i in range(board_size):
        newbin.append(board_bin[i]^xorsum)
    for i in range(board_size):
        if newbin[i]<board_bin[i]:
            newbin[i]=1
        else:
            newbin[i]=0
    return newbin

def user1(board,board_bin,column_size):
    while True:
        show_text("User1 Turn")
        xorsum=None
        xorsum=board_bin[0]^board_bin[1]^board_bin[2]
        if (xorsum):
            print "You have  chance of winning"
        else:
            print "You will loose unless you a move such that Xor sum of remaining gives non zero"
        show_text("The best move would be in column:")
        a=calcbest(board_bin,xorsum)
        for i in range(len(a)):
            if(a[i]!=0):
                show_text(i+1)
        show_text("The best number to remove is:")
        show_text(int(str(xorsum),2))
        show_text("Please enter the column to decrease(1 to 3)")
        col=int(raw_input().strip())

        show_text("Please enter the amount to be removed")
        num=int(raw_input().strip())
        if 1 <= num <= column_size[col-1] and 1 <= col <= board_size:
            break
        
        show_text("Please enter correct values")
    return col,num
    
def user2(board,board_bin,column_size):
    while True:
        show_text("User2 Turn")
        xorsum=None
        xorsum=board_bin[0]^board_bin[1]^board_bin[2]
        if (xorsum):
            print "You have  chance of winning"
        else:
            print "You will loose unless you a move such that Xor sum of remaining gives non zero"
        show_text("The best move would be in column:")
        a=calcbest(board_bin,xorsum)
        for i in range(len(a)):
            if(a[i]!=0):
                show_text(i+1)
        show_text("The best number to remove is:")
        show_text(int(str(xorsum),2))
        show_text("Please enter the column to decrease(1 to 3)")
        col=int(raw_input().strip())

        show_text("Please enter the amount to be removed")
        num=int(raw_input().strip())
        if 1 <= num <= column_size[col-1] and 1 <= col <= board_size :
            break
        
        show_text("Please enter correct values")
    return col,num
        
def nim():
    column_size=[randint(1,7) for i in range(board_size)]
    board = [column_size[n] for n in range(board_size)]
    show_board(board)
    board_bin=["{0:b}".format(column_size[i]) for i in range(board_size)]
    show_board(board_bin)
    board_bin=[int(board_bin[i]) for i in range(board_size)]
    turn,user_turn=(user1,True) if random() < 0.5 else (user2,False)
    while True:
        column,num=turn(board,board_bin,column_size)
        board[column-1]-=num
        board_bin[column-1]="{0:b}".format(board[column-1])
        board_bin[column-1]= int(board_bin[column-1])
        show_board(board)
        if sum(board)==0:
            break
        turn = user2 if turn == user1 else user1
        show_board(board)
        
    show_text("\nThere are no pieces remaining, ")
    show_text("User 1 wins!\n" if turn == user1 else "User2 Wins win!\n")
    sleep(0.5)
    sleep(1.5)
    show_text("\n\nBye.")
        

if __name__ == '__main__':
    nim()