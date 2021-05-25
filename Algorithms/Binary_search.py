array_1 = [1, -6, 17, 29, 105, -30, 0 , -1000, 24, 220]

mid = len(array_1)
low = 0
high = len(array_1) - 1

while array_1[mid] != value and low <= high:
    if value > array_1[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID = ", mid)
