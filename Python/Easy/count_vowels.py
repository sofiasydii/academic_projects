class Solution(object):
    def count_vowels(self, text):
        vowels = "euioaEUIOA"
        count = 0
        
        for char in text:
            if char in vowels:
                count += 1
                
        return count
        
        

def main():
    print("Let's count vowels!")
    text = input("Write a word: ")
    result = Solution().count_vowels(text)
    print(result)
    
main()
