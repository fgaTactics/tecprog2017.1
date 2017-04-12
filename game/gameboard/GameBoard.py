
import pygame
def draw_board(amount_of_row,amount_of_columns):
    """ Draw a chess board with queens, from the_board. """

    pygame.init()
    colors = [(255,255,255), (0,0,0)]    # Set up colors [red, black]

    # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // amount_of_row # sq_sz is length of a square.
    surface_sz = amount_of_columns * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))
    # Draw a fresh background (a blank chess board)
    
    while True :
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;        
        
        for row in range(amount_of_row):           # Draw each row of the board.
            c_indx = row % 2                       # Change starting color on each row
            for col in range(amount_of_columns):   # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # now flip the color index for the next square
                c_indx = (c_indx + 1) % 2    
    
        pygame.display.flip()
    

if __name__ == "__main__":
    draw_board(5,10)    # 7 x 7 to test window siz