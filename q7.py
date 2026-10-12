arr = list(map(int, input("Enter elements: ").split()))

result = []

for x in arr:
    if x != 0:
        result.append(x)

zeros = len(arr) - len(result)
result.extend([0] * zeros)

print("Array after moving zeros:", result)