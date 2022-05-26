num_strings = ['15', '100', '55', '42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"\nThe variable num_strings is a {type(num_strings)}"
      f"\nIt contains the elements {num_strings}"
      f"\nThe element {num_strings[0]} is a {type(num_strings[0])}")

print(f"\nThe variable num_ints is a {type(num_ints)}"
      f"\nIt contains the elements {num_ints}"
      f"\nThe element {num_ints[0]} is a {type(num_ints[0])}")

print(f"\nThe variable num_floats is a {type(num_floats)}"
      f"\nIt contains the elements {num_floats}"
      f"\nThe element {num_floats[0]} is a {type(num_floats[0])}")

print(f"\nThe variable num_lists is a {type(num_lists)}"
      f"\nIt contains the elements {num_lists}"
      f"\nThe element {num_lists[0]} is a {type(num_lists[0])}")

print("\nNow sorting num_strings and num_ints...")
print(f"Sorted num_strings: {sorted(num_strings)}")
print(f"Sorted num_ints: {sorted(num_ints)}")
print("\nStrings are sorted alphabetically while integers are sorted numerically!")
