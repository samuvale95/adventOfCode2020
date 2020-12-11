from collections import Counter

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f]

def part_one(jolts_output):
    diff_1,diff_3 = 0,0

    for index in range(1, len(jolts_output)):
        diff=jolts_output[index]-jolts_output[index-1]
        if(diff==1): diff_1+=1
        elif(diff==3): diff_3+=1

    print(diff_1*diff_3)

def part_two():
    with open("in.txt", "r") as fp:
        lines = [int(line.rstrip()) for line in fp.readlines()]

    jolts = sorted(lines)
    jolts.append(jolts[-1] + 3)

    dp = Counter()
    dp[0] = 1

    for jolt in jolts:
        dp[jolt] = dp[jolt - 1] + dp[jolt - 2] + dp[jolt - 3]

    print(dp[jolts[-1]])

if __name__ == "__main__":
    jolts_output = sorted(read_input('in.txt'))
    jolts_output.insert(0,0)
    jolts_output.append(jolts_output[-1]+3)

    part_one(jolts_output)
    part_two()