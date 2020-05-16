from tkinter import *
from tkinter.ttk import *
file = open("words.txt", "r")
words = file.readlines()
dict = {}
puzzle = "sdgeaofhumbaseli"

for x in range(len(puzzle)):
    dict[x] = []
    size = int(len(puzzle)**0.5)
    if (x > int(size - 1)): dict[x].append(x-size)          #top
    if (x < len(puzzle) - size): dict[x].append(x+size)     #bottom
    if (x%size != size-1): dict[x].append(x+1)              #right
    if (x%size != 0): dict[x].append(x-1)                   #left

    if (x > int(size - 1)) and (x%size != size-1): dict[x].append(x-size+1)
    if (x > int(size - 1)) and (x%size != 0): dict[x].append(x-size-1)
    if (x < len(puzzle) - size) and (x%size != size-1): dict[x].append(x+size+1)
    if (x < len(puzzle) - size) and (x%size != 0): dict[x].append(x+size-1)
for s in range(len(words)):
    words[s] = words[s][0:len(words[s])-1:]
substrings = set()
for i in range(len(words)):
    for j in range(len(words[i])):
        substrings.add(words[i][0:j+1])
def recur(board, substring, pos, l):
    for item in dict[pos]:
        if substring + board[item] in substrings:
            l = recur(board, substring + board[item], item, l)
        if substring == "ca" and item == 2:
            v = "hi"
        if substring + board[item] in words and len(substring + board[item]) >=3:
            l.append(substring + board[item])
    return l
finalList = []
for k in range(len(puzzle)):
    finalList = (recur(puzzle, puzzle[k], k, finalList))
finalSet = set()
for word in finalList:
    finalSet.add(word)
finalList = list(finalSet)
def print_board(board):
    board = list(board)
    for x in range(4):
        for y in range(4):
            add = 1 - len(board[y + 4*x])
            print(board[y + 4*x] + " ", end="")
        print("")
def sort(l):
    for h in range(len(l)):
        for k in range(len(l) - 1):
            if (len(l[k]) > len(l[k+1])):
                l[k], l[k+1] = l[k+1], l[k]
    return l
print("board:")
print_board(puzzle)
print("")
print("all words, sorted:")
for word in sort(finalList):
    print (word)



