import sys

from lib.handler import Handler

handler = Handler(sys.argv[1])
score = handler.get_score()
score.save_file()
