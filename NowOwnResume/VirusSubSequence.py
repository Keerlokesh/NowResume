virus = input()
n = int(input())
res = []

for k in range(n):
    blood = input()
    res = [virus[i: j] for i in range(len(virus))
		for j in range(i + 1, len(virus) + 1)]


    if blood in res:
        print("POSITIVE")
    else:
        print("NEGATIVE")

print(res)
