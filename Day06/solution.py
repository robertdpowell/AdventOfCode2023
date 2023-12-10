lines = open('input.txt').read().split('\n')

def solve1(input):
    race_data = {}
    summary_ways_to_win = []
    race_times = [int(s) for s in lines[0].split() if s.isdigit()]
    race_records = [int(s) for s in lines[1].split() if s.isdigit()]
    for i in range(len(race_times)):
        race_data[race_times[i]] = race_records[i]

    for race_time, race_record in race_data.items():
        ways_to_win = 0
        for i in range (0, race_time):
            pressing_time = i
            duration = race_time - pressing_time
            distance = duration * pressing_time
            if distance > race_record:
                ways_to_win += 1
        summary_ways_to_win.append(ways_to_win)
    product = 1
    for ways_to_win in summary_ways_to_win:
        product *= ways_to_win

    return product

def solve2(input):
    combined_race_data = {}
    race_times = [int(s) for s in lines[0].split() if s.isdigit()]
    race_records = [int(s) for s in lines[1].split() if s.isdigit()]

    for i in range(len(race_times)):
        combined_race_data[race_times[i]] = race_records[i]

    concatenated_time = int(''.join(str(time) for time in race_times))
    concatenated_record = int (''.join(str(record) for record in race_records))

    ways_to_win = 0
    for i in range (0, concatenated_time):
        pressing_time = i
        duration = concatenated_time - pressing_time
        distance = duration * pressing_time
        if distance > concatenated_record:
            ways_to_win += 1
    return ways_to_win

print (f'solution 1 answer is {solve1(input)}')
print (f'solution 2 answer is {solve2(input)}')



