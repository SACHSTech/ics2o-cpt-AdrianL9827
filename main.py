import random
import math

# Fahrenheit to Celsius Converter
def f_to_c_cal():
  print("\n\t***Fahrenheit to Celsius Converter***\n")

  # Get Degrees
  fahrenheit = float(input("Enter the degree in fahrenheit: "))

  # Calculation and Result
  celsius = (fahrenheit - 32) * (5/9)
  print("\nThe degree in celsius is: " + str(celsius))

# Celsius to Fahrenheit Converter
def c_to_f_cal():
  print("\n\t***Celsius to Fahrenheit Converter***\n")

  # Get Degrees 
  celsius = float(input("Enter the degree in Celsius: ") )

  # Calculation and Result
  fahrenheit = (celsius * 9 / 5) + 32
  print("\nThe degree in Fahrenheit is: " + str(fahrenheit))

# Object Distributor
def object_distributer():
  print("\n\t***Object Distributor***\n")

  # Get Objects and Receiver
  obj_dis = str(input("Enter the object ot be distributed: "))
  obj_amt = int(input("Enter the amount of " + obj_dis + "to be distributed"))
  dis_amt = int(input("Enter the number of receivers: " ))

  # Calculation and Result
  obj_receive = obj_amt//dis_amt  
  obj_remain = obj_amt%dis_amt
  print("\nEvery receiver will receive " + str(obj_receive) + "and " + str(obj_remain) + " remaning")

# Hours to Days Convertor
def hours_to_days_conv():
  print("\n\t***Hours to Days Convertor***\n")
  
  # Get Hours
  hours = int(input("Enter the number of hours: "))
 
  # Calculation and Result
  days = hours//24
  remaining_hours = hours%24
  print("\n" + str(hours) + " hours = " + str(days) + " days and " + str(remaining_hours)+" hours.")

# Mins to Days Convertor 
def mins_to_days_conv():
  print("\n\t***Minutes to Days Convertor***\n")

  # Get Mins
  minutes = int(input("Enter the number of minutes: "))

  # Calculation and Result
  days2 = minutes//1440
  remaining_minutes = minutes%1440
  hours2 = remaining_minutes//60
  final_minutes = remaining_minutes - hours2*60
  print("\n" + str(minutes) + " minutes is " + str(days2) + " day(s) " + str(hours2)+" hour(s) and " + str(final_minutes) + " minute(s).")

def number_guesser():
  print("\n\t***Number Guesser***\n")

  # Get Lower and Upper Bounds
  number_min = int(input("Enter lower bound: "))
  number_max = int(input("Enter upper bound: "))

  # Get Random Number
  random_number = random.randint(number_min, number_max)

  # Get Guess Limit
  count = 0
  print("\n\tYou've only ", round(math.log(number_max - number_min + 1, 2))," chances to guess the integer!\n")

  # Main Loop within Guess Limit
  while count < math.log(number_max - number_min + 1, 2):
    count += 1
     
    guess = int(input("Guess a number:- ")) 
     
    # Guessed the Answer
    if random_number == guess:  
       print("Congratulations you did it in ", count, " try")
       break

    # Number too low
    elif random_number > guess:
       print("You guessed too small!")

    # Number too high
    elif random_number < guess:
       print("You Guessed too high!")

  # Main Loop out of Guess Limit
  while not count < math.log(number_max - number_min + 1, 2):
    print("You've used all the chances")
    break

def median_cal():
  count_total = 0
  done = False
  times = 0

  print("\n\t***Median Calculator***\n")
  while not done:
    count = float(input("Enter the number ('-0.1' to stop): "))

    if count == -0.1:
      done = True
    else:
      count_total = count_total + count
      times = times + 1

  median = count_total/times

  print("The median is " + str(median))

def computer_quiz():
  quiz1_score = 0
  print("\nQuestion 1. The storage and organization of files and tasks on a computer is managed by: ")
  print("A. a media player")
  print("B. a computer savy user")
  print("C. the operating system")
  quiz1_q1_ans = str(input("Pick your answer: "))
  
  if quiz1_q1_ans == "C" or quiz1_q1_ans == "c":
    print("\nYou are CORRECT!")
    quiz1_score = quiz1_score + 1
  else:
    print("\nYou are WRONG!")
    quiz1_score = quiz1_score + 0

  print("\nQuestion 2. Available in hardware or software form, this component of a network protects your network from malicious users: ")
  print("A. extender")
  print("B. router")
  print("C. firewall")
  quiz1_q2_ans = str(input("Pick your answer: "))
  
  if quiz1_q2_ans == "C" or quiz1_q2_ans == "c":
    print("\nYou are CORRECT!")
    quiz1_score = quiz1_score + 1
  else:
    print("\nYou are WRONG!")
    quiz1_score = quiz1_score + 0  

  print("\nQuestion 3. This component connects all other components on a computer together: ")
  print("A. hard drive")
  print("B. motherboard")
  print("C. modem")
  quiz1_q3_ans = str(input("Pick your answer: "))
  
  if quiz1_q3_ans == "B" or quiz1_q3_ans == "b":
    print("\nYou are CORRECT!")
    quiz1_score = quiz1_score + 1
  else:
    print("\nYou are WRONG!")
    quiz1_score = quiz1_score + 0  

  print("\nQuestion 4. This type of memory is the slowest in the memory hierarchy: ")
  print("A. storage")
  print("B. external memory")
  print("C. internal memory")
  quiz1_q3_ans = str(input("Pick your answer: "))
  
  if quiz1_q3_ans == "A" or quiz1_q3_ans == "a":
    print("\nYou are CORRECT!")
    quiz1_score = quiz1_score + 1
  else:
    print("\nYou are WRONG!")
    quiz1_score = quiz1_score + 0  

  print("\nQuestion 5. The smallest unit of measurement for storing digital information is: ")
  print("A. byte")
  print("B. bit")
  print("C. hertz")
  quiz1_q3_ans = str(input("Pick your answer: "))
  
  if quiz1_q3_ans == "B" or quiz1_q3_ans == "b":
    print("\nYou are CORRECT!")
    quiz1_score = quiz1_score + 1
  else:
    print("\nYou are WRONG!")
    quiz1_score = quiz1_score + 0  

  print("\nQuestion 6. This type of modem converts data to be transferred via telephone lines: ")
  print("A. DSL")
  print("B. Cable")
  print("C. Cat 5")
  quiz1_q3_ans = str(input("Pick your answer: "))
  
  if quiz1_q3_ans == "A" or quiz1_q3_ans == "a":
    print("\nYou are CORRECT!")
    quiz1_score = quiz1_score + 1
  else:
    print("\nYou are WRONG!")
    quiz1_score = quiz1_score + 0

  print("\nQuestion 7. Whatsapp users started to use this as an alternative as Whatsapp is going to share users' datas to Facebook: ")
  print("A. Twitter")
  print("B. Instagram")
  print("C. Signal")
  quiz1_q3_ans = str(input("Pick your answer: "))
  
  if quiz1_q3_ans == "C" or quiz1_q3_ans == "c":
    print("\nYou are CORRECT!")
    quiz1_score = quiz1_score + 1
  else:
    print("\nYou are WRONG!")
    quiz1_score = quiz1_score + 0

  print("\n\n--You got " + str(quiz1_score) + " out of 7--")

def computer_parts():
  print("\n\t***Computer Parts and Functions***\n")
  com_parts = input("Which computer part you wish to know more? ")

  if com_parts == "Power supply" or com_parts == "power supply":
    print("\nThe power supply is the device that powers all other mechanisms of the PC. It generally plugs into the motherboard. It can connect to either a plug for an outlet (desktop) or an internal battery (laptop).")
    print("\nfrom https://neconnected.co.uk/eight-basic-pc-parts-and-their-functions/")

  if com_parts == "Motherboard" or com_parts == "motherboard":
    print("\nThe motherboard is a paramount computer component as this is the central part where everything else is connecting to. A motherboard is an affably sized circuit board that allows other elements to interact. It has ports, which are facing outside a PC case so that you can plug in a monitor, charge your computer or plug in a mouse. It also has slots for expansions so that you can install additional accessory ports if you wish to do so. The motherboard stores low-level data like the system time even when a PC is switched off. ")
    print("\nfrom https://neconnected.co.uk/eight-basic-pc-parts-and-their-functions/")

  if com_parts == "Input and Output" or com_parts == "input and output":
    print("\nDepending on your particular PC, a variety of devices can be connected to send data into it or out from it. Commonplace input devices include mice (laptops and touchpads), webcams and ergonomic keyboards while output devices are printers, monitors, and speakers. Removable media like SD cards and flash drives can also be utilized for transferring data between PCs. ")
    print("\nfrom https://neconnected.co.uk/eight-basic-pc-parts-and-their-functions/")

  if com_parts == "CPU" or com_parts == "cpu":
    print("\nThe CPU is the PC’s brain since it works the hardest. A CPU does all the calculations needed for a system and varies in speed. The CPU generates heat, and that’s why a fan is installed inside the PC. More powerful CPU’s are required for intense computer work or work that necessitates programming multifaceted software or editing high-definition video. ")
    print("\nfrom https://neconnected.co.uk/eight-basic-pc-parts-and-their-functions/")

  if com_parts == "RAM" or com_parts == "ram":
    print("\nRAM is short-term memory. When you open Microsoft Word, the computer places it in RAM, and when closing the window, that RAM is released. The more RAM on your PC, the more programs can run at the same time. ")
    print("\nfrom https://neconnected.co.uk/eight-basic-pc-parts-and-their-functions/")

  if com_parts == "Hard Disk Drive" or com_parts == "hard disk drive":
    print("\nSince RAM is short-term, your PC needs a place for storing data permanently. This is what a hard drive is for. It has many spinning platters with an arm that writes data to the disk. Hard disks are slow and are replaced by the quicker solid-state drives or SD cards with  SD card reader, which consist of flash memory (like flash drives or smartphones). Both drives are available in a different size to cater for various needs. ")
    print("\nfrom https://neconnected.co.uk/eight-basic-pc-parts-and-their-functions/")

  if com_parts == "Video Card" or com_parts == "video card":
    print("\nVideo cards handle the output of images to the display. They have their own RAMs for doing performing these functions. Several types of video cards can be bought with different power capabilities and prices. ")
    print("\nfrom https://neconnected.co.uk/eight-basic-pc-parts-and-their-functions/")
  
  if com_parts == "Optical Drives" or com_parts == "optical drives":
    print("\nThey are less regular than they used to be, but several machines still have optical drives for reading DVDs or CDs. They can be used for watching movies or listening to music, copying information on a blank disc, or installing software to the disc. ")
    print("\nfrom https://neconnected.co.uk/eight-basic-pc-parts-and-their-functions/")



  





#introduction 
def intro():
  print("\nChoose the page you want to enter:")
  print("1. Converters and Calculators")
  print("2. Quizzes and Games")
  print("3. Information Kiosk")
  menu_page = int(input("\nEnter the page number: "))

  if not menu_page < 4 and menu_page > 0:
    print("\n\nIt is not a valid number")
    intro()

  if menu_page == 1:
    print("\n1. Fahrenheit to Celsius Converter ")
    print("2. Celsius to Fahrenheit Converter ")
    print("3. Object Distributor ")    
    print("4. Hours to Days Convertor ")
    print("5. Minutes to Days Convertor ")
    print("6. Median Calculator")
    menu_page1 = int(input("\nEnter the page number: "))
    if menu_page1 == 1:
      f_to_c_cal()
      intro()
    elif menu_page1 == 2:
      c_to_f_cal()
      intro()
    elif menu_page1 == 3:
      object_distributer()
      intro()
    elif menu_page1 == 4:
      intro()
    elif menu_page1 == 5:
      mins_to_days_conv()
      intro()
    elif menu_page1 == 6:
      median_cal()
      intro()

  if menu_page == 2:
    print("\n1. Computer Quiz")
    print("2. Number Guesser")
    menu_page2 = int(input("\nEnter the page number: "))
    if menu_page2 == 1:
      computer_quiz()
    elif menu_page2 == 2:
      number_guesser()

  if menu_page == 3:
    print("\n1. Computer Parts")
    menu_page3 = int(input("\nEnter the page number: "))
    if menu_page3 == 1:
      computer_parts()

print("\t\t\t\t-----Welcome to my CPT Page-----")
intro()   