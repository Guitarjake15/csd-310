import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Guitarjake15!",
        database="travel_company"
    )

    cursor = conn.cursor()

    query = """
    SELECT
        Location_Name,
        COUNT(Booking_ID) AS Total_Bookings
    FROM Locations
    LEFT JOIN Trips
        ON Locations.Location_ID = Trips.Location_ID
    LEFT JOIN Bookings
        ON Trips.Trip_ID = Bookings.Trip_ID
    GROUP BY Locations.Location_ID, Location_Name
    ORDER BY Total_Bookings DESC;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nOUTLAND ADVENTURES")
    print("BOOKING TRENDS REPORT")
    print("-" * 50)

    if not rows:
        print("No booking data found.")
    else:
        for row in rows:
            print(
                f"Location: {row[0]} | "
                f"Bookings: {row[1]}"
            )

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print("Database Error:", err)