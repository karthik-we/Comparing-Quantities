# COMPARING QUANTITIES FORMULAS

# DISCOUNT FORMULAS

# DISCOUNT

def discount_value(marked_price, sales_price):
    discount_ = marked_price + sales_price
    return discount_


# COST PRICE
def cost_price(purchase_price, overhead_expenses):
    cost_ = purchase_price + overhead_expenses
    return cost_


# COMPOUND INTEREST FORMULAS

# ANNUALLY

def comp_annually(principal, rate, time_period):
    annual = principal * (1 + rate * 100) * time_period
    return annual


# HALF-YEARLY

def comp_half_yearly(principal, rate, time_period):
    half = principal * (1 + rate * 200) * time_period
    return half


# IMPORTANT FORMULAS OF COMPARING QUANTITIES

# COST PRICES OTHER FORMULAS

# USE WHEN SELLING PRICE AND LOSS ARE GIVEN

def cost_price1(selling_price1, profit):
    cost_ = selling_price1 - profit
    return cost_


# USE WHEN SELLING PRICE AND LOSS ARE GIVEN
def cost_price2(selling_price2, loss):
    cost_ = selling_price2 + loss
    return cost_


# SELLING PRICE FORMULAS

# USE WHEN COST PRICE AND PROFIT ARE GIVEN

def selling_price3(cost_price3, profit):
    selling_ = cost_price3 + profit
    return selling_


# USE WHEN COST PRICE AND LOSS ARE GIVEN

def selling_price4(cost_price4, loss):
    selling_ = cost_price4 + loss
    return selling_


# PROFIT

def profit_value(selling_price5, cost_price5):
    profit = selling_price5 - cost_price5
    return profit

# PROFIT PERCENTAGE

def profit_percent(selling_prices, cost_prices):
    profit_percentage = ((selling_prices - cost_prices) / cost_prices) * 100
    return profit_percentage


# LOSS

def loss_value(cost_price6, selling_price6):
    loss = cost_price6 - selling_price6
    return loss

# LOSS PERCENTAGE

def loss_percent(cost_price0, selling_price0, ):
    loss_percentage = ((cost_price0 - selling_price0) / cost_price0 * (selling_price0-cost_price0)) * 100
    return loss_percentage

# NET PRICE

def net_price(marked_price, discount):
    net = marked_price - discount
    return net

    # SALES TAX FORMULAS

    # BILL AMOUNT

def bill_amount(cost_of_commodity, sales_tax):
    amount = cost_of_commodity + sales_tax
    return amount

    # VALUE ADDED TAX

def value_added_tax(tax_charged, tax_paid):
    tax = tax_charged + tax_paid
    return tax

    # ANOTHER FORMULA FOR VALUE ADDED TAX WHEN SELLING AND COST PRICE ARE GIVEN

def value_added_tax1(tax, selling_price7, cost_price7):
    tax1 = tax % (selling_price7 - cost_price7)
    return tax1

    # SIMPLE INTEREST AND TOTAL AMOUNT

def simple_interest(principal, rate_of_interest, time):
    interest = (principal * rate_of_interest * time) / 100
    total_amount = principal + interest
    return interest and total_amount
