n = int(input())
extension = {}
for _ in range(n):
    line = input().split('.')
    extension_name = line[-1]
    if extension_name not in extension:
        extension[extension_name] = 1
    else:
        extension[extension_name] += 1
result = sorted(extension.items())
for item in result:
    print(*item)