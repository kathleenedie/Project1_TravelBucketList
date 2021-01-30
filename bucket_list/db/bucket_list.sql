DROP TABLE IF EXISTS sights;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  continent VARCHAR(255)
);

CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  year INT,
  category VARCHAR(255),
  photo_link VARCHAR(255),
  country_id INT REFERENCES countries(id),
  visited BOOLEAN
);

CREATE TABLE sights (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  star_rating INT,
  city_id INT REFERENCES cities(id)
);
