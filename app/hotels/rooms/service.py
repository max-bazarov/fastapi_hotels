from app.core.service import BaseService
from app.hotels.rooms.models import Room


class RoomsService(BaseService):
    model = Room
