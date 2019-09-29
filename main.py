#!/usr/bin/python
import random

# include array for orientations


def print_cube():
    print("\t\t  " + str(top[0:3]) + "\n\n\t\t  " + str(top[3:6]) + "\n\n\t\t  " + str(top[6:]) + "\n")
    print(str(left[0:3]) + " " + str(front[0:3]) + " " + str(right[0:3]) + "\n")
    print(str(left[3:6]) + " " + str(front[3:6]) + " " + str(right[3:6]) + "\n")
    print(str(left[6:]) + " " + str(front[6:]) + " " + str(right[6:]) + "\n")

    print("\t\t  [" + str(bottom[0]) + ", " + str(bottom[1]) + ", " + str(bottom[2]) + "]\n")
    print("\t\t  [" + str(bottom[3]) + ", " + str(bottom[4]) + ", " + str(bottom[5]) + "]\n")
    print("\t\t  [" + str(bottom[6]) + ", " + str(bottom[7]) + ", " + str(bottom[8]) + "]\n")

    print("\n\t\t  " + str(back[0:3]) + "\n\n\t\t  " + str(back[3:6]) + "\n\n\t\t  " + str(back[6:]) + "\n\n")


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
count = 0

while count < int(number_of_moves):

    # generate a number from 1-12
    random_turn_option = random.randint(1, 12)
    print("turn option: " + str(random_turn_option) + "\n")

    # REGULAR TURNS
    if random_turn_option == 1:  # front turn
        temp1 = top[6]
        temp2 = top[7]
        temp3 = top[8]

        top[6] = left[8]
        top[7] = left[5]
        top[8] = left[2]

        left[8] = bottom[2]
        left[5] = bottom[1]
        left[2] = bottom[0]

        bottom[2] = right[0]
        bottom[1] = right[3]
        bottom[0] = right[6]

        right[0] = temp1
        right[3] = temp2
        right[6] = temp3

        temp4 = front[0]
        temp5 = front[1]
        temp6 = front[2]

        front[0] = front[6]
        front[6] = front[8]
        front[8] = temp6
        front[1] = front[3]
        front[3] = front[7]
        front[7] = front[5]
        front[5] = temp5
        front[2] = temp4

    elif random_turn_option == 2:  # front inverted
        temp1 = top[6]
        temp2 = top[7]
        temp3 = top[8]

        top[6] = right[0]
        top[7] = right[3]
        top[8] = right[6]

        right[0] = bottom[2]
        right[3] = bottom[1]
        right[6] = bottom[0]

        bottom[2] = left[8]
        bottom[1] = left[5]
        bottom[0] = left[2]

        left[8] = temp1
        left[5] = temp2
        left[2] = temp3

        temp4 = front[0]
        temp5 = front[1]
        temp6 = front[2]

        front[0] = temp6
        front[2] = front[8]
        front[8] = front[6]
        front[6] = temp4
        front[1] = front[5]
        front[5] = front[7]
        front[7] = front[3]
        front[3] = temp5

    elif random_turn_option == 3:  # bottom turn
        temp1 = front[6]
        temp2 = front[7]
        temp3 = front[8]

        front[6] = left[6]
        front[7] = left[7]
        front[8] = left[8]

        left[6] = back[2]
        left[7] = back[1]
        left[8] = back[0]

        back[2] = right[6]
        back[1] = right[7]
        back[0] = right[8]

        right[6] = temp1
        right[7] = temp2
        right[8] = temp3

        temp4 = bottom[0]
        temp5 = bottom[1]
        temp6 = bottom[2]

        bottom[0] = bottom[6]
        bottom[6] = bottom[8]
        bottom[8] = temp6
        bottom[1] = bottom[3]
        bottom[3] = bottom[7]
        bottom[7] = bottom[5]
        bottom[5] = temp5
        bottom[2] = temp4

    elif random_turn_option == 4:  # bottom turn inverted
        temp1 = front[6]
        temp2 = front[7]
        temp3 = front[8]

        front[6] = right[6]
        front[7] = right[7]
        front[8] = right[8]

        right[6] = back[0]
        right[7] = back[1]
        right[8] = back[2]

        back[2] = left[6]
        back[1] = left[7]
        back[0] = left[8]

        right[6] = temp1
        right[7] = temp2
        right[8] = temp3

        temp4 = bottom[0]
        temp5 = bottom[1]
        temp6 = bottom[2]

        bottom[0] = temp6
        bottom[2] = bottom[8]
        bottom[8] = bottom[6]
        bottom[6] = temp4
        bottom[1] = bottom[5]
        bottom[5] = bottom[7]
        bottom[7] = bottom[3]
        bottom[3] = temp5

    elif random_turn_option == 5:  # right turn
        temp1 = front[2]
        temp2 = front[5]
        temp3 = front[8]

        front[2] = bottom[2]
        front[5] = bottom[5]
        front[8] = bottom[8]

        bottom[2] = back[2]
        bottom[5] = back[5]
        bottom[8] = back[8]

        back[2] = top[2]
        back[5] = top[5]
        back[8] = top[8]

        top[2] = temp1
        top[5] = temp2
        top[8] = temp3

        temp4 = right[0]
        temp5 = right[1]
        temp6 = right[2]

        right[0] = right[6]
        right[6] = right[8]
        right[8] = temp6
        right[2] = temp4
        right[1] = right[3]
        right[3] = right[7]
        right[7] = right[5]
        right[5] = temp5

    elif random_turn_option == 6:  # right turn inverted
        temp1 = front[2]
        temp2 = front[5]
        temp3 = front[8]

        front[2] = top[2]
        front[5] = top[5]
        front[8] = top[8]

        top[2] = back[2]
        top[5] = back[5]
        top[8] = back[8]

        back[2] = bottom[2]
        back[5] = bottom[5]
        back[8] = bottom[8]

        bottom[2] = temp1
        bottom[5] = temp2
        bottom[8] = temp3

        temp4 = right[0]
        temp5 = right[1]
        temp6 = right[2]

        right[0] = temp6
        right[2] = right[8]
        right[8] = right[6]
        right[6] = temp4
        right[1] = right[5]
        right[5] = right[7]
        right[7] = right[3]
        right[3] = temp5

    elif random_turn_option == 7:  # back turn
        temp1 = bottom[6]
        temp2 = bottom[7]
        temp3 = bottom[8]

        bottom[6] = left[0]
        bottom[7] = left[3]
        bottom[8] = left[6]

        left[0] = top[2]
        left[3] = top[1]
        left[6] = top[0]

        top[2] = right[8]
        top[1] = right[5]
        top[0] = right[2]

        right[8] = temp1
        right[5] = temp2
        right[2] = temp3

        temp4 = back[0]
        temp5 = back[1]
        temp6 = back[2]

        back[0] = back[6]
        back[6] = back[8]
        back[8] = temp6
        back[2] = temp4
        back[1] = back[3]
        back[3] = back[7]
        back[7] = back[5]
        back[5] = temp5

    elif random_turn_option == 8:  # back turn inverted
        temp1 = bottom[6]
        temp2 = bottom[7]
        temp3 = bottom[8]

        bottom[6] = right[8]
        bottom[7] = right[5]
        bottom[8] = right[2]

        right[8] = top[0]
        right[5] = top[1]
        right[2] = top[2]

        top[2] = left[0]
        top[1] = left[3]
        top[0] = left[6]

        left[0] = temp1
        left[3] = temp2
        left[6] = temp3

        temp4 = back[0]
        temp5 = back[1]
        temp6 = back[2]

        back[0] = temp6
        back[2] = back[8]
        back[8] = back[6]
        back[6] = temp4
        back[1] = back[5]
        back[5] = back[7]
        back[7] = back[3]
        back[3] = temp5

    elif random_turn_option == 9:  # top turn
        temp1 = front[0]
        temp2 = front[1]
        temp3 = front[2]

        front[0] = right[0]
        front[1] = right[1]
        front[2] = right[2]

        right[0] = back[8]
        right[1] = back[7]
        right[2] = back[6]

        back[8] = left[0]
        back[7] = left[1]
        back[6] = left[2]

        left[0] = temp1
        left[1] = temp2
        left[2] = temp3

        temp4 = top[0]
        temp5 = top[1]
        temp6 = top[2]

        top[0] = top[6]
        top[6] = top[8]
        top[8] = temp6
        top[1] = top[3]
        top[3] = top[7]
        top[7] = top[5]
        top[5] = temp5
        top[2] = temp4

    elif random_turn_option == 10:  # top turn inverted
        temp1 = front[0]
        temp2 = front[1]
        temp3 = front[2]

        front[0] = left[0]
        front[1] = left[1]
        front[2] = left[2]

        left[0] = back[8]
        left[1] = back[7]
        left[2] = back[6]

        back[8] = right[0]
        back[7] = right[1]
        back[6] = right[2]

        right[0] = temp1
        right[1] = temp2
        right[2] = temp3

        temp4 = top[0]
        temp5 = top[1]
        temp6 = top[2]

        top[0] = temp6
        top[2] = top[8]
        top[8] = top[6]
        top[6] = temp4
        top[1] = top[5]
        top[5] = top[7]
        top[3] = temp5
        top[7] = top[3]

    elif random_turn_option == 11:  # left turn
        temp1 = front[0]
        temp2 = front[3]
        temp3 = front[6]

        front[0] = top[0]
        front[3] = top[3]
        front[6] = top[6]

        top[0] = back[0]
        top[3] = back[3]
        top[6] = back[6]

        back[0] = bottom[0]
        back[3] = bottom[3]
        back[6] = bottom[6]

        bottom[0] = temp1
        bottom[3] = temp2
        bottom[6] = temp3

        temp4 = left[0]
        temp5 = left[1]
        temp6 = left[2]

        left[0] = left[6]
        left[6] = left[8]
        left[8] = temp6
        left[1] = left[3]
        left[3] = left[7]
        left[7] = left[5]
        left[5] = temp5
        left[2] = temp4

    elif random_turn_option == 12:  # left turn inverted
        temp1 = front[0]
        temp2 = front[3]
        temp3 = front[6]

        front[0] = bottom[0]
        front[3] = bottom[3]
        front[6] = bottom[6]

        bottom[0] = back[0]
        bottom[3] = back[3]
        bottom[6] = back[6]

        back[0] = top[0]
        back[3] = top[3]
        back[6] = top[6]

        top[0] = temp1
        top[3] = temp2
        top[6] = temp3

        temp4 = left[0]
        temp5 = left[1]
        temp6 = left[2]

        left[0] = temp6
        left[2] = left[8]
        left[8] = left[6]
        left[6] = temp4
        left[1] = left[5]
        left[5] = left[7]
        left[7] = left[3]
        left[3] = temp5

    print_cube()
    count += 1


