num = 0
basic.show_icon(IconNames.HEART)

def on_forever():
    global num
    if num > 9:
        num = 0
    basic.show_number(num)
    basic.pause(1000)
    num = num + 1
basic.forever(on_forever)
