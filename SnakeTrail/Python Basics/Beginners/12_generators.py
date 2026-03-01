def values():
    yield 1
    yield 2
    yield 3

for value in values():
    print(value)

def gen_prime(start, end):
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                yield i

a = 10
b = 50
print(f"Prime numbers between {a} and {b}:")
for prime in gen_prime(a, b):
    print(prime)                    

#Generators are a powerful tool in Python that allow you to create iterators in a more memory-efficient way. They are defined using the `yield` keyword, which allows the function to return a value and pause its execution, resuming from the same point when the next value is requested. This makes generators particularly useful for working with large datasets or infinite sequences, as they generate values on-the-fly rather than storing them all in memory at once.    
# 1 value generated at a time, and the state of the generator is preserved between calls, allowing for efficient iteration over potentially large or infinite sequences.
#No resuable data.


def gen_countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in gen_countdown(5):
    print(number)

def gen_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci sequence:")
for num in gen_fibonacci(100):
    if num > 100:
        print(f"The first fibonacci number greater than 100 is {num}")
        break