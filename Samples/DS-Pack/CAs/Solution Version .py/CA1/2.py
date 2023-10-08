status = 'found'
##to test :
#f = open('/usr/local/My Folders/University/3rd Term/Data Structure/Practices/CA1/test1.txt')
#nums = f.read()
##end test
n = int(input())
nums = input()
nums = nums.split()
nums = [int(num) for num in nums]
nums.sort()
nums_set = set(nums)

if len(nums_set) != len(nums) :
    print(-1)
    quit()

numsCopy = []
numsCopy = nums.copy()

maxIndex = len(numsCopy) - 1

def is_valid_ls(numsCopy) :
    if numsCopy[0] == (numsCopy[1] + numsCopy[maxIndex]) / 2 or numsCopy[maxIndex] == (numsCopy[maxIndex - 1] + numsCopy[0]) / 2 :
        return False

    for i in range(1, maxIndex) :
        if numsCopy[i] == (numsCopy[i - 1] + numsCopy[i + 1]) / 2 :
            return False

    return True

def make_valid_ls(numsCopy) :
    if numsCopy[0] == (numsCopy[1] + numsCopy[maxIndex]) / 2 :
        numsCopy[0], numsCopy[1] = numsCopy[1], numsCopy[0]

    if numsCopy[maxIndex] == (numsCopy[maxIndex - 1] + numsCopy[0]) / 2 :
        numsCopy[maxIndex], numsCopy[0] = numsCopy[maxIndex], numsCopy[0]

    for i in range(1, len(numsCopy) - 1) :
        if numsCopy[i] == (numsCopy[i - 1] + numsCopy[i + 1]) / 2 :
            numsCopy[i], numsCopy[i + 1] = numsCopy[i + 1], numsCopy[i]



while is_valid_ls(numsCopy) == False :
    make_valid_ls(numsCopy)
    if numsCopy == nums :
        status = 'Not found'
        break

if status == 'found' :
    for num in numsCopy :
        print(num, end = ' ')
    print()
else :
    print(-1)