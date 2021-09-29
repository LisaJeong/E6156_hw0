from database_services.RDBService import RDBService
from application_services.UsersResource.user_rdb_service import UserRDBService
"""
def t1():

    res = RDBService.get_by_prefix(
        "imdbnew", "names_basic_recent", "primaryName", "Tom H"
    )
    print("t1 resule = ", res)
"""


def t2():

    res = RDBService.get_user(
        "aaaaF21", "users"
    )
    print("t2 resuls = ", res)

"""
def t3():

    res = RDBService.create(
        "aaaaf21", "addresses",
            {
                "address1": "520 w 120th St",
                "city": "New York",
                "region": "NY",
                "country": "USA",
                "postal_code": "10027"
            })
    print("t3: res = ", res)

#t2()
t3()
"""

t2()
