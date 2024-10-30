from myapp.models import OrderItem
from myapp.repositories.base_repository import BaseRepository

class OrderItemRepository(BaseRepository):
    _model = OrderItem
