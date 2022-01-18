def make_pizza(size, *toppong):
    """
    Summarize the pizza we are about to make.
    """
    print('\nMaking a {}-inch pizza with the following topping')
    for topping in toppings:
        print('-'+topping)