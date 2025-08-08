print("Python Taxi Meter")
distance = float(input("Enter distance travelled (in km): "))

rate_per_km = 12      
minimum_price = 50     

price = distance * rate_per_km

print("Total price: ₹", price)
