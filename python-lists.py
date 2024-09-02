"""
Question 1. Python List Transformation

Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
Sort the grades in descending order and print the sorted list.
"""
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = grades.sort()
descend_grades = grades.reverse()
print(grades)


# Cleaner code
# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# grades.sort(reverse=True)  
# print(grades)


"""
Task 2: Calculate the average grade and print it.
"""
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average_grade = sum(grades) / len(grades)
print(f"The average grade is: {average_grade}")



"""
Question 2. Advanced List Methods and Identity Operators
Problem Statement: You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? And how can you check to see if Alice is in both submitted and attended in one if statement?
"""

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_and_attended = True  if "Alice" in submitted and "Alice" in attended  else False
print(submitted_and_attended)


"""
Question 3. Advanced Slicing Techniques
Objective: The aim of this assignment is to use Python list slicing.

Problem Statement: You have a list of daily temperatures for one month, and you'd like to extract specific data from it.


Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). Expected Outcome:

83, 85, 86, 87, 88, 89, 90,
"""


temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures = temperatures[7:14]
print(second_week_temperatures)


"""
Task 2: Extract all the temperatures above 100. HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.
"""


# Simpler code
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temperatures_over_100 = temperatures[24:]
print(temperatures_over_100)

# for loop code
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temperatures_over_100 = [x for x in temperatures if x > 100]
print(temperatures_over_100)

