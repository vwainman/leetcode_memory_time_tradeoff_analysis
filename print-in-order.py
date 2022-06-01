# https://leetcode.com/problems/print-in-order/description/
#
# Suppose we have a class:
#
# public class Foo {
# ⁠ public void first() { print("first"); }
# ⁠ public void second() { print("second"); }
# ⁠ public void third() { print("third"); }
# }
#
#
# The same instance of Foo will be passed to three different threads. Thread A
# will call first(), thread B will call second(), and thread C will call
# third(). Design a mechanism and modify the program to ensure that second() is
# executed after first(), and third() is executed after second().
#
# Note:
# We do not know how the threads will be scheduled in the operating system,
# even though the numbers in the input seem to imply the ordering. The input
# format you see is mainly to ensure our tests' comprehensiveness.


from threading import Barrier, Thread

N_THREAD_ENCOUNTERS = 2


def print_first():
    print("first")


def print_second():
    print("second")


def print_third():
    print("third")


class Foo:
    def __init__(self):
        self.first_barrier = Barrier(N_THREAD_ENCOUNTERS)
        self.second_barrier = Barrier(N_THREAD_ENCOUNTERS)

    def first(self, print_first=print_first) -> None:
        print_first()
        self.first_barrier.wait()

    def second(self, print_second=print_second) -> None:
        self.first_barrier.wait()
        print_second()
        self.second_barrier.wait()

    def third(self, print_third=print_third) -> None:
        self.second_barrier.wait()
        print_third()


def print_in_order(method_inputs):
    for thread in method_inputs:
        thread.start()
    for thread in method_inputs:
        thread.join()


if __name__ == "__main__":
    case1_foo = Foo()
    case1_inputs = [Thread(target=case1_foo.first),
                    Thread(target=case1_foo.second),
                    Thread(target=case1_foo.third)]
    print_in_order(case1_inputs)
    case2_foo = Foo()
    case2_inputs = [Thread(target=case2_foo.first),
                    Thread(target=case2_foo.third),
                    Thread(target=case2_foo.second)]
    print_in_order(case2_inputs)
