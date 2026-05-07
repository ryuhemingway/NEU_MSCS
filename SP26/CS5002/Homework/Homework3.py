import numpy as np

a, b, n = 1,366,40 
simulations = 100
count_diff = 0

for i in range(simulations):
    birthdays = np.random.randint(a,b,n)
    
    set_birthdays = set(birthdays)
    len_birthdays = len(birthdays)
    card_set_birthdays = len(set_birthdays)
    
    if len_birthdays != card_set_birthdays:
        count_diff += 1

print(f"Number of times the variables differed: {count_diff}")

