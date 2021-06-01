import numpy
from scipy import stats

marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]
my_mean=numpy.mean(marks_of_students)
my_median=numpy.median(marks_of_students)
my_mode=stats.mode(marks_of_students)
my_range=numpy.ptp(marks_of_students)

print(my_mean)
print(my_median)
print(my_mode)
print(my_range)




