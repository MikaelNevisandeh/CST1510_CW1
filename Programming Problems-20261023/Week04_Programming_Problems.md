# Week 4 – Lists, Dictionaries and Files – Programming Problems

> **Data files:** the files for this lab are in the `DATA/` folder. Keep `DATA/` next to your notebook and open files with paths such as `open("DATA/ages.csv")`. Files you create are saved in your working folder.

## Task 1: Reverse Input
Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read, your program should display them (except for the 0) in reverse order, with one value appearing on each line.

## Task 2: Dice Throws
Create a list of seven dice throws.
- The throws should be randomly generated and added to the list.
- Shuffle the list and print it out.
- Sort the list in descending order and print it out.
- Count the occurrences and print them out.

## Task 3: Sum of a Matrix Row
Write a function that returns the sum of all the elements in a specified row in a matrix using the following header:

```python
def sum_row(matrix, rowIndex):
```

Write a test program that reads a 4-by-4 matrix and displays the sum of each row.

## Task 4: Lottery Ticket
In order to win the top prize in a particular lottery, one must match all 6 numbers on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery organizer. Write a program that generates a random selection of 6 numbers for a lottery ticket. Display the numbers in ascending order.

## Task 5: Count Range
Python's standard library includes a method named `count` that determines how many times a specific value occurs in a list. In this exercise, you will create a new function named `countRange` which determines and returns the number of elements within a list that are greater than or equal to some minimum value and less than some maximum value.

Your function will take three parameters: the list, the minimum value and the maximum value. It will return an integer result.

Include a main program that demonstrates your function for several different lists, minimum values and maximum values. Ensure that your program works correctly for both lists of integers and lists of floating-point numbers.

## Task 6: Sublist
A sublist is a list that makes up part of a larger list. A sublist may be a list containing a single element, multiple elements, or even no elements at all. For example, `[1]`, `[2]`, `[3]` and `[4]` are all sublists of `[1, 2, 3, 4]`. The list `[2, 3]` is also a sublist of `[1, 2, 3, 4]`, but `[2, 4]` is not a sublist of `[1, 2, 3, 4]` because the elements `2` and `4` are not adjacent in the longer list.

The empty list is a sublist of any list. As a result, `[]` is a sublist of `[1, 2, 3, 4]`. A list is a sublist of itself, meaning that `[1, 2, 3, 4]` is also a sublist of `[1, 2, 3, 4]`.

In this exercise you will create a function, `isSublist`, that determines whether or not one list is a sublist of another. Your function should take two lists, `larger` and `smaller`, as its only parameters. It should return `True` if and only if `smaller` is a sublist of `larger`. Write a main program that demonstrates your function.

## Task 7: EDA Challenge: Student Marks Analysis
Perform Exploratory Data Analysis (EDA) using pure Python lists and functions. You have been given a multidimensional list representing student performance data. Each inner list contains: `[Student ID, Name, Math Score, Science Score, English Score]`

```python
student_data = [
    [101, 'Alice', 85, 92, 88],
    [102, 'Bob', 78, 81, 75],
    [103, 'Charlie', 90, 85, 89],
    [104, 'David', 65, 70, 72],
    [105, 'Eve', 88, 95, 90]
]
```

**Tasks:**
1. Write a function or use a list comprehension to calculate the average score for each student and add it as a new element to their list.
2. Find the highest and lowest average scores in the dataset.
3. Filter and print a list of students who have scored above 75 in all subjects.

## Task 8: Pure Python EDA: Custom Statistics Functions
The **median** is a robust statistic that protects us from outliers, while the **mean** is easily skewed. Write functions to calculate both.

1. Write a function `get_mean(data)` that takes a list of numbers and returns their average.
2. Write a function `get_median(data)` that takes a list of numbers, sorts them, and returns the middle value. (Assume the list has an odd number of elements for simplicity.)
3. Test your functions on a regular list and a list with a massive outlier to see the difference.

```python
regular_data = [40, 42, 45, 48, 50]
outlier_data = [40, 42, 45, 48, 1000]
```

## Task 9: Pure Python EDA: Student Marks Analysis
You are working as a data analyst in a school. You have the exam marks of students stored in a list. Your task is to analyze the data.

**Requirements:**
- Store marks of students in a list.
- Calculate the average mark.
- Find the highest and lowest mark using list functions.
- Print the number of students who passed (marks ≥ 50) and failed.

## Task 10: Collecting Positive Numbers
You are writing a small program to help a teacher keep track of positive numbers entered by students. The teacher also wants to know if any even numbers were given.

**Requirements:**
1. Keep asking the user to enter a positive number, or type `"done"` to stop.
2. Store all entered numbers in a **list**.
3. After the input ends:
   * If numbers were entered:
     * Print all the numbers entered.
     * Check the list and print the **first even number**. If no even number exists, print `"No even numbers found"`.
   * If no numbers were entered, print `"No numbers were entered"`.

> **Note**
> * `lower()`: Converts any text into lowercase. Example: `"DONE".lower()` becomes `"done"`. This makes it easier to compare user input without worrying about uppercase/lowercase.
> * `isdigit()`: Checks if a string only contains digits (0–9). Example: `"123".isdigit()` returns `True`, but `"12a".isdigit()` returns `False`. This helps us make sure the user typed a valid number before converting it into an integer.

## Task 11: Profile File
Write a program that:
1. Creates a file called `my_profile.txt`
2. Writes 3 lines: your name, your age, and your favorite color
3. Reads the file back and prints each line with a label

**Example output:** "Name: Alex", "Age: 20", "Favorite Color: Blue"

## Task 12: Simple Shopping List
Create a program that:
1. Writes a shopping list to `shopping.txt` (5 items, one per line)
2. Reads the file and prints "You need to buy: [item]" for each item
3. Counts and displays the total number of items

## Task 13: Temperature Logger
Write a program that:
1. Asks the user for temperatures for 5 days
2. Writes each temperature to `temps.txt` with the day number. Format: "Day 1: 22°C"
3. Reads the file and calculates the average temperature

## Task 14: Movie Collection Tuple
Create a tuple with 3 movies and their release years:

```python
movies = (("Inception", 2010), ("Matrix", 1999), ("Interstellar", 2014))
```

Print:
- The oldest movie
- All movie titles
- Try to change a year (show it causes an error)

## Task 15: Unique Hobbies Set
Two friends share their hobbies:

```python
alex_hobbies = {"reading", "gaming", "cooking", "hiking"}
sam_hobbies = {"gaming", "hiking", "photography", "music"}
```

Find and print:
- Hobbies both enjoy (intersection)
- Hobbies only Alex enjoys
- All unique hobbies combined

## Task 16: Simple Grade Book Dictionary
Create a dictionary for 3 students and their scores:

```python
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
```

Perform these tasks:
- Add a new student "Diana" with score 88
- Update Bob's score to 95
- Print all students with scores above 80
- Calculate and print the average score

## Task 17: Contact Book
Create a contact dictionary:

```python
contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Friend": "555-9012"
}
```

Write a program that:
- Adds a new contact
- Looks up a contact by name
- Prints all contacts in format "Name: Number"

## Task 18: Counting Lines in a File
Write a Python program that reads the `DATA/Les_Brown.txt` file and counts how many lines are in the file.

**Steps:**
1. Open the `DATA/Les_Brown.txt` file in read mode.
2. Read all lines into a list.
3. Use the `len()` function to count the number of lines.
4. Print the total number of lines.

## Task 19: Finding "Dream" Sentences in Les_Brown.txt
From the `DATA/Les_Brown.txt` file, read the content and identify all sentences that contain the word "dream". Write these sentences to a new file called `dream_sentences.txt`.

**Steps:**
1. Open and read the content of `DATA/Les_Brown.txt`.
2. Split the text into sentences.
3. Filter out sentences that contain the word "dream" (case-insensitive).
4. Write these sentences into the new file `dream_sentences.txt`.

## Task 20: Identifying and Converting Text
From the `DATA/Les_Brown.txt` file, read all content. Identify the part of the text that resonates with you, convert that part into uppercase, and write the modified text to a new file called `posiability.txt`.

**Steps:**
1. Open and read the contents of `DATA/Les_Brown.txt`.
2. Find the section of the text that resonates with you.
3. Convert the identified section to uppercase.
4. Replace the original section with the uppercase version in the text.
5. Write the updated text into a new file called `posiability.txt`.

## Task 21: Adding Line Numbers to Python Zen
Create a Python program that reads the content from the `DATA/python_zen.txt` file and adds line numbers to each line. Each line in the output file should start with a line number, followed by a dot and a space, and then the original line from the input file. Skip numbering the first line as it is the title. Save the result into a new file called `numbered_zen.txt`.

**Steps:**
1. Open the `DATA/python_zen.txt` file for reading.
2. Skip the first line (which is the title) when numbering.
3. For each subsequent line, prepend the line number followed by a dot and a space.
4. Write the modified content to a new file called `numbered_zen.txt`.

## Task 22: Reversing Clothing Stock List
Create a program that reads the `DATA/clothing_stock.txt` file and stores all the clothing items in a list. Then reverse the order of the items and write the reversed list into a new file called `reversed_clothing_stock.txt`.

**Steps:**
1. Read all clothing items into a list.
2. Reverse the list.
3. Write the reversed list into a new file.

## Task 23: Identifying Duplicate Entries in Clothing Stock
Create a program that reads the `DATA/clothing_stock.txt` file and identifies if there are any duplicate entries (both item and size). Use a set to find and print these duplicates.

**Steps:**
1. Read the file and store each item in a set.
2. Keep track of duplicate entries.
3. Print any duplicates found.

## Task 24: Counting Different Sizes per Clothing Item
Create a Python program that reads data from the `DATA/clothing_stock.txt` file and counts how many different sizes of each clothing item are available. Store this in a dictionary and print it.

**Steps:**
1. Read the file and extract both clothing items and sizes.
2. Count how many different sizes exist for each item.
3. Store the results in a dictionary and print it.

## Task 25: Managing Study Groups
You are responsible for managing a study group for a course. Each student can be part of multiple study groups, and you need to track which groups a student is enrolled in. Students can join or leave study groups. What data structure would you choose to manage this efficiently, and why?

**Example data:**
```python
{"John": ["Math", "Physics"], "Emily": ["Physics", "Biology"], "Alex": ["Math"]}
```

**Steps:**
1. Choose a data structure that allows quick access to the groups each student belongs to.
2. Write a program that lets students join and leave study groups.
3. Implement a function to display all groups a student is part of.

## Task 26: Managing and Shuffling Playlists
You are developing a music player that lets users create a playlist and shuffle it. Users should be able to add songs, remove songs, and shuffle the playlist randomly. What data structure would you use to represent the playlist, and why?

**Example data:**
```python
["Song A", "Song B", "Song C", "Song D"]
```

**Steps:**
1. Choose a data structure that allows easy addition, removal, and shuffling of songs.
2. Write a program that simulates playlist operations (add, remove, shuffle).
3. Let users shuffle the playlist and display the new order.

## Task 27: Counting Words in Les_Brown.txt
Read the content from `DATA/Les_Brown.txt`, and then count the number of occurrences of each word in the text. Write the word count results to a new file called `word_count.txt`.

**Steps:**
1. Open and read the contents of `DATA/Les_Brown.txt`.
2. Split the content into words and count the frequency of each word.
3. Write the word count in the format: `word: count` to a new file called `word_count.txt`.

## Task 28: Removing Duplicates from Clothing Stock
Write a Python program that reads the `DATA/clothing_stock.txt` file, removes any duplicate entries of clothing items with the same size, and then writes the unique entries to a new file called `unique_clothing_stock.txt`.

**Steps:**
1. Read the clothing items into a list.
2. Remove duplicates by storing them in a set.
3. Write the unique entries to a new file called `unique_clothing_stock.txt`.

## Task 29: Splitting Clothing Stock by Size
Create a Python program that reads the `DATA/clothing_stock.txt` file and splits the clothing items into separate sets based on their size (e.g., all XS items in one set, all M items in another set). Print each set.

**Steps:**
1. Read the file and separate items by their size.
2. Store each size in a different set.
3. Print each set of items.

## Task 30: Managing Event Tickets
You are developing a system to manage event tickets for concerts or sports events. Each event has a limited number of tickets available, and users can purchase tickets if they are still available. You need to track which users have purchased tickets for specific events and how many are still available. What data structure would you use for this task, and why?

**Example data:**
- Available tickets: `{"Concert": 100, "Football Game": 50, "Theater Show": 75}`
- Purchasers: `{"Concert": ["John", "Emily"], "Football Game": ["Alex"], "Theater Show": ["Sam", "John"]}`

**Steps:**
1. Choose a data structure to track ticket availability and purchasers efficiently.
2. Write a program that handles ticket purchases and updates the list of purchasers.
3. Implement functions to check availability and view who has purchased tickets.

## Task 31: Personal Finance App
You are creating a personal finance app that allows users to categorize their expenses and track spending by category (e.g., food, entertainment, travel). Users can add expenses, remove expenses, and see a summary of their spending. What data structure would you choose to store and organize the expenses, and why?

**Example data:**
```python
{"Food": [25, 40, 15], "Entertainment": [50, 20], "Travel": [300, 150]}
```

**Steps:**
1. Choose a data structure that lets users easily add and track expenses by category.
2. Write a program that allows users to input expenses, remove them, and view their total spending by category.
3. Implement a function to display a summary of all spending.

## Task 32: Pure Python EDA – Custom File Parser
Write a function `parse_csv_to_dicts(filepath)` that reads any comma-separated file and returns a list of dictionaries. Then use your function to read `DATA/sample_data.csv` and perform some data analysis.

## Task 33: Safe Number Input

Write a program that keeps asking the user to enter a whole number until they enter a valid one. Use `try`/`except ValueError` so the program prints a friendly message instead of crashing, then prints the number squared.

## Task 34: Safe File Reader

Ask the user for a file name and print its contents. Use `try`/`except` to handle `FileNotFoundError` (print "File not found") and any other error (print a general error message). Test it with `DATA/Les_Brown.txt` and with a file name that does not exist.

## Task 35: Account Balances
The file `DATA/accounts1.txt` has one account per line in the format `id surname balance` (e.g. `101 Smith 150.75`).
1. Read the file and store each account in a dictionary (id → `{"name": ..., "balance": ...}`).
2. Print every account in a formatted table and the total of all balances.
3. Print the name of the account with the highest balance.
4. Use `try`/`except` so the program prints a friendly message if the file is missing.

## Task 36: Ages from a CSV File
The file `DATA/ages.csv` has the header `name,age`.
1. Read the file with `with open(...)` and `split(",")` (skip the header).
2. Store the data as a list of tuples `(name, age)`.
3. Print the oldest and youngest person and the average age.
4. Write the people older than 20 to a new file `adults.txt`, one `name: age` per line.

## Task 37: Appending to Files
Using `DATA/test.txt` and `DATA/user_info.txt`:
1. Read both files and print their contents.
2. Append a new line to `user_info.txt` (e.g. your course) without erasing the existing text.
3. Read the file again and print how many lines and how many characters it contains.
