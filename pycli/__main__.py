import argparse
from .classmodule import MyClass
from .funcmodule import my_function


parser = argparse.ArgumentParser()
parser.add_argument('-x', type=int, default=0,
                    help='set value of x')
args = parser.parse_args()


def main():
    print('x = {}'.format(args.x))

    my_function('hello world')

    my_object = MyClass('G')
    my_object.say_name()


if __name__ == '__main__':
    main()
