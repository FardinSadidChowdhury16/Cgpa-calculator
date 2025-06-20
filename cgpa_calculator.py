# -*- coding: utf-8 -*-
"""Cgpa calculator.ipynb

Original file is located at
    https://colab.research.google.com/drive/1aJWSkxczv1WJ2momDldkNVfIrkqcCLHp
"""

completed=int(input("Total courses completed :"))
currrent_cgpa=float(input("Current Cgpa :"))
taken=int(input("Total courses taken :"))
store=0
for i in range (taken):
  store+=float(input(f"Course {i+1}:"))
store+=(currrent_cgpa*completed)
present_cgpa=store/(taken+completed)
print(f"Your present CGPA is {round(present_cgpa,2)}")

