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

Ask Claude to write a small script that uses a variable in a way that **matters** — a value that changes, or that other lines read from. You decide what the variable should be called and what it stores.

Then:
- Read the code with Claude. Have them point at the variable each time it shows up.
- Change the variable's starting value yourself. Predict what'll be different. Run it. Were you right?
- Bonus: rename the variable to something different across the whole file — see if the program still works the same.

The badge is for *understanding what the variable does* and *predicting how changes ripple through* — not for writing from scratch.
