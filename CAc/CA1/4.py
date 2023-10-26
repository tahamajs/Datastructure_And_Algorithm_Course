
word = input()

# flag = 'NO'


def is_good(ints):
    if len(ints) <= 3:
        # flag = 'NO'
        return 'NO'
    for i in range(len(ints)):
        for j in range(i+1,len(ints)):
            num1 = int(ints[:i+1])
            num2 = int(ints[i+1:j+1])
            if ints[:i+1] [0] == '0' or ints[i+1:j+1][0] == '0':
                continue

            # print(num1,num2)
            numbers = [num1,num2]
            while True:
                next_num = numbers[-1] + numbers[-2]
                next_num_str = str(next_num)
                if ints.startswith(next_num_str,j+1):

                    
                    j += len(next_num_str)
                    numbers.append(next_num)
                else:
                    # print(j,i)
                    break

            if j == len(ints)-1 and len(numbers) >= 3 and i < (j//2) :
                return 'YES'
            # if i > len(ints)//2 :

    return "NO"



print(is_good(word))