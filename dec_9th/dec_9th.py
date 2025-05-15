import sys

sys.setrecursionlimit(100000)


# def get_checksum(filepath):
#     with open(filepath) as file:
#         for line in file:
#             file_layout = str(line)

#     return count_from_front(file_layout, 0, 0, 0)


# def count_from_front(file_layout, position, progress, checksum_total):
#     # count from the front of the file
#     # this part needs a clause to end the recursion

#     file_id = position / 2
#     file_size = int(file_layout[position])
    
#     new_checksum = (file_size * file_id) + (
#         file_size * (file_size - 1) * 0.5
#     )  # I think these sums are wrong
#     print(f"adding {new_checksum}")
#     checksum_total += new_checksum

#     if position == (len(file_layout) - 1):
#         print("count from front")
#         print(f"checksum: {checksum_total}, file layout: {file_layout}")
#         return checksum_total

#     else:
#         print("count from front")
#         print(f"checksum: {checksum_total}, file layout: {file_layout}")
#         return count_from_back(
#             file_layout, position + 1, progress + file_size, checksum_total
#         )


# def count_from_back(file_layout, position, progress, checksum_total):
#     # count from the back of the file
#     # de increment the last file as you go so it doesnt get used twice

#     if position == (len(file_layout) - 1):
#         return checksum_total

#     back_file_id = len(file_layout) / 2
#     back_file_size = int(file_layout[-1])
#     available_space = int(file_layout[position])

#     if available_space < back_file_size:
#         new_checksum = available_space * (back_file_id + (available_space - 1) * 0.5)
#         print(f"adding {new_checksum}")
#         checksum_total += new_checksum

#         new_file_layout = file_layout[:-1] + str(back_file_size - available_space)
#         print("count from back")
#         print(f"checksum: {checksum_total}, file layout: {new_file_layout}")

#         if position == (len(new_file_layout) - 1):
#             return checksum_total

#         else:
#             return count_from_front(
#                 new_file_layout,
#                 position + 1,
#                 progress + available_space,
#                 checksum_total,
#             )

#     elif available_space >= back_file_size:
#         new_checksum = back_file_size * (back_file_id + (back_file_size - 1) * 0.5)
#         print(f"adding {new_checksum}")
#         checksum_total += new_checksum

#         new_file_layout = file_layout[:-2]
#         print("count from back")
#         print(f"checksum: {checksum_total}, file layout: {new_file_layout}")

#         if position == (len(new_file_layout) - 1):
#             return checksum_total

#         else:

#             return count_from_back(
#                 new_file_layout, position, progress + back_file_size, checksum_total
#             )


def sort_files(filepath):
    with open(filepath) as file:
        for line in file:
            file_structure = str(line)

    return get_checksum(file_structure, 0, 0, 0)

def get_checksum(file_structure, index, position, checksum):
    if index % 2 == 0:
        file_structure, index, position, checksum = count_from_front(file_structure, index, position, checksum)
        
    elif index%2 ==1:
        file_structure, index, position, checksum = count_from_back(file_structure, index, position, checksum)
    
    if index == len(file_structure) -1:
        return checksum
    else: 
        return get_checksum(file_structure, index+1, position, checksum)

def count_from_front(file_structure, index, position, checksum):
    file_size = int(file_structure[index])
    file_id = index/2
    for i in range(file_size):
        checksum+= file_id * position
        position += 1
    
    return (file_structure, index, position, checksum)

def count_from_back(file_structure, index, position, checksum):
    available_space = int(file_structure[index])
    back_file_size = int(file_structure[-1])
    back_file_id = (len(file_structure)-1)/2

    if available_space < back_file_size:
        file_structure = file_structure[:-1] + str(back_file_size-available_space)
        for i in range(available_space):
            checksum += back_file_id * position
            position += 1
        
        return (file_structure, index, position, checksum)

    else:
        file_structure = file_structure[:index] + str(available_space-back_file_size) + file_structure[index+1:-2]
        for i in range(back_file_size):
            checksum += back_file_id * position
            position += 1
        
        if available_space > back_file_size:
            return count_from_back(file_structure, index, position, checksum)
        else:
            return (file_structure, index, position, checksum)
        




if __name__ == "__main__":
    print(sort_files("dec_9th/input_1.txt"))
