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

def ord_min(c):
	very_normal_thing = {
		#0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
		'0': 0, 
		'1': 1,
		'2': 2,
		'3': 3,
		'4': 4,
		'5': 5,
		'6': 6,
		'7': 7,
		'8': 8,
		'9': 9,
		'a': 10,
		'b': 11,
		'c': 12,
		'd': 13,
		'e': 14,
		'f': 15,
		'g': 16,
		'h': 17,
		'i': 18,
		'j': 19,
		'k': 20,
		'l': 21,
		'm': 22,
		'n': 23,
		'o': 24,
		'p': 25,
		'q': 26,
		'r': 27,
		's': 28,
		't': 29,
		'u': 30,
		'v': 31,
		'w': 32,
		'x': 33,
		'y': 34,
		'z': 35,
		'A': 36,
		'B': 37,
		'C': 38,
		'D': 39,
		'E': 40,
		'F': 41,
		'G': 42,
		'H': 43,
		'I': 44,
		'J': 45,
		'K': 46,
		'L': 47,
		'M': 48,
		'N': 49,
		'O': 50,
		'P': 51,
		'Q': 52,
		'R': 53,
		'S': 54,
		'T': 55,
		'U': 56,
		'V': 57,
		'W': 58,
		'X': 59,
		'Y': 60,
		'Z': 61,
	}
	return very_normal_thing[c]

def int(f_value):
	# Convert a float to an int not using the built in int()
	# This game does not support int() conversion
	
	def float_to_int_positive(f_value):
		f_str = str(f_value)
		pre_radix_str = ""
		for c in f_str:
			if c == '.':
				break
			pre_radix_str += c

		result = 0
		multiplier = 1
		for i in range(len(pre_radix_str) - 1, -1, -1):
			digit = ord_min(pre_radix_str[i])
			result += digit * multiplier
			multiplier *= 10

		return result
		
	if 0 <= f_value:
		return float_to_int_positive(f_value)
	else:
		return -float_to_int_positive(-f_value)