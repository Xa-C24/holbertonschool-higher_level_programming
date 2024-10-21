# Introduction to Relational Databases

## What is a Relational Database?

A relational database is a database management system (DBMS) in which data is organized into **tables**. Each table consists of rows (called **records** or **tuples**) and columns (called **fields**). This management model allows data to be structured coherently, with relationships between different tables.

## Data Organization

Relational databases store data in the form of tables with several fundamental elements:

- **Tables**: A set of rows and columns that store data. Each table contains distinct records.
- **Rows (or records)**: Represent a unique instance in a table, such as a user or a product.
- **Columns (or fields)**: Represent data attributes, such as name, address, or price.
- **Indexes**: Data structures that improve the speed of lookups in tables by providing quick access to certain rows based on column values.

## Features of Relational Databases

- **Primary Key**: A unique identifier for each record in a table. It ensures that each row in a table is unique.
- **Foreign Key**: A key in one table that refers to the primary key in another table, establishing a relationship between the two tables.
- **Indexes**: Used to speed up queries by pre-computing access paths to data.

## CRUD Operations

In a relational database, the most common operations are often referred to by the acronym **CRUD**, which stands for:

- **Create**: Add new data to the database.
- **Read**: Retrieve data from the database.
- **Update**: Modify existing data.
- **Delete**: Remove data from the database.

## Examples of Relational Database Systems

Some well-known examples of relational database management systems include:

- **MySQL**: One of the most popular relational databases, commonly used in web applications.
- **PostgreSQL**: An advanced open-source relational database known for its SQL compliance and performance.
- **Oracle**: A robust database system used by large enterprises.
- **MariaDB**: A fully open-source fork of MySQL.

## Relations and Joins

Relational databases allow tables to be linked together through **relations**. This enables **joins** between tables to manipulate related data.

Example of a join between two tables:
```sql
SELECT posts.title, comments.body
FROM posts
JOIN comments ON posts.id = comments.post_id
WHERE comments.published = 1;
