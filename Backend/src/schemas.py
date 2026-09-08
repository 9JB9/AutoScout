from pydantic import BaseModel, Field

"""
    **from what i understand**
        you use type annotation to check incoming data and 
        response_model to check the return data from an endpoint
    
    Also, since your data has nested objects, thus nested JSONs,
    you kinda have to make classes that behave like the layers..
    so you would have schemas tied to other schemas

    alsoalso, you can either make the attribute names 1to1 to the 
    json being passed, or you can used alias in field and 
    have the local variable name be whatever you want
    (look up the syntax for this)
"""
class Build(BaseModel):
    make: str
    model: str
    year: int
    trim: str
    transmission: str
    drive_train: str
    fuel_type: str
class ListingMedia(BaseModel):
    photo_links: list[str]
class Dealer(BaseModel):
    pass
class Listing(BaseModel):
    id: str
    vin: str
    heading: str # this seems to be like the car title
    dealer : Dealer
    price: float
    media: ListingMedia
    dist: float # this represents the distance from dealership to the postal code you entered
class Listings(BaseModel):
    num_found: int  
    listings: list[Listing]
class ListingResponse(BaseModel):
    listings: Listings