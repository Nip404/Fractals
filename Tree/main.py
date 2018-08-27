from Engine import Tree
import pygame

window_length = 800

s = [window_length] * 2
pygame.init()
screen = pygame.display.set_mode(s,0,32)
clock = pygame.time.Clock()
pygame.display.set_caption("Fractal Tree by NIP")

def main():
    t = Tree(screen)
    t.draw_tree()

    while True:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    t.binary = not t.binary
                    t.draw_tree()

                elif event.key == pygame.K_d:
                    t.factor += 1 if t.factor < t.maxfactor else 0
                    t.draw_tree()

                elif event.key == pygame.K_a:
                    t.factor -= 1 if t.factor else 0
                    t.draw_tree()

        if pygame.key.get_pressed()[pygame.K_UP]:
            t.delta += 1
            t.draw_tree()
            
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            t.delta -= 1
            t.draw_tree()
            
        if pygame.key.get_pressed()[pygame.K_w]:
            t.decay -= 0.02

            if t.decay <= 1.15:
                t.decay = 1.15
                
            t.draw_tree()
                    
        if pygame.key.get_pressed()[pygame.K_s]:
            t.decay += 0.02
            t.draw_tree()

        print(t.factor,t.delta,t.decay,t.binary)

if __name__ == "__main__":
    main()
