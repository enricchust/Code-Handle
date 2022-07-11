class Door():
    Max_Num_Trials = 3
    def __init__(self, id, code_open, code_fire_alarm, code_unlock):
        self._id = id
        self._code_open, self._code_fire_alarm, self._code_unlock = \
            code_open, code_fire_alarm, code_unlock
        self._locked = False
        self._num_trials = 0

    def process_code(self, code):
        self._log("entered code" + code)
        if not self._locked:
            if code==self._code_open:
                self._num_trials = 0
                self._open()
            elif code==self._code_fire_alarm:
                self._num_trials=0
                self._fire_alarm()
                self._open()
            else: #not a valid code when unlocked
                self._num_trials += 1
                if self._num_trials==Door.Max_Num_Trials:
                    self._lock()
        else:
            if code==self._code_unlock:
                self._unlock()

        def _log(self, action):
            is_locked = "is locked, " if self._locked else ""
            print('door {}, {}{} at {}' \
                    .format(self._id, is_locked, action, time.asctime()))

        def _open(self):
            self._log("open")
            # sends pulse to door's electromagnet so that door can be open

        def _fire_alarm(self):
            self._log("fire alarm")
            # sends message to control station

        def _lock(self):
            self._log("lock")
            self._locked = True

        def _unlock(self):
            self._log("unlock")
            self._locked = False
            self._num_trials = 0




if __name__ == '__main__':
    code_open, code_fire_alarm, code_unlock ='1111','2222','3333'
    d1 = Door('d1', code_open, code_fire_alarm, code_unlock)
    d1.process_code('1111') # opens
    d1.process_code('2222') # opens and fires alarm
    d1.process_code('1234') # first trial
    d1.process_code('4321') # second trial
    d1.process_code('5555') # thrid trial, gets locked
    d1.process_code('6666') # invalid unlock code
    d1.process_code('7777') # invalid unlock code
    d1.process_code('1111') # invalid unlock code
    d1.process_code('3333') # valid unlock code, now can be opened or fire alarm
    d1.process_code('2222') # opens and fires alarm