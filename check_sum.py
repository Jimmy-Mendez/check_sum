f = open("sets.csv", "r")
all_numbers = []
for x in f:
    tmp = [float(x) for x in x.split(',')]
    all_numbers.extend(tmp)

# Since there are 12 numbers in total and we need 3 sets of 4 numbers each,
# we look for combinations of 4 numbers from all_numbers that sum to 100.
from itertools import combinations

# Function to find all unique combinations that sum up to 100, considering all numbers
def find_combinations_sum_to_100(numbers):
    valid_combinations = []
    for combo in combinations(numbers, 4):
        if round(sum(combo), 2) == 100.00:
            valid_combinations.append(combo)
    
    # Filter out combinations to ensure each number is used exactly once
    final_sets = []
    used_indices = set()
    for combo in valid_combinations:
        if all(numbers.index(x) not in used_indices for x in combo):
            final_sets.append(combo)
            used_indices.update(numbers.index(x) for x in combo)
            if len(used_indices) == len(numbers):
                break

    return final_sets

# Finding valid combinations
valid_sets = find_combinations_sum_to_100(all_numbers)
print(valid_sets)
