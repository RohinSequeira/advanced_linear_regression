# Default imports
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression

# We have already loaded the data for you
data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')


# Write your solution here
def polynomial(power=5, Random_State=9):
    model = make_pipeline(PolynomialFeatures(degree=power, include_bias=False),LinearRegression())
    model.fit(X_train[[ 'OverallQual','GrLivArea','GarageCars','GarageArea' ]], y_train)
    return model
