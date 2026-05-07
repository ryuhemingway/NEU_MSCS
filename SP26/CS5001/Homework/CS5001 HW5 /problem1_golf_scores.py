# I confirm that AI code completion tools were disabled while writing this program.
# Name: Ryu Hemingway
# NU ID: 003163519

"""
Problem 1: Golf Scores

The Springfork Amateur Golf Club has a tournament every weekend. The club 
president has asked you to write two programs: 

• A function that will read each player's name and golf score as keyboard input, 
  then save these as records in a file named golf.txt. (Each record will have a 
  field for the player's name and a field for the player's score.)

• A function that reads the records from the golf.txt file and displays them.
"""


def write_golf_scores():

# write file
    newfile = open("golf.txt", "w")

# ask user how many players
    num_players = int(input("How many players do you want to add?"))

# use a range function to iterate through the through out list x num of times
    for i in range(num_players):
        name = input("What is the name of the player")
        score = input("Enter the score for the player")
        
# write to the file and add \n so each player on new line
        newfile.write(name + "\n")
        newfile.write(score + "\n")

#close file and show the file has been saved thus far
    newfile.close()
    print("File saved")

def read_golf_scores():
    # open the file for reading
    file = open("golf.txt", "r")

    # read the first line
    name = file.readline()

    # we need a loop that will execite until there is no more to read so we will use a while loop
    while name != "":
        score = file.readline()

        name = name.rstrip("\n")
        score = score.rstrip("\n")

        # print the output to the user
        print("Player Name:", name)
        print("Golf Score:", score)

        name = file.readline()

    file.close

def main():
    """
    Main function to run the golf scores program
    """
    while True:
        print("\n=== Golf Score Management System ===")
        print("1. Enter golf scores")
        print("2. Display golf scores")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            write_golf_scores()
        elif choice == '2':
            read_golf_scores()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
