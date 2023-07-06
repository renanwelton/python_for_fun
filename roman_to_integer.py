def roman_integer(roman_string):
    """Receives a roman number as a string. Returns an integer."""
    roman_nums = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    nums = []
    for letter in roman_string:
        nums.append(roman_nums[letter])
    res = 0
    while len(nums) > 1:
        if len(nums) == 1 or nums[0] >= nums[1]:
            res += nums[0]
            del nums[0]
        else:
            res += (nums[1] - nums[0])
            del nums[0:2]
    return res