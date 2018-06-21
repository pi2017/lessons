#
# __value = 1   privat
#   value = 1   public
#  _value = 1   protected

# Магические методы __doc__ , __name__
# class Converter

class Converter:
    exchange_rate = {
        'UAH': 26,
        'USD': 1,
        'EURO': 0.8,
    }

    def convert(self, input_rate, value, output_rate):
        usd = value // self.exchange_rate[input_rate]
        return usd * self.exchange_rate[output_rate]


class Currency:
    exchange_rate = {
        'UAH': 26,
        'USD': 1,
        'EURO': 0.8,
    }

    def __init__(self, value, currancy):
        self._value_in_usd = value // self.exchange_rate[currancy]
