class TaxMan: # defines a class named TaxMan 
    def __init__(self, items, sales_tax): # This line defines a constructor method for the TaxMan class. 
        #The constructor is called when an instance of the class is created. 
        #It takes two parameters: items and sales_tax.

        self.items = items # assigns the value of the items parameter to the items attribute of the
        #class instance. The items parameter is expected to be a list of items.
        self.__sales_tax = float(sales_tax.strip('%')) / 100 
        #assigns the value of the sales_tax parameter to the sales_tax attribute 
        # of the class instance. 
         # Convert sales tax string to a decimal value
        # The line removes the '%' character from the string using the
         # strip('%') method, then converts the resulting string to a float. Finally, it divides the 
         # float value by 100 to convert the sales tax to a decimal value.
        self.__total = 0.0 #total attribute of the class instance to 0.0. The total attribute will 
        #store the calculated total price including the sales tax.

    def calc_total(self):#defines a method named calc_total within the TaxMan class.
        # This method calculates the total price including the sales tax.
        total_price = sum(item['price'] for item in self.items)
        #This line calculates the total price of all items in the items list. It uses a generator expression
        #  to iterate over each item in the list and access the 'price' key of each item dictionary. The sum() function is then used to add up all the prices.
        
        self.__total = total_price + (total_price * self.__sales_tax)

        # It multiplies the total_price by the sales_tax and adds the result to the total_price. The 
        # final result is assigned to the total attribute of the class instance.

    def get_total(self):
        return self.__total
