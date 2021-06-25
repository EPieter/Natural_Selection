import data


def pixelConversionH(array_h):
    pixel_h = array_h * data.TILE_SIZE + data.BEGIN_GRID_X + 2
    return pixel_h


def pixelConversionV(array_v):
    pixel_v = array_v * data.TILE_SIZE + data.BEGIN_GRID_Y + 2
    return pixel_v
