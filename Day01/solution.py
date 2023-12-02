import re


def solve1():
    digits = []
    with open("input.py") as f:
        for line in f.readlines():
            firstdigit = re.search(r'\d', line)
            lastdigit = re.search(r'\d', line[::-1])
            if firstdigit and lastdigit:
                combined = firstdigit.group() + lastdigit.group()
                digits.append(int(combined))
        total = sum(digits)
        return total

print (f'Solution 1 answer is {solve1()}')
def solve2():
    converted_digits = []
    number_words = {
        "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4",
        "five": "f5e", "six": "s6", "seven": "s7n", "eight": "e8t", "nine": "n9e"
    }
    with open("input.py") as f:
        for line in f.readlines():
            for word, digit in number_words.items():
                line = line.replace(word, digit)
            firstdigit = re.search(r'\d', line)
            lastdigit = re.search(r'\d', line[::-1])
            combined = firstdigit.group() + lastdigit.group()
            converted_digits.append(int(combined))
        convertedtotal = sum(converted_digits)
        return convertedtotal

print(f'Solution 2 answer is {solve2()}')





