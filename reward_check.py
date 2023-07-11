
def find_best_user(file_path):
    num = 0
    line = []

    with open(file_path, "r") as file:
       for line in file:
           num_str = line.split()[1:]
           if num < 17



def test():
    result = find_best_user("users.txt")
    print(result)

test()