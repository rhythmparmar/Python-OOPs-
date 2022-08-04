def hello_decorator(func):

    def inner1():
        print("Hello,this is before function execution")

        func()
        print("this is after funvction execution")

    return inner1


def china():
    print("Bejing")
def india():
    print("New Delhi")


function_to_be_used=hello_decorator(china)
function_to_be_used()


function_to_be_used=hello_decorator(india)
function_to_be_used()
