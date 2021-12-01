import time


def readfile(filepath):
    fileObj = open(filepath, "r")
    measurements = list(map(get_measurement_value,fileObj.read().splitlines()))
    fileObj.close()
    return measurements


def check_part_one(file):
    measurements = readfile(file)
    total = 0
    before = measurements[0]
    for i in range(len(measurements)):
        current = measurements[i]
        res = current - before
        if res > 0:
            total = total + 1
        before = current

    return total


def get_measurement_value(measurement):
    return int(measurement.split()[0])


def check_part_two(file):
    measurements = readfile(file)
    total = 0
    before = measurements[0] + measurements[1] + measurements[2]
    for i in range(len(measurements) - 2):
        current = measurements[i] + measurements[i + 1] + measurements[i + 2]

        res = current - before
        if res > 0:
            total = total + 1
        before = current

    return total


## Asserts
assert check_part_one("../inputs/input1_test.txt") == 7
assert check_part_two("../inputs/input2_test.txt") == 5

start_time = time.time()
print("- Part one: " + str(check_part_one("../inputs/input1.txt")) + " [%s seconds]" % (time.time() - start_time))

start_time = time.time()
print("- Part two: " + str(check_part_two("../inputs/input2.txt")) + " [%s seconds]" % (time.time() - start_time))
