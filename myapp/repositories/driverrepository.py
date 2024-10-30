from myapp.models import Drivers
from myapp.repositories.base_repository import BaseRepository

class DriverRepository(BaseRepository):
    _model = Drivers
