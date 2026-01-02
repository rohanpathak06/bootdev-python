# return a list of squares of the numbers

def square_numbers(nums):
    squares = []
    for i in nums:
        squares.append(i**2)
        
    return squares

def main():
    numbers = [1,2,3,4,5]
    ans = square_numbers(numbers)
    print(ans)
    
main()