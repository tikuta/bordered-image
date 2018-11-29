#!/usr/bin/env python3

import numpy as np
import imageio
import sys
import os

def print_usage():
    print("""\
Draw 1-dot border to image
Usage: %s [Image file]...

Output will be placed as "[Input filename]_bordered.[extension]"
"""%sys.argv[0], file=sys.stderr)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    for f in sys.argv[1:]:
        im = imageio.imread(f)
        im[0,:,:] = 0 # top
        im[-1,:,:] = 0 # bottom
        im[:,0,:] = 0 # left
        im[:,-1,:] = 0 # right

        root, ext = os.path.splitext(f)
        imageio.imwrite(root + '_bordered' + ext, im)
