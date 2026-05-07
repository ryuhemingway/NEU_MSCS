import matplotlib.pyplot as plt
#show study hours per day
days = [1,2,3,4,5,6,7]
study_hours = [2,3,2.5,4,5,3,6]

plt.plot(days, study_hours, color='blue', marker='o', linestyle ='-', linewidth=2)
plt.title('Study Hours Per Day')
plt.xlabel('Days of the week')
plt.ylabel('Hours Studied')
plt.grid(True)
plt.show()