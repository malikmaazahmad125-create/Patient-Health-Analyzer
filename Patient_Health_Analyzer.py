import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

print("."*30)
print("PATIENT HEALTH ANALYZER")
print("."*30)
patients=[
    {
        "Name":"Ali",
        "Age":"25y",
        "Gender":"Male",
        "Blood Pressure": 120,
        "Heart Rate":72,
        "Cholesterol":180,
        "Blood Sugar":95
    },

    {
            "Name":"Ahmad",
            "Age":"45y",
            "Gender":"Male",
            "Blood Pressure":145,
            "Heart Rate":88,
            "Cholesterol":240,
            "Blood Sugar":130
    },

    {
            "Name":"Sara",
            "Age":"30y",
            "Gender":"Female",
            "Blood Pressure":110,
            "Heart Rate":70,
            "Cholesterol":None,
            "Blood Sugar":90
    },

    {
            "Name":"Ayesha",
            "Age":None,
            "Gender":"Female",
            "Blood Pressure":135,
            "Heart Rate":95,
            "Cholesterol":210,
            "Blood Sugar":None
    },

    {
            "Name":"Usman",
            "Age":"55y",
            "Gender":"Male",
            "Blood Pressure":160,
            "Heart Rate":100,
            "Cholesterol":280,
            "Blood Sugar":160
    }

]
print("."*10,"Patient Health Data","."*10)
for patient in patients:
    print(patient)

print("\n","."*10,"Patient DataFrame","."*10)
patient_data_frame=pd.DataFrame(patients)
print(patient_data_frame)

print("\n","."*10,"Find missing indexes","."*10)
print(patient_data_frame.isnull().sum())

print("\n","."*10,"Convert string type into integer type in DataFrame","."*10)
patient_data_frame["Age"]=patient_data_frame["Age"].str.replace("y","", regex= False)
patient_data_frame["Age"]=pd.to_numeric(patient_data_frame["Age"])
print(patient_data_frame["Age"])


patient_data_frame["Age"]=patient_data_frame["Age"].fillna(patient_data_frame["Age"].mean())
patient_data_frame["Cholesterol"]=patient_data_frame["Cholesterol"].fillna(patient_data_frame["Cholesterol"].mean())
patient_data_frame["Blood Sugar"]=patient_data_frame["Blood Sugar"].fillna(patient_data_frame["Blood Sugar"].mean())
print("\n","."*10,"CLEAN PATIENT HEALTH DATA","."*10)
print(patient_data_frame)

print("\n","."*10," NUMPY HEALTH STATISTICS","."*10)
print("\nBlood_pressure statistics:")

Blood_pressure=patient_data_frame["Blood Pressure"].to_numpy()
print("Avarege blood pressure is:",np.mean(Blood_pressure))
print("Maximum blood pressure is:",np.max(Blood_pressure))
print("Minimum blood pressure is:",np.min(Blood_pressure))


Heart_Rate=patient_data_frame["Heart Rate"].to_numpy()

print("\nHeart_Rate Statistics:")
print("Avarege Heart Rate is:",np.mean(Heart_Rate))
print("Maximum Heart Rate is:",np.max(Heart_Rate))
print("Minimum Heart Rate is:",np.min(Heart_Rate))

cholesterol = patient_data_frame["Cholesterol"].to_numpy()

print("\nCholesterol Statistics:")
print("Average Cholesterol is :", np.mean(cholesterol))
print("Maximum Cholesterol is :", np.max(cholesterol))
print("Minimum Cholesterol is :", np.min(cholesterol))

blood_sugar = patient_data_frame["Blood Sugar"].to_numpy()

print("\nBlood_Sugar Statistics:")
print("Average Blood Sugar is :", np.mean(blood_sugar))
print("Maximum Blood Sugar is :", np.max(blood_sugar))
print("Minimum Blood Sugar is :", np.min(blood_sugar))

print("\n","."*10,"HIGH RISK PATIENTS","."*10)
high_risk_patients=patient_data_frame[
    (patient_data_frame["Blood Pressure"] >140)  |
    (patient_data_frame["Cholesterol"] >220)  |
    (patient_data_frame["Blood Sugar"] > 120)
]
print(high_risk_patients)

print("\n","."*10,"COMPLETE HEALTH PATIENT SUMMARY","."*10)
total_patients=len(patient_data_frame)

average_age=np.mean(patient_data_frame["Age"])
average_blood_pressure=np.mean(patient_data_frame["Blood Pressure"])
average_heart_rate=np.mean(patient_data_frame["Heart Rate"])
average_cholesterol=np.mean(patient_data_frame["Cholesterol"])
average_blood_sugar=np.mean(patient_data_frame["Blood Sugar"])
total_high_risk=len(high_risk_patients)

print("\nTotal Patients:", total_patients)

print("Average Age:", round(average_age, 2))

print("Average Blood Pressure:", round(average_blood_pressure, 2))

print("Average Heart Rate:", round(average_heart_rate, 2))

print("Average Cholesterol:", round(average_cholesterol, 2))

print("Average Blood Sugar:", round(average_blood_sugar, 2))

print("Total High-Risk Patients:", total_high_risk)

# ==========================================
# PATIENT HEALTH DATA VISUALIZATION
# ==========================================

print("\n", "."*10, "PATIENT HEALTH VISUALIZATION", "."*10)


# ------------------------------------------
# BLOOD PRESSURE GRAPH
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    patient_data_frame["Name"],
    patient_data_frame["Blood Pressure"]
)

plt.title("Patient Blood Pressure")

plt.xlabel("Patient Name")

plt.ylabel("Blood Pressure")

plt.show()


# ------------------------------------------
# CHOLESTEROL GRAPH
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    patient_data_frame["Name"],
    patient_data_frame["Cholesterol"]
)

plt.title("Patient Cholesterol Levels")

plt.xlabel("Patient Name")

plt.ylabel("Cholesterol")

plt.show()

# ------------------------------------------
# BLOOD SUGAR GRAPH
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    patient_data_frame["Name"],
    patient_data_frame["Blood Sugar"]
)

plt.title("Patient Blood Sugar Levels")

plt.xlabel("Patient Name")

plt.ylabel("Blood Sugar")

plt.show()
