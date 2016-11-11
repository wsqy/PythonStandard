# coding:utf-8
def get_task_hand_way(task_type="redis", access_way="get_task"):
    task_module = __import__("DataAccess." + task_type.upper(), globals(), locals(), [task_type.capitalize()])
    up_access = getattr(task_module, task_type.capitalize())
    return getattr(up_access(), access_way)

if __name__ == "__main__":
    get_task_hand_way()("a")
