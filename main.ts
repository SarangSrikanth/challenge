input.onButtonPressed(Button.A, function () {
    counterVar += 1
})
input.onButtonPressed(Button.AB, function () {
    counterVar = 0
})
input.onButtonPressed(Button.B, function () {
    counterVar += -1
})
let counterVar = 0
counterVar = 0
basic.forever(function () {
    basic.showNumber(counterVar,50)
})
