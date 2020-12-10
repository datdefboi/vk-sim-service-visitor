from visitor import Visitor

if __name__ == "__main__":
    v = Visitor()
    v.connect_to_api()
    v.enqueue_first_user()
    v.visit_top_user()