from pathlib import Path
from functools import lru_cache
from pydantic import BaseModel

class Settings(BaseModel):
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    MODEL_FILE: Path = BASE_DIR / "model" / "model.pkl"
    VECTOR_FILE: Path = BASE_DIR / "vectorizer" / "vectorizer.pkl"

@lru_cache
def get_settings():
    return Settings()