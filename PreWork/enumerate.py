
my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
my_string = ""
for index, object in enumerate(my_list):
    my_string += object + " "
    if index == 3 or index == 4:
        my_string += "and "
print(my_string)