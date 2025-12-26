# square numbers of a list and Return it as a List

def square_numbers(nums):
    ans = []
    for i in nums:
        ans.append(i**2)
        
    return ans

def main():
    numbers = [1,2,3,4,5]
    result = square_numbers(numbers)
    print(result)
    
main()