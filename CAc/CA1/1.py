inp = input()

dict = {(bin(i)[2:]).zfill(10): 0 for i in range(1024)}
dict_alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

# print(dict)

sum_of_goods = 0
last_seen = '0000000000'

for char in inp:
    if last_seen[dict_alphabet[char]] == '0':
        new_seen = last_seen[:dict_alphabet[char]] + '1' + last_seen[dict_alphabet[char] + 1:]

        if new_seen.count('1') <= 1:
            sum_of_goods += 1
        sum_of_goods += dict[new_seen]

        for index in range(10):
            if new_seen[index] == '0':
                ss = new_seen[:index] + '1' + new_seen[index + 1:]

            else:
                ss = new_seen[:index] + '0' + new_seen[index + 1:]
            sum_of_goods += dict[ss]
        # print(new_seen)
    else:
        new_seen = last_seen[:dict_alphabet[char]] + '0' + last_seen[dict_alphabet[char] + 1:]

        if new_seen.count('1') <= 1:
            sum_of_goods += 1
        sum_of_goods += dict[new_seen]

        for index in range(10):
            if new_seen[index] == '0':
                ss = new_seen[:index] + '1' + new_seen[index + 1:]

            else:
                ss = new_seen[:index] + '0' + new_seen[index + 1:]
            sum_of_goods += dict[ss]

    dict[new_seen] += 1
    # print(new_seen)
    last_seen = new_seen

print(sum_of_goods)




