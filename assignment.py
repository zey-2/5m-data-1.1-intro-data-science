# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number):
    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:   # Check if divisible by 3
        return "Fizz"
    elif number % 5 == 0:   # Check if divisible by 5
        return "Buzz"
    return number


# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """
    return sum(x ** 2 for x in numbers)  # Using a generator expression to calculate the sum of squares



# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string):
    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """
    return sum(1 for char in string if char in "aeiouAEIOU")


# Question 4

# Write a function that counts the number of repeated characters in a string.


def count_repeats(string):
    """Returns the max repetition of repeated characters in a string. If there is no repetition, returns 0.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """
    return len([letter for letter in string if string.count(letter) > 1])


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
