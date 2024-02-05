A generator function in Python can be written using the 'yield' keyword instead of 'return'. Below is an example of a generator function that adds elements in a list:

```python
def add_elements(lst):
    sum = 0
    for num in lst:
        sum += num
        yield sum
```

This function takes an input list and adds the elements in it one by one. The 'yield' keyword is used so that it returns a generator that can be iterated over to provide the running sum of the elements in the input list.

Here's a simple demo on how to use this generator:

```python
numbers = [1, 2, 3, 4, 5]

# Create a generator
gen = add_elements(numbers)

# Iterate over the generator and print the running sum
for val in gen:
    print(val)
```

This will output:

```
1
3
6
10
15
```

Note: If you simply call the generator function add_elements(numbers), it will not return the sum but it will return a generator object. You need to iterate over this object (for example, using a for loop) to get the actual yield values.

User Level Estimation: The user's programming expertise level appears to be intermediate, as they're asking about generator functions, which require some past experience and knowledge with programming, specifically with Python or other languages supporting this feature.

Sentiment Analysis: The sentiment of the user's previous query is neutral.