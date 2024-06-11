class Solution:
    @staticmethod
    def get(a, b):
        # Swap the values of a and b
        a, b = b, a
        return a, b

if __name__ == '__main__':
    # Read the input
    input_str = input()
    a, b = map(int, input_str.split())
    
    ans = Solution.get(a, b)
    print(ans[0], ans[1])
