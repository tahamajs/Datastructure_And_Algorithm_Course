from itertools import groupby


def max_consecutive_zeros(lst):
    zero_counts = [len(list(group)) for key, group in groupby(lst) if key == 0]
    return max(zero_counts, default=0)



n, b = map(int,input().split())

masir = list(map(int,input().split()))

massir_0_1_dict = {i:1 for i in range(n)}




index_mapping_from_sort_to_normal = sorted(range(len(masir)), key=lambda x: masir[x], reverse=True)
index_mapping_from_reversed_sort_to_normal = {reversed_sorted_index: original_index for original_index, reversed_sorted_index in enumerate(index_mapping_from_sort_to_normal)}

sorted_masir = sorted(masir,reverse=True)


shows = []

for i in range(b):
    tmp = tuple(map(int,input().split()))
    shows.append(tmp)
    


soret_shoes = sorted(shows,reverse=True)

reversed_sorted_indexes = [i for i, _ in sorted(enumerate(shows), key=lambda x: x[1], reverse=True)]

index_mapping_from_reversed_sort_to_normal = {reversed_sorted_index: original_index for original_index, reversed_sorted_index in enumerate(reversed_sorted_indexes)}


shows_0_1_dict = {i:1 for i in range(n)}




last_indeex_of_sort_array_masir = 0 


for index , li in enumerate(soret_shoes):
    for j in range(last_indeex_of_sort_array_masir,n):
        if sorted_masir[j] > li[0] :
            massir_0_1_dict[index_mapping_from_sort_to_normal[j]] = 0
            last_indeex_of_sort_array_masir += 1
        else:
            break
    shows_0_1_dict[index_mapping_from_reversed_sort_to_normal[index]] = int(max_consecutive_zeros([massir_0_1_dict[i] for i in range(n)]) < li[1])


for i in range(b):
    print(shows_0_1_dict[i])












