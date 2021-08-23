# Import Flask Dependencies
from flask import Flask

# Set up Flask application instance with the name app.
app = Flask(__name__)

# Create the Flask Routes. You pass the value '/' to @app.route() to signify that this function will respond to web requests for the URL /, which is the main URL.
@app.route("/")
def welcome():
    return(
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
    )

    # Create Precipitation Route.
    @app.route("/api/v1.0/precipitation")
    def precipitation():
        prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
        precipitation = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date >= prev_year).all()
        precip = {date: prcp for date, prcp in precipitation}
        return jsonify(precip)