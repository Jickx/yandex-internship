arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
print(' '.join([str(i) for i in range(max(max(arr1), max(arr2)) + 1) if i in arr1 and i in arr2]))
