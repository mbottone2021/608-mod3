
:
taxPercent = 7.5
purchase = 100
tipPercent = 20
​
class Purchase():
    def calculateCost(purchase, taxPercent, tipPercent):
        taxAmount = purchase * (taxPercent/100)
        tipAmount = purchase * (tipPercent/100)
        totalCost = purchase + taxAmount + tipAmount
        
        print('Purchase: ' + '${:,.2f}'.format(purchase))
        print('Tax: ' + '${:,.2f}'.format(taxAmount))
        print('Tip: ' + '${:,.2f}'.format(tipAmount))
        print('\nTotal Cost: ' + '${:,.2f}'.format(totalCost))
        
Purchase.calculateCost(purchase, taxPercent, tipPercent)
Purchase: $100.00
Tax: $7.50
Tip: $20.00

Total Cost: $127.50
