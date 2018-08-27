import pygame
import math

class Tree:
    def __init__(self,surface):
        self.surf = surface
        self.start = [self.surf.get_width()/2,self.surf.get_height()*0.7]
        self.length = self.surf.get_size()[0]/10
        self.maxfactor = 10

        # Settings
        self.factor = 8
        self.delta = 20
        self.decay = 1.4
        self.binary = True

    def build_tree(self,pos,deg,length,recur=0):
        if not recur:
            return

        heading_vector = [math.cos(math.radians(deg)),math.sin(math.radians(deg))]
        new = [(heading_vector[i]*length)+pos[i] for i in range(2)]
        
        pygame.draw.line(self.surf,(0,0,0),pos,new,1)

        self.build_tree(new,deg-self.delta,length/self.decay,recur-1)
        self.build_tree(new,deg+self.delta,length/self.decay,recur-1)

        if not self.binary:
            self.build_tree(new,deg,length/self.decay,recur-1)

    def draw_tree(self):
        self.surf.fill((255,255,255))
        self.build_tree(self.start,-90,self.length,self.factor)
        pygame.display.flip()
        

