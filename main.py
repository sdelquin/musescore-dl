import sys

from lib.manager import Manager
from lib.utils import init_logger

logger = init_logger()

manager = Manager(sys.argv[1])
score = manager.get_score()
score.save_file()
