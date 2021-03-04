# COMPARING QUANTITIES FORMULAS

# DISCOUNT FORMULAS

# DISCOUNT

def discount_value(marked_price, sales_price):
    discount = marked_price + sales_price
    return discount


# COST PRICE
def cost_price(purchase_price, overhead_expenses):
    cost = purchase_price + overhead_expenses
    return cost


# COMPOUND INTEREST FORMULAS

# ANNUALLY

def comp_annually(principal, rate, time_period):
    annual = principal * (1 + rate * 100) * time_period
    return annual


# HALF-YEARLY

def comp_half_yearly(principal, rate, time_period):
    half = principal * (1 + rate * 200) * time_period
    return half


# IMPORTANT FORMULAE OF COMPARING QUANTITIES

# COST PRICES OTHER FORMULAE

# USE WHEN SELLING PRICE AND PROFIT ARE GIVEN

def cost_price_when_sell_profit_given(selling_price, profit):
    cost  = selling_price - profit
    return cost


# USE WHEN SELLING PRICE AND LOSS ARE GIVEN

def cost_price_when_sell_loss_given(selling_price, loss):
    cost = selling_price + loss
    return cost


# SELLING PRICE FORMULAE

# USE WHEN COST PRICE AND PROFIT ARE GIVEN

def selling_price_when_cost_profit_given(cost, profit):
    selling = cost + profit
    return selling



# USE WHEN COST PRICE AND LOSS ARE GIVEN

def selling_price_when_cost_loss_given(cost, loss):
    selling = cost + loss
    return selling


# PROFIT

def profit_value(selling_price, cost):
    profit = selling_price - cost
    return profit

# PROFIT PERCENTAGE

def profit_percent(selling_price, cost):
    profit_percentage = ((selling_price - cost) / cost) * 100
    return profit_percentage


# LOSS

def loss_value(cost, selling_price):
    loss = cost - selling_price
    return loss

# LOSS PERCENTAGE

def loss_percent(cost, selling_price, ):
    loss_percentage = ((cost - selling_price) / cost * (selling_price-cost)) * 100
    return loss_percentage

# NET PRICE

def net_price(marked_price, discount):
    net = marked_price - discount
    return net

    # SALES TAX FORMULAE

    # BILL AMOUNT

def bill_amount(cost_of_commodity, sales_tax):
    amount = cost_of_commodity + sales_tax
    return amount

    # VALUE ADDED TAX

def value_added_tax(tax_charged, tax_paid):
    tax = tax_charged + tax_paid
    return tax

    # ANOTHER FORMULA FOR VALUE ADDED TAX WHEN SELLING AND COST PRICE ARE GIVEN

def value_added_tax_when_sell_cost_given(tax, selling_price, cost):
    vat = tax % (selling_price - cost)
    return vat

    # SIMPLE INTEREST

def simple_interest(principal, rate_of_interest, time):
    interest = (principal * rate_of_interest * time) / 100
    return interest

    # TOTAL AMOUNT

def total_amount(principal,rate_of_interest,time):
    tot = principal + ((principal * rate_of_interest * time)/100)
    return tot