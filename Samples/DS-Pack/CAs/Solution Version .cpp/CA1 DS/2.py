def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


n = int(input())
nums = [int(i) for i in input().split()]

insertionSort(nums)

b = [None]*(2*n)
for i, j in zip(range(0, 2*n, 2), range(n)):
    b[i] = nums[j]
for i, j in zip(range(1, 2*n, 2), range(n, 2*n)):
    b[i] = nums[j]

print(*b, sep=" ")
