#Felipe Mena
#10/21/2023
#This program handles runs all objects made in the productLibrary.py file and is where the user can interact with the program

from productLibrary import Product
from productLibrary import Application

#test = Product(100,"soccerBall", 250.99, 200.99, 100, 100)

def main():
    print("Welcome to the Product Inventory")
    userInput = Application()
    code = userInput.InputInt("Product Code")
    name = userInput.InputStr("Product Name")
    salePrice = userInput.InputFlo("Product Sale Price")
    manuCost = userInput.InputFlo("Product Manufacture Cost")
    stock = userInput.InputInt("Current Stock")
    estiMontPro = userInput.InputInt("Estimated Monthy Production")

    print("\n_______Product Inventory Stock Statement_______\n")
    print("Product Code:", code)
    print("Product Name:", name,"\n")
    print("Sale Price:", salePrice, "CAD")
    print("Manufacture Cost:", manuCost, "CAD")
    print("Monthly Production:", estiMontPro, "units (Approx.)\n")

    productInst = Product(code, name, salePrice, manuCost, stock, estiMontPro)
    productInst.PredictStockStatement()

main()