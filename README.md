# sqlalchemy-challenge
# Honolulu, Hawaii Climate Analysis and Trip Planning

![lights](https://github.com/onemanlutta/sqlalchemy-challenge/assets/118937365/fd67b81a-089b-414e-9b43-b2430f7d0b0d)
Source: Google

Are you considering a long holiday vacation in Honolulu, Hawaii? This README provides insights into a climate analysis of the area using Python and SQLAlchemy, helping you make informed decisions and plan your trip effectively.

## About the Project

This project focuses on analyzing and exploring climate data for Honolulu, Hawaii. It involves querying a SQLite database containing climate data, performing data exploration and analysis using SQLAlchemy ORM queries, Pandas, and Matplotlib, and creating a Flask app to allow users to interact with the data through API routes.

## Project Structure

### Part 1: Analyze and Explore the Climate Data

#### 1. Setting Up the Environment
- Connect to the SQLite database (`hawaii.sqlite`) using SQLAlchemy.
- Reflect the tables into classes using SQLAlchemy's `automap_base()` function.

#### 2. Precipitation Analysis
- Find the most recent date in the dataset.
- Retrieve the previous 12 months of precipitation data.
- Load the query results into a Pandas DataFrame.
- Plot the precipitation data and print summary statistics.
![precipitation_plot](https://github.com/onemanlutta/sqlalchemy-challenge/assets/118937365/507be101-79f1-4110-a122-cd617e7bc5ab)


#### 3. Station Analysis
- Calculate the total number of stations in the dataset.
- Identify the most active stations and their observation counts.
- Determine the lowest, highest, and average temperatures for the most active station.
- Retrieve the previous 12 months of temperature observation (TOBS) data for the most active station.
- Plot the TOBS data as a histogram.
![tobs](https://github.com/onemanlutta/sqlalchemy-challenge/assets/118937365/978d8103-097a-4f3e-8236-dde0450b7208)


#### 4. Closing the Session
- Close the SQLAlchemy session.

### Part 2: Design the Climate App

#### Flask API Routes
- `/`: Homepage listing all available routes.
- `/api/v1.0/precipitation`: Return JSON representation of precipitation data.
- `/api/v1.0/stations`: Return JSON list of stations.
- `/api/v1.0/tobs`: Return JSON list of temperature observations for the most active station.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Return JSON list of temperature statistics for specified start and end dates.


## References

- Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston. (2012). An overview of the Global Historical Climatology Network-Daily Database. *Journal of Atmospheric and Oceanic Technology*, 29, 897-910. [Link](https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml)

## Project Dependencies

- Python
- SQLAlchemy
- Pandas
- Matplotlib
- Flask
