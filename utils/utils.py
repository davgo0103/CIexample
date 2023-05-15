class Utils():

    def __init__(self):
        self._name = 'utils'

    def add(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('The input argument should be Integer')
        
        return a + b

    def subtract(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('The input argument should be Integer')

        return a - b

    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('The input argument should be Integer')

        return a * b

    def divide(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('The input argument should be Integer')

        if b == 0:
            raise ValueError('Cannot divide by zero')

        return a / b
