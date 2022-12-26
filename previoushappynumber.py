n=int(input('Enter any number:'))
def is_happy(n):
    max_iterations = 100
    sum_squares = 0
    while sum_squares != 1 and max_iterations > 0:
        sum_squares = 0
        while n > 0:
            digit = n % 10
            sum_squares += digit * digit
            n //= 10
        max_iterations -= 1
    return sum_squares == 1

def previous_happy(n):
    while not is_happy(n):
        n -= 1
    return n

print(previous_happy(n))
