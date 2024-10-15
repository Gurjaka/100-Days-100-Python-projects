import playsound, time

wait = input('Time in seconds: ')
while True:
  try:
    wait = int(wait)
    break
  except ValueError:
    print('Invalid input! Must be integer!')
  
for i in range(0,wait):
  print(i)
  time.sleep(1)

playsound("alarm.mp3")