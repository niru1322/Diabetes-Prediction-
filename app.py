import streamlit as st
import pickle as pkl
import pandas as pd

reg = pkl.load(open("CPP.pkl","rb+"))
sc = pkl.load(open("sc.pkl","rb+"))
st.title("Diabetic Patient Prediction Project")
gender = st.selectbox("Select Gender",["male","female","other"])
selgender = 0
if gender=="male":
        selgender=0
elif gender=="female":
        selgender=1
else:
        selgender=2
selage = int(st.number_input("Enter your age",min_value=5,max_value=100))

hypertension  = st.selectbox("Enter Hypertension",["Yes","No"])
selhypertension = 0  
if hypertension == "Yes":
        selhypertension=1

heart_disease  = st.selectbox("enter Heart Disease",["Yes","No"])
selheart_disease =0
if heart_disease=="Yes":
        selheart_disease=1
smoking_history = st.selectbox("Select smoking", ['never', 'No Info', 'former', 'not current', 'ever', 'current'])
selsmoking_history = 0
if smoking_history == 'never':
    selsmoking_history = 0
elif smoking_history == 'former':
    selsmoking_history = 1
elif smoking_history == 'not current' or smoking_history == 'ever' :
    selsmoking_history = 2
elif smoking_history == 'No Info':
    selsmoking_history = -1
else:
    selsmoking_history = 3
selbmi = st.number_input("Enter BMI", min_value = 20, max_value = 50, value = 28)
selHbA1c_level = st.number_input("Enter H1AC Level", min_value = 5.0, max_value = 10.0, value = 6.6, step=0.1)
selblood_glucose_level = st.number_input("Enter Blood Glucose Level", min_value = 25, max_value = 500, value = 200)
if st.button("Check"):
    myinput = [[selgender, selage, selhypertension, selheart_disease, selsmoking_history, selbmi, selHbA1c_level, selblood_glucose_level]]
    
    myinput = pd.DataFrame(data=myinput,columns=['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level'])
    result = reg.predict(sc.transform(myinput))
    if result[0]==1:
         st.write("Person in diabetic")
    else:
        st.write("Person not in diabetic")
