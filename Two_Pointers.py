# VALID PALINDROME (LEETCODE 125)

# Function to check for if a character is alphanumeric
def alphanum(c):
    return(
            ord('A') <= ord('Z') or # Check for uppercase letters
            ord('a') <= ord('z') or # Check for lowercase letters
            ord('0') <= ord('9')    # Check for digits
        )

# Function to check wether the string is a Palindrome or not
def isPalindrome(s: str) -> bool:
    # Initialized 2 pointers, one at start and one at the end
    l, r = 0, len(s) - 1
    while l < r:
            # Checking if left pointer is alphanumeric or not
        while l < r and not alphanum(s[l]):
            l += 1
            
            # Checking if right pointer is alphanumeric or not
        while r > l and not alphanum(s[r]):
            r -= 1
            
            # Checking if letters at both pointers are same or not without 
            # considering their casing
        if s[l].lower() != s[r].lower():
            return False
        
        #Move the pointer pointers inward
        l, r = l + 1, r - 1
    # Returning True if the loop does not return False
    return True


# Example string to check
s = "race a car"

# Call the isPalindrome function
result = isPalindrome(s)

# Print the result
# print(f'Is the string "{s}" a palindrome?: {result}')


# VALID PALINDROME II (LEETCODE 680)

def validPalindrome(s):
    # Initialize a left and right pointer, one at the start and one at the end
    l, r =0, len(s) - 1
    while l < r:
        # If the characters at the current position are not equal
        # Create two substrings
        # 1. Skipping the character at the left pointer 
        # 2. Skipping the character at the right pointer
        if s[l] != s[r]:
            skipLeft, skipRight = s[l + 1: r + 1], s[l : r]

            # Check if either of the substrings after skipping one character is
            # a palindrome or not. This can be done by simply checking if the
            # reverse of these strings is equal to the strings
            return (skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1])
        # Move the pointers inward
        l, r = l + 1, r - 1

    # If the loop completes without finding any inequality, the string is a 
    # valid palindrome
    return True

# Example string to check
s = "abcab"

# Call the isPalindrome function
result = validPalindrome(s)

# Print the result
# print(f'Is the string "{s}" a palindrome?: {result}')


# MINIMUM DIFFERENCE BETWEEN HIGHEST AND LOWEST OF K SCORES (LEETCODE 1984)

def minimumDifference(nums, k):
    # Sort the input list nums
    nums.sort()

    # Initialize the result of positive infinity 
    res  = float("inf")

    # Initialize two pointers for sliding window of size k
    l, r = 0, k - 1

    while r < len(nums):
        res = min(res, nums[r] - nums[l])

        l += 1
        r += 1
    
    return res

print(minimumDifference(nums = [9,4,1,7], k = 2))


# MERGE STRINGS ALTERNATELY (LEETCODE 1768)

def mergeAlternately(word1, word2):
    # Intialize two pointers i and j to iterate through word1 and word2 respectively
    i = j = 0

    # Initialize an empty list to store the merged characters
    res = []

    # Iterate through both word1 and word2 simultaneously until either
    # of them is exhausted
    while i < len(word1) and j < len(word2):
        # Apend the character from word1 at index i to the reslut list
        res.append(word1[i])

        # Append the character from word2 at index j to the result list
        res.append(word2[j])

        # Move the pointers to the next character in each word
        i += 1
        j += 1

    # If there are remaining charcters in word1 or word2 append them to the res
    res.append(word1[i:])
    res.append(word2[j:])

    # Return res and join the characters in the result list to form then merged 
    # strin
    return ''.join(res)

print(mergeAlternately(word1= 'abc', word2= 'pqr'))


# REVERSE STRING (LEETCODE 344)

def reverseString(s):
    # Get the length of the string
    n = len(s)

    # Initialize two pointers, one at the start and one at the end
    i, j = 0, n - 1

    while i < j :
        # Swap the elements ath the pointers with each other
        s[i], s[j] = s[j], s[i]
        # Move the pointers towards each other 
        i += 1
        j -= 1

        # Return the reversed string list
        return s
print(reverseString(s = ["h","e","l","l","o"]))

# IF A STRING IS GIVEN AS A INPUT INSTEAD OF A LIST 

def reverseStringString(s):
    # Convert the string to a list 
    s_list = list(s)
    # Initialize one pointer at start and one at the end
    i, j = 0, len(s_list) - 1
    while i < j :

        # Swap the elements at these pointers with each other
        s_list[i], s_list[j] = s_list[j], s_list[i]

        # Move the pointers towards each other
        i += 1
        j -= 1

        # Join the list characters back into a string
        return ''.join(s_list)
print(reverseStringString(s = "hello"))
