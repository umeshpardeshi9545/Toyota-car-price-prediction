import pickle
import streamlit as st
import urllib.request
from sklearn.linear_model import LogisticRegression


# Raw URL to the model
url = "https://raw.githubusercontent.com/umeshpardeshi9545/Toyota-car-price-prediction/main/toyotaMLR.pkl"

# Load the model
try:
    with urllib.request.urlopen(url) as response:
        model_data = response.read()  # Read bytes
        model = pickle.loads(model_data)  # Load model from bytes
except Exception as e:
    model = None
    st.error(f"Error loading the model: {e}")

def main():
    st.title("Survived or not")
    # Input variables
    Age_08_04 = st.text_input("Age_08_04")
    KM = st.text_input("KM") 
    HP = st.text_input("HP")  
    Automatic = st.text_input("Automatic")
    cc = st.text_input("cc")
    Doors = st.text_input("Doors")
    Gears = st.text_input("Gears")
    Weight = st.text_input("Weight")
    Fuel_Type_CNG = st.text_input("Fuel_Type_CNG")
    Fuel_Type_Diesel = st.text_input("Fuel_Type_Diesel")
    Fuel_Type_Petrol = st.text_input("Fuel_Type_Petrol")

    # Prediction
    if st.button("Predict"):
        try:
            # Ensure inputs are converted to the right types (e.g., float or int)
            makepred = model.predict([[float(Age_08_04), float(KM),float(HP	), float(Automatic), float(cc), 
                                        float(Doors), float(Gears), float(Weight), float(Fuel_Type_CNG), float(Fuel_Type_Diesel), float(Fuel_Type_Petrol)]])
            st.success(f"The Selling Price Of Car is: {round(abs(makepred[0]),2)}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
