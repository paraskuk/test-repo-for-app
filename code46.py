Sure, you can create a generator function in Python that reads multiple files. Here's a simple example:

```python
def file_reader(*filenames):
    for filename in filenames:
        try:
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    yield line
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")

# Usage
for line in file_reader('file1.txt', 'file2.txt', 'file3.txt'):
    print(line)
```

In this function, `file_reader`, it takes in any number of filenames, attempts to open them in read mode one by one, and yield each line of the file. If a file does not exist, it catches the `FileNotFoundError` and informs the user of the missing file, then moves on to the next file. If a file is successfully opened, it reads the file line by line and yields each line. This function can be used to iterate over multiple text files, outputting each line of each file one by one.

Remember to replace 'file1.txt', 'file2.txt', 'file3.txt' with the real filenames that exist and you want to read.

User Level Estimation: Intermediate

Sentiment Analysis: The sentiment of the user's previous query is neutral.