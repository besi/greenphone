import machine
import utime


keys = {
    "32.26": 1,
    "33.26": 2,
    "25.26": 3,
    "32.27": 4,
    "33.27": 5,
    "25.27": 6,
    "32.12": 7,
    "33.12": 8,
    "25.12": 9,
    "33.14": 0,
}

debounce_delay_ms = 200

# WARNING PIN 35 is not usable (probably due to wifi being on)

output_pins = [26, 27, 14, 12]
input_pins = [32, 33, 25]


outputs = []
inputs = []

for x in input_pins:
    inputs.append(machine.Pin(x, machine.Pin.IN, machine.Pin.PULL_DOWN))

for y in output_pins:
    outputs.append(machine.Pin(y, machine.Pin.OUT))

def key_pressed(key):
    print(key)
    utime.sleep_ms(50)

def clear_outputs():
    for o in outputs:
        o.value(0)

while True:
    for output in outputs:

        clear_outputs()
        output.value(1)

        for input in inputs:
            v = input.value()
            if v == 1:
                i = input_pins[inputs.index(input)]
                o = output_pins[outputs.index(output)]
                key = "%i.%i" % (i, o)
                if key in keys:
                    key_pressed(keys[key])
                utime.sleep_ms(debounce_delay_ms)
