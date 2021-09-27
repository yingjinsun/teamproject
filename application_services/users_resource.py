from abc import ABC

from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service


class IMDBUserResource(BaseApplicationResource, ABC):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_by_name_prefix(cls, name_prefix):
        res = d_service.RDBService.get_by_prefix("IMDBFixed", "name_basics",
                                      "primaryName", name_prefix)
        return res
