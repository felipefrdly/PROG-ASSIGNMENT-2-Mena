#Felipe Mena
#10/21/2023
#This program is designed to calculate and simulate sales metrics of diffrent products that a user creates. this file contains all objects that the program revolves around

class Product:
    #initalizes all variables on objects creation
    def __init__(self, proCode, proName, proSalePrice, proManuCost, proStockLevel, approxMonthlyUnits):
        self._proCode = proCode
        self._proName = proName
        self._proSalePrice = proSalePrice
        self.proManuCost = proManuCost
        self.proStockLevel =  proStockLevel
        self.approxMonthlyUnits = approxMonthlyUnits
        
    def SimulateMonthlyProduction():
        pass

    def SimulateProductionSales():
        pass

    def PredictStockStatement():
        pass