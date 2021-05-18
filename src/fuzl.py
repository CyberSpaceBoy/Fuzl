from colorama import Fore, Back, Style 
import os
import math 
import complexio
from replit import audio
from getch import getch
from time import sleep
blocks = []
def clr():os.system('clear')
def play_sound(file):
  audio.play_file(file) 
def add_block(raw,color=Fore.RESET,background=Back.RESET,style=Style.NORMAL):
  block = color + background + style + raw + Fore.RESET + Back.RESET + Style.NORMAL 
  blocks.append(block)
  return block
def art(raw,color=Fore.RESET,background=Back.RESET,style=Style.NORMAL):
  block = color + background + style + raw + Fore.RESET + Back.RESET + Style.NORMAL 
  return block
def getdir():
   first_char = getch();os.system('clear')
   if first_char == '\x1b':
        return {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left'}[getch() + getch()]
   else:
        return first_char
def getkey():
  put = getch().lower()
  os.system('clear')
  return put
class collision:
  def  x(x,x2):
    if round(x) == round(x2):
      return True, 
    else:
      return False 
  def y(y,y2):
    if round(y)==round(y2):
      return True 
    else: 
      return False
def move(x,toX,block):
  magnitude = complexio.gravity.fall_stats(math.floor(x),0,math.floor(toX),0)
  return ' ' * magnitude + block 
def glide(x,toX,block):
  magnitude = int(complexio.gravity.fall_stats(math.floor(x),0,math.floor(toX),0)['X Magnitude'])
  cutscene = []
  for x in range(1,magnitude+1):

     cutscene.append(' ' + block)

  return cutscene
space = " "
newline = "\n"
def calc_x(block):
  mag = 0
  for space in block:
    mag += 1 
  return mag 
def calc_y(block):
  mag = 0
  for newline in block:
    mag += 1 
  return mag 
def fall(block,tm,fall):
 while fall > 0:
   block = "\n"+block+"\033[A"
   print(block)
   sleep(tm)
   fall-=1
   clr() 
plr = "X"
x = 0
y = 0  
#(C)Vertock Softwares Company 2  
# 2021, Version 1.0.0.5
