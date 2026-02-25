# Ben Ledoux, 2/25/2026 9:52 AM CT
# Test python file in terminal

def main():
	print("Hello, World!")
	numList = [5, 7, 4, 2, 8, 9, 5]
	print(f"Current list: {numList}")
	sortedList = simpleSort(numList)
	print(f"Sorted list, O(n^2): {sortedList}")
	binarySortedList = binarySort(numList)
	print(f"Sorted list, O(log(n)): {binarySortedList}")
	target = int(input("Enter number to search for: "))
	index = binarySearch(target, binarySortedList, 0)
	if index == -1:
		print("Target number not found in sorted list...")
	else:
		print(f"Target number found at index {index}: {sortedList[index]}")

def simpleSort(list):
	for i, num in enumerate(list):
		for j in range(i + 1, len(list)):
			if (num > list[j]):
				temp = list[j]
				list[j] = num
				list[i] = temp
	return list

def binarySearch(num, list, i):
	if (len(list) < 1):
		return -1
	n = len(list) // 2
	if (num == list[n]):
		return i + n
	elif (num < list[n]):
		return binarySearch(num, list[:n], 0)
	elif (num > list[n]):
		return binarySearch(num, list[n+1:], i+n+1)
	return -1

def binarySort(list):
	n = len(list)
	if (n < 2):
		return list
	elif (n == 2):
		if list[0] < list[1]:
			return list
		else:
			return [list[1], list[0]]
	elif (n > 2):
		return binarySort(list[:n//2]) + binarySort(list[n//2:])
	return -1

if __name__ == "__main__":
	main()
