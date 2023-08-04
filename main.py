def mph_to_kmph(mph):
   kmph = mph * 1.60934
   return kmph
while True:
   try:
       miles = float(input("Enter miles: "))
       break
   except ValueError:
       print("Invalid input! Please try again...")
kilometers = mph_to_kmph(miles)
print("Total Miles: ", miles)
print("Total Kilometers: ", kilometers)
