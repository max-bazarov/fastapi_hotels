from datetime import date
from typing import Optional
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel


app = FastAPI()


class SHotelSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None
    ) -> None:
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get('/hotels')
def get_hotels(
    search_args: SHotelSearchArgs = Depends()
) -> list[SHotel]:
    hotels = [
        {
            'address': 'Белорусская 15',
            'name': 'Obshaga',
            'start': 5
        }
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.get('/bookings')
def add_booking(booking: SBooking):
    pass
