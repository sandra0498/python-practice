import random
random.randint(0,21)
def get_numbers():
    numbers=[]
    numbers= random.sample(range(0,21),20)
    return numbers

def min_number(numbers):
    lowest=min(numbers)
    return lowest

def max_number(numbers):
    highest=max(numbers)
    return highest

def total_numbers(numbers):
    total=0
    for value in numbers:total+=value
    return total
    
def average_number(total):
    average=total/20
    return average

def displayResults(numbers,lowest, highest,total, average):
    print("here is your list", numbers)
    print("Low:", lowest)
    print("High:", highest)
    print("Total:", total)
    print("Average:", average)
    
        
    

def main():
    numbers=random.sample(range(0,21),20)
    numbers=get_numbers()
    lowest=min_number(numbers)
    highest=max_number(numbers)
    total=total_numbers(numbers)
    average=average_number(total)
    displayResults(numbers, lowest, highest, total, average)
    

main()
    
               
