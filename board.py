import pygame as pg
from constants import *

class Board:
    def __init__(self):
        self.grid = [
            "#################",
            "#...##.....##...#",
            "#.#.###.###.#.#.#",
            "#.#...........#.#",
            "#.#.###.#.###.#.#",
            "#.....#...#.....#",
            "###.#.#####.#.###",
            "#...............#",
            "###.#.#####.#.###",
            "#.....#...#.....#",
            "#.#.###.#.###.#.#",
            "#.#...........#.#",
            "#.#.###.###.#.#.#",
            "#...##.....##...#",
            "#################",
        ]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.eaten = set()   # stores (x, y) of eaten pellets

    def window_size(self):
        return self.cols*TILE_SIZE, self.rows*TILE_SIZE

    def draw(self, surface):
        """Tegn brettet på den gitte pygame-flaten."""
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                rect = pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if tile == '#':
                    pg.draw.rect(surface, DARK_BLUE, rect, border_radius=5)
                elif tile == '.' and (x, y) not in self.eaten:
                    center = (x * TILE_SIZE + TILE_SIZE // 2,
                            y * TILE_SIZE + TILE_SIZE // 2)
                    pg.draw.circle(surface, YELLOW, center, TILE_SIZE // 8)


    def is_road(self, x: int, y: int) -> bool:
        """Returnerer True hvis posisjonen er fri for vegg."""
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return False
        return self.grid[y][x] != '#'
    
    def eat_pellet(self, x: int, y: int) -> bool:
        """Call this when Pac-Man moves onto a tile.
        Returns True if a pellet was eaten."""
        if (x, y) not in self.eaten and self.grid[y][x] == '.':
            self.eaten.add((x, y))
            return True
        return False
