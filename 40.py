'''
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''



'''
We can sum the bits in same positions for all the numbers and take modulo with 3.
The bits for which sum is not multiple of 3, are the bits of number with single occurrence.
'''
def arr3Rpt1Unq(arr):
    ans = 0
    for i in range(32):   # assuming an integer is of 32 bits
        count = 0
        for num in arr:
            if num & (1<<i):
                count += 1
        if count%3 != 0:
            ans |= 1<<i
    return ans    


test_cases = [
    [5,7,5,7,5,7,4],
    [2,4,4,4],
]
for tc in test_cases:
    print(tc, arr3Rpt1Unq(tc))


''' 
Approach 2
More Difficult and Less Intuitive Approcah
'''
def arr3Rpt1Unq_approach2(arr):
    once = twice = 0
    for num in arr:
        twice |= once&num
        once ^= num
        negateThrice = ~(once&twice)
        once &= negateThrice
        twice &= negateThrice
    return once


'''
Explanation of approach 2:

The code makes use of 2 variables.
ones - At any point of time, this variable holds XOR of all the elements which have
appeared "only" once.
twos - At any point of time, this variable holds XOR of all the elements which have
appeared "only" twice.

So if at any point time,
1. A new number appears - It gets XOR'd to the variable "ones".
2. A number gets repeated(appears twice) - It is removed from "ones" and XOR'd to the
variable "twice".
3. A number appears for the third time - It gets removed from both "ones" and "twice".

The final answer we want is the value present in "ones" - coz, it holds the unique element.

So if we explain how steps 1 to 3 happens in the code, we are done.
Before explaining above 3 steps, lets look at last three lines of the code,

not_threes = ~(ones & twos)
ones & = not_threes
twos & = not_threes

All it does is, common 1's between "ones" and "twos" are converted to zero.

For simplicity, in all the below explanations - consider we have got only 4 elements in the array
(one unique element and 3 repeated elements - in any order).

Explanation for step 1
------------------------
Lets say a new element(x) appears.
CURRENT SITUATION - Both variables - "ones" and "twos" has not recorded "x".

Observe the statement "twos| = ones & x".
Since bit representation of "x" is not present in "ones", AND condition yields nothing. So "twos" does not get bit representation of "x".
But, in next step "ones ^= x" - "ones" ends up adding bits of "x". Thus new element gets recorded in "ones" but not in "twos".

The last 3 lines of code as explained already, converts common 1's b/w "ones" and "twos" to zeros.
Since as of now, only "ones" has "x" and not "twos" - last 3 lines does nothing.

Explanation for step 2.
------------------------
Lets say an element(x) appears twice.
CURRENT SITUATION - "ones" has recorded "x" but not "twos".

Now due to the statement, "twos| = ones & x" - "twos" ends up getting bits of x.
But due to the statement, "ones ^ = x" - "ones" removes "x" from its binary representation.

Again, last 3 lines of code does nothing.
So ultimately, "twos" ends up getting bits of "x" and "ones" ends up losing bits of "x".

Explanation for step 3.
-------------------------
Lets say an element(x) appears for the third time.
CURRENT SITUATION - "ones" does not have bit representation of "x" but "twos" has.

Though "ones & x" does not yield nothing .. "twos" by itself has bit representation of "x". So after this statement, "two" has bit representation of "x".
Due to "ones^=x", after this step, "one" also ends up getting bit representation of "x".

Now last 3 lines of code removes common 1's of "ones" and "twos" - which is the bit representation of "x".
Thus both "ones" and "twos" ends up losing bit representation of "x".
'''