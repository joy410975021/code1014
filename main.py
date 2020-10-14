def on_forever():
    for Y in range(5):
        for X in range(5):
            led.plot(X, Y)
            basic.pause(100)
    basic.clear_screen()
    for X2 in range(5):
        for Y2 in range(5):
            led.plot(X2, Y2)
            basic.pause(100)
    basic.clear_screen()
basic.forever(on_forever)
