class Solution(object):
  def isPalindrome(self, x)
  if x < 0:
    return False

original = x
reverse = 0
while x > 0:
  reverse = reverse * 10 + x % 10
  x // 10
return reverse == original
