import array

PROCESS_VARIANCE = 1e-3

class KalmanFilter(object):
#http://scottlobdell.me/2014/08/kalman-filtering-python-reading-sensor-input/
    def __init__(self, process_variance, estimated_measurement_variance):
        self.process_variance = process_variance
        self.estimated_measurement_variance = estimated_measurement_variance
        self.posteri_estimate = 0.0
        self.posteri_error_estimate = 1.0

    def input_latest_noisy_measurement(self, measurement):
        priori_estimate = self.posteri_estimate
        priori_error_estimate = self.posteri_error_estimate + self.process_variance

        blending_factor = priori_error_estimate / (priori_error_estimate + self.estimated_measurement_variance)
        self.posteri_estimate = priori_estimate + blending_factor * (measurement - priori_estimate)
        self.posteri_error_estimate = (1 - blending_factor) * priori_error_estimate

    def get_latest_estimated_measurement(self):
        return self.posteri_estimate

class SMAFilter(object): 
#Simple Moving Average (SMA)
    def __init__(self, historyElems = 10 , initialValue = 5):
        self.array_meanA = array.array('f')
        self.historyElems = historyElems
        for v in range(historyElems):
            self.array_meanA.append(initialValue)

    def filter(self, value):
        n = self.historyElems
        for h in range(n):
            if h < n-1:
                self.array_meanA[h] = self.array_meanA[(h+1)]    # Shift the values in the array to the left
            else:
                self.array_meanA[h] = value
        meanA = 0
        for h in range(n):
            meanA = self.array_meanA[h] + meanA          # Calculate the mean, no weights.
        meanA = meanA/n
        return meanA

class EWMAFilter(object):
#Exponentially Weighted Moving Average (EWMA)
    def __init__(self):
        self.a = 0.20                # Weighting. Lower value is smoother.
        self.previousValue = 0       # Initialise the filter.

    def filter(self, value):
        filteredValue = (1-self.a)*self.previousValue + self.a*value
        self.previousValue = filteredValue   # Prepare for next iteration.
        return filteredValue


if __name__ == '__main__':
    #print(int("44.0"))
    #kf = SMAFilter()
    kf = EWMAFilter()
    print(kf.filter(5))
    print(kf.filter(4))
    print(kf.filter(3))
    print(kf.filter(2))
    print(kf.filter(1))
    print(kf.filter(1))
    print(kf.filter(1))
    print(kf.filter(1))
    print(kf.filter(1))
    print(kf.filter(1))
    print(kf.filter(1))
    print(kf.filter(1))
    print(kf.filter(1))
    print(kf.filter(1))
    print(kf.filter(5))
    print(kf.filter(5))
    print(kf.filter(5))
    print(kf.filter(5))
    print(kf.filter(5))
    print(kf.filter(5))