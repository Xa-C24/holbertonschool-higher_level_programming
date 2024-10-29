# SQL - More queries  

In MySQL (and SQL in general), there are several keywords you can use to manipulate and query the database.  
Here is a list of the main ones: 

1. Database query keywords 

- SELECT : Used to retrieve data from a table.  
- FROM: Indicates the table from which the data is retrieved.  
- WHERE: Filters the results according to a specific condition.  
- JOIN: Combines data from several tables according to conditions.  
- GROUP BY: Groups the results by one or more columns.  
- ORDER BY: Sorts results in ascending or descending order.  
- LIMIT: Limits the number of rows returned in the result.  

2. Data manipulation keywords (DML)  

- INSERT INTO: Adds new rows to a table.  
- UPDATE: Modifies existing data in a table.  
- DELETE FROM: Deletes rows from a table according to specific conditions.  

3. Structure management keywords (DDL)  

- CREATE: Creates a new database, table, index, etc.  
- CREATE DATABASE: Creates a database.  
- CREATE TABLE: Creates a table with specified columns and types.  
- DROP: Deletes a database, table or column.  
- ALTER: Modifies an existing table to add, modify or delete columns.  
- TRUNCATE: Deletes all the rows in a table without deleting the table itself.  

4. Privilege and user management keywords (DCL)  

- GRANT: Assigns specific privileges to a user on specific tables, databases or operations.  
- REVOKE: Removes privileges previously assigned to a user.  

5. Transaction Control Key (TCL)  

- BEGIN or START TRANSACTION: Starts a transaction. 
- COMMIT: Commits the current transaction, applying all changes to the database.  
- ROLLBACK: Reverses all changes made in the current transaction.  
- SAVEPOINT: Defines a restore point to allow a partial ROLLBACK to this point in a transaction.  

MySQL query examples 1.  
Basic query to retrieve data:  
        sql Copy the code 
        SELECT name, age FROM users WHERE age > 18 ORDER BY name;  
        
2. Add data to a table:  
        sql Copy the code INSERT INTO users (name, age) VALUES ('Alice', 30);  
        
3. Modify existing data:  
        sql Copy the code UPDATE users SET age = 31 WHERE name = 'Alice';   

4. Give privileges to a user: 
        sql Copy the code GRANT SELECT, INSERT ON database_name.* TO 'user'@'localhost';