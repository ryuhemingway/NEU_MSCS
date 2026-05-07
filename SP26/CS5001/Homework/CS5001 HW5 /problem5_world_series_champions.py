# I confirm that AI code completion tools were disabled while writing this program.
# Name: Ryu Hemingway
# NU ID: 003163519
"""
Problem 5: World Series Champions

You are given a file named WorldSeriesWinners.txt. This file contains a chronological list of 
the World Series winning teams from 1903 through 2009. (The first line in the file is the name 
of the team that won in 1903, and the last line is the name of the team that won in 2009. Note 
the World Series was not played in 1904 or 1994.) 

Write a program that lets the user enter the name of a team, then displays the number of times 
that team has won the World Series in the time period from 1903 through 2009.
"""


def count_world_series_wins(team_name):

# since we already have the .txt file we dont have to write it, we can just access it.
    file = open("WorldSeriesWinners.txt", "r")
    count = 0

# we learned in class to account for the fact that people may not type the name EXACTLY as in the list so we will strip it and accept lower case
    search_name = team_name.lower()

# loop through the file to check for the number of times the team name has appeared
    for line in file:
        winner = line.strip().lower()

        if winner == search_name:
            count = count + 1

    file.close()
    return count

# use the main function to prompt user input and then it will index our .txt to count the number of occurances 
def main():
    team = input("Enter team name: ")
    wins = count_world_series_wins(team)
    print(f"Total team wins: {wins}")

if __name__ == "__main__":
    main()
