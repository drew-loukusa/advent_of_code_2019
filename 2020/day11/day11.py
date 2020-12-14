from aocd.models import Puzzle

def save_input_to_file(puzzle, day):
    filename = "day" + str(day) + ".txt"
    with open(filename, mode='w+') as f:
        data = puzzle.input_data
        f.write(data)

Year=2020
Day=11

# puzzle = Puzzle(year=Year, day=Day)
# save_input_to_file(puzzle, day=Day)

#infile = "day11ex.txt"
infile = "C:\\source\\advent-of-code\\2020\\day11\\day11ex.txt"
infile = "day11.txt"
seats = [list(line.rstrip()) for line in open(infile)]

MAX_X = len(seats[0]) - 1
MAX_Y = len(seats) - 1

def is_empty(seats, x,y):
    return seats[y][x] in ['L', '.']

def is_occupied(seats, x,y):
    return not is_empty(seats, x, y)

# def adjacent_occupied(seats, x, y):
#     occupied_seats = 0
#     # Count seats above: From (x-1, y-1) -> (x+1, y-1)
#     if y > 0:
#         if x > 0     and is_occupied(seats, x-1, y-1): occupied_seats += 1
#         if is_occupied(seats, x, y-1): occupied_seats += 1
#         if x < MAX_X and is_occupied(seats, x+1, y-1): occupied_seats += 1


#     # Count seats left and right: (x-1, y), (x+1, y)
#     if x > 0     and is_occupied(seats, x-1, y): occupied_seats += 1
#     if x < MAX_X and is_occupied(seats, x+1, y): occupied_seats += 1

#     # Count seats below: From (x-1, y+1) -> (x+1 y+1)
#     if y < MAX_Y:
#         if x > 0     and is_occupied(seats, x-1, y+1): occupied_seats += 1
#         if is_occupied(seats, x, y+1): occupied_seats += 1
#         if x < MAX_X and is_occupied(seats, x+1, y+1): occupied_seats += 1

#     return occupied_seats

def adjacent_occupied(occupied_set, x, y):
    occupied_seats = 0
    # Count seats above: From (x-1, y-1) -> (x+1, y-1)
    if y > 0:
        if x > 0     and (x-1, y-1) in occupied_set: occupied_seats += 1
        if               (x  , y-1) in occupied_set: occupied_seats += 1
        if x < MAX_X and (x+1, y-1) in occupied_set: occupied_seats += 1


    # Count seats left and right: (x-1, y), (x+1, y)
    if x > 0     and (x-1, y) in occupied_set: occupied_seats += 1
    if x < MAX_X and (x+1, y) in occupied_set: occupied_seats += 1

    # Count seats below: From (x-1, y+1) -> (x+1 y+1)
    if y < MAX_Y:
        if x > 0     and (x-1, y+1) in occupied_set: occupied_seats += 1
        if               ( x , y+1) in occupied_set: occupied_seats += 1
        if x < MAX_X and (x+1, y+1) in occupied_set: occupied_seats += 1

    return occupied_seats

def update_seat(seats, seats_copy, occupied_set, occupied_set_copy, x, y):

    # Return 1 or -1 based on if seat was updated to "occupied" or "empty"
    
    # DEF: Adjacent: one of the eight positions immediately up, down, left, right, or diagonal from a seat
    
    # The seat becomes occupied:
    # > If a seat is empty (L) AND
    # > There are no occupied seats adjacent to it
    if is_empty(seats, x, y) and adjacent_occupied(occupied_set, x, y) == 0:
        seats_copy[y][x] = '#'
        occupied_set_copy.add((x,y))
        return 1

    # The seat becomes empty:
    # > If a seat is occupied (#) AND 
    # > Four or more seats adjacent to it are also occupied
    if not is_empty(seats, x, y) and adjacent_occupied(occupied_set, x ,y) >= 4:
        seats_copy[y][x] = 'L'
        occupied_set_copy.remove((x,y))
        return -1

    # Seat state did not change
    return 0 

def simulate_round(seats, seats_copy, occupied_seats, occupied_set, occupied_set_copy):
    for row, y in zip(seats, range(len(seats))): 
        for seat, x in zip(row, range(len(row))):
            if seat == '.': continue 
            occupied_seats += update_seat(seats, seats_copy, occupied_set, occupied_set_copy, x, y)
    
    return occupied_seats

# Part 1
if True:
    last_count = 0
    occupied_set = set()
    occupied_set_copy = occupied_set.copy()
    seats_copy = [ row[:] for row in seats ]
    occupied_count = simulate_round(seats, seats_copy, last_count, occupied_set, occupied_set_copy)
    while last_count != occupied_count:
        last_count = occupied_count
        seats = seats_copy 
        seats_copy = [ row[:] for row in seats ]
        occupied_set = occupied_set_copy
        occupied_set_copy = occupied_set_copy.copy()
        occupied_count = simulate_round(seats, seats_copy, occupied_count, occupied_set, occupied_set_copy)      
    
    print(occupied_count)
    #puzzle.answer_a = result

# Part 2
if True:
    pass

    #puzzle.answer_b = result
