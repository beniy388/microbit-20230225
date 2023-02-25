let num = 0
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    if (num > 9) {
        num = 0
    }
    basic.showNumber(num)
    basic.pause(1000)
    num = num + 1
})
