'''Pagination is the process  of dividing  a large dataset into smaller pages so that clients can fetch data efficiently instead of retrieving everything at once '''

''' there are 3 types of pagination :
1. Offset Pagination: This method uses an offset value to determine which records to return. For example, if you have 100 records and you want to fetch records 21-40, you would set the offset to 20 and the limit to 20.
2. Cursor Pagination: This method uses a cursor value to determine which records to return. 
3. Keyset Pagination: This method uses a key value to determine which records to return. For example, if you have a list of users sorted by their ID, you can use the last user's ID as the key to fetch the next set of users.'''

1. offset- Because inserts and deletes can shift row positions, causing duplicate or missing records between pages. It also becomes slower on very large offsets because the database must skip many rows.
SELECT *
FROM users
LIMIT 20
OFFSET 40;

Good for:

Admin dashboards
Reports
Small datasets


2. Cursor pagination - 
SELECT *
FROM users
WHERE id > 103
LIMIT 20;

3. keyset pagination 
directly use unique column 

SELECT *
FROM users
WHERE id > 103
ORDER BY id
LIMIT 2;

Real-World Use

Large databases

Example:

Banking Transactions
Orders
Event Logs
Sensor Data
ETL Pipelines

Large Data
      │
      ▼
Need Pagination
      │
      ├── Offset
      │     ├─ Simple
      │     ├─ Page Numbers
      │     └─ Slow on Large Data
      │
      ├── Cursor
      │     ├─ Uses Cursor Token
      │     ├─ Fast
      │     └─ Best for Social Media
      │
      └── Keyset
            ├─ Uses ID/Timestamp
            ├─ Very Fast
            └─ Best for ETL & Large Databases

