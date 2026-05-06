# funtion is a first class object

def double_decker():
    print("Starting the double decker")
    def inner_fun():
        print("Inside the inner")
        return 3000

    return inner_fun

# print(double_decker())
# print(double_decker()())

def do_something(work):
    print("Word started")
    # print(work)
    work()
    print("Work ended")

# do_something(2)
# do_something("ami busy")

def coding():
    print("Codingin pythond")

# do_something(coding)

def sleeping():
    print("Sleeping and dreaming in pythond")

do_something(sleeping)