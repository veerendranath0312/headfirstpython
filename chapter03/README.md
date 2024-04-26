# Learnings form Chapter 02

#### Read and close a file using `with` and `open()`. 

- The advantage of `with` keyword is that it automatically closes the file after reading. You don't need to close it externally.
- The `open()` function takes the path of a file that needs to be opened and return a stream. Raise OSError upon failure.
- The `readlines()` method returns the contents of the file as a list of strings.
- Output: `['Contents of the file']`

```python
FILEPATH = "path/to/your/file.txt"

with open(FILEPATH) as file:
    lines = file.readlines()
```

#### Strings

- A `string` is an another data type in Pyhton.
- Indexing starts from `0`.
- Below are some useful string methods:

```python
# Return a list of the substrings in the string, using sep as the separator string.
"1:27.95,1:21.07,1:30.96".split(",")     # ["1:27.95", "1:21.07", "1:30.96"]

# Return a str with the given suffix string removed if present.
"filename.txt".removesuffix(".txt")      # "filename"

# Return a copy of the string with leading and trailing whitespace removed.
"some text\n".strip()                    # "some text"
```

#### Lists

- Lists are the most important and powerful data type in Python.
- Indexing starts from `0`.
- Below are some useful list methods:

```python
numbers = [1, 2, 3, 4, 5]

# Accessing an item of a list
numbers[0]             # 1

# Get the length of a list
num_length = len(numbers)
print(num_length)      # 5

# Append object to the end of the list.
numbers.append(6)      # [1, 2, 3, 4, 5, 6]
```

#### Conversions

- The `int()` BIF converts the strings to numbers.
- The `str()` BIF converts its argument to a string.
- The `round()` BIF round a number to a given precision in decimal digits.

```python
string_number = "16"
number = int(string_number)
print(number)              # 16

number = 12
str_number = str(number)
print(str_number)          # "12"

dec = 20.2345
rounded = round(dec, 2)    # 20.23

```
#### for loops... while loops...

```python
numbers = [1, 2, 3]

# for loop...
for num in nums:
    print(num)

# while loop...
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
```