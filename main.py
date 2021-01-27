while True:
    if input.rotation(Rotation.ROLL) <45:
        light.set_all(light.rgb(255, 0, 255))