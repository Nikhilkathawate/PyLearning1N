# Task #3
#
# ✅ Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
#
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
#
# output - Eq, Iso, Scalene -
#
# Eq. = side 1 == side 2 = side 3

print("Classify triangle based on its side lengths\n")
side1 = int(input("Enter side 1\n"))
side2 = int(input("Enter side 2\n"))
side3 = int(input("Enter side 3\n"))
if side1==side2==side3:
    print("The triangle is 'Equilateral'")
elif side1==side2!=side3 or side2==side3!=side1 or side1==side3!=side2:
    print("The triangle is 'Isosceles'")
else:
     print("The triangle is 'Scalene'")