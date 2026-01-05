# we want to print all the numbers from 1 to 50, but skip every 7th number.

def print_num():
    counter = 0
    for i in range(1, 51):
        counter += 1
        if counter == 7:
            counter = 0
            continue
        print(i)

print_num()
