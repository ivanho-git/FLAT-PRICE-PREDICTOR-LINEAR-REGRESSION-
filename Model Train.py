# Model Training
X_train, X_test, y_train, y_test = train_test_split(
    data[required_cols], data[target_col], test_size=0.4, random_state=10
)
model = LinearRegression()
model.fit(X_train, y_train)
