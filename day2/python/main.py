import time


def readfile(filepath):
    fileObj = open(filepath, "r")
    measurements = fileObj.read().splitlines()
    fileObj.close()
    return measurements


def calculate_horizontal_position_and_depth(file):
    commands = readfile(file)
    horizontal = 0
    depth = 0
    for command in commands:
        command_parts = command.split(' ')
        action = command_parts[0]
        units = int(command_parts[1])
        if action == 'down':
            depth = depth + units
        if action == 'up':
            depth = depth - units
        if action == 'forward':
            horizontal = horizontal + units

    return horizontal * depth


def calculate_aim_horizontal_position_and_depth(file):
    commands = readfile(file)
    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        command_parts = command.split(' ')
        action = command_parts[0]
        units = int(command_parts[1])
        if action == 'down':
            aim = aim + units
        if action == 'up':
            aim = aim - units
        if action == 'forward':
            horizontal = horizontal + units
            depth = depth + (aim * units)

    return horizontal * depth


## Asserts
assert calculate_horizontal_position_and_depth("../inputs/input_test.txt") == 150
assert calculate_aim_horizontal_position_and_depth("../inputs/input_test.txt") == 900


start_time = time.time()
print("- Part one: " + str(calculate_horizontal_position_and_depth("../inputs/input1.txt")) + " [%s seconds]" % (time.time() - start_time))

start_time = time.time()
print("- Part one: " + str(calculate_aim_horizontal_position_and_depth("../inputs/input2.txt")) + " [%s seconds]" % (time.time() - start_time))