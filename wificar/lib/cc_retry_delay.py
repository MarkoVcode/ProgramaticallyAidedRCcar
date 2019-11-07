import time

class cc_retry_delay:
    def __init__(self, initDelay=0.1, maxDelay=30):
        self.retryCounter = 0
        self.initDelay = initDelay
        self.delay = initDelay
        self.maxDelay = maxDelay
 
    def fail(self):
        if self.delay <= self.maxDelay:
            self.retryCounter = self.retryCounter + 1
            self.delay = round((self.delay * self.retryCounter),3)

    def reset(self):
        self.delay = self.initDelay

    def getDelay(self):
        return self.delay

if __name__ == '__main__':
    print("retrydelay")