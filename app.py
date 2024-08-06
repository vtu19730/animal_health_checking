from flask import Flask, render_template, request
from logging import warning
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
import warnings

app = Flask(__name__)

# Load the dataset
data = pd.read_csv("hour.csv")

# ... (Your existing code for data preprocessing and visualization functions)

# Define routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health_dashboard", methods=["GET", "POST"])
def health_dashboard():
    if request.method == "POST":
        # Process form data if needed
        pass

    # Render the health dashboard with visualizations
    # You can use your existing functions to generate plots here
    return render_template("health_dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
