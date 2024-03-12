import socket
import RPi.GPIO as GPIO
import time


def receive_messages(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()
        print(f"Listening for connections on port {port}...")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            print('Received:', data.decode())
            return data.decode()


def cycle_gpio(pin):
    GPIO.setup(pin, GPIO.OUT)

    for x in range(3):
        print("Turning the light on")
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
        print("Turning the light off")
        GPIO.output(pin, GPIO.LOW)
        time.sleep(1)


def cycle_error():
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)

    for x in range(4):
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(1)

        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        time.sleep(1)


if __name__ == "__main__":
    port = 1069

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Receive messages continuously
    while True:
        command = receive_messages(port)
        for letter in command:
            if letter == 'A':
                cycle_gpio(17)
            elif letter == 'B':
                cycle_gpio(18)
            elif letter == 'C':
                cycle_gpio(27)
            elif letter == 'D':
                cycle_gpio(22)
            elif letter == 'E':
                cycle_gpio(23)
            else:
                cycle_error()

        time.sleep(1)
