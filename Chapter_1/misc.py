#square numbers

def square_numbers(numbers):
    squares = []
    for nums in numbers:
        squares.append(nums**2)
        
    return squares

def main():
    numbers = [1,2,3,4,5]
    ans = square_numbers(numbers)
    print(ans)
    
    
main()