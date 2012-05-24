#!/usr/bin/env python

import sys
from scipy import misc
from skimage import util
from skimage import color
import numpy as np
#from 

from joblib import Memory
mem = Memory('_cache')

from skimage import io
io.use_plugin('freeimage')


def get_image(fname):
    arr = io.imread(fname)
    if arr.ndim == 2:
        arr = color.gray2rgb(arr)
    arr = util.img_as_float(arr)
    assert arr.ndim == 3
    return arr


def kolax():
    #filenames = sys.stdin.readlines()
    #filenames = [fn.split('\n')[0] for fn in filenames]
    from glob import glob
    filenames = np.array(glob('tmp_pics-64x64/*jpg'))
    print len(filenames)

    #input_size = 64, 64
    pixel_size = pixh, pixw = 64, 64
    input_filename = './babou-64.jpg'
    batch_size = 10

    # --
    arr_in = get_image(input_filename)
    inh, inw, ind = arr_in.shape

    outh = inh * pixh
    outw = inw * pixw
    outd = ind
    arr_out = np.empty((outh, outw, outd), dtype='float32')

    rng = np.random.RandomState(42)

    tot = inh * inw
    curr = 0
    for j in xrange(inh):
        for i in xrange(inw):
            # -- input pixel
            pix_in = arr_in[j, i]
            # -- output pixel
            ridx = rng.permutation(len(filenames))[:batch_size]
            best_arr = None
            best_l2 = np.inf
            for fname in filenames[ridx]:
                arr = get_image(fname)
                sig = arr.mean(0).mean(0)
                l2 = np.sqrt(((pix_in - sig) ** 2.).sum())
                if l2 < best_l2:
                    best_l2 = l2
                    best_arr = arr
            arr_out[j * pixh: (j + 1) * pixh,
                    i * pixw: (i + 1) * pixw] = best_arr
            #print best_l2
            curr += 1
            if curr % 100 == 0:
                print '%05.02f%%' % (100. * curr / tot)

    misc.imsave('out.png', arr_out)


    #for fname in filenames:
        #print arr.shape


def main():
    kolax()


if __name__ == '__main__':
    main()
