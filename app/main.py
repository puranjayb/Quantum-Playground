import pickle
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .processing import preprocessing
from .schema import FormSchema

app = FastAPI()
settings = get_settings()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def load_model():
    print(settings.BASE_DIR)
    global model
    global vectorizer
    try:
        with open(settings.MODEL_FILE, 'rb') as f:
            model = pickle.load(f)

        with open(settings.VECTOR_FILE, 'rb') as f:
            vectorizer = pickle.load(f)
        print("Model Loadded Successfully")
    except Exception as e:
        print("error", e)

@app.post('/api/predict')
def predict(formData: FormSchema, response: Response):
    try:
        review = formData.dict().get('review', None)
        if review is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {'error': 'Please provide a review'}
        processed_review = preprocessing(review)
        input_data = vectorizer.transform([' '.join(processed_review)])
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            sentiment = 'postive'
        else:
            sentiment = 'negative'
        response.status_code = status.HTTP_200_OK
        return {'sentiment': sentiment}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(e)
        return {'error': "Something went wrong"}