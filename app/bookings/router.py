from fastapi import APIRouter, Depends

from app.bookings.schemas import BookingCreateSchema, BookingReadSchema
from app.bookings.service import BookingService
from app.exceptions import RoomCannotBeBooked
from app.users.dependencies import get_current_user
from app.users.models import User

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)


@router.get('')
async def get_bookings(
    user: User = Depends(get_current_user),
) -> list[BookingReadSchema]:
    return await BookingService.get_all(user_id=user.id)


@router.post('')
async def add_booking(
    booking: BookingCreateSchema,
    user: User = Depends(get_current_user),
):
    booking = await BookingService.create(user.id, **booking.dict())
    if not booking:
        raise RoomCannotBeBooked
