import os

class Stats(object):
    def __init__(self, d):
        self.data = d
        self.freq = {}
        self.mass = {}

    def frequencies(self):
        """Returns a frequency map of the data"""
        if 0 == len(self.freq) and 0 < len(self.data):
            for i, x in enumerate(self.data):
                self.freq[x] = self.freq.get(x, 0) + 1
        return self.freq.copy()

    def pmf(self):
        """Return the probability mass function of the data"""
        if 0 == len(self.mass) and 0 < len(self.data):
            for k, v in self.frequencies().iteritems():
                self.mass[k] = v / float(len(self.data))
        return self.mass.copy()



if __name__ == "__main__":
    data = (2, 3, 9, 2, 3, 9, 2, 1, 0, 1, 2, 0, 2)
    stats = Stats(data)
    print stats.frequencies()
    print stats.pmf()
    print sum(stats.pmf().values())
