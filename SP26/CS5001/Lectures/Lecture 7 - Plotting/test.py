import matplotlib.pyplot as plt

study_time = [1,2,3,4,5,6,7,8,9,10]
exam_scores = [50,55,60,65,70,75,80,85,90,95]

plt.scatter(study_time, exam_scores, color='red', s=100, alpha=0.5)
plt.title('Study Time vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.show()