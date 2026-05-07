"""
Problem 1: Tuition Increase
Name: Ryu Hemingway
NU ID: 003163519

# I confirm that AI code completion tools were disabled while writing this program.

At one college, the tuition for a full-time student is $8,000 per semester. 
It has been announced that the tuition will increase by 3 percent each year 
for the next 5 years. Write a program with a loop that displays the projected 
semester tuition amount for the next 5 years.
"""

def calculate_tuition_for_year(current_tuition, increase_rate):
    # create calculation for new tuition
    new_tuition = current_tuition * (1+increase_rate)
    return new_tuition

def display_tuition_projection(starting_tuition, increase_rate, num_years):
    #create header
    print("Year: Tuition")

    #ensure that the tuition that we start with is labeled as current_tuition
    current_tuition = starting_tuition

    #write the range function so that the loop continues for as long as it is in range which should be 5 years
    for year in range(1, num_years + 1):
        current_tuition = calculate_tuition_for_year(current_tuition, increase_rate)
        print(f"{year}: {current_tuition:.2f})")


def main():
   
   #define the parameters given to us in the instructions
   initial_tuition = 8000
   interest_rate = 0.03
   num_years = 5

   display_tuition_projection(initial_tuition, interest_rate, num_years)


# Run the program
main()
