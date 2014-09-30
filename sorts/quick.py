import random
def quicksort (arr):
	array = arr
	if len(arr)<2:
		print "hi"
		return arr
	else:
		left=1
		right =len(arr)-1
		pivot = 0
		while left<=right :
			while arr[left]<arr[pivot]:
				left+=1
			while arr[right]>arr[pivot]:
				right-=1
			if left<=right:
				arr[left],arr[right]=arr[right],arr[left]
				left+=1
				right-=1
		arr[pivot],arr[right]=arr[right],arr[pivot]
		pivot = right
		print arr
		print pivot,left, right
		quicksort(arr[:pivot])
		print arr
		quicksort(array[pivot+1:])
		return arr

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
print quicksort (a)
