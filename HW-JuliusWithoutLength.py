def Julius(string, shift):
    letters = "abcdefghijklmnopqrstuvwxyz"
    c_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "123456789"
    result = ""

    for ch in string:
        if ch in letters:
            key = (letters.index(ch) + shift) % len(letters)
            result += letters[key]
        elif ch in c_letters:
            key = (c_letters.index(ch) + shift) % len(c_letters)
            result += c_letters[key]
        elif ch in nums:
            key = (nums.index(ch) + shift) % len(nums)
            result += nums[key]
        else:
            result += ch
    return result

text = input("Text: ")
shift = int(input("How much every character should shift? "))

print(Julius(text, shift))