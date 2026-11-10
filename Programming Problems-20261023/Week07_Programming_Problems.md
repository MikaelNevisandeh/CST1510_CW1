# Week 7 – Strings and Text Manipulation – Programming Problems

## Task 1: Clean Survey Responses
You received messy survey responses. Clean each response by:
1. Removing leading/trailing whitespace
2. Converting to lowercase
3. Printing the cleaned version

**Methods to use:** `strip()`, `lower()`

```python
responses = [
    "  VERY SATISFIED  ",
    "somewhat happy   ",
    "  NOT Happy  ",
    "   NEUTRAL",
    "  dissatisfied  "
]
```

## Task 2: Validate Student IDs
Write a function `is_valid_id(student_id)` that returns `True` if the student ID:
- Starts with `"M00"`
- Has exactly 9 characters
- The remaining characters after "M00" are all digits

Test it with the list below.

**Methods to use:** `startswith()`, `len()`, `isdigit()`

```python
student_ids = ["M00123456", "M0012345", "X00123456", "M00ABCDEF", "M00987654"]
```

## Task 3: Parse CSV Data
Split each row of CSV data and print a formatted summary.

**Methods to use:** `split()`, f-strings

```python
csv_data = [
    "Alice,25,London,Data Analyst",
    "Bob,30,Paris,Engineer",
    "Charlie,22,Berlin,Student"
]

# For each row, split by comma and print:
# "Alice is a 25 year old Data Analyst based in London"
```

## Task 4: Count Keywords in Feedback
Count how many times each keyword appears across all feedback. Join all feedback into one string (lowercase), then count each keyword.

**Methods to use:** `lower()`, `count()`

```python
feedback = [
    "The product quality is great",
    "Fast delivery but poor quality",
    "Great product and great delivery",
    "Quality could be better"
]

keywords = ['great', 'quality', 'delivery']
```

## Task 5: Format Customer Names
Clean and format each name to **Title Case**, then create an email by taking the first name (lowercase) + `.` + surname (lowercase) + `@company.com`.

**Methods to use:** `strip()`, `title()`, `lower()`, `split()`, string concatenation

```python
raw_names = [
    "  JOHN smith  ",
    "mary JOHNSON",
    "  bob WILSON  "
]

# Expected output:
# John Smith → john.smith@company.com
# Mary Johnson → mary.johnson@company.com
# Bob Wilson → bob.wilson@company.com
```

## Task 6: Classify Server Log Entries
Write a function `classify_logs(logs)` that takes a list of log strings and:
1. Counts how many `ERROR`, `INFO`, and `WARNING` entries there are
2. Extracts and prints the **timestamp** from each entry
3. Returns the three counts

**Methods to use:** `startswith()`, `split()`, `strip()`

```python
logs = [
    "[14:32:05] ERROR: Disk full",
    "[14:32:10] INFO: Server started",
    "[14:33:01] WARNING: High memory usage",
    "[14:33:15] INFO: Backup complete",
    "[14:34:00] ERROR: Connection refused",
    "[14:35:22] WARNING: CPU at 90%"
]
```

## Task 7: Simple Sentiment Analyser
Write a function `analyse_sentiment(reviews)` that:
1. Cleans each review (`strip()`, `lower()`)
2. Classifies it as **positive**, **negative**, or **neutral** using keyword lists
3. Returns a dictionary with counts and a list of which reviews are negative

**Methods/Functions to use:** `strip()`, `lower()`, `any()`, `in`

```python
reviews = [
    "  AMAZING product, Love it!!!  ",
    "terrible experience   ",
    "  It was okay  ",
    "WORST purchase ever",
    "  fantastic quality  ",
    "poor customer service",
    "  Not bad, not great  "
]

positive_words = ['amazing', 'love', 'fantastic', 'great', 'excellent']
negative_words = ['terrible', 'worst', 'poor', 'awful', 'horrible']
```

## Task 8: Data Validation Pipeline
Write a function `validate_record(record)` that takes a CSV string and checks:
1. It has exactly 4 fields (name, age, email, phone)
2. Name contains only letters and spaces
3. Age is a valid number between 18 and 100
4. Email contains `@` and `.`
5. Phone starts with `+` or `0`

Return a list of **error messages** (empty list = valid record).

Use `all()` to check if ALL fields are non-empty first.

**Methods to use:** `split()`, `isdigit()`, `isalpha()`, `startswith()`, `all()`

```python
records = [
    "Alice Smith,25,alice@email.com,+447123456789",
    "Bob,abc,bob@email,07123456789",
    "Charlie123,30,charlie@mail.com,447123456789",
    ",22,missing@mail.com,+440000000000"
]
```

## Task 9: Word Frequency Counter
Write a function `word_frequency(text)` that:
1. Converts text to lowercase
2. Removes punctuation (`.`, `,`, `!`, `?`)
3. Splits into words
4. Returns a **dictionary** of word → count
5. Prints the top 5 most common words

**Methods to use:** `lower()`, `replace()`, `split()`, `count()`

```python
text = """Data science is the study of data. Data scientists use data to find patterns.
Machine learning is a part of data science. Scientists study data every day!
The science of data is growing, and data is everywhere."""
```

**Extension:** read `DATA/Les_Brown.txt` with `open()` and run `word_frequency` on its contents.

## Task 10: Password Strength Checker
Write a function `check_password(password)` that scores a password (0–5):

| Rule | Points |
|------|--------|
| At least 8 characters | +1 |
| Contains uppercase letter | +1 |
| Contains lowercase letter | +1 |
| Contains a digit | +1 |
| Contains a special character (`@#$%!`) | +1 |

Print the score and a label: **Weak** (0-2), **Medium** (3-4), **Strong** (5).

If the password contains a space, print a message and reject it.

**Methods to use:** `len()`, `isupper()`, `islower()`, `isdigit()`, `any()`

```python
test_passwords = [
    "hello",
    "Hello123",
    "My Pass!",
    "Str0ng@Pass",
    "12345678"
]
```

## Task 11: Caesar Cipher Encoder & Decoder
Write **two** functions:
1. `encode(text, key)` — shifts each letter forward by `key` positions
2. `decode(text, key)` — reverses the shift to get the original text

Rules:
- Only shift letters (a-z). Leave spaces, digits, and punctuation unchanged
- Wrap around: `z` shifted by 1 → `a`
- Preserve case: uppercase stays uppercase
- Verify: `decode(encode(text, key), key)` should return the original text

**Methods to use:** `ord()`, `chr()`, `isalpha()`, `isupper()`, `islower()`

```python
original = "Hello World! 123"
key = 5
```

## Task 12: Text Data Cleaning Pipeline
Build a `clean_dataset(records)` function that processes raw text records. Each record is a string with fields separated by `|`.

The function should:
1. Skip records where **any** field is empty
2. Clean names to **Title Case** and remove extra spaces
3. Validate that age is a number (18–120)
4. Validate email format (contains `@` and has a `.` after the `@`)
5. Standardise country names to **uppercase**
6. Return two lists: `valid_records` and `invalid_records` with reasons

**Methods to use:** `split()`, `strip()`, `title()`, `upper()`, `isdigit()`, `all()`, `find()`

```python
raw_data = [
    "  john SMITH  | 25 | john.smith@email.com | united kingdom ",
    "  MARY  johnson | abc | mary@email | france",
    " | 30 | test@test.com | germany",
    "  bob wilson  | 17 | bob@mail.com | spain  ",
    "  alice Brown  | 28 | alice.b@data.org | italy  ",
    "charlie DAVIS | 35 | | usa"
]
```

## Task 13: Analyse & Report on Text Corpus
Write a function `text_report(text)` that produces a complete analysis:

1. **Basic stats:** Total characters, words, sentences, average word length
2. **Character breakdown:** Count of uppercase, lowercase, digits, spaces, punctuation
3. **Top 5 words:** Most frequently used words (exclude common words: 'the', 'a', 'is', 'and', 'of', 'to', 'in')
4. **Longest and shortest words**
5. **Print a formatted report** using string formatting

**Methods to use:** `split()`, `lower()`, `replace()`, `count()`, `isupper()`, `islower()`, `isdigit()`, `isspace()`, `join()`, `center()`, `ljust()`

```python
corpus = """Artificial Intelligence is transforming every industry. From healthcare to finance,
AI systems are making decisions that affect millions of people. Machine Learning,
a subset of AI, enables computers to learn from data without being explicitly programmed.
Deep Learning takes this further with neural networks inspired by the human brain.
In 2024, Large Language Models like GPT have shown remarkable abilities in understanding
and generating human language. The future of AI is both exciting and challenging."""
```

**Extension:** read `DATA/python_zen.txt` with `open()` and produce a `text_report` for it.

## Task 14: Build a Simple Search Engine
Create a function `search(documents, query)` that:
1. Takes a list of document strings and a search query
2. Returns documents **ranked** by how many times the query words appear
3. The search should be **case-insensitive**
4. If query has multiple words, count matches for **each** word
5. Show a relevance score and highlight which query words were found

**Methods to use:** `lower()`, `split()`, `count()`, `any()`, `all()`, `strip()`, `replace()`

```python
documents = [
    "Python is a great programming language for data science and machine learning",
    "Data analysis with Python involves cleaning and processing large datasets",
    "Machine learning models can predict outcomes from historical data",
    "Web development with JavaScript and HTML is different from data work",
    "Python data science libraries include NumPy and Pandas for data processing"
]

# Test searches
search(documents, "data science")
search(documents, "Python machine learning")
```
