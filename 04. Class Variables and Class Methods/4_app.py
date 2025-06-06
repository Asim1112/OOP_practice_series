# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that
# allows changing the bank name. Show that it affects all instances.



class Bank:
    bank_name = "MCB"

    
    @classmethod
    def change_bank(cls, name):
        cls.bank_name = name
        print(cls.bank_name)



print("\nBank Name before Changes:")
bank1 = Bank()
print(bank1.bank_name)
bank1.change_bank("UBL")



Bank.change_bank("HBL")


print("\nBank Name After Changes:")
bank2 = Bank()
print(bank2.bank_name)
bank2.change_bank("ABL")
