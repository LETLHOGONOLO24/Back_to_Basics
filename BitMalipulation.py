def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num  # XOR all elements

    return result

# Example test
print(singleNumber([4, 1, 2, 1, 2]))
