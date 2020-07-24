class Logger:

    def __init__(self):
        self.d = dict()


    def shouldPrintMessage(self, timestamp, message):
        if message not in self.d:
            self.d[message] = timestamp
            return True

        if timestamp - self.d[message] >= 10:
            self.d[message] = timestamp
            return True
        else:
            return False

