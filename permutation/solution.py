
def permute3(i, n):
	if i == n:
		tpl = tuple(result)
		if tpl in s:
			return
		s.add(tpl)
		print(r)
		return
	
	for j in range(n):
		if taken[j]:
			continue
		taken[j] = True
		result[i] = ara[j]
		permute3(i+1, n)
		taken[j] = False

def permute4(l, r):
	if l == r:
		print(ara)
		return
	
	for i in range(l, r+1):
		if ara[i] in ara[l:i]:
			continue
		ara[l], ara[i] = ara[i], ara[l]
		permute4(l+1, r)
		ara[l], ara[i] = ara[i], ara[l]

def permute1(i, n):
	if i == n:
		print(result)
		return
	for j in range(n):
		if taken[j]:
			continue
		result[i] = ara[j]
		taken[j] = True
		permute1(i+1, n)
		taken[j] = False

def permute2(i, n):
	if i == n:
		print(ara)
		return

	for j in range(i, n):
		ara[i], ara[j] = ara[j], ara[i]
		permute2(i+1, n)
		ara[i], ara[j] = ara[j], ara[i]

if __name__ == "__main__":
	ara = [1, 2, 3, 4]
	n = len(ara)
	# result = [0] * n
	# taken = [False] * n
	permute2(0, len(ara))