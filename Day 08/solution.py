input = open('input.txt').read()
lines = input.split('\n')
instructions = list(lines[0])
steps_to_zzz = []

nodes = []
def solve1():
    for line in lines[2:]:
        location = line.split('=')[0].strip()
        left = line.split('(')[1].split(',')[0].strip()
        right = line.split(')')[0].split(',')[1].strip()
        nodes.append((location, left, right))

    current_position = 'AAA'
    while current_position != 'ZZZ':
        for instruction in instructions:
            if instruction == 'R':
                for node in nodes:
                    if node[0] == current_position:
                        current_position = node[2]
                        steps_to_zzz.append(node)
                        break

            elif instruction == 'L':
                for node in nodes:
                    if node[0] == current_position:
                        current_position = node[1]
                        steps_to_zzz.append(node)
                        break
    return len(steps_to_zzz)


def solve2():
    for line in lines[2:]:
        location = line.split('=')[0].strip()[-1]
        left = line.split('(')[1].split(',')[0].strip()
        right = line.split(')')[0].split(',')[1].strip()
        nodes.append((location, left, right))
    print (nodes)

    cycle_lengths = []
    for start_node in nodes:
        if start_node[0] == 'A':
            cycles = 0
            current_position = start_node[0]

            while current_position[0] != 'Z':
                for instruction in instructions:
                    if instruction == 'R':
                        for node in nodes:
                            if node[0] == current_position:
                                current_position = node[2]
                                cycles += 1
                                print (cycles)
                                break

                    elif instruction == 'L':
                        for node in nodes:
                            if node[0] == current_position:
                                current_position = node[1]
                                cycles += 1
                                print(cycles)
                                break
        cycle_lengths.append(cycles)
    print (cycle_lengths)
solve2()
# print (f'solution 1 answer is {solve1()}')