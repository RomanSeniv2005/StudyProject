from myapp.models import WarehouseReservations
from myapp.repositories.base_repository import BaseRepository

class WarehouseReservationRepository(BaseRepository):
    _model = WarehouseReservations
