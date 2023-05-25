def check(input_func):
    def output_func(*args):
        name = args[0]
        age = args[1]
        if age < 0: age = 1
        input_func(name, age)
        # print("ya vipolnilsya do func")
        # input_func()
        # print("ya vipolnilsya posle func")

    return output_func


@check
def print_person(name, age):
    print(f"Name: {name} Age: {age}")


print_person("Tom", 56464)
print_person("syhe", 7478)


