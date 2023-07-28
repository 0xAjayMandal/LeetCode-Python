class Solution:
    def isPalindrome(self, s: str) -> bool:
        num1 = "".join(x for x in s if x.isalnum())
        num1 = num1.lower()
        num2 = "".join(reversed(num1))
        return num1 == num2