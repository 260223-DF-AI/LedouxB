# Ben Ledoux, 2/25/2026 9:52 AM CT
# Test python file in terminal

import time
from random import randint

def main():
	print("Hello, World!")
	# numList = [5, 7, 4, 2, 8, 9, 5, 10, 1, 144, 32, 2934, 453, 3]
	numList = [randint(1, 100) for _ in range(100)]
	# print(f"Starting list: {numList}")
	
	start = time.time()
	sortedList = simpleSort(numList)
	end = time.time()
	print(f"Sorted list, O(n^2), runtime {(end - start) * 1000:.2f}ms")
	print(sortedList)
	
	start = time.time()
	binarySortedList = binarySort(numList)
	end = time.time()
	print(f"Sorted list, O(log(n)), runtime {(end - start) * 1000:.2f}ms")
	print(binarySortedList)
	
	target = int(input("Enter number to search for: "))
	index = binarySearch(target, binarySortedList, 0)
	if index == -1:
		print("Target number not found in sorted list...")
	else:
		print(f"Target number found at index {index}: {binarySortedList[index]}")

def simpleSort(list):
	n = len(list)
	for i in range(n):
		for j in range(n - i - 1):
			if (list[j] > list[j + 1]):
				list[j], list[j + 1] = list[j + 1], list[j]
	return list

def binarySearch(target, list: list, i: int) -> int:
	if (len(list) < 1):
		return -1
	n = len(list) // 2
	if (target == list[n]):
		return i + n
	elif (target < list[n]):
		return binarySearch(target, list[:n], i)
	elif (target > list[n]):
		return binarySearch(target, list[n+1:], i+n+1)
	return -1

def binarySort(list: list) -> list:
	n = len(list)
	if (n < 2):
		return list
	elif (n == 2):
		if list[0] < list[1]:
			return list
		else:
			return [list[1], list[0]]
	elif (n > 2):
		first_half = binarySort(list[:n//2])
		second_half = binarySort(list[n//2:])
		combined_list = []
		while first_half and second_half:
			if first_half[0] < second_half[0]:
				combined_list.append(first_half.pop(0))
			else:
				combined_list.append(second_half.pop(0))
		return combined_list + first_half + second_half
	return -1

if __name__ == "__main__":
	main()
