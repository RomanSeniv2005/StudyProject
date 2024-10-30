from myapp.models import Items
from myapp.repositories.base_repository import BaseRepository

class ItemRepository(BaseRepository):
    _model = Items
