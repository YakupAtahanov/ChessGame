import arcade
import chess
import config

class ChessGame(arcade.Window):
    def __init__(self, width, height, offset = 20):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height

        self.BOARD_OFFSET = offset

        self.BOARD_SIZE = width - (self.BOARD_OFFSET * 2) if width < height else height - (self.BOARD_OFFSET * 2)
        self.BOARD_POS_X = ((self.WINDOW_WIDTH // 2) - (self.BOARD_SIZE // 2))
        self.BOARD_POS_Y = ((self.WINDOW_HEIGHT // 2) - (self.BOARD_SIZE // 2))

        self.CELL_SIZE = self.BOARD_SIZE // 8

        self.PIECE_OFFSET = 0
        self.SPRITE_SCALING_PIECE = ((self.CELL_SIZE * 0.99)/45)

        self.board = None
        self.existing_pieces = arcade.SpriteList()
        

    def start_game(self):
        self.draw_board()

    def draw_board(self):
        arcade.open_window(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, "Chess Game")

        arcade.set_background_color(arcade.csscolor.GREY)
    
        # RENDER START
        arcade.start_render()

        # arcade.draw_lrtb_rectangle_filled(self.BOARD_POS_X, self.BOARD_POS_X + self.BOARD_SIZE, self.BOARD_POS_Y + self.BOARD_SIZE, self.BOARD_POS_Y, arcade.csscolor.GREEN)
        color_change = True
        for row in range(8):
            for column in range(8):
                current_color = arcade.csscolor.CADET_BLUE if color_change else arcade.csscolor.WHITE
                color_change = not color_change
                cell_bottom_most_coordinate = self.BOARD_POS_Y + (self.CELL_SIZE * row)
                cell_left_most_coordinate = self.BOARD_POS_X + (self.CELL_SIZE * column)
                # print(cell_left_most_coordinate, cell_bottom_most_coordinate)
                arcade.draw_lrtb_rectangle_filled(cell_left_most_coordinate, cell_left_most_coordinate + self.CELL_SIZE, cell_bottom_most_coordinate + self.CELL_SIZE, cell_bottom_most_coordinate, current_color)
            color_change = not color_change

        self.draw_pieces()

        self.existing_pieces.update()
        
        #RENDER FINISH
        arcade.finish_render()

        arcade.run()

    def draw_pieces(self):
        self.board = chess.Board()
        current_pieces = self.board.piece_map()
        # piece = arcade.Sprite(pieces.black_king["root"], self.SPRITE_SCALING_PIECE)
        for cell in current_pieces:
            symbol = current_pieces[cell].symbol()
            piece = arcade.Sprite(config.pieces[symbol]["root"], self.SPRITE_SCALING_PIECE)
            self.existing_pieces.append(piece)
            piece.center_x = self.BOARD_POS_X + (self.CELL_SIZE // 2) + (self.CELL_SIZE * config.cells[cell]["column"])
            piece.center_y = self.BOARD_POS_Y + (self.CELL_SIZE // 2) + (self.CELL_SIZE * config.cells[cell]["row"])
            piece.draw()

    def update_board():
        pass

    def chess_handler(self):
        pass
    
width = int(input("Window Width: "))
height = int(input("Window Height: "))
offset = int(input("Board Offset: "))
game = ChessGame(width, height, offset)
game.start_game()
