from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    data_dir = "realtime_vehicle_data"
    metadata = load_metadata(data_dir)
    return render_template('index.html', data=metadata.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
