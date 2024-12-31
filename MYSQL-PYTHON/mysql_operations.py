import mysql.connector

def db_connection(func):
    def connection(*vargs,**kwargs):
        database = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your password',
            database='testdb'
        )
        cursor=database.cursor()
        try:
            func(cursor,database,*vargs,**kwargs)
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            database.close()
            print("Connection Closed.")
        
    return connection

def fetch_all_records(func):
    def wrapper(cursor,database,*args,**kwargs):
        try:
            func(cursor,database,*args,**kwargs)
            cursor.execute("SELECT * FROM employees")
            records = cursor.fetchall()
            print("\n All Employee Records:")
            for record in records:
                print(record)
            
        except mysql.connector.Error as e:
            print(f'Error: {e}')       
    return wrapper


@db_connection
def create_table(cursor,database):
    query='''CREATE TABLE IF NOT EXISTS employees(
    emp_id VARCHAR(10) PRIMARY KEY,
    emp_name VARCHAR(30) NOT NULL,
    emp_role VARCHAR(20) NOT NULL,
    emp_salary FLOAT NOT NULL,
    doj DATE NOT NULL
    )'''
    cursor.execute(query)
    database.commit()
    print("Table 'employees' created successfully.")

@db_connection
@fetch_all_records
def insert_record(cursor,database,emp_id,emp_name,emp_role,emp_salary,doj):
    query1='INSERT INTO employees(emp_id,emp_name,emp_role,emp_salary,doj) VALUES(%s,%s,%s,%s,%s)'
    cursor.execute(query1,(emp_id,emp_name,emp_role,emp_salary,doj))
    database.commit()
    print("Employee record inserted succesfully.")

@db_connection
@fetch_all_records
def insert_manyrecord(cursor,database,data):
    query='INSERT INTO employees(emp_id,emp_name,emp_role,emp_salary,doj) VALUES(%s,%s,%s,%s,%s)'
    cursor.executemany(query,data)
    database.commit()
    print("Multiple Employee records inserted succesfully.")

@db_connection
@fetch_all_records
def update_record(cursor,database,emp_id):
    query="UPDATE employees SET emp_name='KIRAN' WHERE emp_id=%s"
    cursor.execute(query,(emp_id,))
    database.commit()
    print("Update record in employees table.")

@db_connection
@fetch_all_records
def delete_record(cursor,database,emp_id):
    query='DELETE FROM employees WHERE emp_id=%s'
    cursor.execute(query,(emp_id,))
    database.commit()
    print("Delete record in the employees table")

@db_connection
def orderby_record(cursor,database):
    query1='SELECT * FROM employees ORDER BY emp_name'
    cursor.execute(query1)
    records = cursor.fetchall()
    for record in records:
        print(record)
    database.commit()
    print('Retrieve the records order by employees name')
    

@db_connection
@fetch_all_records
def truncate_rows(cursor,database):
    query='DELETE FROM employees'
    cursor.execute(query)
    database.commit()
    print('Delete all records in employees table')

@db_connection
@fetch_all_records
def drop_table(cursor,database):
    query='DROP TABLE employees'
    cursor.execute(query)
    database.commit()
    print('employees table dropped from the database.')

@db_connection
def like_record(cursor,database):
    query='SELECT * FROM employees WHERE emp_name LIKE "uda%" AND emp_salary>=30000'
    cursor.execute(query)
    records=cursor.fetchall()
    for record in records:
        print(record)
    database.commit()
    print("Retrieve the records based on LIKE/AND")

    
