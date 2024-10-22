from pydantic import BaseModel
from datetime import date

# Define a Pydantic model for the data

class Allocation(BaseModel):
    employee_id : int
    vehicle_id: int
    driver_id: int
    allocation_date: str
    