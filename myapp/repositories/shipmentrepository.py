from myapp.models import Shipments
from myapp.repositories.base_repository import BaseRepository

class ShipmentRepository(BaseRepository):
    _model = Shipments
