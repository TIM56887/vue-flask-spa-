import joblib
import numpy as np
# 加载已经训练好的模型
model = joblib.load('model.sav')
Le = joblib.load('label_encoder.pkl')
enc = joblib.load('onehot_encoder.pkl')
typeencoder = joblib.load('type_encoder.pkl')

def caculate (data):
    data = np.array([data])
    onehotlabels = enc.transform(data[:,0].reshape(-1, 1))
    data = np.delete(data, 0, 1)
    data = np.concatenate((onehotlabels, data), axis=1)
    le_list = [34,35,36]
    for i in le_list:
        data[:,i] = Le.transform(data[:, i])
    data[:,28] = typeencoder.transform(data[:, 28])
    data = data.astype(np.float64)
    return model.predict(data)[0][0]
