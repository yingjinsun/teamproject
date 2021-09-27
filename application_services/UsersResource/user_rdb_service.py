from database_services.RDBService import RDBService


class UserRDBService(RDBService):

    def __init__(self):
        pass

    @classmethod
    def get_user_and_address(cls, template):

        wc, args = RDBService.get_where_clause_args(template)
        sql = "select * from db.users left join db.addresses on " + \
                "db.primary_address_id = db.addresses.id"

        res = RDBService.run_sql(sql, args, fetch=True)
        return res

