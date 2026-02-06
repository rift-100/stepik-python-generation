def switch_to_10(num, system):
    digits = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]
    result = 0
    pow = len(str(num)) - 1
    for n in str(num).upper():
        result += digits.index(n) * system**pow
        pow -= 1
    return result


print(switch_to_10(111111, 2))
print(switch_to_10("1AF2", 16))

for i in range(2, 17):
    if switch_to_10(88, i) == switch_to_10(32, i) + switch_to_10(22, i) + switch_to_10(
        16, i
    ) + switch_to_10(17, i):
        print(i)
        break


def switch_from_10(num, system):
    digits = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]
    rest = ""
    while num >= system:
        rest = digits[num % system] + rest
        num //= system

    return str(num) + rest

print(switch_from_10(1000, 16))
print(switch_from_10(513, 2))
