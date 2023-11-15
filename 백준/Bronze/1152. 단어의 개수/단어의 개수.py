a = input()
if a == " ":
    print(0)
else:
    print(len(a.strip().split(" ")))