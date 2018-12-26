# Sal's shipping project

def get_best_ship_rate(ground_cost, drone_cost, premium_ground_cost):
  if (ground_cost < drone_cost) and (ground_cost < premium_ground_cost):
      return 'The best shipping rate is regular ground at ' + str(ground_cost)
  elif (drone_cost < ground_cost) and (drone_cost < premium_ground_cost):
      return 'The best shipping rate is by drone at ' + str(drone_cost)
  elif (premium_ground_cost < ground_cost) and (premium_ground_cost < drone_cost):
      return 'The best shipping rate is by Premium Ground at ' + str(premium_ground_cost)
  else:
      return 'There is a tie in shipping rates.  Choose your preferred method.  Rates:\nGround cost - ' + str(ground_cost) + '\nDrone cost - ' + str(drone_cost) + '\nPremium ground cost - ' + str(premium_ground_cost)

    
ground_flat_rate = 20.0
premium_ground_cost = 125.0

weight = float(input('Enter package weight - '))

if weight <= 2:
    ground_cost = round((weight * 1.5) + ground_flat_rate, 2)
    drone_cost = round(weight * 4.5, 2)
elif weight > 2 and weight <= 6:
    ground_cost = round((weight * 3) + ground_flat_rate, 2)
    drone_cost = weight * 9
elif weight > 6 and weight <= 10:
    ground_cost = round((weight * 4) + ground_flat_rate, 2)
    drone_cost = round(weight * 12, 2)
else:
    ground_cost = round((weight * 4.75) + ground_flat_rate, 2)
    drone_cost = round(weight * 14.25, 2)

print(get_best_ship_rate(ground_cost, drone_cost, premium_ground_cost))



    

               
