# Import the dependencies.
from flask import Flask, jsonify
from flask import render_template
# from flask import request
import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################

# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    ''' 
    return """
    <h1>Available Routes:</h1>
    <ul>
        <li><a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a></li>
        <li><a href="/api/v1.0/stations">/api/v1.0/stations</a></li>
        <li><a href="/api/v1.0/tobs">/api/v1.0/tobs</a></li>
        <li><a href="/api/v1.0/<start>">/api/v1.0/&lt;start&gt;</a></li>
        <li><a href="/api/v1.0/<start>/<end>">/api/v1.0/&lt;start&gt;/&lt;end&gt;</a></li>
    </ul>
    """
    '''
    return render_template("index.html")

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Convert the query results to a dictionary using date as the key and prcp as the value."""
    # Calculate the date one year from the last date in the dataset
    prev_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the last 12 months of precipitation data
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year_date).all()
    # Convert the query results to a dictionary with appropriate labels
    precipitation_dict = [{"date": date, "precipitation": prcp} for date, prcp in precipitation_data]
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    # Query all stations
    results = session.query(Station.station).all()
    # Convert list of Row objects into list of dictionaries
    stations_list = [{"station": row[0]} for row in results]
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Query the dates and temperature observations of the most-active station for the previous year of data."""
    # Query the most active station
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count().desc()).first()[0]
    # Calculate the date one year from the last date in the dataset
    prev_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the last 12 months of temperature data for the most active station
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= prev_year_date).all()
    # Convert list of tuples into normal list with appropriate labels
    tobs_list = [{"date": date, "temperature": tobs} for date, tobs in results]
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def temp_start(start):
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start date."""
    # Query TMIN, TAVG, and TMAX for all dates greater than or equal to the start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    # Convert list of tuples into normal list with appropriate labels
    temp_stats = {"start_date": start, "min_temperature": results[0][0], "avg_temperature": results[0][1], "max_temperature": results[0][2]}
    return jsonify(temp_stats)

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start, end):
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for the specified start-end range."""
    # Query TMIN, TAVG, and TMAX for dates between the start and end date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    # Convert list of tuples into normal list with appropriate labels
    temp_stats = {"start_date": start, "end_date": end, "min_temperature": results[0][0], "avg_temperature": results[0][1], "max_temperature": results[0][2]}
    return jsonify(temp_stats)

if __name__ == '__main__':
    app.run(debug=True)
