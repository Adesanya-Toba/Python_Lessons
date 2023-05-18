# Most built-in exceptions derive from the Exception class
# The Exception, SystemExit and KeyboardInterrupt class derives from the BaseException class
from decimal import Decimal
import time

class MyCustomException(ValueError):
    pass

# We could also customize the initializer and add other methods 
class InvalidWithdrawal(ValueError):
    def __init__(self, balance:Decimal, amount:Decimal) -> None:
        super().__init__(f'account does not have ${amount}!')
        self.amount = amount
        self.balance = balance

    def overage(self) -> Decimal:
        return self.amount - self.balance


if __name__ == '__main__':

    try:
        balance = Decimal(25.00)
        raise InvalidWithdrawal(balance, Decimal(50.00))
    except InvalidWithdrawal as ex:
        print("I'm sorry, your withdrawal is more than your balance "
              f"by ${ex.overage()}")
    
    num = 2
    msg = (f'There is one' 
           if num == 1 
           else f'There are many!'
           )
    print(msg)
    # Catching system exceptions
    cnt = 0
    while True:
        try:
            
            print('I am always running!')
            time.sleep(1)
        except:
            print("Why do you wanna stop me! Haha, you can't!!")
            if cnt == 0: raise BaseException("I'll let you go now. Lol")
            cnt -= 1

        # raise MyCustomException('Who do you think you are?')