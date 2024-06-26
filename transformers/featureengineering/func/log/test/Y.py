import numpy as np
from deepspace.transformers.model.regression.linear.func.log.Abstract import FuncTransformer

class Exp(FuncTransformer):
    '''Target Feature Engineering'''
    def __init__(self, feature, new_feature):
            FuncTransformer.__init__(self, feature, new_feature, np.exp)
    def transform(self, ds):
        df = ds.inv_test_data_pred
        df[self.feature] = np.exp(df[self.new_feature])
        return ds
    def get_data(self, ds):
        return ds.inv_test_data

