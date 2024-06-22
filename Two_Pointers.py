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
print(f'Is the string "{s}" a palindrome?: {result}')


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
print(f'Is the string "{s}" a palindrome?: {result}')


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
    # Intialize two pointers i and j to iterate through 
    # word1 and word2 respectively
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


# MERGED SORTED ARRAY (LEETCODE 88)

def merge(nums1, m, nums2, n):
    # Calculate the index where the merged array will start from
    p = m + n - 1

    # Decrement m and to point to the last elements of nums1 and nums2 respectively 
    m -= 1
    n -= 1

    # Loop until both nums1 and nums2 have elements remaining 
    while m >= 0  and n >= 0:
        
        # Compare the last elements of nums1 and nums2
        if nums1[m] > nums2[n]:
            
            # If the last element if nums1 is greater, place it at position p
            nums1[p] = nums1[m]

            # Move the pointer m to the previous element un n ums1
            m -= 1
        
        else:

            # If the last element of nums2 is greater or equal, place it 
            # at position p
            nums1[p] = nums2[n]

            # Move the pointer p to the previous position for the next element
            n -= 1
        
        # Move the pointer p to the previous position for the next element
        p -= 1
    
    # If there are are elements remaining in nums2, copy them to the beginging 
    # of nums1
    nums1[:n + 1] = nums2[:n + 1]

    return nums1


print(merge(nums1= [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))    


# MOVE ZEROES (LEETCODE 283)

def moveZeroes(nums):
    
    # Initialize the left pointer to keep track if the position where non-zero 
    # elements should be placed
    l = 0 

    # Iterate throught the array using a right pointer 'r'
    for r in range(len(nums)):
        
        # If the current element is non-zero
        if nums[r] != 0:
            
            # Swap the current non-zero element with the element at the left 
            # pointer position
            nums[l], nums[r] = nums[r], nums[l]

            # Move the left pointer to the next position
            l += 1
    
    return nums

print(moveZeroes(nums = [0,1,0,3,12]))
             

# REMOVE DUPLICATES FROM SORTED ARRAY (LEETCODE 26)

def removeDuplicates(nums):
    
    # Initialize left pointer and right pointer to zero
    l = 0

    # Iterate through the array
    for r in range(len(nums)):

        # Check if the current element is different from previous element 
        if r == 0 or nums[r] != nums[r - 1]:

            # If different, copy the element to the left pointer 
            nums[l] = nums[r]

            # Increment the left pointer
            l += 1
    
    # Return the length of the modified array 
    return l

print(removeDuplicates(nums = [1,1,2,3]))

# SORT COLORS (ARRANGE COLORS IN S30) (LEETCODE 75)

def sortColors(nums):

    # Initialize pointers for three sections of the list 
    
    # Leftmost and rightmost indices of unsorted part
    l, r = 0, len(nums) - 1  

    # Current index being processed
    i = 0

    while i <= r :

        # If the current element is 0
        if nums[i] == 0:

            # Move it to the begining of the list (0 secton)
            nums[l], nums[i] = nums[i], nums[l]

            # Expand the 0 section
            l += 1

        # If the current element is 2:
        elif nums[i] == 2:
            
            # Move it to the end of the list (2 section)
            nums[i], nums[r] = nums[r], nums[i]

            # Shrink the unsorted section
            r -= 1

            # Re- check thw swapped element (since it might now be a 0 or 1)
            i -= 1

        # Move to the next element 
        i += 1

    return nums

print(sortColors(nums = [2,0,2,1,1,0]))


# ASSIGN COOKIES (LEETCODE 455)

def findContentChildren(g, s):

    # Sort the list g
    g.sort()

    # Sort the list s
    s.sort()

    # Initialize two pointers on at the start and one at the start of s
    i, j = 0, 0

    # Initializw result variable called content_children to track 
    # number of content children
    content_children = 0

    # Iterate through both the lists 
    while i < len(g) and j < len(s):

        # If the element at s is greater than element at g then 
        # increment content_children
        if s[j] >= g[i]:
            content_children += 1

            # Increment the i pointer
            i += 1
        
        # Increment the j pointer 
        j += 1

    # Return the number of content children
    return content_children

print(findContentChildren(g = [1,2], s = [1,2,3]))


# FIND FIRST PALINDROMIC STRING IN THE ARRAY (LEETCODE 2108)

def firstPalindrome(words):

    # Iterate through each word in the words list
    for w in words:

        # Initialize two pointers, one ate the start of the wach word and 
        # one at the end of each word
        l, r = 0, len(w) - 1

        # While the start letter and end letter are the same of the single word
        while w[l] == w[r] :

            # If the pointers meet then return the word w 
            if l >= r:
                return w

            # # Move the pointers towards each other 
            l, r = l + 1, r - 1

    # If there is no palindrome in the list then return empty string
    return "" 
    
print(firstPalindrome(words = ["abc","car","ada","racecar","cool"]))
