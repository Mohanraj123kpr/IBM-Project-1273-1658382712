CREATE TABLE USER (
    RollNumber varchar(10) NOT NULL PRIMARY KEY,
    Email varchar(255) NOT NULL,
    Username varchar(255) NOT NULL UNIQUE,
    Password varchar(255) NOT NULL
);

INSERT INTO USER VALUES ('104012', 'kabilan@gmail.com', 'kabilan', 'kabs@123');
SELECT * FROM USER;

-- 
UPDATE USER SET Email='kabilan@gmail.com' WHERE RollNumber='104012';
SELECT * FROM USER;
-- 
DELETE FROM USER WHERE ROLLNUMBER='104012';
SELECT * FROM USER;
-- 
DELETE FROM USER WHERE USERNAME='kabilan';
SELECT * FROM USER;