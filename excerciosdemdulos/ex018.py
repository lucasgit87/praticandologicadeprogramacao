import math
angulo = int(input('Digite qualquer ângulo: '))
radi = math.radians(angulo)
s = math.sin(radi)
cos = math.cos(radi)
tan = math.tan(radi)

print(f'Em um ângulo de {angulo:.2f} o seno é {s:.2f}, cosseno é {cos:.2f} e a tangente é {tan:.2f} é os radianos {radi:.2f}')