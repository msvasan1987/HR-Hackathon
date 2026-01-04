import pandas as pd 
import joblib 

model = joblib.load("hr_promotion_pred_model.pkl")

features = ['department', 'region', 'education', 'recruitment_channel',
            'length_of_service','previous_year_rating','age']

sample = pd.DataFrame({
    "department":["Sales"],
    "region":["APAC"],
    "education":["Bachelor"],
    "recruitment_channel":["sourcing"],
    "length_of_service": [2],
    "previous_year_rating": [2],
    "age": [2]
})

#Make prediciton 
pred = model.predict(sample)
print(f"Predicted Promotion: Rs. {pred[0]}")