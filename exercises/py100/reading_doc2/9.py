"""
TypeError
The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)
What does a TypeError indicate? Try running the above code, then use the resulting error message to determine exactly what is wrong. (You don't have to fix this code.)
"""
# TypeError means that an operation or function is applied to an object of inappropriate type.

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet) + 5