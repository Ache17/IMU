import serial


class Subscriber(object):
    def __init__(self):
        pass

    def callback(self, dat):
        raise NotImplementedError


class printSubscriber(Subscriber):
    def callback(self, dat):
        print(dat)


class serialReader(object):

    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.dat = None
        self.subscribers = []

    def read_forever(self):
        with serial.Serial(self.port, baudrate=self.baudrate) as ser:
            while True:
                self.dat = ser.readline()

                for callback in self.subscribers:
                    callback(self.dat)

    def addSubscriber(self, subscriber: Subscriber):
        self.subscribers.append(subscriber.callback)


if __name__ == "__main__":
    s = serialReader("COM7", 115200)
    s1 = printSubscriber()
    s.addSubscriber(s1)

    s.read_forever()
