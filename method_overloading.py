# Method overloading is an example of compile time polymorphism. More than one method of the same class shares the
# method name having different signatures. Method overloading is used to add more to the behaviour of methods and
# there is no need of more than one class for method overloading.
# Note: Python does not support method overloading. We may overload the methods but can only use the latest defined method

def add(datatype, *args):
    if datatype == 'int':
        answer = 0

    if datatype == 'str':
        answer = ''

    for x in args:
        answer = answer + x

    print(answer)

add('int', 5, 6)
add('str', )