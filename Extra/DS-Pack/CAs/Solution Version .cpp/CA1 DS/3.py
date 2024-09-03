def reversedGetNextZeroIndex(li: list):
    for n in range(len(li) - 1, -1, -1):
        if li[n] == "0": yield n

total = int(input())

for _ in range(total):
    pair = [int(i) for i in input().split()]

    rhsBinary = bin(pair[1])[2:]
    if rhsBinary.find("0") == -1:
        print(pair[1])
        continue

    biggest2sPowerInRange = 2 ** (len(rhsBinary) - 1) - 1
    if biggest2sPowerInRange > pair[0]:
        print(biggest2sPowerInRange)
        continue

    base2 = list(bin(pair[0])[2:].zfill(len(rhsBinary)))

    mostOnes = base2.copy()
    for n in reversedGetNextZeroIndex(base2):
        base2[n] = "1"
        if int("".join(base2), 2) > pair[1]: break
        mostOnes = base2.copy()

    print(int("".join(mostOnes), 2))
