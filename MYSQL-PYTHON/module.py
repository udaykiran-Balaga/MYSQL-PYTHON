import mysql_operations #mysql_operations.py -->module name

#call the function to create database and table
mysql_operations.create_table()

#call function to insert one record
mysql_operations.insert_record('abc@1','uday','senior developer',50000,'2020-01-01')

employee_data = [
    ('abc@2', 'kiran', 'senior developer', 50000, '2020-01-01'),
    ('abc@3', 'jyostna', 'HR', 50000, '2020-05-01'),
    ('abc@4', 'manoj', 'junior developer', 50000, '2024-07-01'),
    ('abc@5', 'udaykiran', 'senior developer', 50000, '2020-01-01')
]
# call the function to insert multiple records into table
mysql_operations.insert_manyrecord(data=employee_data)

#call the function to update record based on employee id
mysql_operations.update_record('abc@2')

#invoke function to delete the record in the table
mysql_operations.delete_record('abc@4')

#function call to orderby clause on emp_name column
mysql_operations.orderby_record()

#invoke function to delete all rows in the table
mysql_operations.truncate_rows()

# Drop the entire table from the database
mysql_operations.drop_table()

# This function invoke the condition of Like and AND/OR
mysql_operations.like_record()

