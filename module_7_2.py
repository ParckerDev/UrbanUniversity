def custom_write(file_name: str, strings: list):
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}
        for index, string in enumerate(strings):
            strings_positions[(index + 1, file.tell())] = string
            file.write(string + '\n')
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)