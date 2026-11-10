# Week 6 – Pandas – Programming Problems

Data: the `DATA/` folder must be next to your notebook, e.g. `pd.read_csv('DATA/students.csv')`. Tasks 1–14 use `DATA/students.csv` (and `DATA/students_missing.csv` where stated) with columns `Name`, `Age`, `Course`, `Grade`, `Attendance`, `City`, `Scholarship`.

## Task 1: Load and Explore
Load `DATA/students.csv` and print:
1. The **first 5 rows** of the dataset.
2. The **last 3 rows**.
3. The **number of rows and columns** (use `shape`).
4. The **column names** as a list.

**Expected output (partial):**
```
Shape: (25, 7)
Columns: ['Name', 'Age', 'Course', 'Grade', 'Attendance', 'City', 'Scholarship']
```

## Task 2: Data Types and Summary
Using the loaded DataFrame:
1. Display the **data type** of each column.
2. Run `describe()` to get summary statistics.
3. Answer (as a `print` statement):
   - What is the **average grade**?
   - What is the **maximum attendance**?
   - What is the **youngest student's age**?

**Hint:** Use `df['column'].mean()`, `.max()`, `.min()`.

## Task 3: Selecting Columns and Rows
1. Create a new DataFrame called `grades_df` containing only the columns `Name`, `Course`, and `Grade`. Display the first 8 rows.
2. Use `iloc` to display rows **5 to 9** (positions).
3. Use `loc` to display the **Name** and **City** of the student at index `3`.

**Hint:** For multiple columns, use `df[['col1', 'col2']]`.

## Task 4: Simple Filtering
1. Display all students who study in **London**. How many are there?
2. Display students whose **Grade is below 65**. Print their Name and Grade.
3. Use `value_counts()` on the `City` column to see how many students are in each city.

**Expected output (partial):**
```
Students in London: 11
```

## Task 5: Sort the Data
1. Sort the students by **Grade** from **highest to lowest** and display the top 5.
2. Sort by **City** (A → Z), and within each city, by **Grade** (lowest → highest). Display the first 10 rows of the result.

**Hint:** `sort_values(['col1', 'col2'], ascending=[True, False])`

## Task 6: Grade Analysis with Multiple Conditions
1. Find all students who:
   - Study **Computer Science** or **Data Science** (`isin()`), **AND**
   - Have a **Grade above 75**, **AND**
   - Have an **Attendance above 80**

   Display their Name, Course, Grade, and Attendance.
2. How many students are at **risk of failing** (Grade < 60)? Print their names and grades.
3. Find all **scholarship students from Manchester** with a Grade above 80. Display Name, Grade, and Scholarship.

## Task 7: Add New Columns
Add the following columns to the DataFrame:
1. **`Result`** — `'Pass'` if Grade >= 60, `'Fail'` otherwise. Use `.apply()` with a `lambda` function.
2. **`Combined_Score`** — calculated as `Grade × 0.7 + Attendance × 0.3`. Round to 1 decimal place.
3. Display Name, Grade, Attendance, Result, Combined_Score for the **first 10 rows**.
4. Print how many students **Passed** and how many **Failed**.

**Hint:** `df['Result'].value_counts()`

## Task 8: Course Statistics with Groupby
Group the data by **Course** and calculate:
- `Count` — number of students
- `Avg_Grade` — average grade (rounded to 1 decimal)
- `Max_Grade` — highest grade
- `Avg_Attendance` — average attendance (rounded to 1 decimal)

Use `groupby().agg()` with named aggregations. Sort the result by **Avg_Grade** from highest to lowest.

**Expected output (approximate):**
```
                  Count  Avg_Grade  Max_Grade  Avg_Attendance
Course
Computer Science      8       78.1         95            83.4
Mathematics           6       82.2         91            86.3
...
```

## Task 9: Handling Missing Data
Load **`DATA/students_missing.csv`** (this file has some missing values).
1. Print how many missing values are in **each column**.
2. Display only the rows that have **at least one missing value**.
3. Fix the missing values:
   - Fill missing **Grade** with the **column average** (round to 1 decimal).
   - Fill missing **Scholarship** with `'Unknown'`.
   - Fill missing **Course** with `'Unknown'`.
   - Drop any rows where **Attendance** is missing.
   - Drop any rows where **Age** is missing.
4. Check that no missing values remain (use `isnull().sum()`).
5. Save the cleaned DataFrame to `DATA/students_clean.csv` (no index).

**Hint:** Use `fillna()` for step 3, and `dropna(subset=[...])` for dropping.

## Task 10: City vs Scholarship Analysis
Using the clean `students.csv`:
1. Group by **City** and count how many students are in each city.
2. Group by **City** and calculate the **average Grade** per city. Sort from highest to lowest average.
3. Group by **Scholarship** and calculate the **average Grade**. Does having a scholarship relate to higher grades?
4. Group by **City and Scholarship** together and count students. Which city has the most scholarship students?

**Hint:** For grouping by two columns: `df.groupby(['City', 'Scholarship'])`

## Task 11: Grade Bands
Add a column called `Grade_Band` to the DataFrame using these rules:

| Grade | Band |
|-------|------|
| 90 – 100 | `'A'` |
| 80 – 89 | `'B'` |
| 70 – 79 | `'C'` |
| 60 – 69 | `'D'` |
| below 60 | `'F'` |

1. Use a function with `apply()` or `pd.cut()` to create the `Grade_Band` column.
2. Display Name, Grade, and Grade_Band for all students.
3. Print a **count** of students per Grade Band (use `value_counts()`).
4. Which **course** has the most students with a Band A or B grade?

**Hint for `pd.cut()`:**
```python
bins   = [0, 59, 69, 79, 89, 100]
labels = ['F', 'D', 'C', 'B', 'A']
df['Grade_Band'] = pd.cut(df['Grade'], bins=bins, labels=labels)
```

## Task 12: City Performance Report
Produce a **city-level performance summary** DataFrame with these columns:

| Column | What to calculate |
|--------|------------------|
| `Students` | Count of students per city |
| `Avg_Grade` | Average grade per city (1 dp) |
| `Avg_Attendance` | Average attendance per city (1 dp) |
| `Pass_Rate` | Percentage of students with Grade ≥ 60 (1 dp) |
| `Performance` | `'Above Average'` if Avg_Grade > overall mean, else `'Below Average'` |

**Steps:**
1. Calculate the overall average grade first (`df['Grade'].mean()`).
2. Build the summary using `groupby('City').agg()`.
3. Add the `Pass_Rate` column manually (calculate pass rate within each city group).
4. Add the `Performance` column comparing each city's avg grade to the overall mean.
5. Save the final summary to `DATA/city_report.csv` (no index).
6. Print the table sorted by `Avg_Grade` (highest first).

**Hint for Pass_Rate:**
```python
city_pass = df.groupby('City').apply(lambda g: (g['Grade'] >= 60).sum() / len(g) * 100)
```

## Task 13: Scholarship Deep Dive
Investigate whether scholarships are awarded to the right students. Answer each question with a `print()` statement and the calculation:
1. What **percentage** of all students have a scholarship?
2. What is the **average Grade** for scholarship students vs non-scholarship students? Is there a meaningful difference?
3. For each **Course**, calculate:
   - Total students
   - Students with scholarship
   - Scholarship **rate** (as %)

   Display as a table, sorted by scholarship rate (highest first).
4. Are scholarship students **more likely to attend** classes? Compare average `Attendance` for scholarship vs non-scholarship.
5. Write a **short summary** (as a comment in the code cell) of your findings in 3–4 sentences.

## Task 14: Full EDA Report
Using only Pandas, produce a **complete exploratory data analysis** of the students dataset. Answer **all** of the following questions:
1. Which **course is the most popular** (most students)?
2. Who are the **top 3 students** overall by Grade?
3. What is the **average attendance** for students who Pass vs Fail? (Define Pass as Grade ≥ 60)
4. Is there a **correlation between Attendance and Grade**? Use `.corr()` on those two columns and interpret the result in a comment.
5. Build and **export a course summary** to `DATA/eda_report.csv` containing one row per course:

| Column | Description |
|--------|-------------|
| `Course` | Course name |
| `Student_Count` | Total students |
| `Avg_Grade` | Average grade |
| `Avg_Attendance` | Average attendance |
| `Pass_Rate_Pct` | % of students with Grade ≥ 60 |
| `Scholarship_Pct` | % of students with a scholarship |

Print the final report table.

**Hint — correlation interpretation:**
```
Close to  1.0 → strong positive relationship
Close to  0.0 → no relationship
Close to -1.0 → strong negative relationship
```

## Task 15: Iris Dataset – Explore
Load `DATA/iris_dataset.csv` with `pd.read_csv`.
1. Show the first 5 rows, `shape`, `dtypes` and `describe()`.
2. How many flowers are there of each `target` species (`value_counts()`)?
3. Check for missing values and duplicated rows.

## Task 16: Iris Dataset – Group Analysis
1. Calculate the **mean** of every measurement per species with `groupby('target')`.
2. Which species has the largest average petal length? Which has the smallest average sepal width?
3. Add a column `petal_area` (`petal length × petal width`) and show the 5 flowers with the largest petal area.
4. Calculate the correlation between `petal length (cm)` and `petal width (cm)` and interpret it in a comment.

## Task 17: Cars Dataset
Load `DATA/CARS.text` (comma-separated, columns include `model`, `mpg`, `cyl`, `hp`, `wt`, `am`).
1. Show the 5 cars with the best `mpg` and the 5 with the worst.
2. Show cars with 4 cylinders and `hp` above 90.
3. Group by `cyl` and calculate the count, average `mpg` and average `hp`.
4. Add a column `Efficiency` that is `'High'` if `mpg` ≥ 25, `'Medium'` if `mpg` ≥ 18 and `'Low'` otherwise, and count the cars in each category.
5. Save the result to `cars_clean.csv` (no index).

## Task 18: Reading Excel and CSV Files
1. Load `DATA/data.xlsx` with `pd.read_excel()` (you may need `pip install openpyxl`) and load `DATA/sample_data.csv` with `pd.read_csv()`.
2. Compare the two DataFrames: do they have the same columns and the same rows?
3. Combine them into one DataFrame with `pd.concat()`, remove duplicate rows and show the result.
4. Filter the people older than 30 and sort them by `Age`.
