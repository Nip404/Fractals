import pygame
import sys

### SETTINGS

# Default (Recommended) = 4
layers = 4
window_width = 500
animate = True

# in milliseconds
animation_delay = 0

pygame.init()
s = [window_width]*2
screen = pygame.display.set_mode(s, 0, 32)
clock = pygame.time.Clock()
pygame.display.set_caption("Sierpinsky Carpet by NIP")

def draw(centre, length, i, recursive_lim):
    pygame.draw.rect(screen, [0]*3, (centre[0] - (length/2), centre[1] - (length/2), length, length), 0)

    if i >= recursive_lim:
        return

    events()

    for n in [[centre[0]-length, centre[1]-length], [centre[0], centre[1]-length], [centre[0]+length, centre[1]-length], [centre[0]-length, centre[1]], [centre[0]+length, centre[1]], [centre[0]-length, centre[1]+length], [centre[0], centre[1]+length], [centre[0]+length, centre[1]+length]]:
        draw(n, length/3, i+1, recursive_lim)

        if animate:
            pygame.display.flip()
            pygame.time.wait(animation_delay)

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def main():
    layers = 4

    screen.fill((255, 255, 255))
    draw([i/2 for i in s], s[0]/3, 0, layers)
    pygame.display.flip()
    
    while True:
        events()

if __name__ == "__main__":
    main()
