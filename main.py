#!/usr/bin/python
import copy
import random
import heapq
# include array for orientations
from queue import PriorityQueue

number_of_moves = 0

# arrays to hold cube face positions
# [top left, top middle, top right,
# middle left, middle middle, middle right,
# bottom left, bottom middle, bottom right]
top = [9, 7, 1, 2, 4, 8, 5, 3, 6]
front = [1, 5, 2, 4, 6, 3, 7, 8, 9]
bottom = [5, 9, 6, 3, 7, 8, 2, 4, 1]
back = [8, 2, 9, 1, 5, 7, 6, 3, 4]
left = [3, 8, 7, 2, 1, 9, 5, 6, 4]
right = [8, 6, 3, 2, 1, 9, 4, 5, 7]

top1 = [9, 7, 1, 2, 4, 8, 5, 3, 6]
front1 = [1, 5, 2, 4, 6, 3, 7, 8, 9]
bottom1 = [5, 9, 6, 3, 7, 8, 2, 4, 1]
back1 = [8, 2, 9, 1, 5, 7, 6, 3, 4]
left1 = [3, 8, 7, 2, 1, 9, 5, 6, 4]
right1 = [8, 6, 3, 2, 1, 9, 4, 5, 7]

cube_start = [top, front, bottom, back, left, right]
cube_randomize = [top, front, bottom, back, left, right]
cube_solve = [top1, front1, bottom1, back1, left1, right1]


def print_cube():
    print("\t\t  " + str(top[0:3]) + "\n\n\t\t  " + str(top[3:6]) + "\n\n\t\t  " + str(top[6:]) + "\n")
    print(str(left[0:3]) + " " + str(front[0:3]) + " " + str(right[0:3]) + "\n")
    print(str(left[3:6]) + " " + str(front[3:6]) + " " + str(right[3:6]) + "\n")
    print(str(left[6:]) + " " + str(front[6:]) + " " + str(right[6:]) + "\n")

    print("\t\t  [" + str(bottom[0]) + ", " + str(bottom[1]) + ", " + str(bottom[2]) + "]\n")
    print("\t\t  [" + str(bottom[3]) + ", " + str(bottom[4]) + ", " + str(bottom[5]) + "]\n")
    print("\t\t  [" + str(bottom[6]) + ", " + str(bottom[7]) + ", " + str(bottom[8]) + "]\n")

    print("\n\t\t  " + str(back[0:3]) + "\n\n\t\t  " + str(back[3:6]) + "\n\n\t\t  " + str(back[6:]) + "\n\n")


def make_move_1(c):
    temp1 = c[0][6]
    temp2 = c[0][7]
    temp3 = c[0][8]

    c[0][6] = c[4][8]
    c[0][7] = c[4][5]
    c[0][8] = c[4][2]

    c[4][8] = c[2][2]
    c[4][5] = c[2][1]
    c[4][2] = c[2][0]

    c[2][2] = c[5][0]
    c[2][1] = c[5][3]
    c[2][0] = c[5][6]

    c[5][0] = temp1
    c[5][3] = temp2
    c[5][6] = temp3

    temp4 = c[1][0]
    temp5 = c[1][1]
    temp6 = c[1][2]

    c[1][0] = c[1][6]
    c[1][6] = c[1][8]
    c[1][8] = temp6
    c[1][1] = c[1][3]
    c[1][3] = c[1][7]
    c[1][7] = c[1][5]
    c[1][5] = temp5
    c[1][2] = temp4


def make_move_2(c):
    temp1 = c[0][6]
    temp2 = c[0][7]
    temp3 = c[0][8]

    c[0][6] = c[5][0]
    c[0][7] = c[5][3]
    c[0][8] = c[5][6]

    c[5][0] = c[2][2]
    c[5][3] = c[2][1]
    c[5][6] = c[2][0]

    c[2][2] = c[4][8]
    c[2][1] = c[4][5]
    c[2][0] = c[4][2]

    c[4][8] = temp1
    c[4][5] = temp2
    c[4][2] = temp3

    temp4 = c[1][0]
    temp5 = c[1][1]
    temp6 = c[1][2]

    c[1][0] = temp6
    c[1][2] = c[1][8]
    c[1][8] = c[1][6]
    c[1][6] = temp4
    c[1][1] = c[1][5]
    c[1][5] = c[1][7]
    c[1][7] = c[1][3]
    c[1][3] = temp5


def make_move_3(c):
    temp1 = c[1][6]
    temp2 = c[1][7]
    temp3 = c[1][8]

    c[1][6] = c[4][6]
    c[1][7] = c[4][7]
    c[1][8] = c[4][8]

    c[4][6] = c[3][2]
    c[4][7] = c[3][1]
    c[4][8] = c[3][0]

    c[3][2] = c[5][6]
    c[3][1] = c[5][7]
    c[3][0] = c[5][8]

    c[5][6] = temp1
    c[5][7] = temp2
    c[5][8] = temp3

    temp4 = c[2][0]
    temp5 = c[2][1]
    temp6 = c[2][2]

    c[2][0] = c[2][6]
    c[2][6] = c[2][8]
    c[2][8] = temp6
    c[2][1] = c[2][3]
    c[2][3] = c[2][7]
    c[2][7] = c[2][5]
    c[2][5] = temp5
    c[2][2] = temp4


def make_move_4(c):
    temp1 = c[1][6]
    temp2 = c[1][7]
    temp3 = c[1][8]

    c[1][6] = c[5][6]
    c[1][7] = c[5][7]
    c[1][8] = c[5][8]

    c[5][6] = c[3][0]
    c[5][7] = c[3][1]
    c[5][8] = c[3][2]

    c[3][2] = c[4][6]
    c[3][1] = c[4][7]
    c[3][0] = c[4][8]

    c[4][6] = temp1
    c[4][7] = temp2
    c[4][8] = temp3

    temp4 = c[2][0]
    temp5 = c[2][1]
    temp6 = c[2][2]

    c[2][0] = temp6
    c[2][2] = c[2][8]
    c[2][8] = c[2][6]
    c[2][6] = temp4
    c[2][1] = c[2][5]
    c[2][5] = c[2][7]
    c[2][7] = c[2][3]
    c[2][3] = temp5


def make_move_5(c):
    temp1 = c[1][2]
    temp2 = c[1][5]
    temp3 = c[1][8]

    c[1][2] = c[2][2]
    c[1][5] = c[2][5]
    c[1][8] = c[2][8]

    c[2][2] = c[3][2]
    c[2][5] = c[3][5]
    c[2][8] = c[3][8]

    c[3][2] = c[0][2]
    c[3][5] = c[0][5]
    c[3][8] = c[0][8]

    c[0][2] = temp1
    c[0][5] = temp2
    c[0][8] = temp3

    temp4 = c[5][0]
    temp5 = c[5][1]
    temp6 = c[5][2]

    c[5][0] = c[5][6]
    c[5][6] = c[5][8]
    c[5][8] = temp6
    c[5][2] = temp4
    c[5][1] = c[5][3]
    c[5][3] = c[5][7]
    c[5][7] = c[5][5]
    c[5][5] = temp5


def make_move_6(c):
    temp1 = c[1][2]
    temp2 = c[1][5]
    temp3 = c[1][8]

    c[1][2] = c[0][2]
    c[1][5] = c[0][5]
    c[1][8] = c[0][8]

    c[0][2] = c[3][2]
    c[0][5] = c[3][5]
    c[0][8] = c[3][8]

    c[3][2] = c[2][2]
    c[3][5] = c[2][5]
    c[3][8] = c[2][8]

    c[2][2] = temp1
    c[2][5] = temp2
    c[2][8] = temp3

    temp4 = c[5][0]
    temp5 = c[5][1]
    temp6 = c[5][2]

    c[5][0] = temp6
    c[5][2] = c[5][8]
    c[5][8] = c[5][6]
    c[5][6] = temp4
    c[5][1] = c[5][5]
    c[5][5] = c[5][7]
    c[5][7] = c[5][3]
    c[5][3] = temp5


def make_move_7(c):
    temp1 = c[2][6]
    temp2 = c[2][7]
    temp3 = c[2][8]

    c[2][6] = c[4][0]
    c[2][7] = c[4][3]
    c[2][8] = c[4][6]

    c[4][0] = c[0][2]
    c[4][3] = c[0][1]
    c[4][6] = c[0][0]

    c[0][2] = c[5][8]
    c[0][1] = c[5][5]
    c[0][0] = c[5][2]

    c[5][8] = temp1
    c[5][5] = temp2
    c[5][2] = temp3

    temp4 = c[3][0]
    temp5 = c[3][1]
    temp6 = c[3][2]

    c[3][0] = c[3][6]
    c[3][6] = c[3][8]
    c[3][8] = temp6
    c[3][2] = temp4
    c[3][1] = c[3][3]
    c[3][3] = c[3][7]
    c[3][7] = c[3][5]
    c[3][5] = temp5


def make_move_8(c):
    temp1 = c[2][6]
    temp2 = c[2][7]
    temp3 = c[2][8]

    c[2][6] = c[5][8]
    c[2][7] = c[5][5]
    c[2][8] = c[5][2]

    c[5][8] = c[0][0]
    c[5][5] = c[0][1]
    c[5][2] = c[0][2]

    c[0][2] = c[4][0]
    c[0][1] = c[4][3]
    c[0][0] = c[4][6]

    c[4][0] = temp1
    c[4][3] = temp2
    c[4][6] = temp3

    temp4 = c[3][0]
    temp5 = c[3][1]
    temp6 = c[3][2]

    c[3][0] = temp6
    c[3][2] = c[3][8]
    c[3][8] = c[3][6]
    c[3][6] = temp4
    c[3][1] = c[3][5]
    c[3][5] = c[3][7]
    c[3][7] = c[3][3]
    c[3][3] = temp5


def make_move_9(c):
    temp1 = c[1][0]
    temp2 = c[1][1]
    temp3 = c[1][2]

    c[1][0] = c[5][0]
    c[1][1] = c[5][1]
    c[1][2] = c[5][2]

    c[5][0] = c[3][8]
    c[5][1] = c[3][7]
    c[5][2] = c[3][6]

    c[3][8] = c[4][0]
    c[3][7] = c[4][1]
    c[3][6] = c[4][2]

    c[4][0] = temp1
    c[4][1] = temp2
    c[4][2] = temp3

    temp4 = c[0][0]
    temp5 = c[0][1]
    temp6 = c[0][2]

    c[0][0] = c[0][6]
    c[0][6] = c[0][8]
    c[0][8] = temp6
    c[0][1] = c[0][3]
    c[0][3] = c[0][7]
    c[0][7] = c[0][5]
    c[0][5] = temp5
    c[0][2] = temp4


def make_move_10(c):
    temp1 = c[1][0]
    temp2 = c[1][1]
    temp3 = c[1][2]

    c[1][0] = c[4][0]
    c[1][1] = c[4][1]
    c[1][2] = c[4][2]

    c[4][0] = c[3][8]
    c[4][1] = c[3][7]
    c[4][2] = c[3][6]

    c[3][8] = c[5][0]
    c[3][7] = c[5][1]
    c[3][6] = c[5][2]

    c[5][0] = temp1
    c[5][1] = temp2
    c[5][2] = temp3

    temp4 = c[0][0]
    temp5 = c[0][1]
    temp6 = c[0][2]

    c[0][0] = temp6
    c[0][2] = c[0][8]
    c[0][8] = c[0][6]
    c[0][6] = temp4
    c[0][1] = c[0][5]
    c[0][5] = c[0][7]
    c[0][3] = temp5
    c[0][7] = c[0][3]


def make_move_11(c):
    temp1 = c[1][0]
    temp2 = c[1][3]
    temp3 = c[1][6]

    c[1][0] = c[0][0]
    c[1][3] = c[0][3]
    c[1][6] = c[0][6]

    c[0][0] = c[3][0]
    c[0][3] = c[3][3]
    c[0][6] = c[3][6]

    c[3][0] = c[2][0]
    c[3][3] = c[2][3]
    c[3][6] = c[2][6]

    c[2][0] = temp1
    c[2][3] = temp2
    c[2][6] = temp3

    temp4 = c[4][0]
    temp5 = c[4][1]
    temp6 = c[4][2]

    c[4][0] = c[4][6]
    c[4][6] = c[4][8]
    c[4][8] = temp6
    c[4][1] = c[4][3]
    c[4][3] = c[4][7]
    c[4][7] = c[4][5]
    c[4][5] = temp5
    c[4][2] = temp4


def make_move_12(c):
    temp1 = c[1][0]
    temp2 = c[1][3]
    temp3 = c[1][6]

    c[1][0] = c[2][0]
    c[1][3] = c[2][3]
    c[1][6] = c[2][6]

    c[2][0] = c[3][0]
    c[2][3] = c[3][3]
    c[2][6] = c[3][6]

    c[3][0] = c[0][0]
    c[3][3] = c[0][3]
    c[3][6] = c[0][6]

    c[0][0] = temp1
    c[0][3] = temp2
    c[0][6] = temp3

    temp4 = c[4][0]
    temp5 = c[4][1]
    temp6 = c[4][2]

    c[4][0] = temp6
    c[4][2] = c[4][8]
    c[4][8] = c[4][6]
    c[4][6] = temp4
    c[4][1] = c[4][5]
    c[4][5] = c[4][7]
    c[4][7] = c[4][3]
    c[4][3] = temp5


def randomize():
    count = 0
    while count < int(number_of_moves):

        # generate a number from 1-12
        random_turn_option = random.randint(1, 12)
        print("turn option: " + str(random_turn_option) + "\n")

        # REGULAR TURNS
        if random_turn_option == 1:  # front turn
            make_move_1(cube_randomize)
        elif random_turn_option == 2:  # front inverted
            make_move_2(cube_randomize)
        elif random_turn_option == 3:  # bottom turn
            make_move_3(cube_randomize)
        elif random_turn_option == 4:  # bottom turn inverted
            make_move_4(cube_randomize)
        elif random_turn_option == 5:  # right turn
            make_move_5(cube_randomize)
        elif random_turn_option == 6:  # right turn inverted
            make_move_6(cube_randomize)
        elif random_turn_option == 7:  # back turn
            make_move_7(cube_randomize)
        elif random_turn_option == 8:  # back turn inverted
            make_move_8(cube_randomize)
        elif random_turn_option == 9:  # top turn
            make_move_9(cube_randomize)
        elif random_turn_option == 10:  # top turn inverted
            make_move_10(cube_randomize)
        elif random_turn_option == 11:  # left turn
            make_move_11(cube_randomize)
        elif random_turn_option == 12:  # left turn inverted
            make_move_12(cube_randomize)

        print_cube()
        count += 1


def calc_heuristic(cube1):
    total_duplicates = []
    face_index = 0
    duplicated_numbers = [[], [], [], [], [], [], [], [], []]
    for _ in cube1:  # for each face count the occurrences of 1-9
        counts_of_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        counts_of_numbers[0] = cube1[face_index].count(1)
        counts_of_numbers[1] = cube1[face_index].count(2)
        counts_of_numbers[2] = cube1[face_index].count(3)
        counts_of_numbers[3] = cube1[face_index].count(4)
        counts_of_numbers[4] = cube1[face_index].count(5)
        counts_of_numbers[5] = cube1[face_index].count(6)
        counts_of_numbers[6] = cube1[face_index].count(7)
        counts_of_numbers[7] = cube1[face_index].count(8)
        counts_of_numbers[8] = cube1[face_index].count(9)

        # add up total duplicates for this face
        temp_val = 0
        for x_score in counts_of_numbers:  # for every count of numbers
            if x_score >= 2:  # if there are more than 2 of that number
                duplicated_numbers[face_index].append(x_score)
                temp_val = temp_val + x_score  # add that to the amount of duplicates
            elif x_score <= 2:
                duplicated_numbers[face_index].append(x_score)
                temp_val = temp_val + 0
        total_duplicates.append(temp_val)
        face_index = face_index + 1

    largest_number_of_duplicates = max(total_duplicates)
    indices_of_max = [i for i, x in enumerate(total_duplicates) if x == largest_number_of_duplicates]
    indices_of_max_heuristics = []
    # print("index of max duplicates " + str(indices_of_max))

    # calculate heuristic
    for r in indices_of_max:  # for each index containing the largest number of duplicated numbers
        temp_list = duplicated_numbers[r]
        # print("duplicated numbers of face " + str(temp_list))
        duplicated = []  # list of duplicated numbers for that face
        duplicated_used = []  # list of duplicated numbers already used in heuristic calculation
        x_score = 0
        y_score = 0
        z_score = 0

        # create list of duplicated numbers for this face
        for s in temp_list:
            if s > 1:
                duplicated.append(temp_list.index(s)+1)

        # print("duplicated " + str(duplicated))
        # ----- calculate x(f) = the number of rows in which all 3 tiles in the row are a tile from duplicates
        if cube_randomize[r][0] in duplicated and cube_randomize[r][1] in duplicated and cube_randomize[r][1] in duplicated:
            x_score = x_score + 1
            duplicated_used.append(cube_randomize[r][0])
            duplicated_used.append(cube_randomize[r][1])
            duplicated_used.append(cube_randomize[r][2])
        if cube_randomize[r][3] in duplicated and cube_randomize[r][4] in duplicated and cube_randomize[r][5] in duplicated:
            x_score = x_score + 1
            duplicated_used.append(cube_randomize[r][3])
            duplicated_used.append(cube_randomize[r][4])
            duplicated_used.append(cube_randomize[r][5])
        if cube_randomize[r][6] in duplicated and cube_randomize[r][7] in duplicated and cube_randomize[r][8] in duplicated:
            x_score = x_score + 1
            duplicated_used.append(cube_randomize[r][6])
            duplicated_used.append(cube_randomize[r][7])
            duplicated_used.append(cube_randomize[r][8])
        # ----- calculate y(f) = the number of columns in which all 3 tiles in the row are a tile from duplicates
        if cube_randomize[r][0] in duplicated and cube_randomize[r][3] in duplicated and cube_randomize[r][6] in duplicated:
            y_score = y_score + 1
            duplicated_used.append(cube_randomize[r][0])
            duplicated_used.append(cube_randomize[r][3])
            duplicated_used.append(cube_randomize[r][6])
        if cube_randomize[r][1] in duplicated and cube_randomize[r][4] in duplicated and cube_randomize[r][7] in duplicated:
            y_score = y_score + 1
            duplicated_used.append(cube_randomize[r][1])
            duplicated_used.append(cube_randomize[r][4])
            duplicated_used.append(cube_randomize[r][7])
        if cube_randomize[r][2] in duplicated and cube_randomize[r][5] in duplicated and cube_randomize[r][8] in duplicated:
            y_score = y_score + 1
            duplicated_used.append(cube_randomize[r][2])
            duplicated_used.append(cube_randomize[r][5])
            duplicated_used.append(cube_randomize[r][8])
        # ----- the number of remaining duplicate pairs
        for t in range(9):
            if cube_randomize[r][t] in duplicated and cube_randomize[r][t] not in duplicated_used:
                z_score = z_score + 1
                duplicated_used.append(cube_randomize[r][t])
        heuristic_value = x_score + y_score + z_score
        # print("x score : " + str(x_score))
        # print("y score : " + str(y_score))
        # print("z score : " + str(z_score))
        # print("h score : " + str(heuristic_value))
        indices_of_max_heuristics.append(heuristic_value)

    return max(indices_of_max_heuristics)


class Tree(object):
    def __init__(self):
        self.child = []
        self.value = ()

    def create_children(self):
        for i in range(0, 12):
            self.child.append(Tree())

    def set_children_values(self, list):
        for i in range(0, len(list)):
            self.child[i].value = list[i]


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, other = (), parent=()):
        self.parent = parent

        self.g = other[1]
        self.h = other[2]
        self.f = other[0]
        self.cube_position = other[3]
        self.move_made = other[4]

    def __eq__(self, other):
        self.parent = None
        self.g = other[1]
        self.h = other[2]
        self.f = other[0]
        self.cube_position = other[3]
        self.move_made = other[4]


# /////////////////////////////////
# Code taken from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# I slightly modified it to fit my needs
# /////////////////////////////////
def a_star():
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    start = (0, 0, 0, cube_solve, 0)
    end = (0, 0, 0, cube_randomize, 0)
    print(cube_start)
    print(cube_randomize)
    # Create start and end node
    start_node = Node(start)
    end_node = Node(end)

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    # Loop until you find the end
    while len(open_list) > 0:
        print("inside while loop")
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        print("current_node.cube_position")
        print(current_node.cube_position)
        print("end_node.cube_position")
        print(end_node.cube_position)
        # Found the goal
        if current_node.cube_position == end_node.cube_position:
            print("found goal")
            path1 = []
            current = current_node
            while current is not None:
                path1.append(current.move_made)
                current = current.parent
            return path1[::-1]  # Return reversed path

        # Generate children
        children = generate_children(current_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child.cube_position == closed_child.cube_position:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = calc_heuristic(child.cube_position)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child.cube_position == open_node.cube_position and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


# function used to generate a node's children
def generate_children(current_node):
    print("got to generate children")
    # for every possible move, generate a tuple and push it on to the heap
    children_tuples = []
    for i in range(12):  # generate first possible twelve tuples
        cube_temp = copy.deepcopy(current_node.cube_position)
        if i == 0:
            make_move_1(cube_temp)
        if i == 1:
            make_move_2(cube_temp)
        if i == 2:
            make_move_3(cube_temp)
        if i == 3:
            make_move_4(cube_temp)
        if i == 4:
            make_move_5(cube_temp)
        if i == 5:
            make_move_6(cube_temp)
        if i == 6:
            make_move_7(cube_temp)
        if i == 7:
            make_move_8(cube_temp)
        if i == 8:
            make_move_9(cube_temp)
        if i == 9:
            make_move_10(cube_temp)
        if i == 10:
            make_move_11(cube_temp)
        if i == 11:
            make_move_12(cube_temp)
        temp_tuple = (0, 0, 0, cube_temp, i + 1)
        children_tuples.append(temp_tuple)

    children_nodes = []
    for i in children_tuples:
        print(i)
        temp_node = Node(i, current_node)
        children_nodes.append(temp_node)
    print("children nodes : ")
    for _ in children_nodes:
        print("!")
    return children_nodes


# ------------- START PROGRAM EXECUTION HERE ----------------------



print("Starting Cube Positions \n\n")
print_cube()

print("Possible Turn Directions: ")
print("1: front turn")
print("2: front turn inverted")
print("3: bottom turn")
print("4: bottom turn inverted")
print("5: right turn")
print("6: right turn inverted")
print("7: back turn")
print("8: back turn inverted")
print("9: top turn")
print("10: top turn inverted")
print("11: left turn")
print("12: left turn inverted")

number_of_moves = input("\nEnter the number of moves you want to randomize the cube: ")

print("random 1: " + str(cube_randomize))
randomize()
print("random 2: " + str(cube_randomize))
path = a_star()
print("Path to undo cube: ")
print(path)
