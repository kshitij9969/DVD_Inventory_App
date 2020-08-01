import mysql.connector

db = ''


def setup():
    global db
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mumbai@123',
        db='dvddb'
    )


def add(TITLE, STAR_NAME, YOR, GENRE):
    setup()
    global db
    cursor = db.cursor()
    query = 'INSERT INTO DVD_TABLE ( '
    attributes = {'TITLE': TITLE, 'STAR_NAME': STAR_NAME, 'YOR': YOR, 'GENRE': GENRE}

    for i in attributes:
        if attributes[i]:
           query += i + ','
    else:
        query = query[:-1]
        query += ')'
    query = query + ' VALUES ( '
    for i in attributes:
        if attributes[i]:
            query += "'" + str(attributes[i]) + "'" + ', '
    else:
        query = query[:-2]
        query += ')'
    try:
        cursor.execute(query)
        db.commit()
        print('successfully added')
    except:
        db.rollback()
        print('error adding to the database, try again!')


def search(TITLE, STAR_NAME, YOR, GENRE):
    setup()
    global db
    cursor = db.cursor()
    query = 'SELECT * FROM DVD_TABLE WHERE '
    attributes = {'TITLE': TITLE, 'STAR_NAME': STAR_NAME, 'YOR': YOR, 'GENRE': GENRE}
    for i in attributes:
        if attributes[i]:
            query += (i + '=' + "'" +str(attributes[i]))+ "'"  + ' AND '
    else:
        query = query[:-4]
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except:
        return 'couldn\'t search, try again'


def modify(TITLE, STAR_NAME, YOR, GENRE):
    setup()
    global db
    cursor = db.cursor()
    query = 'UPDATE DVD_TABLE SET '
    attributes = {'TITLE': TITLE, 'STAR_NAME': STAR_NAME, 'YOR': YOR, 'GENRE': GENRE}
    for i in attributes:
        if attributes[i]:
            query += (i + '=' + "'" + attributes[i] + "'" + ", ")
    else:
        query = query[:-2]
        query += (' WHERE TITLE = ' + "'" + attributes['TITLE'] + "'")

    try:
        cursor.execute(query)
        db.commit()
        print('updated successfully!')
    except:
        db.rollback()
        return 'couldn\'t update try again'


def delete(TITLE):
    setup()
    global db
    cursor = db.cursor()
    query = 'DELETE FROM DVD_TABLE WHERE TITLE = ' + "'" + str(TITLE) + "'"
    try:
        cursor.execute(query)
        db.commit()
        return 'deleted successfully'
    except:
        return 'cannot delete try again'
