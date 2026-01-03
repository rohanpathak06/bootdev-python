# entry point function

def main():
    value = add(2, 3)
    print_ans(value)
    
def print_ans(v):
    print(f"the value after sum is: {v}.")
    
def add(a, b):
    result = a + b;
    return result

main()