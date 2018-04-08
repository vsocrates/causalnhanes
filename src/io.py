#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import xport

import numpy as np
import pandas as pd


def xpt_to_df(fp):
    """
    Convert the xpt file to a pd.DataFrame.

    Params:
    -------
    fp: str
        The filepath to the dataset.

    Returns:
    --------
    df: pd.DataFrame
        The data converted to a dataframe type for easier computations.
    """
    if not os.path.exists(fp):
        raise ValueError('The filepath {0:s} does not exist! Ensure you are using the right path!'.format(os.path.abspath(fp)))
    # Check filepath type
    elif fp[-3:].lower() != 'xpt':
        raise ValueError('The filepath provided is not a .xpt file!')
    # Convert to a DataFrame object
    else:
        with open(fp, 'rb') as f:
            df = xport.to_dataframe(f)

    return df


if __name__ == "__main__":
	# Setup this file as current working directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    df = xpt_to_df('../data/nhanes/2015_2016/demographics/DEMO_I.XPT')
    print(df.head())
