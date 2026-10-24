"""Functions for calculating steps in exchanging currency."""


def exchange_money(budget, exchange_rate):
    """Return the value of the foreign currency you can receive."""
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Return the amount left of your starting currency after the exchange."""
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Return the total value of the bills, excluding fractional amounts."""
    return int(denomination * number_of_bills)


def get_number_of_bills(amount, denomination):
    """Return the number of whole bills in the amount."""
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Return the leftover amount that can't be exchanged into whole bills."""
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Return the maximum value, in whole bills, after the exchange fee."""
    fee = exchange_rate / 100 * spread
    actual_rate = exchange_rate + fee
    exchanged = budget / actual_rate
    bills = exchanged // denomination
    return int(bills * denomination)