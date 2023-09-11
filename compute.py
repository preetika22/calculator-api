class NumberInput(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def number_decoder(obj):
        return NumberInput(obj['first'], obj['second'])

# class for calculation
class Calculator(object):

    def add(self, first, second):
        return first + second

    def subtract(self, first, second):
        return first - second