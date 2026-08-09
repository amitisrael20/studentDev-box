CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL
);

INSERT INTO students (name, course)
VALUES
    ('Alice', 'Algorithms'),
    ('Bob', 'Databases');