from myapp.models import Routes
from myapp.repositories.base_repository import BaseRepository

class RouteRepository(BaseRepository):
    _model = Routes
