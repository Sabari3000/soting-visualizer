import pygame
import random
import sys
import time

def visualize(x=-1, y=-1, z=-1):
    window.fill((0, 0, 0))
    for i, height in enumerate(arr):
        color = (170, 183, 184)  # default color
        if complete:
            color = (100, 180, 100)
        elif i == x or i == z:
            color = (100, 180, 100)
        elif i == y:
            color = (165, 105, 189)
        
        pygame.draw.rect(window, color, (i * RECT_SIZE, SCREEN_HEIGHT - height, RECT_SIZE, height))
    pygame.display.update()

def randomize_and_load_array():
    global arr
    arr = [random.randint(10, SCREEN_HEIGHT - 10) for _ in range(ARR_SIZE)]

def bubble_sort():
    global complete
    complete = False
    for i in range(ARR_SIZE - 1):
        for j in range(ARR_SIZE - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                visualize(j, j + 1)
                pygame.time.delay(10)
    complete = True

# Screen settings
SCREEN_WIDTH = 910
SCREEN_HEIGHT = 750
ARR_SIZE = 130
RECT_SIZE = 7

# Initialize array and state variables
arr = []
complete = False

# Pygame initialization
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

randomize_and_load_array()
running = True
show_controls = True

while running:
    if show_controls:
        print("Press 1 to start Bubble Sort, Press R to Randomize Array, Press Q to Quit.")
        show_controls = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_r:
                randomize_and_load_array()
                complete = False
                print("Array randomized.")
            elif event.key == pygame.K_1:
                print("Bubble Sort started.")
                bubble_sort()
                print("Bubble Sort complete.")

    visualize()
pygame.quit()
sys.exit()