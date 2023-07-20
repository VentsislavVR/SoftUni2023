#                                                          [['0', 'K', '0', 'K', '0'],
#                                                          ['K', '0', '0', '0', 'K'],
#                                                          ['0', '0', 'K', '0', '0'],
#                                                          ['K', '0', '0', '0', 'K'],
#                                                          ['0', 'K', '0', 'K', '0']]
size = int(input())
matrix = [list(input()) for _ in range(size)]
# a = [-2, -1, 1, 2 ]
# positions = [(x,y) for x in a for y in a if abs(x) != abs(y)]
positions = (
    (2, 1),  # two down one right.
    (2, -1),  # two down one left .
    (-1, 2),  # two right one up.
    (1, 2),   # two right one down.
    (-2, -1), # two up one left.
    (-2, 1),  # two up one right.
    (-1, -2), # two left one up.
    (1, -2),  # two left one down.
)
removed_knights = 0


while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):  # Calculate the number of columns based on the current row.
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0<= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1
                if attacks > max_attacks:
                    knight_with_most_attacks_pos = [row,col]
                    max_attacks = attacks
    if knight_with_most_attacks_pos:
        matrix[knight_with_most_attacks_pos[0]][knight_with_most_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break
print(removed_knights)


