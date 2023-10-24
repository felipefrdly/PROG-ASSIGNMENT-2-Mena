#Felipe Mena
#10/21/2023
#This program is designed to calculate and simulate sales metrics of diffrent products that a user creates. this file contains all objects that the program revolves around
import random

class Product:
    #initalizes all variables on objects creation
    def __init__(self, proCode, proName, proSalePrice, proManuCost, proStockLevel, approxMonthlyUnits):
        self._proCode = proCode
        self._proName = proName
        self._proSalePrice = proSalePrice
        self._proManuCost = proManuCost
        self._proStockLevel =  proStockLevel
        self._approxMonthlyUnits = approxMonthlyUnits
        
    #THIS WAS A PAIN TO SET UP :(
    def PredictStockStatement(self):
        stock = self._approxMonthlyUnits + self._proStockLevel #sets the stock by adding the monthly units made and the current stock level
        salesOfYear = 0 #empty variable for storing yearly sales
        manufactAYear = 0 #empty variable for storing manufacturing total

        for i in range(1,13):
            unitsSold = random.randint(self._approxMonthlyUnits -10 , self._approxMonthlyUnits + 10) #estimates the units sold by generating a number between 1 and the units manufactured +/- 10
            newStock = stock - unitsSold #creates a variable to store the stock after the units are sold
            print(f"Month {i}:") #Display the month
            print(f"Manufactured: {self._approxMonthlyUnits}") #Display the manufactured units
            print(f"Sold: {unitsSold}") #displays the units sold
            print(f"Stock: {newStock}\n") #displays the new stock
            stock = newStock + self._approxMonthlyUnits #updates the stock for next month by adding the monthly units
            
            salesOfYear += unitsSold #adds the units sold that month to the total
            manufactAYear += self._approxMonthlyUnits #adds the units manufactured to the total
            
        netProfit = (salesOfYear * self._proSalePrice) - (manufactAYear * self._proManuCost) #forumla that calculates net profit
        print(f"Net Proftis: ${round(netProfit, 2)} CAD") #displays net profit

#test = Product(100,"soccerBall", 250.99, 200.99, 100, 100)

#test.PredictStockStatement()


class Application:
    def InputInt(self):
        while True: #users in the loop until a suitable choice is given
            try:
                question = int(input("TEST INT: ")) #asks question as an int
                return(question) #returns answer if true
            except ValueError: #if the value of the input is not an int display debug message and loop
                print("Not an int")
                continue

    def InputStr(self):
        while True:
            try:
                question = str(input("TEST STR: "))
                return(question)
            except ValueError:
                print("Not an str")
                continue

    def InputFlo(self):
        while True:
            try:
                question = float(input("TEST FLOAT: "))
                return(question)
            except ValueError:
                print("Not an float")
                continue