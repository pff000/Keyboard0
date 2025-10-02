print("Starting")

import board
import neopixel
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.col_pins = (board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP3)
keyboard.row_pins = (board.A3, board.GP24, board.GP25, board.GP18, board.GP19, board.GP20, board.GP1, board.GP0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    
    [KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7,
     KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U,
     KC.ESC, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J,
     KC.LEFT_SHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M,
     KC.LEFT_CONTROL, KC.LEFT_ALT, KC.LEFT_SUPER, KC.MO(1), KC.SPACE, KC.SPACE, KC.SPACE, KC.LEFT,
     KC.N8, KC.N9, KC.N0, KC.BACKSPACE, KC.COMMA, KC.DOT, KC.SLASH, KC.RIGHT_SHIFT,
     KC.I, KC.O, KC.P, KC.BACKSLASH, KC.UP, KC.DOWN, KC.RIGHT, KC.QUOTE,
     KC.K, KC.L, KC.SEMICOLON, KC.ENTER, KC.LBRACKET, KC.RBRACKET, KC.KP_MINUS, KC.KP_PLUS],

    [KC.TRNS, KC.F1, KC.F2, KC.F3, KC.F5, KC.F5, KC.F6, KC.F7,
     KC.DEL, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.F8, KC.F9, KC.F10, KC.F11, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS],

]

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

if __name__ == '__main__':
    pixel = neopixel.NeoPixel(board.GP16, 1, brightness=0.1, auto_write=False)
    pixel.fill(PURPLE)
    pixel.show()
    keyboard.go()

