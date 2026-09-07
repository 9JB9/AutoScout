from fastapi import FastAPI

# CORS related imports
from fastapi.middleware.cors import CORSMiddleware

# dotenv related imports
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

#middleware configuration
origins=[
    "http://localhost:5173",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

"""
    **Small distinction between path and query parameters**
        - Paths are for when you are going for one specific resource.
        - Query are for when you are filtering for a collection of resources that have
          the parameters you passed in common.
"""
# based on the notes above, we are filtering for a collection of resources
# so we have (should?) use query parameters
"""
they can aso be used together... if path identifies a collection of things, you can have
the query parameters filter that collection down
"""

@app.get('/api/listings/') 
async def get_cars(
    zip: str | None = None, # this just says that postal code can be either string or None, but either way the default value is None
    radius: int | None = None, # for these None values, we will do some error handling some day 
    make: str | None = None,
    model: str | None = None
):
    base_url = os.getenv("BASE_URL")
    api_key = os.getenv("API_KEY")
    secret = os.getenv("SECRET")

    # for now we are going to work assuming all parameters are filled... error handling can be done later.. and some of it
    # can be layered in the front end also... also SCHEMAS
    api_url = api_key + 'search/car/active'
    pass