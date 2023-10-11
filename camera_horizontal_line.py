#!/usr/bin/python3

from picamera2 import Picamera2
import RPi.GPIO as GPIO

from time import sleep
import pygame
from pygame.locals import *
from io import BytesIO
from libcamera import controls

camera = Picamera2()
capture_config = camera.create_still_configuration()
camera.configure(camera.create_preview_configuration())
camera.set_controls({"AfMode": controls.AfModeEnum.Continuous}) #continious autofocus
# camera.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 10.0}) #manual autofocus

# success = camera.autofocus_cycle()
# job = camera.autofocus_cycle(wait=False)
# success = camera.wait(job)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

# GPIO setup
GPIO.setmode(GPIO.BCM)
INPUT_PIN = 17  # Change to the GPIO pin number you're using to receive the signal
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# def display_image(image_stream):
#     # Load image stream into pygame and display it
#     image_stream.seek(0)
#     image = pygame.image.load(image_stream)
#     screen.blit(image, (0, 0))
#     pygame.display.flip()

# def display_image(image_stream):
#     image_stream.seek(0)
#     image = pygame.image.load(image_stream)
#     img_rect = image.get_rect(center=(pygame.display.Info().current_w//2, pygame.display.Info().current_h//2))
#     screen.blit(image, img_rect)
#     pygame.display.flip()

def display_image(image_stream):
    image_stream.seek(0)
    image = pygame.image.load(image_stream)
    image = pygame.transform.scale(image, (pygame.display.Info().current_w, pygame.display.Info().current_h))
    
    screen.blit(image, (0, 0))
    line_color = (255, 0, 0)  # Color of the line, in this case, red
    # vertical line
    line_start = (pygame.display.Info().current_w // 2, 0)  # Starting point of the line
    line_end = (pygame.display.Info().current_w // 2, pygame.display.Info().current_h)  # Ending point of the line
    # horizontal line
    line_start = (0, pygame.display.Info().current_h // 2)  # Starting point of the line
    line_end = (pygame.display.Info().current_w, pygame.display.Info().current_h // 2 )  # Ending point of the line
    line_width = 5  # Width of the line in pixels
    
    pygame.draw.line(screen, line_color, line_start, line_end, line_width)
    pygame.display.flip()

def capture_and_show():
    data = BytesIO()
    camera.start()
    camera.capture_file(data, format='jpeg')
    display_image(data)

print("Waiting for signal...")

try:
    # camera.start_preview()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == MOUSEBUTTONDOWN):
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
