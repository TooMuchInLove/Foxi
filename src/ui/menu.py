from sys import exit
from pygame import draw, font, mouse, quit


class MenuApp:
    """ Класс главного меню приложения """
    __slots__ = ("__screen", "__w", "__h", "__COLORS", "__MENU", "__SIZE_MENU", "__STYLE", "pos",)

    def __init__(self, screen, w, h, colors, menu) -> None:
        self.__screen = screen
        self.__w = w
        self.__h = h
        self.__COLORS = colors
        self.__MENU = menu
        self.__SIZE_MENU = len(self.__MENU)
        self.__STYLE = font.SysFont('Consolas', 35)

    def draw_menu(self) -> None:
        # Список позиций пунктов МЕНЮ [ x, y, width, height ];
        self.pos = []
        # Отрисовываем ФОН;
        draw.rect(self.__screen, self.__COLORS[5], (0, 0, self.__w, self.__h))
        # Получаем координаты МЫШИ;
        x, y = mouse.get_pos()
        # Формируем компоненты МЕНЮ;
        for i in range(self.__SIZE_MENU):
            text = self.__STYLE.render(self.__MENU[i][1], True, self.__COLORS[2])
            if self.__MENU[i][0] == 0:
                text = self.__STYLE.render(self.__MENU[i][1], True, self.__COLORS[0])
            self.pos += [[
                # [ x, y, width, height ]
                (self.__w - text.get_size()[0])/2,
                (self.__h - text.get_size()[1]*self.__SIZE_MENU)/2 + i*(text.get_size()[1] + 5),
                text.get_size()[0],
                text.get_size()[1]
            ]]
            # Определяем, находится ли курсор в зоне МЕНЮ;
            item_x, item_y, item_w, item_h = self.pos[i]
            if item_x <= x <= item_x + item_w and item_y <= y <= item_y + item_h and self.__MENU[i][0] != 0:
                text = self.__STYLE.render(self.__MENU[i][1], True, self.__COLORS[1])
            self.__screen.blit(text, (self.pos[i][0], self.pos[i][1]))

    def get_position_cursor(self) -> bool:
        # Получаем координаты МЫШИ;
        x, y = mouse.get_pos()
        # Определяем, находится ли курсор в зоне МЕНЮ;
        for i in range(self.__SIZE_MENU):
            item_x, item_y, item_w, item_h = self.pos[i]
            if item_x <= x <= item_x + item_w and item_y <= y <= item_y + item_h:
                # Убираем из меню всё ненужное;
                if self.__SIZE_MENU > 3:
                    self.__MENU = self.__MENU[:3]
                    return False
                # Выходим из игры;
                if self.__MENU[i][0] == 2:
                    quit()
                    exit()
        return True
