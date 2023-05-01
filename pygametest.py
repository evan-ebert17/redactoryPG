#if this has an error ignore it, it works...
import pygame
############################################
import sys

pygame.init()

# Screen settings
WIDTH, HEIGHT = 640, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrolling Text Box Example")

# Text settings
FONT = pygame.font.Font("VT323-Regular.ttf", 21)
TEXT_COLOR = (255, 255, 255)
TEXTMAIN = """ "As your eyes begin to open and your senses come about you, you find yourself in an abandoned stone Temple."\n
                 "Its walls cracked and its ceilings collapsed in many places, the once-majestic structure now lies in ruin."\n
                 "It's as if time has stood still in this abandoned temple, as now the scent of decay and mustiness permeates the air." \n
                 "The only source of light shimmers down as weak rays of sunshine filtering through the broken ceiling, casting a dusty glow on the crumbling stone pillars."\n
                 "It is hard to imagine a place, as grand as this, is all but helpless against the elements."\n
"""


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


class TextBox:
    def __init__(self, x, y, w, h, text,margin_x=5, margin_y=5, padding_x=5, padding_y=5):
        self.rect = pygame.Rect(x, y, w, h)
        self.margin_x = margin_x
        self.margin_y = margin_y
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.text = text
        self.lines = [line.strip() for line in text.splitlines()]
        self.rendered_text = []
        self.render()

    def render(self):
        for line in self.lines:
            words = line.split(' ')
            current_line = ''
            for word in words:
                test_line = current_line + word + ' '
                text_width, _ = FONT.size(test_line)
                if text_width < self.rect.width:
                    current_line = test_line
                else:
                    self.rendered_text.append(current_line.strip())
                    current_line = word + ' '
            self.rendered_text.append(current_line.strip())

    def draw(self, surface, scroll):
        original_clip = surface.get_clip()
        surface.set_clip(self.rect)
        for i, line in enumerate(self.rendered_text):
            draw_text(line, FONT, TEXT_COLOR, surface, self.rect.x + self.margin_x + self.padding_x, self.rect.y + self.margin_y + self.padding_y - scroll + i * FONT.get_linesize())
        surface.set_clip(original_clip)



def main():
    clock = pygame.time.Clock()
    scroll = 0

    #userText = "> ";

    textDescriptions = TextBox(50, 260, 540, 57, TEXTMAIN)
    #userInput = TextBox(50, 50, 50,50,userText)

    while True:
        dt = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEWHEEL:
                #print(event.x, event.y);
                if event.y > 0:
                    scroll -= 10
                elif event.y < 0:
                    scroll += 10
            #if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            #    if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
            #        userText = userText[:-1]
  
            # Unicode standard is used for string
            # formation
            #    else:
            #        userText += event.unicode

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            scroll -= 5
        if keys[pygame.K_DOWN]:
            scroll += 5

        scroll = max(0, min(scroll, len(textDescriptions.rendered_text) * FONT.get_linesize() - textDescriptions.rect.height))

        screen.fill((0, 0, 0))
        textDescriptions.draw(screen, scroll)
        #userInput.draw(screen,None)
        pygame.draw.rect(screen, (255, 255, 255), textDescriptions.rect, 2)
        #pygame.draw.rect(screen, (255,255,255), userInput.rect,2)
        pygame.display.flip()


if __name__ == "__main__":
    main()