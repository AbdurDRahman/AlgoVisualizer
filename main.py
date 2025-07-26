
from UI import button, draw_down_menu, functions, list_display, menu, UIconstants
from visualizer.sorting import bubbleSort, insertionSort, mergeSort, quickSort, selectionSort
import pygame
def main():


    pygame.init()
    screen = None
    result = menu.render_main_menu(screen)
    if result is None : return 
    list_display , dropdown , generate_arr_button  = result
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
