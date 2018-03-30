#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import xport

import numpy as np 


def xpt_to_np(fp):
    """
    Convert the xpt file to a np.ndarray.

    Params:
    -------
    fp: str
        The filepath to the dataset.

    Returns:
    --------
    X: np.ndarray
        The data converted to a numpy format for easier computation.
    """
    if not os.path.exists(fp):
        raise ValueError('The filepath {0:s} does not exist! Ensure you are using the right path!'.format(os.path.abspath(fp)))
    else:
        # Check if the file type is the one we want
        if fp[-3:].lower() != 'xpt':
            raise ValueError('The file provided is not a .xpt file!')
        # Convert to a numpy array
        else:
            with open(fp, 'rb') as f:
                X = xport.to_numpy(f)    

    return X


if __name__ == "__main__":
	# Setup this file as current working directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    X = xpt_to_np('../data/DEMO_I.XPT')
    print(X.shape)
    # with open('../data/DEMO_I.xpt', 'rb') as f:
    #     reader = xport.Reader(f)
    #     print(reader.fields)
    #     for row in xport.Reader(f):
    #         print(row)
