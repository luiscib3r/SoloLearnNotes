import sys

sys.stdin = open('random.txt')

import numpy as np

random_state = int(input())

n = int(input())

rows = []

for i in range(n):
    rows.append([float(a) for a in input().split()])

X = np.array(rows)
y = np.array([int(a) for a in input().split()])

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state)

model = RandomForestClassifier(random_state=random_state, n_estimators=5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred)