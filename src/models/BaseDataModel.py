from helpers.config import get_settings, Settings
from .db_schemas import Project

class BaseDataModel:
    def __init__(self, db_client: object):
        self.app_settings = get_settings()
        self.db_client = db_client