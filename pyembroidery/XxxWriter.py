from .ReadHelper import read_int_16le, read_int_8, read_int_32be, signed8, signed16
from .EmbThread import EmbThread

# 7F 08 00 00 is color change.
# 7F 01 xx yy is unstitched.
# 7F 7F 02 14 is end.

def write(pattern, f, settings=None):

    num_of_colors = read_int_16le(f)
