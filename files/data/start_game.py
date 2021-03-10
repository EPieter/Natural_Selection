from .imports import *

# fetches display size
infoObject = pg.display.Info()

# display size
screen = pg.display.set_mode((infoObject.current_w, infoObject.current_h))

# Setup the clock for a decent frame rate
clock = pg.time.Clock()

