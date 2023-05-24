data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

for data in data_tuple:
  if type(data) == str:
     letters.append(data)
  elif type(data) != float:
    numbers.append(data)

letters.append(numbers.pop(0))
numbers.insert(1, 2)

numbers = tuple(sorted(x**2 for x in numbers))
letters[-2], letters[1] = letters[-2].upper(),letters[1].lower()

letters = tuple (letters[::-1])

print(letters, numbers)