# Recursive function to check if a number is even 🤪
def recursive_is_even(n):
  if n == 0:
    return True
  elif n == 1:
    return False
  elif n > 0:
    return recursive_is_even(n - 2)
  else:
    return recursive_is_even(n + 2)

# Test cases
print(f"recursive_is_even(2): {recursive_is_even(2)}")
print(f"recursive_is_even(3): {recursive_is_even(3)}")
print(f"recursive_is_even(1000): {recursive_is_even(1000)}")
print(f"recursive_is_even(1001): {recursive_is_even(1001)}")
print(f"recursive_is_even(-2): {recursive_is_even(-2)}")
print(f"recursive_is_even(-3): {recursive_is_even(-3)}")
print(f"recursive_is_even(-1000): {recursive_is_even(-1000)}")
print(f"recursive_is_even(-1001): {recursive_is_even(-1001)}")
