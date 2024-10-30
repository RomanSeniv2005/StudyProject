from myapp.models import Clients
from myapp.repositories.base_repository import BaseRepository

class ClientRepository(BaseRepository):
    _model = Clients
