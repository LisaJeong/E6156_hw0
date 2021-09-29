from database_services.RDBService import RDBService


class UserRDBService(RDBService):

    def __init__(self):
        pass

    @classmethod
    def get_user(cls, template):

        wc, args = RDBService.get_where_clause_args(template)
        sql = "select * from users"

        res = RDBService.run_sql(sql, args, fetch=True)
        return res

