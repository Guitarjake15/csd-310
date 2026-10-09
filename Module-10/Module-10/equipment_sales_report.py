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
        COUNT(Sale_ID) AS Transactions,
        COALESCE(SUM(Sale_Quantity), 0) AS Units_Sold
    FROM Equipment
    LEFT JOIN Equipment_Sales
        ON Equipment.Equipment_ID = Equipment_Sales.Equipment_ID
    GROUP BY Equipment.Equipment_ID, Equipment_Name
    ORDER BY Units_Sold DESC;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nOUTLAND ADVENTURES")
    print("EQUIPMENT SALES REPORT")
    print("-" * 50)

    if not rows:
        print("No equipment sales data found.")
    else:
        for row in rows:
            print(
                f"Equipment: {row[0]} | "
                f"Transactions: {row[1]} | "
                f"Units Sold: {row[2]}"
            )

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print("Database Error:", err)