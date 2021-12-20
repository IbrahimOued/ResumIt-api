# Import statements
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.summarize import api_router

# Our REACT app will be running on this IP and PORT
#client_apps = ['http://localhost:3000']

# Create app
app = FastAPI()
# register your router
app.include_router(api_router)

# Register App with CORS middleware to allow resourse sharing between different domains/origins
app.add_middleware(
    CORSMiddleware,
    # allow_origins=client_apps,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
