class Solution(object):
  def reverseString(self, string):
    result = ""
    for char in string:
      result = char + result
    return result
    
def main():
    final = Solution().reverseString("formula")
    print(final)
    
main()
