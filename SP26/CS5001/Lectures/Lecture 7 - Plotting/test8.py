import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
exam_scores = np.random.normal(75,10,100)

plt.hist(exam_scores, bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Exam Scores')
plt.xlabel('Scores')
plt.ylabel('Number of Students')
plt.axvline(exam_scores.mean(), color='red', linestyle='--', label='Mean')
plt.legend()
plt.show()