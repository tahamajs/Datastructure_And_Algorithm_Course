
input_word = input()


max_length = 0
start_index = 0
current_length = 0
last_seen = {}

for index, char in enumerate(input_word):

    if char in last_seen and last_seen[char] >= start_index :
        start_index = last_seen[char] + 1
        current_length = index - start_index +1
    else:
        current_length += 1

    last_seen[char] = index
    if current_length > max_length:
        max_length = current_length

print(max_length)

