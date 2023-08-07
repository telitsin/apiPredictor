from fastapi import FastAPI
from services.predictor import LoadModel

app = FastAPI()

"""Replace this part for loading real models"""
my_heart_failure_predictor = LoadModel()
my_lung_cancer_predictor1 = LoadModel()
my_hiv_aids_predictor = LoadModel()

@app.get("/heart_failure_prediction")
async def heart_failure_prediction(age: int, sex: int, cp: int, chol: int):
    return my_heart_failure_predictor.predict(age=age, sex=sex, cp=cp, chol=chol)


@app.get("/lung_cancer_predictor")
async def lung_cancer_predictor(age: int, wheezing: int, fatigue: int, coughing: int,
                                shortness_of_breath: int, smoking: int, swallowing_difficulty: int):
    return my_lung_cancer_predictor1.predict(age=age, wheezing=wheezing, fatigue=fatigue, coughing=coughing,
                                          shortness_of_breath=shortness_of_breath, smoking=smoking,
                                          swallowing_difficulty=swallowing_difficulty)


@app.get("/hiv_aids_predictor")
async def hiv_aids_predictor(age: int, gender: int, hiv_diagnoses: int, linked_to_care: int, plwdhi_prevalence: int):
    return my_hiv_aids_predictor.predict(age=age, gender=gender, hiv_diagnoses=hiv_diagnoses,
                                      linked_to_care=linked_to_care, plwdhi_prevalence=plwdhi_prevalence)
