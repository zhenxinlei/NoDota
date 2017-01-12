# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import matplotlib.pyplot as plt
#import seaborn as sns

#%matplotlib inline

pd.set_option('display.max_columns', 120)
with pd.HDFStore("/Users/Unikang/PycharmProjects/NoDota/src/data/train.h5", "r") as train:
    # Note that the "train" dataframe is the only dataframe in the file
    df = train.get("train")
df.head()
#Test commit