class Solution(object):
    def addNums(self, a, b):
        i = len(a) - 1  
        j = len(b) - 1   
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry
            carry = total // 10
            result = str(total % 10) + result

            i -= 1
            j -= 1

        return result


def main():
    s = Solution()
    print(s.addNums("333", "222"))   
    print(s.addNums("999", "1"))   
    print(s.addNums("5", "7"))     

main()
