from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service


class IMDBArtistResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_by_name_prefix(cls, name_prefix):
        res = d_service.RDBService.get_by_prefix("db", "name_basics",
                                      "primaryName", name_prefix)
        return res