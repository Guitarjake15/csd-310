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
        Equipment_Name,
        Purchase_Date,
        TIMESTAMPDIFF(
            YEAR,
            Purchase_Date,
            CURDATE()
        ) AS Age_Years
    FROM Equipment
    WHERE TIMESTAMPDIFF(
        YEAR,
        Purchase_Date,
        CURDATE()
    ) >= 5;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nOUTLAND ADVENTURES")
    print("AGING INVENTORY REPORT")
    print("-" * 50)

    if not rows:
        print("No equipment older than five years found.")
    else:
        for row in rows:
            print(
                f"Equipment: {row[0]} | "
                f"Purchase Date: {row[1]} | "
                f"Age: {row[2]} years"
            )

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print("Database Error:", err)