from CodeHandler import *

class Door():
    def __init__(self, id, code_handler):
        self.id = id
        self._code_handler = code_handler
        self.num_trials = 0
        self.locked = False

    def process_code(self, code):
        self._code_handler.handle_code(code, self)

    def open(self):
        print('open door {}'.format(self.id))

    def reset_state(self):
        self.num_trials = 0
        self.locked = False

if __name__ =='__main__':
    code_open, code_fire_alarm, code_unlock = '1111','2222','3333'
    chain1 = Log(Unlock(code_unlock, FireAlarm(code_fire_alarm,Open(code_open, Lock(None,None)))))
    chain2 = Log(Open(code_open,None))
    chain3 = Log(FireAlarm(code_fire_alarm, Open(code_open,None)))
    d1 = Door('d1', chain1)
    if True\



            :
        d1.reset_state()
        d1.process_code('1111')  # opens
        d1.process_code('2222')  # opens and fires alarm
        d1.process_code('1234')  # first trial
        d1.process_code('4321')  # second trial
        d1.process_code('5555')  # thrid trial, gets locked
        d1.process_code('6666')  # invalid unlock code
        d1.process_code('7777')  # invalid unlock code
        d1.process_code('1111')  # invalid unlock code
        d1.process_code('3333')  # valid unlock code, now can be opened or fire alarm
        d1.process_code('2222')  # opens and fires alarm

    if False:
        d1.reset_state()
        d1._code_handler = chain2

        d1.process_code('1111')  # opens
        d1.process_code('2222')  # opens and fires alarm
        d1.process_code('1234')  # first trial
        d1.process_code('4321')  # second trial
        d1.process_code('5555')  # thrid trial, gets locked
        d1.process_code('6666')  # invalid unlock code
        d1.process_code('7777')  # invalid unlock code
        d1.process_code('1111')  # invalid unlock code
        d1.process_code('3333')  # valid unlock code, now can be opened or fire alarm
        d1.process_code('2222')  # opens and fires alarm

    if False:
        d1.reset_state()
        d1._code_handler = chain3

        d1.process_code('1111')  # opens
        d1.process_code('2222')  # opens and fires alarm
        d1.process_code('1234')  # first trial
        d1.process_code('4321')  # second trial
        d1.process_code('5555')  # thrid trial, gets locked
        d1.process_code('6666')  # invalid unlock code
        d1.process_code('7777')  # invalid unlock code
        d1.process_code('1111')  # invalid unlock code
        d1.process_code('3333')  # valid unlock code, now can be opened or fire alarm
        d1.process_code('2222')  # opens and fires alarm
