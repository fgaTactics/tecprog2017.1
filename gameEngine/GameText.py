import pygame


class GameText:

    text_list = []
    position_list = []

    @classmethod
    def print(cls, text, x_position, y_position):
        cls.text_list.append(text)
        cls.position_list.append((x_position, y_position))

    @classmethod
    def print_text_list(cls, screen):
        font_color = 250, 250, 250
        background_color = 5, 5, 5
        font = pygame.font.Font(None, 40)

        list_length = len(cls.text_list)
        for i in range(0, list_length):
            renderer = font.render(cls.text_list[i], 0, font_color, background_color)
            screen.blit(renderer, (cls.position_list[i][0], cls.position_list[i][1]))

    @classmethod
    def reset_text_list(cls):
        cls.text_list.clear()
