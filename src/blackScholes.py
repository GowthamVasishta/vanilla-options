import math
from scipy.stats import norm

class BSOptionPricer:


    def __init__(self, underlying_spot, strike, rf_rate, time_to_expiry, vol, option_type):
        self.underlying_spot = underlying_spot
        self.strike = strike
        self.rf_rate = rf_rate/100
        self.time_to_expiry = time_to_expiry
        self.vol = vol/100
        self.option_type = option_type


    def _get_d1(self):
        self.d1 = ((math.log(self.underlying_spot/self.strike) + (self.rf_rate + (pow(self.vol, 2)/2)* self.time_to_expiry)) / (self.vol * math.sqrt(self.time_to_expiry)))
        return self.d1


    def _get_d2(self):
        try:
            self.d1
        except AttributeError:
            self.d1 = self._get_d1()
        
        self.d2 = self.d1 - (self.vol * math.sqrt(self.time_to_expiry))
        return self.d2

    def _get_strike_pv(self):
        strike_pv = self.strike * math.exp(-self.rf_rate * self.time_to_expiry)
        return strike_pv


    def price(self):
        d1 = self._get_d1()
        d2 = self._get_d2()
        strike_pv = self._get_strike_pv()

        nd1 = norm.cdf(d1)
        nd2 = norm.cdf(d2)

        call_price = (self.underlying_spot * nd1) - strike_pv * nd2

        if(self.option_type == "c"):
            return call_price
        elif(self.option_type == "p"):
            put_price = call_price + strike_pv - self.underlying_spot
            return put_price
        else:
            return false 



