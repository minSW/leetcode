from threading import Event

class Foo:
    def __init__(self):
        self.event1 = Event()
        self.event2 = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        
        self.event1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event1.wait()
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        
        self.event2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event2.wait()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        
    
#     # not use threading library
# class Foo:
#     def __init__(self):
#         self.first_exec = False
#         self.second_exec = False
#         pass


#     def first(self, printFirst: 'Callable[[], None]') -> None:
#         # printFirst() outputs "first". Do not change or remove this line.
#         printFirst()
        
#         self.first_exec = True


#     def second(self, printSecond: 'Callable[[], None]') -> None:
#         while not self.first_exec :
#             continue
        
#         # printSecond() outputs "second". Do not change or remove this line.
#         printSecond()
        
#         self.second_exec = True


#     def third(self, printThird: 'Callable[[], None]') -> None:
#         while not self.second_exec :
#             continue
        
#         # printThird() outputs "third". Do not change or remove this line.
#         printThird()