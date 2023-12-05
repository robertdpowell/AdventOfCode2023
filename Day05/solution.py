input = open('input.txt').read()

def parse_input(input):
    sections = input.strip().split('\n\n')

    parsed_seeds = list(map(int, sections[0].split(":")[1].split()))

    parsed_seeds_to_soil = sections[1].split('\n')[1:]
    print (f'Now parsing seeds to soil')
    seed_to_soil_map = {}
    for line in parsed_seeds_to_soil:
        dest_start, src_start, length = map(int, line.split())
        for i in range(length):
            seed_to_soil_map[src_start + i] = dest_start + i

    parsed_soil_to_fertilizer = sections[2].split('\n')[1:]
    print(f'Now parsing soil to fertilizer')
    soil_to_fertilizer_map = {}
    for line in parsed_soil_to_fertilizer:
        dest_start, src_start, length = map(int, line.split())
        for i in range(length):
            soil_to_fertilizer_map[src_start + i] = dest_start + i

    parsed_fertilizer_to_water = sections[3].split('\n')[1:]
    print(f'Now parsing fertilizer to water')
    fertilizer_to_water_map = {}
    for line in parsed_fertilizer_to_water:
        dest_start, src_start, length = map(int, line.split())
        for i in range(length):
            fertilizer_to_water_map[src_start + i] = dest_start + i

    parsed_water_to_light = sections[4].split('\n')[1:]
    print(f'Now parsing water to light')
    water_to_light_map = {}
    for line in parsed_water_to_light:
        dest_start, src_start, length = map(int, line.split())
        for i in range(length):
            water_to_light_map[src_start + i] = dest_start + i

    parsed_light_to_temperature = sections[5].split('\n')[1:]
    print(f'Now parsing light to temperature')
    light_to_temperature_map = {}
    for line in parsed_light_to_temperature:
        dest_start, src_start, length = map(int, line.split())
        for i in range(length):
            light_to_temperature_map[src_start + i] = dest_start + i

    parsed_temperature_to_humidity = sections[6].split('\n')[1:]
    print(f'Now parsing temperature to humidity')
    temperature_to_humidity_map = {}
    for line in parsed_temperature_to_humidity:
        dest_start, src_start, length = map(int, line.split())
        for i in range(length):
            temperature_to_humidity_map[src_start + i] = dest_start + i

    parsed_humidity_to_location = sections[7].split('\n')[1:]
    print(f'Now parsing humidity to location')
    humidity_to_location_map = {}
    for line in parsed_humidity_to_location:
        dest_start, src_start, length = map(int, line.split())
        for i in range(length):
            humidity_to_location_map[src_start + i] = dest_start + i

    print (parsed_seeds, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map)

    return parsed_seeds, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map

def solve1():
    processed_seeds = []
    parsed_seeds, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map = parse_input(input)
    for seed in parsed_seeds:
        if seed in seed_to_soil_map:
            seed = seed_to_soil_map[seed]
        else:
            seed = seed
        if seed in soil_to_fertilizer_map:
            seed = soil_to_fertilizer_map[seed]
        else:
            seed = seed
        if seed in fertilizer_to_water_map:
            seed = fertilizer_to_water_map[seed]
        else:
            seed = seed
        if seed in water_to_light_map:
            seed = water_to_light_map[seed]
        else:
            seed = seed
        if seed in light_to_temperature_map:
            seed = light_to_temperature_map[seed]
        else:
            seed = seed
        if seed in temperature_to_humidity_map:
            seed = temperature_to_humidity_map[seed]
        else:
            seed = seed
        if seed in humidity_to_location_map:
            seed = humidity_to_location_map[seed]
        else:
            seed = seed

        processed_seeds.append(seed)
        print (f'Processed seed {seed}')

    return (min(processed_seeds))

print (f'The answer to part 1 is {solve1()}')
