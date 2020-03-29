-- How many entries in the countries table are from Africa?
SELECT COUNT(*) as 'African countries'
FROM countries
WHERE continent = 'Africa';

-- What was the total population of the continent of Oceania in 2005?
SELECT population_years.year as 'Year', SUM(population_years.population) as 'Total Pop. in Oceania (Million)'
FROM population_years
JOIN countries
	ON countries.id = population_years.country_id
WHERE population_years.year = '2005' AND countries.continent = 'Oceania'
GROUP BY 1;

-- What is the average population of countries in South America in 2003?
SELECT population_years.year, AVG(population_years.population) as 'Average Pop. in South America (Million)'
FROM population_years
JOIN countries
	ON countries.id = population_years.country_id
WHERE population_years.year = '2003' AND countries.continent = 'South America'
GROUP BY 1;

-- What country had the smallest population in 2007?
SELECT population_years.year as 'Year', countries.name as 'Country', population_years.population as 'Population (Million)'
FROM population_years
JOIN countries
	ON countries.id = population_years.country_id
WHERE population_years.population = (SELECT MIN(population_years.population) FROM population_years WHERE population_years.year = '2007')
	AND population_years.year = '2007'
GROUP BY 1;

-- What is the average population of Poland during the time period covered by this dataset?
SELECT countries.name as 'Country', AVG(population_years.population) as 'Ave. Pop. (Million)'
FROM population_years
JOIN countries
	ON countries.id = population_years.country_id
WHERE countries.name = 'Poland';

-- How many countries have the word “The” in their name?
SELECT COUNT(*)
FROM countries
WHERE name LIKE '% The%';

-- What was the total population of each continent in 2010?
SELECT countries.continent as 'Continent', population_years.year as 'Year', SUM(population_years.population) as 'Total Pop. (Million)'
FROM countries
JOIN population_years
	ON countries.id = population_years.country_id
WHERE population_years.year = '2010'
GROUP BY 1;