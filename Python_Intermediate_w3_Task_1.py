while True:
    filename_read = input('Enter file to read ')
    try:
        with open(filename_read, 'r') as file_read:
            text = file_read.readlines()
    except FileNotFoundError:
        print('There isn\'t such filename')
    else:
        filename_write = input('Enter file to write ')
        with open(filename_write, 'w') as file_write:
            for i in range(1, len(text) + 1):
                file_write.write(f'{i}: {text[i - 1]}')
        break



