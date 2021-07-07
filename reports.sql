### Clean the talent_vp database
DROP DATABASE IF EXISTS kaspien;

### Create and select the kaspien database
CREATE DATABASE kaspien;
USE kaspien;

### Create the SALES table
CREATE TABLE SALES (
	PRODUCT_ID VARCHAR(50) NOT NULL,
	UNITS_ORDERED INTEGER NOT NULL,
	ORDER_DATE DATE NOT NULL
);

### Enable import data from file
SET GLOBAL local_infile=1;

### Import the data_engineering_data.in file, assuming it is in the /tmp directory
LOAD DATA LOCAL INFILE '/tmp/data_engineering_data.in' INTO TABLE SALES FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

### Select command to retrieve the total report grouped by product and by week of the year (format YYYYWW)
SELECT (YEARWEEK(ORDER_DATE) +1) AS YEAR_WEEK, PRODUCT_ID, SUM(UNITS_ORDERED) AS TOTAL_UNITS_SOLD
FROM SALES
GROUP BY PRODUCT_ID, YEAR_WEEK
ORDER BY YEAR_WEEK;

### Select command to retrieve the average report grouped by product and by week of the year (format YYYYWW)
SELECT (YEARWEEK(ORDER_DATE) +1) AS YEAR_WEEK, PRODUCT_ID, AVG(UNITS_ORDERED) AS AVERAGE_UNITS_SOLD
FROM SALES
GROUP BY PRODUCT_ID, YEAR_WEEK
ORDER BY YEAR_WEEK;