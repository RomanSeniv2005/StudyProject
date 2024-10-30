from myapp.models import Orders
from myapp.repositories.base_repository import BaseRepository

class OrderRepository(BaseRepository):
    _model = Orders
