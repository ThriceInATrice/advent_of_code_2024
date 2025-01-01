from pprint import pprint


def get_antinode_count(filepath):
    with open(filepath) as file:
        line_data = [line for line in file]

    antena_list = get_antenas(line_data)

    antena_pairs = get_antena_pairs(antena_list)

    antinodes = get_antinodes(antena_pairs, len(line_data))

    return len(antinodes)


def get_antenas(line_data):
    acceptable_symbol_codes = (
        [i for i in range(48, 58)]
        + [i for i in range(65, 91)]
        + [i for i in range(97, 123)]
    )

    antenas = [
        coord_list
        for coord_list in [
            [
                (y, x)
                for y in range(len(line_data))
                for x in range(len(line_data[y]))
                if line_data[y][x] == chr(ascii_code)
            ]
            for ascii_code in acceptable_symbol_codes
        ]
        if coord_list != []
    ]

    return antenas


def get_antena_pairs(antena_list):
    antena_pairs = [
        (coord_1, coord_2)
        for coords in antena_list
        for coord_1 in coords
        for coord_2 in coords
        if coord_1 != coord_2
    ]

    return antena_pairs


def get_antinodes(antena_pairs, grid_size):
    antinodes = [
        (2 * pair[0][0] - pair[1][0], 2 * pair[0][1] - pair[1][1])
        for pair in antena_pairs
        if 0 <= (2 * pair[0][0] - pair[1][0]) < grid_size
        and 0 <= (2 * pair[0][1] - pair[1][1]) < grid_size
    ]

    return set(antinodes)


def get_harmonic_antinode_count(filepath):
    with open(filepath) as file:
        line_data = [line for line in file]

    antena_list = get_antenas(line_data)
    # print(f"anena list: {antena_list}")

    antena_pairs = get_antena_pairs(antena_list)
    # print(f"antena pairs: {antena_pairs}")
    
    harmonic_antinodes = get_harmonic_antinodes(antena_pairs, len(line_data))
    # print(f"harmonic antinodes: {harmonic_antinodes}")

    return len(harmonic_antinodes)


def get_harmonic_antinodes(antena_pairs, grid_size):
    antinodes = []
    
    for pair in antena_pairs:
        antinodes += [pair[0], pair[1]]
        within_grid = True
        while within_grid:
            new_node = (2* antinodes[-1][0] - antinodes[-2][0], 2* antinodes[-1][1] - antinodes[-2][1])
            if 0 <= new_node[0] < grid_size and 0 <= new_node[1] < grid_size:
                antinodes.append(new_node)
            else:
                within_grid = False
            
    return set(antinodes)


if __name__ == "__main__":
    pprint(f"antinode count: {get_antinode_count('dec_8th/input_1.txt')}")
    pprint(
        f"harmonic antinode count: {get_harmonic_antinode_count('dec_8th/input_1.txt')}"
    )
