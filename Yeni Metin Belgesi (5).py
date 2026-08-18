from time import sleep

class coffee_machine:
  def __init__(self, machine_name, coffee_amount, water_amount, coffee_usage, water_usage):
    self.coffee_amount = coffee_amount
    self.water_amount = water_amount
    self.coffee_usage = coffee_usage
    self.water_usage = water_usage
    self.machine_name = machine_name
  def make_coffee(self, how_many_cups):
    sum_coffee_need = how_many_cups * self.coffee_usage
    sum_water_need = how_many_cups * self.water_usage
    if sum_coffee_need <= self.coffee_amount:
      if sum_water_need <= self.water_amount:
        seconds = 10
        for i in range(9):
          print(f"Coffee will be ready after {seconds} minutes.")
          sleep(0.8)
          seconds -= 1
        print(f"Coffee will be ready after {seconds} minute.")
        sleep(1.1)
        seconds = 10
        print("Your coffee is ready, bon appetit!\n")
        self.coffee_amount -= sum_coffee_need
        self.water_amount -= sum_water_need
      else:
        needed_water = sum_water_need - self.water_amount
        print(f"There is not enough water, add at least {needed_water}ml of water")
        print("You are being redirected to menu...")
        sleep(1)
    else:
      needed_coffee = sum_coffee_need - self.coffee_amount
      print(f"There is not enough coffee, add at least {needed_coffee}g of coffee")
      print("You are being redirected to menu...")
      sleep(1)

  def add_ingredients(self, adding_coffee, adding_water):
    self.coffee_amount += adding_coffee
    self.water_amount += adding_water

  def available_cups(self):
    max_with_cof = self.coffee_amount // self.coffee_usage
    max_with_wat = self.water_amount // self.water_usage
    return min(max_with_cof, max_with_wat)


machine1 = coffee_machine("machine1", 500, 1000, 8.5, 200)
machine_list = [machine1]
#available_cupss = machine1.available_cups()
#print(available_cupss)

number_of_machines = len(machine_list)

def add_machine():
  global new_machine
  global machine_list
  global number_of_machines
  global current_machine
  lever_per_cup = True
  new_name = input("Enter a name for your new coffee machine: ")
  while lever_per_cup == True:
    try:  
      cof_per_cup = int(input("Enter how many g of coffee the machine uses per cup: "))
      wat_per_cup = int(input("Enter how many ml of water the machine uses per cup: "))
      lever_per_cup = False
    except:
      print("Something went wrong. Please enter an integer.\n")
  new_machine = coffee_machine(new_name, 0, 0, cof_per_cup, wat_per_cup)
  machine_list.append(new_machine)
  number_of_machines = len(machine_list)
  print(f"[{new_name}] has been added to the machine list.")
  if number_of_machines == 1:
    current_machine = new_machine

lever_general = True
lever_choose = True
lever_adding_what = True
lever_adding_ing = True
while lever_general == True:
  while lever_choose == True:
    number_of_machines = len(machine_list)
    print("Machine List:")
    for i in range(1, number_of_machines+1):
      print(f"{i} - {machine_list[i-1].machine_name}")
    try:
      current_machine = input("To continue, select one of the machines you have: ")
      for l in machine_list:
        if current_machine == str(l.machine_name):
          current_machine = l
          lever_choose = False
      if lever_choose == False:
        continue    
      if current_machine.isnumeric() == True:
        if int(current_machine) <= number_of_machines:
          current_machine = machine_list[int(current_machine)-1]
          lever_choose = False
      else:
        raise TypeError
    except: 
      print("Something went wrong. Please enter the number or the name of one of the machines you have.\n")
  try:
    operation = int(input(f"You are in the menu of [{current_machine.machine_name}]. What do you want to do?\nPress 1 to make coffee\nPress 2 to add ingredients\nPress 3 to add a new machine into the program\nPress 4 to remove one of the machines in the program\nPress 5 to see the list of machines saved\nPress 6 to go back to the machine selection interface\nPress 0 for leaving the menu\n"))
  except:
    print("\nSomething went wrong. Try again. Be sure that you've entered one of these numbers: 1, 2 and 0.")
    continue
  if operation == 0:
    lever_general = False
  elif operation == 1:
    print(f"Remaining ingredients:\n{current_machine.coffee_amount}g of Coffee\n{current_machine.water_amount}g of Water.\n{current_machine.coffee_usage}g of coffee and {current_machine.water_usage} ml of water are used per cup")
    cup_count = int(input("\nHow many cups of coffee do you want? "))
    current_machine.make_coffee(cup_count)
  elif operation == 2:
    lever_adding_what = True
    lever_adding_ing = True
    while lever_adding_what == True:
      adding = input("What do you want to add?\nPress [a] for adding water\nPress [b] for adding coffee\n")
      adding = adding.lower()
      while lever_adding_ing == True:
        if adding == "a":
          try:
            added_water = int(input("How many ml of water do you want to add into the machine? "))
          except:
            print("\nSomething went wrong. Please enter a number.")
            continue
          current_machine.add_ingredients(0, added_water)
          print(f"{added_water} ml of water have been added into the machine.")
          lever_adding_ing = False
          lever_adding_what = False
        elif adding == "b":
          try:
            added_coffee = int(input("How many g of coffee do you want to add into the machine? "))
          except:
            print("\nSomething went wrong. Please enter a number.")
            continue
          current_machine.add_ingredients(added_coffee, 0)
          print(f"{added_coffee} g of coffee have been added into the machine.")
          lever_adding_ing = False
          lever_adding_what = False
        else:
          print("\nSomething went wrong. Please enter one of these letters without the brackets: [a] or [b]")
          break
  elif operation == 3:
    add_machine()
    print(machine_list)
  elif operation == 4:
    print("Here is the list of the machines you have:")
    for m in range(1, number_of_machines+1):
      print(f"{m} - {machine_list[m-1].machine_name}")
    rem_mach = input("Enter the name of the machine you want to remove: ")
    try:
      for j in machine_list:
        if rem_mach == str(j.machine_name):
          rem_mach = j
      machine_list.remove(rem_mach)
      print(f"Machine called [{rem_mach.machine_name}] had been removed from your list.")
      number_of_machines = len(machine_list)
      if number_of_machines == 0:
        print("You have to add at least 1 machine for using the program. You are redirecting to menu of machine adding...")
        sleep(1)
        add_machine()
    except:
      print("Something went wrong. Please enter the name of one of the machines you have. You are redirecting to menu...")
  elif operation == 5:
    print("Here is the list of the machines you have:")
    
    for k in range(1, number_of_machines+1):
      print(f"{k} - {machine_list[k-1].machine_name}")
  elif operation == 6:
    lever_choose = True
    
print("You're exiting...")
sleep(1)
print("Good bye.")