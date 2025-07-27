from UI.menu import *
from UI.button import * 
from UI.draw_down_menu import * 
from UI.list_display import * 
from UI.UIconstants  import *
from visualizer.sorting import bubbleSort, insertionSort, mergeSort, quickSort, selectionSort
from functions import *
import pygame


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    result = render_main_menu(screen)
    if result is None : return 

    list_display , dropdown , generate_arr_button  = result
    clock = pygame.time.Clock()
    running = True 

    while running :
        
        screen.fill(SCREEN_COLOR)
        list_display.draw(screen)
        generate_arr_button.draw(screen)
        dropdown.draw(screen)

        
    
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT: 
                running = False 
    
            if event.type == pygame.MOUSEBUTTONDOWN:
    
                if(generate_arr_button.is_clicked(event.pos)):
                    list_display.generate_arr()
                    revertColor(list_display.buttons)
                    
            dropdown.handle_event(event)
            if dropdown.get_selected() is not None  and dropdown.active is False:
                dropdown.draw(screen)
                algo_name = dropdown.get_selected()
                generator = get_generator(algo_name)
                result = performSimpleSort(screen, list_display, generate_arr_button, dropdown, clock, generator)
                if result == "quit":
                    running = False
                dropdown.selected_index = None

    
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()
