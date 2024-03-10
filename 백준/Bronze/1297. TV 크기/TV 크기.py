d, h, w = map(int, input().split())
divider = (h ** 2 + w ** 2) ** 0.5
print(int(d * h / divider), int(d * w / divider))