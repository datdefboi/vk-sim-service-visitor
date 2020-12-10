from queue import Queue
from api import get_api


class Visitor:
    def __init__(self):
        self.user_q = Queue()
        self.communities = {}

    def connect_to_api(self):
        self.api = get_api()

    def enqueue_first_user(self):
        self.user_q.put(self.api.users.get()[0]["id"])

    def visit_top_user(self):
        c_u = self.user_q.get()

        subs = self.api.users.getSubscriptions(user_id=c_u)
        group_ids = str(subs["groups"]["items"])[1:-1]
        groups = self.api.groups.getById(group_ids=group_ids)
        

