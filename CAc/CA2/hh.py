from itertools import groupby

def max_consecutive_zeros(lst):
    zero_counts = [len(list(group)) for key, group in groupby(lst) if key == 0]
    return max(zero_counts, default=0)

# Example usage
my_list = [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
result_zeros = max_consecutive_zeros(my_list)
print("Max Consecutive Zeros:", result_zeros)
