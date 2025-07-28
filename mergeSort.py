import pygame

from UI.UIconstants import * 
from visualizer.sorting.mergeSort import *
from UI.menu import *

#MERGE SORT CONSTANTS
MERGE_ARRAYS_OFFSET = 10
MERGE_ROW_1 = [False , False]
MERGE_ROW_2 = [False , False , False , False]
MERGE_ROW_3 = [False , False , False , False , False , False , False , False]
MERGE_ROW_4 = [False , False , False , False , False , False]

MERGE_ROW_5 = [False , False ]
MERGE_ROW_6 = [False , False , False , False]
MERGE_ROW_7 = [False , False]
MERGE_ROW_8 = [False]
def performMergeSort(screen,list_display,generate_arr_button,dropdown,clock,generator):
    next(generator)
    Reset_rows()
    play_button = render_play_all_button(screen)
    next_button = render_next_button(screen)
    SORT_TYPE = str(generator.gi_code.co_name)
    lists = []
    count = 1 
    while True:
        screen.fill(SCREEN_COLOR)
        list_display.draw(screen)
        dropdown.draw(screen)
        play_button.draw(screen)
        next_button.draw(screen)
        for lst in lists:
            lst.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if play_button.is_clicked(event.pos):
                    for gen in generator:
                        continue 
                    return
                
                elif next_button.is_clicked(event.pos):
                
                    try:
                        
                        curr_gen = next(generator)
                        manageLayers(screen, curr_gen, lists , count)
                        count += 1
                    
                    except StopIteration: 

                        return

    pygame.display.flip()
    clock.tick(60)

def get_merge_row(length, is_sorted , count):
    
    if not is_sorted:
        if count in (1,14):
            return MERGE_ROW_1, 50, 5
        elif count in (2,6,15,19):
            return MERGE_ROW_2, 100, 3
        elif count in (3 , 4 , 7 , 8 , 16 , 17 ,20 , 21):
            return MERGE_ROW_3, 150, 2
        elif count in (9 , 10 , 22 , 23 ):
            return MERGE_ROW_4, 200, 2
    
    else:
        if count in(11 , 24):
            return MERGE_ROW_5, 250, 2
        elif count in (5 , 12 , 18 , 25):
            return MERGE_ROW_6, 300, 3
        elif count in (13 , 26 ):
            return MERGE_ROW_7, 350, 5
        elif count == 27:
            return MERGE_ROW_8, 400, 1
    return None, None, None


def manageLayers(screen, iterator, lists , count):
    items, is_sorted = iterator
    items = list(items)  
    row, y, width_multiplier = get_merge_row(len(items), is_sorted , count)
    x_add_factor = 0
    if row:
        num = findEmptyElementOfRow(row)
        x_add_factor = x_factor_calculator(count)
        if num != -1:
            
            lists.append(render_custom_list(items, y, x_add_factor + LIST_WIDTH * num * width_multiplier))
            row[num] = True
    
def findEmptyElementOfRow(row):
    for i in range(len(row)):
        if row[i] is False:
            return i
    return -1  

def x_factor_calculator(count):
    x_factor_map = {
        2: 35,
        5: 35,
        6: 75,
        9: 330,
        10: 330,
        11: 370,
        12: 170,
        13: 115,
        14: 280,
        15: 255,  
        16: 105,
        17: 105,
        18: 265,  
        19: 295,  
        20: 105,
        21: 105,
        22: 680,
        23: 680,
        24: 825,  
        25: 305,  
        26: 395,  
        27: 270,
    }
    return x_factor_map.get(count, 0)


def Reset_rows():
    for i in range(len(MERGE_ROW_1)):
        MERGE_ROW_1[i] = False
    for i in range(len(MERGE_ROW_2)):
        MERGE_ROW_2[i] = False
    for i in range(len(MERGE_ROW_3)):
        MERGE_ROW_3[i] = False
    for i in range(len(MERGE_ROW_4)):
        MERGE_ROW_4[i] = False
    for i in range(len(MERGE_ROW_5)):
        MERGE_ROW_5[i] = False
    for i in range(len(MERGE_ROW_6)):
        MERGE_ROW_6[i] = False
    for i in range(len(MERGE_ROW_7)):
        MERGE_ROW_7[i] = False
    for i in range(len(MERGE_ROW_8)):
        MERGE_ROW_8[i] = False