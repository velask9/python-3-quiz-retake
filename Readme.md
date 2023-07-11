# Python Quiz Coding Challenge

 Weeks II & III

### Instructions
1. Fork and clone this repository.
2. Familiarize yourself with the file structure of this repository.
3. Achieve the following objectives by ***carefully reading what is being asked and executing***.

### Objectives

You are given a file named `users.txt`. Your goal is to find the user with the most rewards points.

# Problem: Name checker
Implement a function called `find_best_user()` (in `reward_check.py`) which accepts a name of a plain text file to validate. This function parses the [users.txt](users.txt) file and **finds the user with the highest REWARDS POINTS**. 

**find_best_user() returns the first name of the user with the highest rewards points.** This function is consumed in the following manner:

Test Case:
```python
def test():
    result = find_best_user("users.txt")
    print(f"Congratulations {result}! You have a lot of rewards points, would you like to spend them?")

test()
```

Output:
```
Invalid first name: 'B1ll'
```

- This tests your ability to read files, select the correct data, manipulate strings and use Exceptions in python.

**GLHF :)**
