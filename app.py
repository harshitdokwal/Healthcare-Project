import streamlit as st
import pandas as pd
import pickle
from xgboost import XGBClassifier

#when open pickle model use this commmand
with open("XGB_Model_Healthcare.pkl","rb") as file:
    model = pickle.load(file)

st.title("Medical Test Result XGB Model")
st.write("This model predicts test result into 'Abnormal', 'Normal' or 'Inconclusive'")
st.subheader("Enter your information")

age = st.number_input("Age",min_value=0,max_value = 100)
Gender = st.selectbox("Gender",["Male","Female"])
blood_type = st.selectbox("Blood Type",["Select","A-","AB+","A+","AB-","B+","B-","O+"])
medical_condition = st.selectbox("Medical Conditions",["Select","Asthma","Cancer","Diabities","Hyper Tension","Obesity","Arthritis"])
admission_type= st.selectbox("Admission Type",["Select","Emergency","Urgent","Elective"])
medication = st.selectbox("Medication",["Select","Ibuprofen","Lipitor","Paracetamol","Penicillin","Aspirin","Ibuprofen"])

# in input data we will put all the variables that were in x.test
input_data = pd.DataFrame({"Age":[age],
                            "Gender_Male":[1 if Gender=="Male" else 0],
                            'Blood Type_A-':[1 if blood_type=="A-" else 0],
                            'Blood Type_AB+':[1 if blood_type=="AB+" else 0],
                            'Blood Type_O-':[1 if blood_type=="O-" else 0],
                            'Blood Type_A-':[1 if blood_type=="A-" else 0],
                            'Blood Type_AB-':[1 if blood_type=="AB-" else 0],
                            'Blood Type_B+':[1 if blood_type=="B+" else 0],
                            'Blood Type_O+':[1 if blood_type=="O+" else 0],
                            'Medical Condition_Asthma':[1 if medical_condition=="Asthma" else 0],
                            'Medical Condition_Cancer':[1 if medical_condition=="Cancer" else 0],
                            'Medical Condition_Diabetes':[1 if medical_condition=="Diabities" else 0],
                            'Medical Condition_Hypertension':[1 if medical_condition=="Hypertension" else 0],
                            'Medical Condition_Obesity':[1 if medical_condition=="Obesity" else 0],
                            'Medication_Ibuprofen':[1 if medication=="Ibuprofen" else 0],
                            'Medication_Lipitor':[1 if medication=="Lipitor" else 0],
                            'Medication_Paracetamol':[1 if medication=="Paracetamol" else 0],
                            'Medication_Penicillin':[1 if medication=="Penicillin" else 0],
                            'Medication_Aspirin':[1 if medication=="Aspirin" else 0],
                            'Admission Type_Emergency':[1 if admission_type=="Emergency" else 0],
                            'Admission Type_Urgent':[1 if admission_type=="Urgent" else 0],
                            'Admission Type_Elective':[1 if admission_type=="Elective" else 0]})

expected_order = ['Age', 'Gender_Male', 'Blood Type_A-', 'Blood Type_AB+',
       'Blood Type_AB-', 'Blood Type_B+', 'Blood Type_B-', 'Blood Type_O+',
       'Blood Type_O-', 'Medical Condition_Asthma', 'Medical Condition_Cancer',
       'Medical Condition_Diabetes', 'Medical Condition_Hypertension',
       'Medical Condition_Obesity', 'Admission Type_Emergency',
       'Admission Type_Urgent', 'Medication_Ibuprofen', 'Medication_Lipitor',
       'Medication_Paracetamol', 'Medication_Penicillin']
input_data = input_data.reindex(columns = expected_order)

if st.button("Predict"):
    prediction = model.predict(input_data)
    result_mapping = {2:"Normal",1:"Inconclusive",0:"Abnormal"}
    result = result_mapping[prediction[0]]
    st.write(f"The Predicted outcome is: **{result}**")