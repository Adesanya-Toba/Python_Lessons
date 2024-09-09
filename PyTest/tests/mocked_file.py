# my_package/my_module.py
with open("mocked-file.txt", "r") as file:
    data = file.read()


def get_data():
    return data
