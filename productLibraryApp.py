#Felipe Mena
#10/21/2023
#This program handles runs all objects made in the productLibrary.py file and is where the user can interact with the program

from productLibrary import Product
from productLibrary import Application

def main():
    print("Welcome to the Product Inventory")
    userInput = Application()
    code = userInput.InputInt()
    name = userInput.InputStr()
    salePrice = userInput.InputFlo()
    manuCost = userInput.InputFlo()
    stock = userInput.InputInt()
    estiMontPro = userInput.InputInt()

    productInst = Product(code, name, salePrice, manuCost, stock, estiMontPro)
    productInst.PredictStockStatement()

main()