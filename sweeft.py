#1
from collections import Counter

n = int(input())
word_list = []

for i in range (0,n):
    word = input()
    word_list.append(word)

t = tuple(Counter(word_list).values())
l = len(t)
print(l)
print(*t, sep=' ')

#2
def biggerIsGreater(w):
    w_list = list(w)
    ind = len(w_list)-1
    while ind > 0 and w_list[ind] <= w_list[ind-1]:
        ind = ind-1

    if ind <= 0:
        return'no answer'
    else:
        all_greater = w_list[ind:]
        all_greater.sort()
        for i in all_greater:
            if i>w_list[ind-1]:
                greater = i
                break
        w_list.reverse()
        greater = w_list.index(greater)
        f_greater = len(w_list) - 1 - greater
        w_list.reverse()
        w_list[ind-1], w_list[f_greater] = w_list[f_greater], w_list[ind-1]
        greater_word = w_list[:ind] + sorted(w_list[ind:])
        return ''.join(greater_word)

#testing
n = int(input())
for i in range(n):
    word = input()
    (print(biggerIsGreater(word)))


#3
def bomberMan(n, grid):
    fullgrid = []

    if n == 1:
        return grid
    elif n % 2 == 0:
        for i in range(len(grid)):
            fullgrid.append('O' * len(grid[0]))
        return fullgrid
    elif n % 4 == 3:
        return detonate(grid)
    else:
        return detonate(detonate(grid))


def detonate(grid):
    row = len(grid)
    column = len(grid[0])

    fullgrid = []
    for i in range(len(grid)):
            fullgrid.append(['O'] * column)

    bombs = []
    for each in range(row):
        for i in range(column):
            if grid[each][i] == 'O':
                bombs.append((each, i))
    # print(bombs)
    cells = [(-1, 0), (1, 0), (0, 0),  (0, 1), (0, -1)]

    for each in bombs:
        for i in cells:
            if 0 <= each[0] + i[0] < row and 0 <= each[1] + i[1] < column:
                fullgrid[each[0] + i[0]][each[1] + i[1]] = '.'
    final = []
    for each in fullgrid:
        final.append(''.join(each))
    return final

#about project:
#i dont know how to create API, although i know how to use API properly. i also have worked with flask framework, you can
#check out my first flask website (link in my CV).