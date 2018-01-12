def greet_person(sPersonName):
    """
    says hello
    """
    if sPersonName == "Mona":
        raise Exception("we don't like you, Mona")
    print("Hi there {0}".format(sPersonName))

greet_person("Mona")
#greet_person("Smita")
