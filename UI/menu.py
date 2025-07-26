from .button import * 
from .list_display import * 
from .draw_down_menu import * 
from .UIconstants import *
from .functions import *
import pygame 


def render_main_menu():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Algorithm Visualizer")
    
    dropdown_font = pygame.font.Font(None,DROP_DOWN_FONT_SIZE)
    list_elements_font = pygame.font.Font(None ,LIST_FONT_SIZE)
    button_font = font = pygame.font.SysFont("Arial", GEN_ARR_FONT_SIZE)
    
    list_display = ListDisplay(
        ARRAY , LIST_CORDINATES[0] , LIST_CORDINATES[1] ,
        LIST_WIDTH , LIST_HEIGHT , list_elements_font ,
        LIST_BACKGROUND_COLOR , LIST_TEXT_COLOR ,
        LIST_BOARDER_COLOR
        )
    
    dropdown = Dropdown(
        DROPDOWN_COORDINATES[0] , DROPDOWN_COORDINATES[1],
        DROP_DOWN_WIDTH , DROP_DOWN_HEIGHT,
        dropdown_font, DROPDOWN_BOX_COLOR,
        DROPDOWN_HOVER_COLOR , DROPDOWN_TEXT_COLOR , LIST_OF_ALGORITHMS
        )

    generate_arr_button = Button(
        GEN_ARR_COORDINATES[0] , GEN_ARR_COORDINATES[1] ,
        GEN_ARR_WIDTH , GEN_ARR_HEIGHT , GEN_ARR_TEXT ,
        button_font ,GEN_ARR_BG_COLOR , GEN_ARR_TEXT_COLOR
        )
    
    clock = pygame.time.Clock()
    running = True 

    while running :
        
        screen.fill(SCREEN_COLOR)
        list_display.draw(screen)
    
        generate_arr_button.draw(screen)
        generate_arr_button
    
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT: 
                running = False 
    
            if event.type == pygame.MOUSEBUTTONDOWN:
    
                if(generate_arr_button.is_clicked(event.pos)):
                    list_display.generate_arr()
            dropdown.handle_event(event)
    
        dropdown.draw(screen)
    
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()