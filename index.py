from fastapi import FastAPI
from routes.route import allo

app = FastAPI() #creating instance for FastAPI
app.include_router(allo) #includeing router for allocation
