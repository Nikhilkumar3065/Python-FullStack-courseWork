units = int(input("Enter the units: "))
bill=0

if 0<units<=100:
    bill = units*3

elif 100<units<=200:
    bill = 300 + (units - 100)*5

elif 200<units<=300:
    bill = 300 + 500 + (units - 200)*7

elif units>300:
    bill = 300 + 500 + 700 + (units -300)*10

    
gst= bill+bill*0.05

if gst > 5000:
    print(f"Final Bill(included gst): {gst-500}")
else:
    print(f"Final Bill(included gst): {gst}")
