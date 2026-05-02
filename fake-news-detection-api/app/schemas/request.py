from pydantic import BaseModel, Field

class NewsRequest(BaseModel):
    text: str = Field(..., example="Breaking news government passes law")
