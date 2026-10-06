def show_films(cursor, title):
    print("\n-- {} --".format(title))

    cursor.execute("""
        SELECT film_name AS Name,
               film_director AS Director,
               genre_name AS Genre,
               studio_name AS Studio
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """)

    films = cursor.fetchall()

    for film in films:
        print("Name: {}, Director: {}, Genre: {}, Studio: {}".format(
            film[0], film[1], film[2], film[3]
        ))
# ⭐ Your try block starts HERE
try:
    db = mysql.connector.connect(
        user="root",
        password="Guitarjake15!",
        host="127.0.0.1",
        database="movies"
    )

    cursor = db.cursor()

    # First display
    show_films(cursor, "DISPLAYING FILMS")

    # INSERT
    insert_query = """
    INSERT INTO film (film_name, film_director, genre_id, studio_id)
    VALUES ('Inception', 'Christopher Nolan', 1, 2);
"""
cursor.execute(insert_query)
db.commit()
    """
    cursor.execute(insert_query)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    update_query = """
    UPDATE film
    SET genre_id = 5
    WHERE film_name = 'Alien';
"""
cursor.execute(update_query)
db.commit()

    """
    cursor.execute(update_query)
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # ⭐ DELETE
    delete_query = """
        DELETE FROM film
        WHERE film_name = 'Gladiator';
    """
    cursor.execute(delete_query)
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    print(err)

finally:
    db.close()
