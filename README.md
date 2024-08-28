# LiquidLens
para adquirir imagenes se utiliza take_image.py (python3) que utiliza picamera2 y openCV para adquirir una image.
Dependencias:
    picamera2
    opencv-python
    time
    glob
    smbus

ejecucion:
    para tomar una imagen se executa el comando:
    python3 take_image.py -v XXX  
    el voltage* (-v, --voltage) debe ser un valor entre 0 y 255.
    ej: python3 take_image.py 172
    Ademas existen argumentos como:
    -x --xsize utilizado para cambiar ancho de la imagen (defaul = 3280)
    -y --ysize utilizado para cambiar alto de la imagen (defaul = 2464)
    -r --resize utilizado como factor de reescalamiento de imagen capturada (defaul = 1)

Para ver la operacion de la camara en tiempo real  