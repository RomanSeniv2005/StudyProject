from myapp.models import GoodsTypes
from myapp.repositories.base_repository import BaseRepository

class GoodsTypeRepository(BaseRepository):
    _model = GoodsTypes
