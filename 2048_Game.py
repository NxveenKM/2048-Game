import random
import os

def start_game():
    mat = [[0] * 4 for _ in range(4)]
    add_new_tile(mat)
    add_new_tile(mat)
    return mat

def add_new_tile(mat):
    r, c = random.randint(0, 3), random.randint(0, 3)
    while mat[r][c] != 0:
        r, c = random.randint(0, 3), random.randint(0, 3)
    mat[r][c] = 2 if random.random() < 0.9 else 4

def compress(mat):
    new_mat = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos += 1
    return new_mat

def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
    return mat

def move_left(mat):
    mat = compress(mat)
    mat = merge(mat)
    mat = compress(mat)
    return mat

def move_right(mat):
    mat = [row[::-1] for row in mat]  # Reverse each row
    mat = move_left(mat)  # Use left move logic
    mat = [row[::-1] for row in mat]  # Reverse back
    return mat

def move_up(mat):
    mat = list(zip(*mat))  # Transpose the matrix
    mat = move_left(mat)  # Use left move logic
    mat = list(zip(*mat))  # Transpose back
    return [list(row) for row in mat]  # Convert back to list of lists

def move_down(mat):
    mat = list(zip(*mat))  # Transpose the matrix
    mat = move_right(mat)  # Use right move logic
    mat = list(zip(*mat))  # Transpose back
    return [list(row) for row in mat]  # Convert back to list of lists

def get_current_state(mat):
    for row in mat:
        if 2048 in row:
            return 'WON'
    if any(0 in row for row in mat):
        return 'GAME NOT OVER'
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] or mat[j][i] == mat[j + 1][i]:
                return 'GAME NOT OVER'
    return 'LOST'

def print_matrix(mat):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in mat:
        print("\t".join(str(num) if num != 0 else "." for num in row))
    print()

# Main game loop
if __name__ == "__main__":
    mat = start_game()
    while True:
        print_matrix(mat)  # Display the matrix
        move = input("Press the command (W/A/S/D): ").upper()
        if move == 'W':
            mat = move_up(mat)
        elif move == 'A':
            mat = move_left(mat)
        elif move == 'S':
            mat = move_down(mat)
        elif move == 'D':
            mat = move_right(mat)
        else:
            print("Invalid input! Please use W, A, S, or D.")
            continue

        state = get_current_state(mat)
        if state != 'GAME NOT OVER':
            print_matrix(mat)  # Display the final state
            print(state)
            break

        add_new_tile(mat)
