from myapp.models import Vehicles
from myapp.repositories.base_repository import BaseRepository

class VehicleRepository(BaseRepository):
    _model = Vehicles
