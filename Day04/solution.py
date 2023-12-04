lines = open('input.txt').read().split('\n')
total_sum = 0
def parseCard(line):
    sides = line.split(' | ')

    #extract the winning numbers slicing out the card number and convert to int
    winning_nums = sides[0].split(':', 1)[1].strip()
    winning_nums = list(map (int, winning_nums.split()))

    #extract the losing numbers and convert to int
    your_nums = sides[1].strip()
    your_nums = list(map (int, your_nums.split()))

    return winning_nums, your_nums

def solve1():
    total_sum = 0
    for line in lines:
        winning_nums, your_nums = parseCard(line)
        power = 0
        for i in winning_nums:
            for j in your_nums:
                if i == j:
                    power +=1
        if power == 0:
            cardscore = 0
        else:
            cardscore = 1 * 2 ** (power -1)
        total_sum += cardscore

    return (total_sum)

def solve2():
    cards_queue = []
    original_cards = len(lines)
    processed_cards = original_cards
    for line in lines:
        cards_queue.append(line)

    while cards_queue:
        current_line = cards_queue.pop(0) #FIFO queue pop the first element in the list and assign it to current_line
        winning_nums, your_nums = parseCard(current_line)
        winning_set = set(winning_nums)
        your_set = set(your_nums)
        matches = winning_set.intersection(your_set)

        current_index = lines.index(current_line)

        for i in  range(len(matches)):
            next_card_index = current_index + i + 1
            if next_card_index < original_cards:
                cards_queue.append(lines[next_card_index])
                processed_cards += 1
                print (f'Adding card {next_card_index} to queue')
    print (f'Processed {processed_cards} cards')
# print (f'The answer to part 1 is {solve1()}')
solve2()
