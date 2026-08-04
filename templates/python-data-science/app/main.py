import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

numbers = np.array([1, 2, 3, 4, 5])

data = pd.DataFrame({
    "x": numbers,
    "y": numbers * 2
})

model = LinearRegression()
model.fit(data[["x"]], data["y"])

print("StudentDev-Box Python Data Science environment is working!")
print(data)
print(f"Model coefficient: {model.coef_[0]}")