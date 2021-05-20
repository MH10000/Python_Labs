'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
entry_stock_price_gbp = 10
exit_stock_price_gbp = 15
usd_gbp_entry = 1.3
usd_gbp_exit = 1.4

def usd_entry(price, rate):
    entry_amount_usd = price * rate
    return entry_amount_usd

def usd_exit(price, rate):
    exit_amount_usd = price * rate
    return exit_amount_usd
 
    def profit_usd(open, close):
        profit_ = exit_amount_usd - entry_amount_usd
        return profit_
    
        def profit_condition():
            if profit_ > 2:
                print("nice profit!")
            else:
                print("better luck next time!")

print(usd_entry(entry_stock_price_gbp, usd_gbp_entry))
print(usd_exit(exit_stock_price_gbp, usd_gbp_exit))
print()

