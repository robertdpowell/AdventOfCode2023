with open('input.txt') as f:
    map_data = [list(line.strip()) for line in f]
    map_height = len(map_data)
    map_width = len(map_data[0])
def is_special_character(char):
    return not (char.isdigit() or char == '.')

def is_star(char):
    return (char == '*')
def check_for_special_characters(row, col):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
    for dr, dc in directions:
        adjacent_row, adjacent_col = row + dr, col + dc # check the adjacent cells
        if 0 <= adjacent_row < map_height and 0 <= adjacent_col < map_width: # if the adjacent cell is within the map
            if is_special_character(map_data[adjacent_row][adjacent_col]):
                return True
    return False

def check_for_numbers_surrounding_star(row, col):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
    adjacent_digits = set()
    for dr, dc in directions:
        adjacent_row, adjacent_col = row + dr, col + dc # check the adjacent cells
        if 0 <= adjacent_row < map_height and 0 <= adjacent_col < map_width: # if the adjacent cell is within the map
            if map_data[adjacent_row][adjacent_col].isdigit():
                adjacent_digits.add((adjacent_row, adjacent_col))
                print (f'Adjacent digits are {adjacent_digits}')
    # if len(adjacent_digits) == 2:
        print(f'Adjacent digits are {adjacent_digits}')
        return True



def solve1():
    total_sum = 0
    for row in range(map_height):
        col = 0
        while col < map_width:
            if map_data[row][col].isdigit(): # if the current character is a digit
                current_num = map_data[row][col] # start with the current digit
                next_col = col + 1 # check the next column
                valid_number = False # assume the number is not valid

                if check_for_special_characters(row, col): # check if the current number is valid
                    valid_number = True # if it is, set the flag to True

                while next_col < map_width and map_data[row][next_col].isdigit(): # while the next column is a digit
                    if check_for_special_characters(row, next_col): # check if the current number is valid
                        valid_number = True # if it is, set the flag to True
                    current_num += map_data[row][next_col] # add the current digit to the current number
                    next_col += 1 # check the next column

                if valid_number: # if the number is valid
                    total_sum += int(current_num)

                col = next_col - 1 # set the current column to the next column
            col += 1 # check the next column

    return total_sum

def solve2():
    total_sum = 0
    for row in range(map_height):
        col = 0
        while col < map_width:
            if is_star(map_data[row][col]):  # Check if the current character is a star ('*') using your function
                if check_for_numbers_surrounding_star(row, col):
                    total_sum += 1
            col += 1
    return total_sum

# print (f'Solution 2 answer is {total_sum}')
print (f'Solution 1 answer is {solve1()}')
print (f'Solution 2 answer is {solve2()}')

