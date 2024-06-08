"""
Practice Problems: Medium 1
Question 1
Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers had video screens.

For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one more hyphen than the line above it. The output should start out like this:

-The Flintstones Rock!
--The Flintstones Rock!
---The Flintstones Rock!
    ...
"""
# # for padding in range(1, 11):
# #   print('-' * padding + 'The Flintstones Rock!') # my

# for padding in range(1, 11):
#     print(f'{"-" * padding}The Flintstones Rock!')

"""
Question 2
Alan wrote the following function, which was intended to return all of the factors of number:

def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop. How can he make this work? Note that we're not looking to find the factors for negative numbers, but we want to handle it gracefully instead of going into an infinite loop.

Bonus Question: What is the purpose of number % divisor == 0 in that code?
"""
# Line number % divisor == 0 checks whether there is a remainder when when dividing number by given divisor. If there is no remainder, then this divisor is number's factor.
# def factors(number):
#     divisor = number
#     result = []
#     while divisor > 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# print(factors(-5))

"""
Question 3
Alyssa was asked to write an implementation of a rolling buffer. You can add and remove elements from a rolling buffer. However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.

She wrote two implementations of the code for adding elements to the buffer:

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer
Is there a difference between these implementations, other than the way she is adding an element to the buffer?
"""
# Yes, there is. In first implementation we mutate the existing list. In second - create a new one.
# def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
#     print(id(buffer))
#     buffer.append(new_element)
#     print(id(buffer))
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer
# add_to_rolling_buffer1([1, 2], 4, 5)

# def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
#     print(id(buffer))
#     buffer = buffer + [new_element]
#     print(id(buffer))
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# add_to_rolling_buffer2([1, 2], 4, 5)

"""
Question 4
What will the following two lines of code output?

print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)
Don't look at the solution before you answer.
"""
# # Floating point imprecision
# print(0.3 + 0.6) # 0.8999999999
# print(0.3 + 0.6 == 0.9) # False

"""
Question 5
What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))
Bonus Question

How can you reliably test if a value is nan?
"""
# # Output will be False: NaN is the only value in Python that is not equal to itself
# # Reliable method to test if value is nan: using math.isnan() method
# nan_value = float("nan")

# print(nan_value == float("nan"))

"""
Question 6
What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)
"""
# # We don't reassign answer variable, so output is 34
# answer = 42

# def mess_with_it(some_number):
#     return some_number + 8

# new_answer = mess_with_it(answer)

# print(answer - 8)

"""
Question 7
One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"
After writing this function, he typed the following code:

mess_with_demographics(munsters)
Before Grandpa could stop him, Spot hit the Enter key with his tail. Did the family's data get ransacked? Why or why not?
"""
# # Yes, data was changed. Since dictionary is a mutable data type, when we pass it as argument, it's a reference to original dict, not copy.
# munsters = {
#     "Herman": {"age": 32, "gender": "male"},
#     "Lily": {"age": 30, "gender": "female"},
#     "Grandpa": {"age": 402, "gender": "male"},
#     "Eddie": {"age": 10, "gender": "male"},
#     "Marilyn": {"age": 23, "gender": "female"},
# }

# def mess_with_demographics(demo_dict):
#     demo_dict['Herman'] = 3

# mess_with_demographics(munsters)
# print(munsters)