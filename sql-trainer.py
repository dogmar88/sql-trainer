import PySimpleGUI as sg
from random import shuffle
import time
import shutil
x = [[i] for i in range(1,350)]
shuffle(x)
print(x)
n=0
layout = [[sg.Text('Persistent window')], [sg.Image('base\\'+str(x[n][0])+'.png')], [sg.Input()], [sg.Button('Read'), sg.Exit()]]
otvety={1: 'A', 2: 'A', 3: 'C', 4: 'BD', 5: 'A', 6: 'ABD', 7: 'B', 8: 'A', 9: 'B', 10: 'BE', 11: 'C', 12: 'A', 13: 'B', 14: 'C', 15: 'C', 16: 'C', 17: 'D', 18: 'BD', 19: 'AC', 20: 'C', 21: 'B', 22: 'D', 23: 'D', 24: 'CDE', 25: 'D', 26: 'D', 27: 'D', 28: 'D', 29: 'D', 30: 'B', 31: 'B', 32: 'D', 33: 'D', 34: 'AB', 35: 'CD', 36: 'B', 37: 'D', 38: 'D', 39: 'AC', 40: 'C', 41: 'C', 42: 'A', 43: 'C', 44: 'B', 45: 'AE', 46: 'B', 47: 'CD', 48: 'AD', 49: 'B', 50: 'A', 51: 'B', 52: 'C', 53: 'C', 54: 'AC', 55: 'BD', 56: 'B', 57: 'D', 58: 'B', 59: 'D', 60: 'D', 61: 'A', 62: 'C', 63: 'C', 64: 'C', 65: 'B', 66: 'B', 67: 'A', 68: 'A', 69: 'D', 70: 'ACD', 71: 'CDF', 72: 'C', 73: 'ACE', 74: 'ABE', 75: 'BDE', 76: 'ABE', 77: 'ACD', 78: 'ABC', 79: 'AC', 80: 'ABE', 81: 'BDE', 82: 'ABC', 83: 'BE', 84: 'AD', 85: 'CDE', 86: 'BE', 87: 'BD', 88: 'BD', 89: 'AD', 90: 'AD', 91: 'AC', 92: 'DE', 93: 'AB', 94: 'AC', 95: 'CF', 96: 'D', 97: 'ABD', 98: 'BCF', 99: 'D', 100: 'A', 101: 'A', 102: 'C', 103: 'AE', 104: 'AB', 105: 'D', 106: 'BD', 107: 'D', 108: 'CE', 109: 'AE', 110: 'BCE', 111: 'CD', 112: 'AB', 113: 'BEF', 114: 'D', 115: 'BDE', 116: 'BD', 117: 'BCF', 118: 'BDF', 119: 'ADF', 120: 'B', 121: 'B', 122: 'ABD', 123: 'AE', 124: 'CFG', 125: 'C', 126: 'AB', 127: 'D', 128: 'AB', 129: 'AB', 130: 'A', 131: 'CF', 132: 'AC', 133: 'DE', 134: 'BC', 135: 'ADE', 136: 'BD', 137: 'BD', 138: 'CD', 139: 'EF', 140: 'AD', 141: 'DEF', 142: 'ACD', 143: 'AF', 144: 'CE', 145: 'AC', 146: 'ABF', 147: 'ABC', 148: 'BC', 149: 'AD', 150: 'AEFG', 151: 'BCE', 152: 'AB', 153: 'AF', 154: 'DEF', 155: 'D', 156: 'AC', 157: 'ACE', 158: 'B', 159: 'B', 160: 'CD', 161: 'B', 162: 'BCE', 163: 'AD', 164: 'BDG', 165: 'BE', 166: 'CDE', 167: 'ACF', 168: 'DE', 169: 'ABC', 170: 'A', 171: 'AC', 172: 'B', 173: 'AE', 174: 'AB', 175: 'AC', 176: 'CF', 177: 'ACFHJ', 178: 'C', 179: 'CDF', 180: 'AD', 181: 'ABE', 182: 'C', 183: 'B', 184: 'CD', 185: 'CDG', 186: 'AF', 187: 'ABD', 188: 'B', 189: 'BE', 190: 'ABC', 191: 'AB', 192: 'D', 193: 'D', 194: 'A', 195: 'CD', 196: 'AE', 197: 'AE', 198: 'BDE', 199: 'BCD', 200: 'ABD', 201: 'ACF', 202: 'CE', 203: 'DE', 204: 'ACD', 205: 'B', 206: 'BDE', 207: 'AB', 208: 'AC', 209: 'ADE', 210: 'B', 211: 'A', 212: 'D', 213: 'C', 214: 'D', 215: 'BC', 216: 'CE', 217: 'AC', 218: 'D', 219: 'ACE', 220: 'C', 221: 'CE', 222: 'DE', 223: 'C', 224: 'B', 225: 'AC', 226: 'ADF', 227: 'AE', 228: 'B', 229: 'A', 230: 'BD', 231: 'B', 232: 'CDE', 233: 'A', 234: 'CE', 235: 'B', 236: 'AB', 237: 'B', 238: 'A', 239: 'CD', 240: 'B', 241: 'D', 242: 'D', 243: 'AEF', 244: 'A', 245: 'D', 246: 'BE', 247: 'AD', 248: 'D', 249: 'C', 250: 'C', 251: 'A', 252: 'A', 253: 'BD', 254: 'C', 255: 'C', 256: 'DEH', 257: 'BCD', 258: 'B', 259: 'AC', 260: 'D', 261: 'C', 262: 'C', 263: 'CD', 264: 'D', 265: 'C', 266: 'A', 267: 'AD', 268: 'AD', 269: 'AB', 270: 'BD', 271: 'BE', 272: 'AB', 273: 'A', 274: 'D', 275: 'C', 276: 'D', 277: 'C', 278: 'C', 279: 'E', 280: 'B', 281: 'E', 282: 'D', 283: 'A', 284: 'C', 285: 'B', 286: 'D', 287: 'C', 288: 'A', 289: 'D', 290: 'B', 291: 'C', 292: 'A', 293: 'A', 294: 'AC', 295: 'AC', 296: 'AC', 297: 'AB', 298: 'AB', 299: 'AB', 300: 'AF', 301: 'AC', 302: 'AE', 303: 'BD', 304: 'AD', 305: 'A', 306: 'AE', 307: 'A', 308: 'D', 309: 'C', 310: 'D', 311: 'C', 312: 'A', 313: 'C', 314: 'D', 315: 'C', 316: 'ABE', 317: 'C', 318: 'ADE', 319: 'BCD', 320: 'CD', 321: 'BD', 322: 'AB', 323: 'BC', 324: 'CD', 325: 'BDE', 326: 'AC', 327: 'A', 328: 'DE', 329: 'CE', 330: 'AB', 331: 'A', 332: 'AC', 333: 'BCF', 334: 'BDF', 335: 'CEF', 336: 'AE', 337: 'CDF', 338: 'ACF', 339: 'BE', 340: 'A', 341: 'AD', 342: 'AE', 343: 'B', 344: 'CDF', 345: 'ACF', 346: 'BDE', 347: 'AE', 348: 'AC', 349: 'E'}

def sverka(x,y):
    print(otvety[x])
    if y==otvety[x]:
        print ('excellent')
        return 1
    else:
        shutil.copyfile("base\\"+str(x)+".png", "mistakes\\"+str(x)+" - correct was "+str(otvety[x])+".png")
        print ('no, it is a '+otvety[x])
    return 0
    
    
ball=0
layout = [[sg.Text('You have 100 questions and 150 minutes.\n Real exam has 78 questions and 120 minutes.\nSome questions suppose several answers like ABC, you should order it by alphabet, CBA will be treated as a mistake.\nYou should get 67% to pass the exam, I would recommend to get the 85%, because dump is not full,\ngood luck)')], [sg.Button('Go')]]
window = sg.Window('Trainer', layout)
while True:
    event, values = window.read()
    if event in ('Go'):
        break

window.close()
layout = [[sg.Text(' ')], [sg.Button('Ok')]]

current_time = 0
paused = False
start_time = int(round(time.time() * 100))
verno=''

while True:
    window.close()
    layout = [[sg.Text(str(verno))],
         [sg.Text(size=(15, 2), key='text')],[sg.Text('Question ' +str(n+1)+' out of 100')], [sg.Image('base\\'+str(x[n][0])+'.png')], [sg.Input()], [sg.Button('Read')]]
    print(str(x[n][0])+'.png')
    window = sg.Window('Trainer', layout)
    event, values = window.read(timeout=10)
    current_time = int(round(time.time() * 100)) - start_time
    window['text'].update('min/sec: {:02d}:{:02d}'.format((current_time // 100) // 60, (current_time // 100) % 60))
    event, values = window.read(timeout = 90000)
    print (values[1].upper())
    ball=ball+sverka(x[n][0],values[1].upper())
    if sverka(x[n][0],values[1].upper())==1: verno='Correct!'
    else: verno='Mistake!'
    print (str(ball)+' - score')
    n=n+1
    if n>=len(x) or n>100:
        window.close()
        layout = [  [sg.Text('Result is '+str(ball)+' out of '+str(n-1))]]
        window = sg.Window('Window Title', layout)
        while True:
            event, values = window.read(timeout = 90000)
            if event in (sg.WIN_CLOSED):
                window.close()
    if event in (sg.TIMEOUT_KEY):
        sverka(x[n][0],' ')
        continue
    window.close()


    
