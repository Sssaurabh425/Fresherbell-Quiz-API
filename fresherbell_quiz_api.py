from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()
class model_input(BaseModel):
    id : int

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"],
)

#load model
loaded_model = pickle.load(open('quiz_recommend.sav','rb'))
quiz_model = pickle.load(open('quizzes.sav','rb'))

@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}

@app.post('/fresherbell_quiz_api')
def quiz_recommend(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    id = input_dictionary['id']
    q_index = quiz_model[quiz_model['id'] == id].index[0]
    distances = loaded_model[q_index]
    quiz_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    a = []  
    for i in quiz_list:
        a.append((quiz_model.iloc[i[0]]['id']).tolist())
    return a