# squares
 
def eval_squares(nums):
    squares = []
    for number in nums:
        squares.append(number ** 2)
        
    return squares

def main():
    nums = [1,2,3,4,5]
    ans = eval_squares(nums)
    print(ans)
    
    
main()   