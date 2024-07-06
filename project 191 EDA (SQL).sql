create database pharmaceutical_inventory;
use pharmaceutical_inventory;

select count(Material) from `sql data set`;

###### first business movement ########

##### MEAN ############

select avg(`Qty in Un. of Entry`) from `sql data set`;
select avg(`Qty in OPUn`) from `sql data set`;
select avg(`Qty in order unit`) from `sql data set`;
select avg(`Amount in LC`) from `sql data set`;
select avg(`Quantity`) from `sql data set`;
select avg(`Material Doc. Year`) from `sql data set`;

######### MEDIAN ############

SELECT `Qty in Un. of Entry` As `Qty in Un. of Entry`
FROM(
    SELECT `Qty in Un. of Entry`, ROW_NUMBER() OVER( ORDER BY `Qty in Un. of Entry`) AS row_num,
	COUNT(*) OVER() AS total_count
    FROM `sql data set`
) AS sunquery
WHERE row_num = ( total_count + 1 ) / 2 OR  row_num = ( total_count + 2 ) / 2;



SELECT `Qty in OPUn` As `Qty in OPUn`
FROM(
    SELECT `Qty in OPUn`, ROW_NUMBER() OVER( ORDER BY `Qty in OPUn`) AS row_num,
	COUNT(*) OVER() AS total_count
    FROM `sql data set`
) AS sunquery
WHERE row_num = ( total_count + 1 ) / 2 OR  row_num = ( total_count + 2 ) / 2;



SELECT `Qty in order unit` As `Qty in order unit`
FROM(
    SELECT `Qty in order unit`, ROW_NUMBER() OVER( ORDER BY `Qty in order unit`) AS row_num,
	COUNT(*) OVER() AS total_count
    FROM `sql data set`
) AS sunquery
WHERE row_num = ( total_count + 1 ) / 2 OR  row_num = ( total_count + 2 ) / 2;



SELECT `Amount in LC` As `Amount in LC`
FROM(
    SELECT `Amount in LC`, ROW_NUMBER() OVER( ORDER BY `Qty in order unit`) AS row_num,
	COUNT(*) OVER() AS total_count
    FROM `sql data set`
) AS sunquery
WHERE row_num = ( total_count + 1 ) / 2 OR  row_num = ( total_count + 2 ) / 2;



SELECT `Quantity` As `Quantity`
FROM(
    SELECT `Quantity`, ROW_NUMBER() OVER( ORDER BY `Quantity`) AS row_num,
	COUNT(*) OVER() AS total_count
    FROM `sql data set`
) AS sunquery
WHERE row_num = ( total_count + 1 ) / 2 OR  row_num = ( total_count + 2 ) / 2;



SELECT `Material Doc. Year` As `Material Doc. Year`
FROM(
    SELECT `Material Doc. Year`, ROW_NUMBER() OVER( ORDER BY `Material Doc. Year`) AS row_num,
	COUNT(*) OVER() AS total_count
    FROM `sql data set`
) AS sunquery
WHERE row_num = ( total_count + 1 ) / 2 OR  row_num = ( total_count + 2 ) / 2;



####### MODE #########

SELECT `Qty in Un. of Entry` AS `Qty in Un. of Entry`
FROM (
SELECT `Qty in Un. of Entry`, COUNT(*) AS frequency
FROM `sql data set`
GROUP BY 1
ORDER BY frequency DESC
LIMIT 1
) AS subquery;



SELECT `Qty in OPUn` AS `Qty in OPUn`
FROM (
SELECT `Qty in OPUn`, COUNT(*) AS frequency
FROM `sql data set`
GROUP BY 1
ORDER BY frequency DESC
LIMIT 1
) AS subquery;



SELECT `Qty in order unit` AS `Qty in order unit`
FROM (
SELECT `Qty in order unit`, COUNT(*) AS frequency
FROM `sql data set`
GROUP BY 1
ORDER BY frequency DESC
LIMIT 1
) AS subquery;



SELECT `Amount in LC` AS `Amount in LC`
FROM (
SELECT `Amount in LC`, COUNT(*) AS frequency
FROM `sql data set`
GROUP BY 1
ORDER BY frequency DESC
LIMIT 1
) AS subquery;



SELECT `Material Doc. Year` AS `Material Doc. Year`
FROM (
SELECT `Material Doc. Year`, COUNT(*) AS frequency
FROM `sql data set`
GROUP BY 1
ORDER BY frequency DESC
LIMIT 1
) AS subquery;



#Second Business Moments-Variance,Standard Deviation,Range

# To calculate Standard Deviation  

SELECT STDDEV(`Qty in Un. of Entry`) AS `Qty in Un. of Entry` FROM `sql data set`;
SELECT STDDEV(`Qty in OPUn`) AS `Qty in OPUn` FROM `sql data set`;
SELECT STDDEV(`Qty in order unit`) AS `Qty in order unit` FROM `sql data set`;
SELECT STDDEV(`Amount in LC`) AS `Amount in LC` FROM `sql data set`;
SELECT STDDEV(`Material Doc. Year`) AS `Material Doc. Year` FROM `sql data set`;



############# VARIANCE ###########

SELECT variance(`Qty in Un. of Entry`) AS `Qty in Un. of Entry` FROM `sql data set`;
SELECT variance(`Qty in OPUn`) AS `Qty in OPUn` FROM `sql data set`;
SELECT variance(`Qty in order unit`) AS `Qty in order unit` FROM `sql data set`;
SELECT variance(`Amount in LC`) AS `Amount in LC` FROM `sql data set`;
SELECT variance(`Material Doc. Year`) AS `Material Doc. Year` FROM `sql data set`;



########## RANGE #######

SELECT max(`Qty in Un. of Entry`) - min(`Qty in Un. of Entry`) AS `Qty in Un. of Entry` FROM `sql data set`;
SELECT max(`Qty in OPUn`) - min(`Qty in OPUn`) AS `Qty in OPUn` FROM `sql data set`;
SELECT max(`Qty in order unit`) - min(`Qty in order unit`) AS `Qty in order unit` FROM `sql data set`;
SELECT max(`Amount in LC`) - min(`Amount in LC`) AS `Amount in LC` FROM `sql data set`;
SELECT max(`Material Doc. Year`) - min(`Material Doc. Year`) AS `Material Doc. Year` FROM `sql data set`;



############# THIRD BUSINESS MOVEMENT ############

SELECT(
SUM(POWER(`Qty in Un. of Entry` - (SELECT AVG(`Qty in Un. of Entry`) FROM `sql data set`), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(`Qty in Un. of Entry`) FROM `sql data set`), 3))
) AS skewness
FROM `sql data set`;


SELECT(
SUM(POWER(`Qty in OPUn` - (SELECT AVG(`Qty in OPUn`) FROM `sql data set`), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(`Qty in OPUn`) FROM `sql data set`), 3))
) AS skewness
FROM `sql data set`;


SELECT(
SUM(POWER(`Qty in order unit` - (SELECT AVG(`Qty in order unit`) FROM `sql data set`), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(`Qty in order unit`) FROM `sql data set`), 3))
) AS skewness
FROM `sql data set`;



SELECT(
SUM(POWER(`Amount in LC` - (SELECT AVG(`Amount in LC`) FROM `sql data set`), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(`Amount in LC`) FROM `sql data set`), 3))
) AS skewness
FROM `sql data set`;



SELECT(
SUM(POWER(`Material Doc. Year` - (SELECT AVG(`Material Doc. Year`) FROM `sql data set`), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(`Material Doc. Year`) FROM `sql data set`), 3))
) AS skewness
FROM `sql data set`;



############### FOURTH BUSINESS MOVEMENT ##############

SELECT
(
(SUM(POWER(`Qty in Un. of Entry` - (SELECT AVG(`Qty in Un. of Entry`) FROM `sql data set`), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(`Qty in Un. of Entry`) FROM `sql data set`), 4))) - 3
) AS kurtosis
FROM `sql data set`;


SELECT
(
(SUM(POWER(`Qty in OPUn` - (SELECT AVG(`Qty in OPUn`) FROM `sql data set`), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(`Qty in OPUn`) FROM `sql data set`), 4))) - 3
) AS kurtosis
FROM `sql data set`;


SELECT
(
(SUM(POWER(`Qty in order unit` - (SELECT AVG(`Qty in order unit`) FROM `sql data set`), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(`Qty in order unit`) FROM `sql data set`), 4))) - 3
) AS kurtosis
FROM `sql data set`;


SELECT
(
(SUM(POWER(`Amount in LC` - (SELECT AVG(`Amount in LC`) FROM `sql data set`), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(`Amount in LC`) FROM `sql data set`), 4))) - 3
) AS kurtosis
FROM `sql data set`;


SELECT
(
(SUM(POWER(`Material Doc. Year` - (SELECT AVG(`Material Doc. Year`) FROM `sql data set`), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(`Material Doc. Year`) FROM `sql data set`), 4))) - 3
) AS kurtosis
FROM `sql data set`;



############## QUESTIONS IN EDA DOCUMENT ##############

# 1.	What is the total quantity of material received (goods receipt)? 

select sum(Quantity) as total_quantity from `sql data set`;

# 2.	Which plant has the highest number of materials?

select (Quantity) as quantity_count from `sql data set`
group by Quantity order by Quantity desc 
limit 1;

# 4.	What is the average quantity of material moved per transaction in 2022?

SELECT AVG(`Quantity`) AS avg_quantity_per_transaction
FROM `sql data set`
WHERE (`Material Doc. Year`) = 2022;

# 5.	Questions on Financial Impact What is the total financial value of material received in 2024?

SELECT SUM(`Amount in LC`) AS total_financial_value
FROM `sql data set`
WHERE (`Material Doc. Year`) = 2024;





