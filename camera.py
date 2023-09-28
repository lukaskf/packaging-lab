from picamera2 import Picamera2
import RPi.GPIO as GPIO

from time import sleep
import pygame
from pygame.locals import *
from io import BytesIO

camera = Picamera2()
capture_config = camera.create_still_configuration()
camera.configure(camera.create_preview_configuration())

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

# GPIO setup
GPIO.setmode(GPIO.BCM)
INPUT_PIN = 17  # Change to the GPIO pin number you're using to receive the signal
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def display_image(image_stream):
    # Load image stream into pygame and display it
    image_stream.seek(0)
    image = pygame.image.load(image_stream)
    screen.blit(image, (0, 0))
    pygame.display.flip()

def capture_and_show():
    camera.start()
    data = BytesIO()
    camera.capture_file(data, format='jpeg')
    display_image(data)

print("Waiting for signal...")

try:
    camera.start_preview()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                camera.stop_preview()
                pygame.quit()
                GPIO.cleanup()
                exit()
                
        if GPIO.input(INPUT_PIN) == GPIO.HIGH:
            print("Signal detected! Capturing and displaying image...")
            capture_and_show()
            sleep(0.05)  # Sleep for 50ms for rapid capture/display
finally:
    camera.stop_preview()
    pygame.quit()
    GPIO.cleanup()
    camera.close()