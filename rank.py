import sys

# def swap(arr, i, j):
# 	k = arr[i]
# 	arr[i] = arr[j]
# 	arr[j] = k


# def sort(arr, start, end):
# 	length = end - start + 1
# 	if length == 1 or length == 0:
# 		return
# 	if length == 2:
# 		if compare(arr[start], arr[end]):
# 			swap(arr, start, end)
# 		return
# 	# otherwise, pick a pivot and start (left hand point by convention)
# 	pivot = arr[start]
# 	left = start + 1
# 	right = end

# 	# sort based on the pivot
# 	while left <= right:
# 		if compare(arr[right], pivot):
# 			right -= 1
# 			continue
# 		if compare(pivot, arr[left]):
# 			left += 1
# 			continue
# 		swap(arr, left, right)
# 		left -= 1
# 		right -= 1

# 	# put pivot in the middle
# 	swap(arr, start, right)

# 	# sort left and right sub arrays
# 	sort(arr, start, right - 1)
# 	sort(arr, right + 1, end)

# given two sorted lists, return a new list of all sorted elements
def merge(a, b):
	c = []
	i = 0
	j = 0
	while i < len(a) and j < len(b):
		if not compare(a[i], b[j]):
			c.append(a[i])
			i += 1
		else:
			c.append(b[j])
			j += 1
	while i < len(a):
		c.append(a[i])
		i += 1
	while j < len(b):
		c.append(b[j])
		j += 1
	return c 

def mergesort(arr):
	if len(arr) == 1 or len(arr) == 0:
		return arr
	if len(arr) == 2:
		if compare(arr[0], arr[1]):
			return [arr[1], arr[0]]
		else:
			return arr
	mid = len(arr) // 2
	a = mergesort(arr[:mid])
	b = mergesort(arr[mid:])
	return merge(a, b)


# true if a >= b, false otherwise
def compare(a, b):
	print(f"Which is greater, '{a}' (a), or '{b}' (b) ?")
	answer = input("a/b: ") 
	return answer == 'b'


with open(sys.argv[1]) as f:
	lines = f.read().splitlines()

print(mergesort(lines))