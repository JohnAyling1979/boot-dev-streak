import sys

# 🤪
def recursive_is_even(n):
  if n == 0:
    return True
  elif n == 1:
    return False
  elif n > 0:
    return recursive_is_even(n - 2)
  else:
    return recursive_is_even(n + 2)

# 🧐
def last_digit_is_even(n):
  even_digits = "02468"
  s = str(n)

  if s == "":
    return True
  elif s[-1] in even_digits:
    return True
  else:
    return False

# 🤓
def is_even(n):
  return n % 2 == 0

# Test cases
sys.setrecursionlimit(10000000)

print(f"recursive_is_even(2): {recursive_is_even(2)}")
print(f"recursive_is_even(3): {recursive_is_even(3)}")
print(f"recursive_is_even(1000): {recursive_is_even(1000)}")
print(f"recursive_is_even(1001): {recursive_is_even(1001)}")
print(f"recursive_is_even(-2): {recursive_is_even(-2)}")
print(f"recursive_is_even(-3): {recursive_is_even(-3)}")
print(f"recursive_is_even(-1000): {recursive_is_even(-1000)}")
print(f"recursive_is_even(-1001): {recursive_is_even(-1001)}")
print(f"recursive_is_even(10000000): {recursive_is_even(10000000)}")

print("--------------------------------")

print(f"last_digit_is_even(2): {last_digit_is_even(2)}")
print(f"last_digit_is_even(3): {last_digit_is_even(3)}")
print(f"last_digit_is_even(1000): {last_digit_is_even(1000)}")
print(f"last_digit_is_even(1001): {last_digit_is_even(1001)}")
print(f"last_digit_is_even(-2): {last_digit_is_even(-2)}")
print(f"last_digit_is_even(-3): {last_digit_is_even(-3)}")
print(f"last_digit_is_even(-1000): {last_digit_is_even(-1000)}")
print(f"last_digit_is_even(-1001): {last_digit_is_even(-1001)}")
print(f"last_digit_is_even(10000000): {last_digit_is_even(10000000)}")

print("--------------------------------")

print(f"is_even(2): {is_even(2)}")
print(f"is_even(3): {is_even(3)}")
print(f"is_even(1000): {is_even(1000)}")
print(f"is_even(1001): {is_even(1001)}")
print(f"is_even(-2): {is_even(-2)}")
print(f"is_even(-3): {is_even(-3)}")
print(f"is_even(-1000): {is_even(-1000)}")
print(f"is_even(-1001): {is_even(-1001)}")
print(f"is_even(10000000): {is_even(10000000)}")
