# student_finance_calculator

Overview:
Console-based application to calculate the amount of student debt which
a student will owe on their statement at the end of tax year 2023-2024.

Installation:
This application can be run using the file: student_finance.py
It does not need any other files.

In the variables section the average student loan interest rate is stated for the
5 countries: Australia, New Zealand, Sweden, United Kingdom and United States.
To update for later years (beyond 2023 - 2024) these values could be updated to
the then current interest rates.

Functionality:
First, the programme asks for input of the total student debt amount on the
user’s student finance statement.

Then a list of countries is displayed and the user is asked to input which
country they studied in and where they took out the government-backed student
loan.

If the user studied in Australia, Sweden or the United Kingdom then the
calculation happens and is printed in the console without requiring any
further input.

If the user studied in New Zealand they are asked if they still live in
New Zealand or moved abroad, as this affects how much interest is added to
their student loan. The calculation happens and is printed out in the console.

If the user studied in the United States they are asked if they took out a
federal or a student loan, as this calculator can only calculate the amount of
federal student loan.

Then for the federal student loan, the user is asked which of the 3 options of
student loans they took out, as these all come with separate interest rates.
The calculation happens and is printed out in the console.
