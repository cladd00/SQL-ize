# 1. import Flask
from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


@app.route("/")
def welcome():
    """List of all available api routes."""
    return(
            "Available Routes:<br>"
            "/api/v1.0/precipitation"
            "/api/v1.0/stations"
            "/api/v1.0/tobs"
            "/api/v1.0/<start>"
            "/api/v1.0/<start>/<end>"
            )

@app.route("/api/v1.0/precipitation")
def precipitation():
    results_a = session.query(measurements.tobs,measurements.date).\
        filter(measurements.date >= '2017-01-01').all()
    result_a = []
    for result in results_a:
        result_a_dict ={}
        result_a_dict['date'] = measurements.date
        result_a_dict['tobs'] = measurements.date
        result_a.append(result_a_dict)
        
    return jsonify(results_a)

@app.route("/api/v1.0/stations")
def stations():
    result_b = session.query(measurements.station).group_by(measurements.station).all()
    result_b_list = []
    for result in result_b_list:
        result_b_list.append(result_b)
    return jsonify(result_b_list)

@app.route("/api/v1.0/tobs")
def tobs():
    result_c = session.query(measurements.tobs,measurements.date).\
        filter(measurements.date >= '2017-01-01')
    result_c_list = []
    for result in result_c_list:
        result_c_list.append(result_c)
    return jsonify(result_c_list)


if __name__ == "__main__":
    app.run(debug=True)