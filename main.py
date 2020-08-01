import controller

while(1):
    print('1. Add a DVD')
    print('2. Search')
    print('3. Modify a DVD')
    print('4. Delete a DVD')
    print('5. Exit')
    choice = int(input())

    if choice == 1:
        TITLE = input('Enter the title: ')
        TITLE = '' if TITLE is None else TITLE
        STAR_NAME = input('Enter the star name: ')
        STAR_NAME = '' if STAR_NAME is None else STAR_NAME
        YOR = input('Enter the year of release(YYYY-MM-DD): ')
        YOR = '' if YOR is None else YOR
        GENRE = input('Enter the genre: ')
        GENRE = '' if GENRE is None else GENRE
        genre = ['HORROR', 'ROMANCE', 'COMEDY', 'ACTION', 'DRAMA', '']
        if GENRE.upper() not in genre:
            print('Genre not allowed. You must enter one from horror, romance, comedy, action, and drama')
            continue
        else:
            response = controller.add(TITLE=TITLE, STAR_NAME=STAR_NAME, YOR=YOR, GENRE=GENRE.upper())
            print(response)
            continue

    if choice == 2:
        TITLE = input('Enter the title: ')
        TITLE = '' if TITLE is None else TITLE
        STAR_NAME = input('Enter the star name: ')
        STAR_NAME = '' if STAR_NAME is None else STAR_NAME
        YOR = input('Enter the year of release(YYYY-MM-DD): ')
        YOR = '' if YOR is None else YOR
        GENRE = input('Enter the genre: ')
        GENRE = '' if GENRE is None else GENRE
        genre = ['HORROR', 'ROMANCE', 'COMEDY', 'ACTION', 'DRAMA', '']
        if GENRE.upper() not in genre:
            print('Genre not allowed. You must enter one from horror, romance, comedy, action, and drama')
            continue
        else:
            response = controller.search(TITLE=TITLE, STAR_NAME=STAR_NAME, YOR=YOR, GENRE=GENRE.upper())
            print(response)
            continue

    if choice == 3:
        TITLE = input('Enter the title: ')
        TITLE = '' if TITLE is None else TITLE
        STAR_NAME = input('Enter the star name: ')
        STAR_NAME = '' if STAR_NAME is None else STAR_NAME
        YOR = input('Enter the year of release(YYYY-MM-DD): ')
        YOR = '' if YOR is None else YOR
        GENRE = input('Enter the genre: ')
        GENRE = '' if GENRE is None else GENRE
        genre = ['HORROR', 'ROMANCE', 'COMEDY', 'ACTION', 'DRAMA', '']
        if GENRE.upper() not in genre:
            print('Genre not allowed. You must enter one from horror, romance, comedy, action, and drama')
            continue
        else:
            response = controller.modify(TITLE=TITLE, STAR_NAME=STAR_NAME, YOR=YOR, GENRE=GENRE.upper())
            print(response)
            continue

    if choice == 4:
        TITLE = input('Enter the title: ')
        TITLE = '' if TITLE is None else TITLE
        response = controller.delete(TITLE=TITLE)
        print(response)
        continue

    if choice == 5:
        break
    else:
        print('Invalid choice. Try again')
        continue

