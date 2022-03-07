'''Wahooo'''

max = 0
max_book=None

print('1 = Old Testament\n2 = New Testament\n3 = Book of Mormon\n4 = Doctrine and Covenants\n5 = Pearl of Greatest prices ')
picker = input('Which book of scripture would you like to learn more about?\n')

with open('books_and_chapters.txt') as books:
    for i in books:
        clean_book = i.strip()
        line = clean_book.split(':')
        if picker == '3':

            if line[2] == 'Book of Mormon':
                
                print(f'Scripture: {line[2]}, Book: {line[0]}, Chapters: {line[1]}')
                if int(line[1]) > max:
                    max=int(line[1])
                    max_book = line[0]
        elif picker == '1':
             
            if line[2] == 'Old Testament':
                
                print(f'Scripture: {line[2]}, Book: {line[0]}, Chapters: {line[1]}')
                if int(line[1]) > max:
                    max=int(line[1])
                    max_book = line[0]
        elif picker == '2':
             
            if line[2] == 'New Testament':
                
                print(f'Scripture: {line[2]}, Book: {line[0]}, Chapters: {line[1]}')
                if int(line[1]) > max:
                    max=int(line[1])
                    max_book = line[0]
        elif picker == '4':
             
            if line[2] == 'Doctrine and Covenants':
                
                print(f'Scripture: {line[2]}, Book: {line[0]}, Chapters: {line[1]}')
                if int(line[1]) > max:
                    max=int(line[1])
                    max_book = line[0]
        elif picker == '5':
             
            if line[2] == 'Pearl of Great Price':
                
                print(f'Scripture: {line[2]}, Book: {line[0]}, Chapters: {line[1]}')
                if int(line[1]) > max:
                    max=int(line[1])
                    max_book = line[0]

print(f'{max_book} has the the most chapters at {max} ')


