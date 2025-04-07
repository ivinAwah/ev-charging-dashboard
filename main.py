from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    data = pd.read_csv('stations_data.csv')
    total_stations = data.shape[0]
    return f"EV Charging Dashboard — Total Stations: {total_stations}"

if __name__ == '__main__':
    app.run(debug=True)