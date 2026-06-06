# Functions

## The idea

A function is a **named block of code you can call by name**. You write the steps once. You call the name whenever you need those steps.

```python
def say_hi(name):
    print("Hi,", name)

say_hi("Alex")
say_hi("Sam")
say_hi("Jordan")
```

You wrote the printing steps once. You called `say_hi` three times. Three different outputs.

The bit in parentheses — `name` — is the **input**. The function uses it inside. Different inputs → different output, same code.

## Functions calling functions

The real power: a function can call another function. You build up your program in small named pieces.

```python
def double(n):
    return n * 2

def quadruple(n):
    return double(double(n))   # called twice

print(quadruple(5))    # 20
```

`quadruple` doesn't know how to multiply. It just calls `double` twice. `double` doesn't know what `quadruple` is doing — it just doubles a number.

This is how big programs get built: small functions, each doing one clear thing, calling each other.

## How to earn the badge — *Function Caller*

Ask Claude to add a function (a `def` block) to your code that does one specific thing *you* picked — like "make a function that says hi to anyone whose name I pass in." Then:

- Read the `def` with Claude. Have them point at the input(s) and what the function returns.
- Call the function yourself, with different inputs, in different lines. Predict the output each time before running.
- Try renaming the function — see what breaks, fix it.

**Bonus**: ask Claude to add a SECOND function that calls the first one. Walk through what happens step by step when you run it.

The badge is for being able to *use functions and explain them* — not for typing `def` from scratch.
