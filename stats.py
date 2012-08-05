import math

class Stats(object):
    def __init__(self, d):
        self.data = d
        self.freq = {}
        self.mass = {}
        # Summary statistics
        self.size = len(self.data)
        self.mu   = sum(self.data) / float(self.size)

    def length(self):
        """Returns the len of the data"""
        return self.size 

    def mean(self):
        """Return the arithmetic mean of the data"""
        return self.mu

    def variance(self):
        """Return the variance of the data"""
        return sum(map(lambda x: pow(x - self.mean(), 2), self.data)) / float(self.length())

    def stdev(self):
        """Return the standard deviation of the data"""
        return math.sqrt(self.variance())

    def frequencies(self):
        """Return a frequency map of the data"""
        if (not self.freq) and self.length():
            for i, x in enumerate(self.data):
                self.freq[x] = self.freq.get(x, 0) + 1
        return self.freq.copy()

    # TODO: reimplement using map()
    def pmf(self):
        """Return the probability mass function of the data"""
        if (not self.mass) and self.length():
            for k, v in self.frequencies().iteritems():
                self.mass[k] = v / float(self.length())
        return self.mass.copy()

# Test things out
if __name__ == "__main__":
    data = (2, 3, 9, 2, 3, 9, 2, 1, 0, 1, 2, 0, 2)
    stats = Stats(data)
    print stats.frequencies()
    print stats.pmf()
    print sum(stats.pmf().values())
    print stats.mean()
    print stats.variance()
    print stats.stdev()
