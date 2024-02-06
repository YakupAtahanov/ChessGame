import chess

board = chess.Board()
print(type(board))
items = board.piece_map()
print(items[63].symbol())
print(items[62].symbol())
print(items[0].symbol())
print(items[1].symbol())
# print(items[63].symbol)
# print(items[63].symbol)
# print(items[63].symbol)
# print(items[63].symbol)
# for item in items:
#     print(items[item])
# print(board)