from newone import client


def find_user(username):
    print(username)
    result = client.Employees.Users.find_one({"username": username})
    return result


def reg_user(new_user):
    result = client.Employees.Users.insert_one(new_user)
    return result



