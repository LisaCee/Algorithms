def find_subarray(arr, total):

    for i in range(0, len(arr)):
        # take the value we have at start index
        current_sum = arr[i]
        if current_sum == total:
            return (i, i)
        for j in range(i + 1, len(arr)):
            current_sum += arr[j]
            if current_sum == total:
                return(i, j)
            elif current_sum > total:
                break

    return None


print(find_subarray([1, 4, 20, 3, 10, 5], 33))
print(find_subarray([1, 4, 0, 0, 3, 10, 5], 7))
print(find_subarray([1, 4], 0))
print(find_subarray([33], 33))
print(find_subarray([], 2))
# unsorted array of pos ints, find continous subarray which adds to sum
# return tuple with start/end indexes

# examples
# [1, 4, 20, 3, 10, 5], sum = 33    answer is (2, 4)
# [1, 4, 0, 0, 3, 10, 5], sum = 7   answer is (1, 4)
# [1, 4], sum = 0   answer is None
# [33], sum = 33    answer is (0, 0)


# Find the odd (occurrence) int
# code wars
# def find_it(seq):
# dict for each time num occurs
# loop key/val and % 2
# told that we are given array of ints and only 1 repeats an odd number of times
# frequency = {}

# for num in seq:
#   if num not in frequency:
#     frequency[num] = 1
#   else:
#     frequency[num] += 1
# for key, value in frequency.items():
#   if value % 2 != 0:
#     return key


## recursion and time/space complexity ##
# def factorial(n):
#   # 4! = 4x3x2x1 = 24
#   if n <= 1:
#     return 1
#   return n * factorial(n - 1)

# print(factorial(4))
# print(factorial(10))
# print(factorial(-10))
# print(factorial(1000))
# stack overflow

# def factorial(n):
#   total = 1
#   for num in range(1, n+ 1):
#     total *= num
#   return total

# print(factorial(4))
# print(factorial(10))
# print(factorial(-10))
# print(factorial(1000))

# cache = {}

# def fib(n):
#   # check if we've already done fib(n)
#   if n in cache.keys():
#     return cache[n]

#   if n <= 1:
#     return n

#   fib_result = fib(n - 1) + fib(n - 2)
#   cache[n] = fib_result

#   return fib_result

#   # store result in cache

# print(fib(10))
