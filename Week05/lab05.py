# Week 05 Lab: Recursion & Functions - Completed
# COMP2152 - Python Programming
# Rasul Dadashbayli - 101527648

print("=" * 60)
print("WEEK 05 LAB: RECURSION & FUNCTIONS")
print("=" * 60)

# ============================================================
# Question 1: Fibonacci Number (LeetCode #509)
# ============================================================
print("\n" + "=" * 50)
print("Question 1: Fibonacci Number (#509)")
print("=" * 50)


def fib(n):
    # Base case 1 - If n equals 0, return 0
    if n == 0:
        return 0

    # Base case 2 - If n equals 1, return 1
    if n == 1:
        return 1

    # Recursive case - Return fib(n-1) + fib(n-2)
    return fib(n - 1) + fib(n - 2)


# Test cases for Fibonacci
print("Fibonacci Sequence (F(0) to F(10)):")
print("-" * 30)
for i in range(11):
    result = fib(i)
    print("F(" + str(i) + ") = " + str(result))

# ============================================================
# Question 2: FizzBuzz (LeetCode #412)
# ============================================================
print("\n" + "=" * 50)
print("Question 2: FizzBuzz (#412)")
print("=" * 50)


def fizz_buzz(n):
    result = []

    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check if divisible by BOTH 3 and 5 FIRST
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # Then check if divisible by 3 only
        elif i % 3 == 0:
            result.append("Fizz")
        # Then check if divisible by 5 only
        elif i % 5 == 0:
            result.append("Buzz")
        # Otherwise, append the number as a string
        else:
            result.append(str(i))

    return result


# Test cases for FizzBuzz (as provided in starter)
print("\nTest Case 3: n = 15")
print("Output: " + str(fizz_buzz(15)))

# ============================================================
# Question 3: Binary Search (LeetCode #704)
# ============================================================
print("\n" + "=" * 50)
print("Question 3: Binary Search (#704)")
print("=" * 50)


# Part A: Iterative Solution
def binary_search_iterative(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            # search left half
            right = mid - 1
        else:
            # search right half
            left = mid + 1

    return -1


# Part B: Recursive Solution
def binary_search_recursive(nums, target, left, right):
    # Base case - If left > right, return -1 (target not found)
    if left > right:
        return -1

    # Calculate mid
    mid = (left + right) // 2

    # If nums[mid] == target, return mid
    if nums[mid] == target:
        return mid

    # If target < nums[mid], recurse on left half
    if target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)

    # If target > nums[mid], recurse on right half
    else:
        return binary_search_recursive(nums, target, mid + 1, right)


# Wrapper function for recursive solution
def search_recursive(nums, target):
    if len(nums) == 0:
        return -1
    return binary_search_recursive(nums, target, 0, len(nums) - 1)


# Test cases for Binary Search
print("\n--- Part A: Iterative Binary Search ---")
nums_test = [-1, 0, 3, 5, 9, 12]
print("Target 9 in " + str(nums_test) + " -> Index: " + str(binary_search_iterative(nums_test, 9)))

print("\n--- Part B: Recursive Binary Search ---")
print("Target 9 in " + str(nums_test) + " -> Index: " + str(search_recursive(nums_test, 9)))

# Verification
print("\nVerification for Target 100: " + str(binary_search_iterative(nums_test, 100)))