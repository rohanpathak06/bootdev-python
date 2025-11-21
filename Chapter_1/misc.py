# squares of all numbers in a list

def square_numbers(nums):
    squares = []
    for num in nums:
        squares.append(num**2)
        
    return squares

def main():
    numbers = [1,2,3,4,5]
    ans = square_numbers(numbers)
    print(ans)
    
main()