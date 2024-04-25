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
numbers[0]      # 1
```

#### Conversions

- The `int()` BIF converts the strings to numbers

```python
string_number = "16"
number = int(string_number)
print(number)
# 16
```
