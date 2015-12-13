import compy


def main(sc):

    sc.printf('Hello',color=17)

    sc.printf('Hello', color=18)

    sc.printf('Hello', color=19)

    sc.printf('Hello, ',color=7)

    sc.printf('partner!', color=16)

    sc.printf('Hello',color=5)

    sc.printf('Hello, or better...', color=10, stay=True)

    sc.printf('Good bye!!!',color=12)

compy.run(main)


