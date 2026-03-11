w1 = input()
n = int(input())
w2 = input()

slice_a = w1[:n]
slice_b = w1[n+1:]

result = slice_a + w2 + slice_b
print(result)
