from os import system
from random import randint

THRESHOLD = 3
MAX_COMMITS = 3

def commit():
  system("echo $(date) >> output.txt")
  system("git add output.txt")
  system("git commit -m Update output.txt")
  system("git push")

if (randint(0, 10) > THRESHOLD):
  for i in range(randint(0, MAX_COMMITS)):
    commit()