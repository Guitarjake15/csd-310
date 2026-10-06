"""
Jacob Richman
CSD-310
Module 6 Assignment
Movies: Table Queries
"""

import mysql.connector

# Connect to database

db = mysql.connector.connect(
    host="localhost",
    user="movies_user",
    password="popcorn",
    database="movies"
)

cursor = db.cursor()

# Display Studio Records

print("\n-- DISPLAYING Studio RECORDS --\n")

cursor.execute("SELECT * FROM studio")

studios = cursor.fetchall()

for studio in studios:
    print(f"Studio ID: {studio[0]}")
    print(f"Studio Name: {studio[1]}")
    print()

# Display Genre Records

print("\n-- DISPLAYING Genre RECORDS --\n")

cursor.execute("SELECT * FROM genre")

genres = cursor.fetchall()

for genre in genres:
    print(f"Genre ID: {genre[0]}")
    print(f"Genre Name: {genre[1]}")
    print()

# Display Films Under 2 Hours

print("\n-- DISPLAYING Short Film RECORDS --\n")

cursor.execute("""
SELECT film_name, film_runtime
FROM film
WHERE film_runtime < 120
""")

films = cursor.fetchall()

for film in films:
    print(f"Film Name: {film[0]}")
    print(f"Runtime: {film[1]}")
    print()

# Display Films Grouped by Director

print("\n-- DISPLAYING Director RECORDS in Order --\n")

cursor.execute("""
SELECT film_name, film_director
FROM film
ORDER BY film_director
""")

directors = cursor.fetchall()

for film in directors:
    print(f"Film Name: {film[0]}")
    print(f"Director: {film[1]}")
    print()

db.close()