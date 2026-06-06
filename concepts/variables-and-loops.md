# Variables and Loops

## Variables — names for things

A variable is a **name you give to a value** so you can use it later. That's it.

```python
name = "Alex"
print("Hi", name)
```

You said "the value `Alex` is called `name`." Now anywhere you write `name`, the computer reads `Alex`.

Why bother? Because you can change the value once, and every place that uses the name updates automatically:

```python
score = 0
print(score)        # 0
score = score + 10
print(score)        # 10
```

## Loops — doing things many times

A loop says "do this block of code over and over until I tell you to stop."

```python
for i in range(5):
    print("hello", i)
```

Output:
```
hello 0
hello 1
hello 2
hello 3
hello 4
```

The variable `i` takes a different value each time. That's the magic — variables + loops let one short piece of code do a lot of work.

## How to earn the badge — *Variable Whisperer*

In a file *you* wrote (not a template), use a variable that **the program depends on**. Not just a value you set once — a value that changes, or that other lines read from.

Example: a script that asks the user a number, stores it in a variable, then prints something based on it. Or a loop that builds up a list.

Show Claude.
