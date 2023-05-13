# Setup feedback system
from learntools.core import binder
binder.bind(globals())
from learntools.feature_engineering_new.ex3 import *

import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor


def score_dataset(X, y, model=XGBRegressor()):
    # Label encoding for categoricals
    for colname in X.select_dtypes(["category", "object"]):
        X[colname], _ = X[colname].factorize()
    # Metric for Housing competition is RMSLE (Root Mean Squared Log Error)
    score = cross_val_score(
        model, X, y, cv=5, scoring="neg_mean_squared_log_error",
    )
    score = -1 * score.mean()
    score = np.sqrt(score)
    return score


# Prepare data
df = pd.read_csv("../input/fe-course-data/ames.csv")
X = df.copy()
y = X.pop("SalePrice")

# YOUR CODE HERE
X_1 = pd.DataFrame()  # dataframe to hold new features

X_1["LivLotRatio"] = df.GrLivArea / df.LotArea
X_1["Spaciousness"] = (df.FirstFlrSF + df.SecondFlrSF) / df.TotRmsAbvGrd
X_1["TotalOutsideSF"] = df.WoodDeckSF + df.OpenPorchSF + df.EnclosedPorch + df.Threeseasonporch + df.ScreenPorch

# YOUR CODE HERE
# One-hot encode BldgType. Use `prefix="Bldg"` in `get_dummies`
X_2 = pd.get_dummies(df.BldgType, prefix="Bldg")
X_2 = X_2.mul(df.GrLivArea, axis=0)


X_3 = pd.DataFrame()

# YOUR CODE HERE
X_3["PorchTypes"] = df[[
    "WoodDeckSF",
    "OpenPorchSF",
    "EnclosedPorch",
    "Threeseasonporch",
    "ScreenPorch",
]].gt(0.0).sum(axis=1)

X_4 = pd.DataFrame()

# YOUR CODE HERE

X_4["MSClass"] = df.MSSubClass.str.split("_", n=1, expand=True)[0]


X_5 = pd.DataFrame()

# YOUR CODE HERE
X_5["MedNhbdArea"] = df.groupby("Neighborhood")["GrLivArea"].transform("median")

X_new = X.join([X_1, X_2, X_3, X_4, X_5])
score_dataset(X_new, y)










