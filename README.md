# Salary Predictor Using Linear Regression

[![Streamlit App](https://img.shields.io/badge/Streamlit-Click%20Here-brightgreen)](https://salary-predictor-using-linear-regression.streamlit.app/)

## Overview

This is a web application built using Streamlit that predicts salaries based on user input data. The application uses a linear regression model to provide salary predictions.

## Features

- Simple and intuitive user interface
- Real-time salary prediction
- Based on linear regression model

## How to Use

1. **Visit the App**: Go to the [Salary Predictor App](https://salary-predictor-using-linear-regression.streamlit.app/).
2. **Input Data**: Enter the required details such as years of experience.
3. **Get Prediction**: Click the predict button to get the estimated salary based on the input data.

## Installation (Local Development)

To run this app locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone (https://github.com/fajjos/Salary-Predictor-using-Linear-Regression.git)
    cd salary-predictor
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the Requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## File Structure

```plaintext
salary-predictor/
├── README.md
├── app.py
├── requirements.txt
└── model.pkl
