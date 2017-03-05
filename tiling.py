#!/usr/bin/python

import time
start = time.time()

import os, sys
   
def setWindow(posX, posY, sizeX, sizeY):
    values = {        
        'gravity': 0,
        'posX': int(posX),
        'posY': int(posY),
        'sizeX': int(sizeX),
        'sizeY': int(sizeY)
    }
    #os.system('wmctrl -r :ACTIVE: -e {},{},{},{},{}'.format(0, posX, posY, sizeX, sizeY))
    cmd = 'wmctrl -r :ACTIVE: -e {gravity},{posX},{posY},{sizeX},{sizeY}'.format(**values)
    print cmd
    os.system(cmd)

# ~100ms
#import wx
#app = wx.PySimpleApp()
#resX, resY = wx.DisplaySize()

# ~80ms
#import gtk
#window = gtk.Window()
#screen = window.get_screen()
#resX = screen.get_width()
#resY = screen.get_height()

# ~50ms
#from PyQt4 import QtGui
#app = QtGui.QApplication([])
#resX = app.desktop().screenGeometry().width()
#resY = app.desktop().screenGeometry().height()

# ~25ms
#import subprocess
#res = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
#resX, resY = res.split('x')
#resX = int(resX)
#resY = int(resY)

# ~25ms
res = os.popen("xrandr | grep \* | cut -d' ' -f4").read()
print res
resX, resY = res.split('\n')[0].split('x')
resX = int(resX)
resY = int(resY)

windowHeadHeight = 24
tasklistHeight = 22

# nach goldenem schnitt:
#big = 0.618
#small = 0.382
big = 0.5
small = 0.5
        

def unmaximize():
  cmd = 'wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz'
  os.system(cmd)

unmaximize()

if sys.argv[1] == 'upper_left':
    x = 0
    y = 0
    width = resX * small
    height = resY * big - windowHeadHeight - tasklistHeight
    setWindow(x, y, width, height)
    
elif sys.argv[1] == 'lower_left':
    x = 0
    y = resY * big - 1
    width = resX * small
    height = resY * small - windowHeadHeight - tasklistHeight
    setWindow(x, y, width, height)
    
elif sys.argv[1] == 'upper_right':
    x = resX * small
    y = 0
    width = resX * big + 1
    height = resY * big - windowHeadHeight - tasklistHeight
    setWindow(x, y, width, height)
    
elif sys.argv[1] == 'lower_right':
    x = resX * small
    y = resY * big - 1
    width = resX * big
    height = resY * small - windowHeadHeight - tasklistHeight
    setWindow(x, y, width, height)

elif sys.argv[1] == 'bottom':
    x = 0
    y = resY * big - 1
    width = resX
    height = resY * small - windowHeadHeight - tasklistHeight
    setWindow(x, y, width, height)    
    
elif sys.argv[1] == 'top':
    x = 0
    y = 0
    width = resX
    height = resY * big - windowHeadHeight - tasklistHeight
    setWindow(x, y, width, height)

elif sys.argv[1] == 'left':
    x = 0
    y = windowHeadHeight
    width = resX * small
    height = resY - windowHeadHeight - tasklistHeight
    setWindow(x, y, width, height)    

elif sys.argv[1] == 'right':
    x = resX * small
    y = windowHeadHeight
    width = resX * big
    height = resY - windowHeadHeight - tasklistHeight
    setWindow(x, y, width, height)

elif sys.argv[1] == 'full':
    x = 0
    y = 0
    width = resX
    height = resY - windowHeadHeight - tasklistHeight
    setWindow(x, y, width, height)
    
print time.time() - start
