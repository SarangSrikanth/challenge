def on_button_pressed_a():
    global counterVar
    counterVar += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global counterVar
    counterVar = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global counterVar
    counterVar += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

counterVar = 0
counterVar = 0

def on_forever():
    basic.show_number(counterVar)
basic.forever(on_forever)
