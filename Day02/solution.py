def solve1():
    lines = open('input.py').read().split('\n')
    invalid_games = set()
    gamesum = 0
    for line in lines:
        parts = line.split(':')
        game = parts[0]
        gameID = int(game[4:])
        gamesum += gameID
        hands = parts[1].split(';')

        for hand in hands:
            turns = hand.split(',')
            for turn in turns:
                turn = turn.strip()
                turn_parts = turn.split(' ')
                colour = turn_parts[1]
                count = int(turn_parts[0])
                if (colour == 'red' and count > 12) or (colour == 'green' and count > 13) or (colour == 'blue' and count > 14):
                    invalid_games.add(gameID)
                    break
    solution = gamesum - sum(invalid_games)
    return (solution)

def solve2():
    powersum = 0
    lines = open('input.py').read().split('\n')
    for line in lines:
        bluelist = []
        redlist = []
        greenlist = []
        parts = line.split(':')
        hands = parts[1].split(';')

        for hand in hands:
            turns = hand.split(',')
            for turn in turns:
                turn = turn.strip()
                turn_parts = turn.split(' ')
                colour = turn_parts[1]
                count = int(turn_parts[0])
                if colour == 'red':
                    redlist.append(count)
                elif colour == 'green':
                    greenlist.append(count)
                elif colour == 'blue':
                    bluelist.append(count)
        maxred = max(redlist)
        maxgreen = max(greenlist)
        maxblue = max(bluelist)
        power = maxred * maxgreen * maxblue
        powersum += power
    return powersum


print (f'Solution 1 answer is {solve1()}')
print (f'Solution 1 answer is {solve2()}')
