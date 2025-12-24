# Awkawrd sort interface because this game doesn't have the common library
# Have to rewrite sort by hand
def sort(items, key_index, reverse=False):
	if len(items) <= 1:
		return items
	
	mid = 0
	length = len(items)
	while mid * 2 < length:
		mid = mid + 1
	mid = mid - 1
	
	pivot = items[mid][key_index]
	left = []
	middle = []
	right = []
	
	for x in items:
		if x[key_index] < pivot:
			left.append(x)
		elif x[key_index] == pivot:
			middle.append(x)
		else:
			right.append(x)
	
	if reverse:
		return sort(right, key_index, reverse) + middle + sort(left, key_index, reverse)
	
	return sort(left, key_index) + middle + sort(right, key_index)