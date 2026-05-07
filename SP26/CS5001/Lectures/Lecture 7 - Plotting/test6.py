import matplotlib.pyplot as plt

#example: programming languages popularity
languages = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
students = [45,30,15,35,10]

plt.barh(languages, students, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.title('Programming Languages learned by Students')
plt.xlabel('Language')
plt.ylabel('Number of Students')
plt.show()