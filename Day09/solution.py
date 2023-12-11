input = open('input.txt').read()



def solve1():
    total_sum = 0

    for line in input.split('\n'):
        history = [int(x) for x in line.split()]
        history_diff = []
        history_breakdowns = []
        all_history_breakdowns = []
        history_breakdowns.append(history)

        while True:
            history_diff = [history [i+1] - history[i] for i in range(len(history)-1)]
            history_breakdowns.append(history_diff)

            if all (x == 0 for x in history_diff):
                break

            history = history_diff

        for i in range (len(history_breakdowns)):
            sum_of_final_digits = sum(breakdown[-1] for breakdown in history_breakdowns[i:] if breakdown)
            history_breakdowns[i].append(sum_of_final_digits)

        total_sum += history_breakdowns[0][-1]
    return total_sum

def solve2():
    total_sum = 0

    for line in input.split('\n'):
        history = [int(x) for x in line.split()]
        history_diff = []
        history_breakdowns = []
        all_history_breakdowns = []
        history_breakdowns.append(history)

        while True:
            history_diff = [history [i+1] - history[i] for i in range(len(history)-1)]
            history_breakdowns.append(history_diff)

            if all (x == 0 for x in history_diff):
                break

            history = history_diff

        for i in range (len(history_breakdowns)):
            sum_of_first_digits = sum(breakdown[0] for breakdown in history_breakdowns[i+1:] if breakdown)
            print(f'sum of first digits is {sum_of_first_digits} because {history_breakdowns[i:]}')
            history_breakdowns[i].insert(0,sum_of_first_digits)

        total_sum += history_breakdowns[0][0]
    return total_sum


print (f'solution 1 answer is {solve1()}')
print (f'solution 2 answer is {solve2()}')


