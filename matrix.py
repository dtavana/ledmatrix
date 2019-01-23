import time
import sys
import datetime
import RPi.GPIO as GPIO


#Defines
r0 = 18
r1 = 23
r2 = 24
r3 = 25
r4 = 12
r5 = 16
r6 = 20
r7 = 21

c0 = 26
c1 = 19
c2 = 13
c3 = 6
c4 = 5
c5 = 22
c6 = 27
c7 = 17

rows = [r0, r1, r2, r3, r4, r5, r6, r7]
columns = [c0, c1, c2, c3, c4, c5, c6, c7]

def main():
  try:
    GPIO.setmode(GPIO.BCM)
    setup()
    #lightAll()
    print("----Starting Print")
    #text = sys.argv[1]
    text = "a"
    time.sleep(1)
    #All columns that need to be on for a given row
    for letter in text:
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=2)
        while(True):
          if datetime.datetime.now() >= endTime:
            break
          currentOn = nameToFunc[letter]
          #currentOn = {r0: [c0, c2, c4, c6]}
          for row in rows:
            GPIO.output(row, False)
            for column in columns:
              if row in currentOn and column in currentOn[row]:
                GPIO.output(column, True)
                time.sleep(.005)
                GPIO.output(column, False)
            GPIO.output(row, True)
    print("----Print Finished")
  except Exception as e:
    print("error")
    print(e)
  finally:
    GPIO.cleanup()

def setup():
  for row in rows:
    GPIO.setup(row, GPIO.OUT)
    GPIO.output(row, True)
  for column in columns:
    GPIO.setup(column, GPIO.OUT)
    GPIO.output(column, False)

def lightAll():
  print("----Starting Test")
  for row in rows:
    GPIO.output(row, False)
    for column in columns:
      GPIO.output(column, True)
      time.sleep(.25)
      GPIO.output(column, False)
    GPIO.output(row, True)
  print("----Test Finished")

#Letter Functions
def a():
  return{r0: [c3], r1: [c4], r2: [c5], r3: [c6], r4: [c7]}
  

nameToFunc = {'a': a()}

if __name__ == "__main__":
  main()
