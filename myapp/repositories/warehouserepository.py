from myapp.models import Warehouses
from myapp.repositories.base_repository import BaseRepository

class WarehouseRepository(BaseRepository):
    _model = Warehouses
