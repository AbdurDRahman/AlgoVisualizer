from visualizer.sorting.bubbleSort import * 
from visualizer.sorting.insertionSort import *
from visualizer.sorting.mergeSort import *
from visualizer.sorting.quickSort import *
from visualizer.sorting.selectionSort import *
from mergeSort import performMergeSort
from UI.menu import *
from UI.UIconstants import (ARRAY , SCREEN_COLOR , LIST_BACKGROUND_COLOR , SORTED_LIST_COLOR)
import pygame 

def get_generator(algo_name):
    
    if algo_name == "Bubble Sort":
        return bubbleSort(ARRAY)
    elif algo_name == "Insertion Sort":
        return insertionSort(ARRAY)
    elif algo_name == "Merge Sort":
        return mergeSort(ARRAY)
    elif algo_name == "Quick Sort":
        return quickSort(ARRAY)
    elif algo_name == "Selection Sort":
        return selectionSort(ARRAY)
    else:
        raise ValueError("Unknown algorithm name")

def performSimpleSort(screen,list_display,generate_arr_button,dropdown,clock,generator):
    
    SORT_TYPE = str(generator.gi_code.co_name)
   
    if SORT_TYPE == "mergeSort":
   
        performMergeSort(screen, list_display, generate_arr_button, dropdown, clock, generator)
        sortedColor(list_display.buttons, len(list_display.buttons), SORT_TYPE)
        return 
    
    play_button = render_play_all_button(screen)
    next_button = render_next_button(screen)
    
    while True:
        
        screen.fill(SCREEN_COLOR)
        list_display.draw(screen)
        dropdown.draw(screen)
        play_button.draw(screen)
        next_button.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if play_button.is_clicked(event.pos):
                    finishSimpleSort(screen, list_display, generate_arr_button, dropdown, clock, play_button, next_button, generator)
                    sortedColor(list_display.buttons, len(list_display.buttons), SORT_TYPE)
                    return
                
                elif next_button.is_clicked(event.pos):
                
                    try:
                    
                        indexes = next(generator)
                        if(SORT_TYPE == "quickSort"):
                            if(indexes[3] is False):
                                quickSortChangeColor(list_display.buttons, indexes[0], indexes[1], indexes[2])
                            else:
                                quickSortSortedColor(list_display.buttons, indexes[0], indexes[2]) 
                        else:
                            changeColor(list_display.buttons, indexes[0], indexes[1])
                            sortedColor(list_display.buttons, indexes[0] if SORT_TYPE != "bubbleSort" else indexes[2], SORT_TYPE)
                    
                    except StopIteration: 
                        sortedColor(list_display.buttons, len(list_display.buttons))
                        return

    pygame.display.flip()
    clock.tick(60)
    
def changeColor(buttons , i , j):
    
    revertColorExceptBlue(buttons)
    
    for num,button in enumerate(buttons):
    
        if num == i or num == j:
            button.background_color = "green"

def sortedColor(buttons,i,SORT_TYPE = "no need really"):
    
    for num, button in enumerate(buttons):
        
        if num < i and (SORT_TYPE != "bubbleSort"):
            button.background_color = SORTED_LIST_COLOR
        
        else : break 
    
    if SORT_TYPE != "bubbleSort": return 
    
    check = len(ARRAY) - i
    
    for num, button in enumerate(buttons):
        
        if num >= check and SORT_TYPE == "bubbleSort":
            button.background_color = SORTED_LIST_COLOR
        
def revertColor(buttons):
    
    for button in buttons:
        button.background_color = LIST_BACKGROUND_COLOR

def finishSimpleSort(screen, list_display, generate_arr_button, dropdown, clock , play_button, next_button , generator):
    
    while True:
        
        screen.fill((255, 255, 255))
        list_display.draw(screen)
        dropdown.draw(screen)
        play_button.draw(screen)
        next_button.draw(screen)
        try:
            next(generator)
        except StopIteration:
            break

 
    pygame.display.flip()
    clock.tick(1000)

def quickSortChangeColor(buttons , i , mid , j):
    revertColorExceptBlue(buttons)

    for num, button in enumerate(buttons):
        
        if num < mid and num >= i:
            button.background_color = "green"
        
        elif num == mid :
            button.background_color = "yellow"
        
        elif num > mid and num <= j:
            button.background_color = "green"

def quickSortSortedColor(buttons, i, j):
    
    for num , button in enumerate(buttons):
    
        if num >= i and num <= j:
            button.background_color = SORTED_LIST_COLOR

def revertColorExceptBlue(buttons):
    
    for button in buttons:
    
        if button.background_color != SORTED_LIST_COLOR and button.background_color != "yellow":
            button.background_color = LIST_BACKGROUND_COLOR

