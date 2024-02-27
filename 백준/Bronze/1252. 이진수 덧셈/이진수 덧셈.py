bin_a, bin_b = input().split()
a, b = int(bin_a, 2), int(bin_b, 2)
print(bin(a + b).replace('0b', ''))