
-- create table
CREATE TABLE OR REPALCE employee (
    employeeID int primary key unique,
    name varchar(250),
    age int,
    department varchar(250),
    salary int,
    joindate date,
    tenure_year int
)