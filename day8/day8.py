# uri: https://adventofcode.com/2021/day/8
from base import get_input

file_path = get_input(8, ".txt")

INPUT = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce"""

INPUT = INPUT.replace("|\n", "| ")

##
# INPUT = file_path.read_text()
lines = INPUT.splitlines()

# count = 0
# for line in lines:
#     input, output = line.split(" | ")
#
#     input_blocks = [b for b in output.split()]
#
#     for block in input_blocks:
#         if len(block) in {2,3,4,7}:
#             count += 1

# print(f"part 1 {count=}")


# part 2


for line in lines + lines:
    digit = {}
    input, output = line.split(" | ")
    input_blocks = [set(b) for b in input.split()]

    # use the input to determine the digits
    for block in 3 * input_blocks:
        if block in digit.values():
            pass

        elif len(block) == 2:
            digit[1] = block
        elif len(block) == 4:
            digit[4] = block
        elif len(block) == 3:
            digit[7] = block
        elif len(block) == 7:
            digit[8] = block
        elif len(block) == 5:
            # check if it is either 2, 5 or 3.
            # 2 and 4 lights up 7
            # 3 and 7 lights up 6
            # other is 5
            if 2 not in digit and 4 in digit and len(block | digit[4]) == 7:
                digit[2] = block
            elif 5 not in digit and 7 in digit and len(block | digit[7]) == 6:
                digit[5] = block
            elif 3 not in digit and 2 in digit and 5 in digit:
                digit[3] = block
        elif len(block) == 6:
            # check if it is either 2, 5 or 3.
            # 6 and 1 light up 7
            # 0 and 5 light up 7
            # other is 9
            if 6 not in digit and 1 in digit and len(block | digit[1]) == 7:
                digit[6] = block
            elif 0 not in digit and 5 in digit and len(block | digit[5]) == 7:
                digit[0] = block
            elif 9 not in digit and 6 in digit and 0 in digit:
                digit[9] = block

    # # inverse the lookup of the digits for each line
    # if len(digit) != 10:
    #     raise ValueError(f"Not enough values in digit - saw {len(digit)}: {digit}")


    def lookup_digit(block: set) -> int:
        """Return the actual digit from digit when the blocks match."""
        n = [k for k, v in digit.items() if v == block]
        return n[0]


    # use the output to calculation the number
    output_blocks = [set(b) for b in output.split()]
    number = []

    for i,v in enumerate(output_blocks):
        d = lookup_digit(v)
        number.append(d * 10**i)

    print(f"{sum(number)=}")
pass
