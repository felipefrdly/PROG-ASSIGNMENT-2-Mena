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
        self.proManuCost = proManuCost
        self.proStockLevel =  proStockLevel
        self.approxMonthlyUnits = approxMonthlyUnits
        
    def SimulateMonthlyProduction(self):
        pass

    #this method simulates how many of the product are sold each month 
    def SimulateProductionSales(self):
        unitsSold = random.randint(self.approxMonthlyUnits -10 , self.approxMonthlyUnits + 10) #estimates the units sold by generating a number between 1 and the units manufactured +/- 10
        return unitsSold

    def PredictStockStatement(self, totalunitsSold):
        monthlyStock = self.approxMonthlyUnits - totalunitsSold
        return monthlyStock

test = Product(1,1,1,1,1,100)

print(test.SimulateProductionSales())
test.PredictStockStatement(test.SimulateProductionSales())
