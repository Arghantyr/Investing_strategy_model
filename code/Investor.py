class Investor:
    """
    All the data about the investor.

    Takes information characteristic for the investor, i.e.: initial funds (unitless measure),
    luck (50% at standard), risk, profit and creates an instance of an investor.

    Parameters:
    -----------------

    name: str
        Name of the investors instance.

    initial_funds: int = 1000
        Initial sum of money to be invested.

    funds:
        Current funds holded by the investor.

    luck: float = 0.5
        A collective paramater dependent on proper investment entry, investment exit. Must be a value
        from range (0,1)
    """

    def __init__(self, name: str, initial_funds: int=1000, luck: float=0.5):

        self.name = name
        self.initial_funds = initial_funds
        self.funds = initial_funds
        self.luck = luck

    def change(self, attribute = 'name', new_value = None):

        setattr(self, attribute, new_value)
