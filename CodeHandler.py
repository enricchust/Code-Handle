from abc import abstractmethod, ABC
from main import *
import time


class CodeHandler(ABC):
    def __init__(self,next_handler):
        self._next_handler = next_handler

    @abstractmethod
    def handle_code(self,code,door):
        if self._next_handler is not None:
            self._next_handler.handle_code(code,door)
        else:
            print("reached out of chain")

class Open(CodeHandler):
    def __init__(self, code, next_handler):
        self._code = code
        super().__init__(next_handler)

    def handle_code(self, code, door):
        if not door.locked:
            if(code == self._code):
                door.reset_state()
                door.locked = False
                door.open()
            else:
                door.num_trials += 1
                print('{} trials'.format(door.num_trials))
                super().handle_code(code, door)
        else:
            super().handle_code(code, door)


class Lock(CodeHandler):
    def __init__(self, code, next_handler):
        super().__init__(next_handler)

    def handle_code(self, code, door):
        if(door.num_trials>=3):
            door.locked = True
            print(f"Door {door.id} locked")
        super().handle_code(code, door)


class Unlock(CodeHandler):
    def __init__(self, code, next_handler):
        self._code = code
        super().__init__(next_handler)

    def handle_code(self, code, door):
        print("handle Open")
        if door.locked:
            if(code==self._code):
                door.reset_state()
                print(f"Door {door.id} unlocked")
        else:
            super().handle_code(code, door)


class FireAlarm(CodeHandler):
    def __init__(self, code, next_handler):
        self._code = code
        super().__init__(next_handler)

    def handle_code(self, code, door):
        if not door.locked:
            if(code == self._code):
                door.open()
                print("fire alarm activated")
                door.reset_state()
            else:
                door.num_trials += 1
                print('{} trials'.format(door.num_trials))
                super().handle_code(code, door)

        else:
            super().handle_code(code, door)

class Log(CodeHandler):
    def __init__(self,next_handler):
        super().__init__(next_handler)

    def handle_code(self, code,door):
        if door.locked:
            is_locked = "but it is locked"
        else:
            is_locked = "and it is not locked"
        print(f"Code '{code}' used in door {door.id} is_locked at {time.asctime()}")
        super().handle_code(code, door)

            