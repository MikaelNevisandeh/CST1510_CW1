# Week 1 – Values, Types and Input/Output – Programming Problems

## Task 1: Questionnaire
Write a program that asks for name, interest, nationality, course, and programming experience, then prints a formatted summary using escape sequences (`\n`, `\t`).

**Example Output:**
```
User Information:
	Name: Alice
	Interest: Security
	Nationality: UK
	Course: Cyber
	Experience: Beginner
```

## Task 2: Rectangle Area & Perimeter
Calculate and print the area and perimeter of a rectangle using fixed values: width = 4.5 and height = 7.9.
Formulas: `area = width * height`, `perimeter = 2 * (width + height)`.

**Example Output:**
```
Area = 35.55
Perimeter = 24.80
```

## Task 3: Convert Pounds to Kilograms
Ask the user for a value in pounds, convert to kilograms using `1 lb = 0.454 kg`, and print the result.

**Example Output:**
```
55.5 pounds is 25.197 kilograms
```

## Task 4: Convert Feet to Meters
Ask the user for a value in feet, convert to meters using `1 ft = 0.305 m`, and print the result.

**Example Output:**
```
16.5 feet is 5.0325 meters
```

## Quick Check (no code submission)
- What data type does `input()` return? Use `type(input("x"))` to verify.
- Show one example of an escape sequence in `print()`.
- What is the difference between `/` and `//`? Provide a one-line example for each.

## Task 5: Total Time to Watch a Series
Compute total viewing time (no breaks) for a series:
- 5 seasons, 10 episodes per season
- Season 1: 45 minutes 35 seconds per episode
- Seasons 2–5: 35 minutes 15 seconds per episode

Display the total as hours, minutes, and seconds.

**Example Output:**
```
Total time: 39h 30m 0s
```

## Task 6: Savings Projection (3 Years)
Compute final savings after 3 years given:
- Save £10 every week for 3 years
- Year 1 bonus: +£20 each week
- Every 2 weeks: −£0.50 (sister)

Assume 52 weeks per year; use arithmetic and augmented assignment; no conditionals.

**Example Output:**
```
Final savings after 3 years: £4689.50
```

## Task 7: Cyber: HTTP Log Composer
Ask for IP, method, path, status, and bytes, then print a single combined log line (Apache-style).

**Example Output:**
```
192.168.1.10 - "POST /auth" 401 512
```

## Task 8: Pure Python EDA: Dataset Metadata
Ask for dataset name, rows, and columns. Print:
- dataset name in quotes
- rows and columns
- total cells (rows × columns)

**Example Output:**
```
"sales.csv"
Rows: 120
Columns: 8
Cells: 960
```

## Task 9: IT: INI-style Config Printer
Ask for three `key=value` pairs (via separate prompts) and print them as an INI block with indentation.

**Example Output:**
```
[config]
	max_connections = 200
	timeout = 30
	region = eu-west-2
```

## Task 10: Sum of First n Integers
Ask for a positive integer `n` and compute the sum `n*(n+1)//2`. Print the result.

**Example Output:**
```
Sum of 1..10 = 55
```

## Task 11: Population Projection (5 Years)
Assume current population is 312032486 and 1 year = 365 days.
Rates: birth every 7s, death every 13s, immigrant every 45s.
Compute projected population for each of the next 5 years using integer division (`//`).

**Example Output:**
```
Year 1: 315,xxx,xxx
...
Year 5: ...
```
*Optional hint:* Compute yearly net change once; then add each year.

## Task 12: Payroll Statement
Ask for: employee name, hours worked, hourly rate, federal tax rate, state tax rate.
Print a formatted payroll slip with gross pay, each deduction, and net pay (2 d.p.).

**Example Output:**
```
Employee: Smith
Gross pay: £97.50
Federal withholding: £19.50
State withholding: £8.78
Net pay: £69.22
```
