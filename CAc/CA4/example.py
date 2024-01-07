for i in range(3):
    for j in range(i):
        print(j, i)



def reverse_interval(arr, start, end):
    return arr[:start] + arr[start:end + 1][::-1] + arr[end + 1:]


print(reverse_interval("aaaafffttt" , 0, 5))