#a simple program for guess number game
num = int(input("Enter your lucky number: "))
if (num == 33):
 print("YOU HAVE WON!!")
elif  (num >= 20 and num <= 28):
 print("TOO LOW!!")
elif (num >= 29 and num <= 34):
 print("ALMOST THERE!!")
elif (num >= 35 and num <= 40):
 print("TOO HIGH!!")
else:
 print ("IN THE RANGE OF 20 TO 40")