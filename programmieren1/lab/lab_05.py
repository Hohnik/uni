import doctest

def main():
    doctest.testmod()

class VendingMachine(object):
    """A vending machine that vends some product for some price
    - constructor(item, count)
    - vend() -> sideeffects + print
    - add_funds(int) -> sideeffect + print

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'


    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    # YOUR CODE HERE

    price = None
    item = None
    balance = 0
    stock_amount = 0

    def __init__(self, item: str, price: int):
        self.item = item
        self.price = price
        

    def add_funds(self, balance: int):
        if self.stock_amount == 0:
            return f"Nothing left to vend. Please restock. Here is your ${balance}."

        self.balance += balance
        return f"Current balance: ${self.balance}"
    
    def restock(self, amount: int):
        self.stock_amount += amount
        return f"Current {self.item} stock: {self.stock_amount}"
        

    def vend(self):
        if self.stock_amount== 0:
            return 'Nothing left to vend. Please restock.'
        
        if self.balance < self.price:
            return f'Please add ${self.price - self.balance} more funds.'
        
        change = self.balance - self.price
        self.balance = 0
        self.stock_amount -= 1
        
        if change:
            return f'Here is your {self.item} and ${change} change.'

        return f'Here is your {self.item}.'
    
if __name__ == "__main__":
    main()