import time

import mysql.connector

# Database connection setup (replace with your own credentials)
# connecting to sql
host = input("Enter host name : ")
user = input("Enter user name : ")
passwd = input("Enter passwd : ")
database = input("Enter any existing database name : ")
db_config = {
     "host": f"{host}",
     "user": f"{user}",
     "password": f"{passwd}",
     "database": f"{database}"
}

try:
    with mysql.connector.connect(**db_config) as connection:
        cursor = connection.cursor()

        # Create a new database if it doesn't exist
        new_database_name = input("Enter the name of the database you want to create: ")
        create_database_query = f"CREATE DATABASE IF NOT EXISTS {new_database_name}"
        cursor.execute(create_database_query)
        connection.commit()
        print(f"Database '{new_database_name}' created or already exists.")

        # Switch to the new database
        db_config["database"] = new_database_name
        connection.database = new_database_name

        table_name = input("Enter a table name: ")

        # Create table if it doesn't exist
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("  #

        while True:
            column_name = input("Enter a column name (or 'done' to finish): ")
            if column_name.lower() == 'done':
                break

            # # Get data type and constraint inputs (similar to your code)
            # data_type = input("Enter the data type for the column: ")
            # constraint = input("Enter constraints for the column (or leave blank): ")
            d1 = {
                '1': 'CHAR(50)', '2': 'VARCHAR(50)', '3': 'BLOB(1000)', '4': 'INT',
                '5': 'TINYINT', '6': 'BIGINT', '7': 'BIT(2)', '8': 'FLOAT',
                '9': 'DOUBLE', '10': 'BOOLEAN', '11': 'DATE', '12': 'TIME', '13': 'YEAR'
            }

            print("Options for data types: ", d1)
            data = input(f"Enter the data_type for column '{column_name}': ")

            data_type = d1.get(data, data)  # Use the provided data_type or keep it as is

            constraint = input("Do you want to enter constraints for the column ('y' or leave blank): ")

            if constraint.lower() == "y":
                d2 = {
                    '1': 'NOT NULL', '2': 'UNIQUE', '3': 'PRIMARY KEY', '4': 'FOREIGN KEY',
                    '5': 'CHECK', '6': 'DEFAULT', '7': 'CREATE INDEX'
                }

                print("Options for constraints: ", d2)
                con = input(f"Enter the constraint for column '{column_name}' (or leave blank): ")
                constraint = d2.get(con, con)  # Use the provided constraint or keep it as is

            # Build the column part of the CREATE TABLE query
            create_table_query += f"{column_name} {data_type} {constraint}, "

        create_table_query = create_table_query.rstrip(", ") + ")"  #
        cursor.execute(create_table_query)
        connection.commit()
        print(f"Table '{table_name}' created successfully.")

        time.sleep(2)
        while True:
            print("\nAvailable Operations:")
            print("1. Insert Data")
            print("2. Select Data")
            print("3. Update Data")
            print("4. Delete Data")
            print("5. Alter Table (Add Column)")
            print("6. Drop Table")
            print("7. Create Database")
            print("8. Drop Database")
            print("0. Exit")
            choice = input("Enter your choice (1/2/3/4/5/6): ")

            # Insert Data
            if choice == '1':
                column_names = input("Enter column names (comma-separated): ").split(',')
                values = input("Enter values (comma-separated): ").split(',')
                placeholders = ', '.join(['%s'] * len(values))
                insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholders})"
                cursor.execute(insert_query, values)
                connection.commit()
                print("Data inserted successfully.")

            # Select Data
            elif choice == '2':
                columns_to_select = input("Enter columns to select (comma-separated) or '*' for all: ")
                select_query = f"SELECT {columns_to_select} FROM {table_name}"
                cursor.execute(select_query)
                results = cursor.fetchall()
                for row in results:
                    print(row)

            # Drop
            # Update Data
            elif choice == '3':  # Update Data
                column_to_update = input("Enter the column to update: ")
                new_value = input("Enter the new value: ")
                criteria_column = input("Enter the criteria column: ")
                criteria_value = input("Enter the criteria value: ")
                update_query = f"UPDATE {table_name} SET {column_to_update} = %s WHERE {criteria_column} = %s"
                cursor.execute(update_query, (new_value, criteria_value))
                connection.commit()
                print("Data updated successfully.")

            # Delete Data
            elif choice == '4':
                column_to_delete = input("Enter the column to delete by: ")
                value_to_delete = input("Enter the value to delete: ")
                delete_query = f"DELETE FROM {table_name} WHERE {column_to_delete} = %s"
                cursor.execute(delete_query, (value_to_delete,))
                connection.commit()
                print("Data deleted successfully.")

            # Alter Table (Add Column)
            elif choice == '5':
                new_column_name = input("Enter the new column name: ")
                new_column_data_type = input("Enter the data type for the new column: ")
                alter_query = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {new_column_data_type}"
                cursor.execute(alter_query)
                connection.commit()
                print(f"New column '{new_column_name}' added to the table.")

            # Drop Table
            elif choice == '6':
                confirm = input(f"Are you sure you want to drop the '{table_name}' table (y/n): ").lower()
                if confirm == 'y':
                    drop_query = f"DROP TABLE IF EXISTS {table_name}"
                    cursor.execute(drop_query)
                    connection.commit()
                    print(f"Table '{table_name}' dropped successfully.")
                else:
                    print(f"Table '{table_name}' was not dropped.")

            # Create Database
            elif choice == '7':
                new_database_name = input("Enter the name of the database you want to create: ")
                create_database_query = f"CREATE DATABASE IF NOT EXISTS {new_database_name}"
                cursor.execute(create_database_query)
                connection.commit()
                print(f"Database '{new_database_name}' created or already exists.")

            # Drop Database
            elif choice == '8':
                database_to_drop = input("Enter the name of the database you want to drop: ")
                confirm = input(f"Are you sure you want to drop the '{database_to_drop}' database (y/n): ").lower()
                if confirm == 'y':
                    drop_query = f"DROP DATABASE IF EXISTS {database_to_drop}"
                    cursor.execute(drop_query)
                    connection.commit()
                    print(f"Database '{database_to_drop}' dropped successfully.")
                else:
                    print(f"Database '{database_to_drop}' was not dropped.")

            # Exit
            elif choice == '0':
                print("Thanks for using!!!")
                break

except mysql.connector.Error as error:
    print("Error:", error)

