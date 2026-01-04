import streamlit as st #framework building interactive web application directly from python without an UI
import pandas as pd
import joblib

model = joblib.load("hr_promotion_pred_model.pkl")

st.set_page_config(page_title = "HR Promotion Prediction",page_icon="", layout = 'centered')

st.title("HR Promotion Prediction APP")
st.markdown("""This app is going to predict ***Promotion*** based on the 
input values I provide, Once done click ***Predict Promotion*** button""")


with st.form("input_form"):
    st.header("Enter Product & Outlet Details")
    col1, col2 = st.columns(2)
    with col1: 
        department = st.selectbox("Department", ['Sales & Marketing', 'Operations', 'Technology', 'Analytics', 'R&D', 'Procurement', 'Finance', 'HR', 'Legal'])
        region = st.selectbox("Region", ['region_7','region_22','region_19','region_23','region_26','region_2',
     'region_20','region_34','region_1','region_4','region_29','region_31',
     'region_15','region_14','region_11','region_5','region_28','region_17',
     'region_13','region_16','region_25','region_10','region_27','region_30',
     'region_12','region_21','region_8','region_32','region_6','region_33',
     'region_24','region_3','region_9','region_18'])
        education = st.selectbox("Education", ["Master's & above", "Bachelor's", "Below Secondary"])
        recruitment_channel = st.selectbox("Recruitment Channel", ['sourcing', 'other', 'referred'])
         
      

    with col2: 
        
        length_of_service =st.number_input("Experience", min_value=0.0, step= 0.5)
        age = st.number_input("Age", min_value=0, step= 1)
        previous_year_rating = st.selectbox("Prev yr Rating", [1,2,3,4,5])

    # values = st.text_input("Enter multiple MPRs")
    # m_values = [float(v) for v in values.split(',')]
    # st.write("MRPs entered:",m_values)
    #uploaded = st.file_uploder("Enter your CSV",type = ['csv','xlsx'])
    #data = pd.read_csv(uploaded)
    submitted = st.form_submit_button("Predict Promotion")
    

if submitted: 
    input_df = pd.DataFrame({
    "department": [department],
    "region": [region],
    "education": [education],
    "recruitment_channel": [recruitment_channel],
    "length_of_service": [length_of_service],
    "age": [age],
    "previous_year_rating": [previous_year_rating]
    })
    print(input_df)
    pred = model.predict(input_df)
    result = "Promoted" if pred[0] == 1 else "Not Promoted"
    st.success(f"Prediction: {result}")
    