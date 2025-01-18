from pydantic import BaseModel

class GuideCreateSchema(BaseModel):
    name: str
    email: str
    nationality: str
    location: str
    whatsapp: str
    telegram: str
    languages: str
    gender: str
    places: str
    vehicle: str
    vehicle_capacity: int
    # vehicle_photo: str
    vehicle_type: str

class GuideUpdateSchema(BaseModel):
    name: str = None
    email: str = None
    nationality: str = None
    location: str = None
    whatsapp: str = None
    telegram: str = None
    languages: str = None
    gender: str = None
    places: str = None
    vehicle: str = None
    vehicle_capacity: int = None
    # vehicle_photo: str = None
    vehicle_type: str = None

    
class GuideSearchSchema(BaseModel):
    location: str
    vehicle_type: str
    nationality: str
    languages: str
    gender: str
    vehicle_capacity: int