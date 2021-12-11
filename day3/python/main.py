import time

CRITERIA_LESS_COMMON_BIT = 1

CRITERIA_MOST_COMMON_BIT = 0


def readfile(filepath):
    fileObj = open(filepath, "r")
    measurements = fileObj.read().splitlines()
    fileObj.close()
    return measurements


def process_bits(report):
    results = []
    for bit in report[0]:
        results.append([0, 0])

    for report_line in report:
        for i in range(0, len(report_line)):
            bit = report_line[i]
            if bit == '0':
                results[i][0] = results[i][0] + 1
            else:
                results[i][1] = results[i][1] + 1

    return results


def calculate_gamma_and_epsilon(file):
    report = readfile(file)
    bits_processed = process_bits(report)

    gamma_rate = ''
    epsilon_rate = ''

    for i in range(0, len(bits_processed)):
        result = bits_processed[i]
        more_common_bit = '0' if result[0] > result[1] else '1'
        less_common_bit = '1' if result[0] > result[1] else '0'

        gamma_rate = gamma_rate + more_common_bit
        epsilon_rate = epsilon_rate + less_common_bit

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_oxygen_and_co2_rating(file):
    report = readfile(file)
    oxigen = int(calculate_individual_rating(report, CRITERIA_MOST_COMMON_BIT, 0), 2)
    co2 = int(calculate_individual_rating(report, CRITERIA_LESS_COMMON_BIT, 0), 2)

    return oxigen * co2


def calculate_individual_rating(data, criteria, index):
    if len(data) == 1:
        return data[0]

    bits_processed = process_bits(data)
    common_bit = ('0' if bits_processed[index][0] > bits_processed[index][1] else '1') if criteria == CRITERIA_MOST_COMMON_BIT else (
        '1' if bits_processed[index][0] > bits_processed[index][1] else '0')

    data_filtered = list(filter(lambda report_line: report_line[index] == common_bit, data))
    index += 1

    return calculate_individual_rating(data_filtered, criteria, index)


## Asserts
assert calculate_gamma_and_epsilon("../inputs/input_test.txt") == 198
assert calculate_oxygen_and_co2_rating("../inputs/input_test.txt") == 230


start_time = time.time()
print("- Part one: " + str(calculate_gamma_and_epsilon("../inputs/input.txt")) + " [%s seconds]" % (
        time.time() - start_time))

start_time = time.time()
print("- Part one: " + str(calculate_oxygen_and_co2_rating("../inputs/input.txt")) + " [%s seconds]" % (time.time() - start_time))
