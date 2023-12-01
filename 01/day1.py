import numpy as np 
import re

## part 1
def cal_values(codes):
    calibration_values = []
    for code in codes:
        num = ""
        for e in code:
            if e.isdigit():
                num += e
        calibration_values.append(int(num[0]+num[-1]))
    return calibration_values

## part 2
def read_numbers(codes):
    numbers = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    exp = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d+))'
    calibration_values = []
    for code in codes:
        num_str = ""
        split = re.findall(exp, code)
        # print(split)
        for s in split:
            if s in numbers.keys():
                num_str += numbers[s]
            elif s.isdigit():
                num_str += s
        # print(num_str, int(num_str[0]+num_str[-1]))
        calibration_values.append(int(num_str[0]+num_str[-1]))
    return np.sum(calibration_values)

## main  
with open("input.txt", "r") as f:
    txt = f.read()

codes = txt.split()
calibration_values = read_numbers(codes)
print(calibration_values)