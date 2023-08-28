from src.blackScholes import BSOptionPricer
import matplotlib.pyplot as plt
import numpy as np


# option specs
spots = np.arange(75, 126, 1).tolist()
strike = 100
rf_rate = 5.5
time_to_expiry = 0.5
vol = 20


call_prices = []
put_prices = []
call_payoff_at_expiry = []
put_payoff_at_expiry = []


for spot in spots:
    #calculate call option prices
    option_type = "c"
    option_obj = BSOptionPricer(spot, strike, rf_rate, time_to_expiry, vol, option_type)
    call_price = option_obj.price()
    call_prices.append(call_price)
    
    #calculate call option payoff at expiry
    call_payoff = max(0, spot - strike)
    call_payoff_at_expiry.append(call_payoff)


    #calculate put option prices
    option_type = "p"
    option_obj = BSOptionPricer(spot, strike, rf_rate, time_to_expiry, vol, option_type)
    put_price = option_obj.price()
    put_prices.append(put_price)

    # call put option payoff at expiry
    put_payoff = max(0, strike - spot)
    put_payoff_at_expiry.append(put_payoff)



# Plot the graph
plt.plot(spots, call_prices, label="Call price")
plt.plot(spots, put_prices, label = "Put Price")
#plt.plot(spots, call_payoff_at_expiry, label = "Call payoff at expiry")
#plt.plot(spots, put_payoff_at_expiry, label = "Put payoff at expiry")
plt.xlabel("Spot")
plt.ylabel("Option Price")
plt.title("Option Price Analysis")
plt.legend()
plt.show()
