from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from network_traffic_analyzer import analyze_traffic  # Import the analysis function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Call the analyze_traffic function from network_traffic_analyzer
    fig = analyze_traffic()

    # Save the result to the static folder
    fig.savefig('static/analysis.png')
    plt.close()

    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
