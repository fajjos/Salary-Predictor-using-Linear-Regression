import streamlit as st 
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go 
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("Data//Salary_Data.csv")
url = 'https://github.com/fajjos/Salary-Predictor-using-Linear-Regression'

lr = LinearRegression()
x = np.array(data["YearsExperience"]).reshape(-1,1)
lr.fit(x,np.array(data["Salary"]))

nav = st.sidebar.radio("Navigation", ["Home", "Prediction","Contribute", "About"])

if nav == "Home":
    st.write("Home")
    st.image("Data//sal.jpg", width=500)
    if st.checkbox("Show Table"):
        st.table(data)
    graph =  st.selectbox("What kind of Graph ?", ["Non-Interactive", "Interactive"])
    val = st.slider("Filter Data using years", 0,20)
    data = data.loc[data["YearsExperience"]>= val]
    if graph == "Non-Interactive":
        fig, ax = plt.subplots(figsize=(10,5))
        # plt.figure(figsize=(10,5))
        ax.scatter(data["YearsExperience"], data["Salary"])
        ax.set_ylim(0)
        ax.set_xlabel("Years of Experience")
        ax.set_ylabel("Salary")
        ax.set_title("Years of Experience Vs Salary ")
        plt.tight_layout()
        st.pyplot(fig)

    if graph == "Interactive": 
        layout = go.Layout(
            xaxis = dict(range=[0,16]),
            yaxis = dict(range = [0,2100000])
        )
        fig = go.Figure(data= go.Scatter(x=data["YearsExperience"], y=data["Salary"],mode= "markers"), 
        layout = layout)
        st.title("Years of Experience Vs Salary")
        st.plotly_chart(fig)


if nav == "Prediction":
    st.write("Prediction")
    st.header("Know ypur Salary")
    val = st.number_input("Enter your experience", 0.00, 20.00, step= 0.25)
    val = np.array(val).reshape(1, -1)
    pred = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your Predicted Salary is {round(pred)}")

if nav == "Contribute":
    st.write("Contribute")
    st.header("Contribute to Our Dataset")
    ex = st.number_input("Enter your Experienxe", 0.0, 20.0)
    sal = st.number_input("Enter your salary", 0.00, 10000000.00, step = 1000.0)
    if st.button("Submit"):
        to_add  = {"YearsExperience": [ex], "Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("Data//Salary_Data.csv", mode = "a", header = False, index= False)
        st.success("Submitted")

if nav == "About":
    st.header("About ")
    st.write("This is a Machine Learning Project, based upon the StreamLit that can predict and give graphs to your salaries.")
    st.write("You can always contribute to this Project by Going to the Contribute Section.")

    # st.markdown(f'''
    #             <a href={url}><button style="background-color: BlueWhite;">Github </button></a>
    #             ''', unsafe_allow_html=True)
    st.write("Source Code for this Project is availible at:")
    st.link_button("GitHub", "https://github.com/fajjos/Salary-Predictor-using-Linear-Regression")



