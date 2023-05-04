from datetime import date

from sqlalchemy import func, insert, select

from app.bookings.models import Booking
from app.core.service import BaseService
from app.database import async_session_maker
from app.hotels.rooms.models import Room


class BookingService(BaseService):
    model = Booking

    @classmethod
    async def create(
        cls, user_id: int, room_id: int, date_from: date, date_to: date
    ):
        """
        WITH booked_room AS (
        SELECT * FROM bookings
        WHERE room_id = 1 AND
        date_to >= '2023-06-20' AND
        date_from <= '2023-07-05'
        )
        SELECT r.quantity - count(br.room_id) AS room_available FROM rooms r
        LEFT JOIN booked_room br ON br.room_id = r.id
        WHERE r.id = 1
        GROUP BY r.quantity, br.room_id;
        """
        booked_rooms = (
            select(Booking)
            .where(
                (Booking.room_id == room_id)
                & (
                    (Booking.date_to >= date_to)
                    & (Booking.date_from <= date_from)
                )
            )
            .cte('booked_rooms')
        )
        get_rooms_left = (
            select(
                (Room.quantity - func.count(booked_rooms.c.room_id)).label(
                    'rooms_left'
                )
            )
            .select_from(Room)
            .join(
                booked_rooms, booked_rooms.c.room_id == Room.id, isouter=True
            )
            .where(Room.id == room_id)
            .group_by(Room.quantity, booked_rooms.c.room_id)
        )
        async with async_session_maker() as session:
            rooms_left = await session.execute(get_rooms_left)

            rooms_left: int = rooms_left.scalar()
            print(rooms_left)
            if rooms_left > 0:
                get_price = select(Room.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                add_booking = (
                    insert(Booking)
                    .values(
                        room_id=room_id,
                        user_id=user_id,
                        date_from=date_from,
                        date_to=date_to,
                        price=price,
                    )
                    .returning(Booking)
                )
                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
            return None