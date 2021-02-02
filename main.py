while True:
    print(input.rotation(Rotation.ROLL))
    if input.rotation(Rotation.ROLL) <45:
        light.set_all(light.rgb(255, 0, 255))
    else:
        light.clear()