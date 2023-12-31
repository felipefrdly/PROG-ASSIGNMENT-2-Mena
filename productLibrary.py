#Felipe Mena
#10/21/2023
#This program is designed to calculate and simulate sales metrics of diffrent products that a user creates. this file contains all objects that the program revolves around
import random

"""
The product class is meant to handle all math and display all results in a visually pleasing way
"""
class Product:
    """This method initalizes all variables on objects creation"""
    def __init__(self, proCode, proName, proSalePrice, proManuCost, proStockLevel, approxMonthlyUnits):
        self._proCode = proCode
        self._proName = proName
        self._proSalePrice = proSalePrice
        self._proManuCost = proManuCost
        self._proStockLevel =  proStockLevel
        self._approxMonthlyUnits = approxMonthlyUnits
        
    """This method handles math of the stock statement and displays it for each month"""
    def PredictStockStatement(self):
        stock = self._approxMonthlyUnits + self._proStockLevel #sets the stock by adding the monthly units made and the current stock level
        salesOfYear = 0 #empty variable for storing yearly sales
        manufactAYear = 0 #empty variable for storing manufacturing total

        for i in range(1,13):
            unitsSold = random.randint(self._approxMonthlyUnits -10 , self._approxMonthlyUnits + 10) #estimates the units sold by generating a number between 1 and the units manufactured +/- 10
            newStock = stock - unitsSold #creates a variable to store the stock after the units are sold
            print(f"Month {i}:") #Display the month
            print(f"|   Manufactured: {self._approxMonthlyUnits}") #Display the manufactured units
            print(f"|   Sold: {unitsSold}") #displays the units sold
            print(f"|   Stock: {newStock}") #displays the new stock
            stock = newStock + self._approxMonthlyUnits #updates the stock for next month by adding the monthly units
            
            salesOfYear += unitsSold #adds the units sold that month to the total
            manufactAYear += self._approxMonthlyUnits #adds the units manufactured to the total
            
        netProfit = (salesOfYear * self._proSalePrice) - (manufactAYear * self._proManuCost) #forumla that calculates net profit
        print(f"Net Proftis: ${round(netProfit, 2)} CAD") #displays net profit

"""
The Application class handles all user input that the program needs. Do note that each method is built the same, please use the comments 
from the first method if you want to understand whats going on
"""
class Application:
    def InputInt(self, data):
        while True: #users in the loop until a suitable choice is given
            try:
                question = int(input("Please enter the " + data + ": ")) #asks question as an int
                return(question) #returns answer if true
            except ValueError: #if the value of the input is not an int display debug message and loop
                print("Please enter the data as a whole number!")
                continue

    def InputStr(self, data): #does the same thing as method above but with strings
        while True:
            try:
                question = str(input("Please enter the " + data +": "))
                return(question)
            except ValueError:
                print("Please enter the data in text!")
                continue

    def InputFlo(self, data): #does the same thing as method above but with floats
        while True:
            try:
                question = float(input("Please enter the " + data + ": "))
                return(question)
            except ValueError:
                print("Please enter the data as a decimal number!")
                continue