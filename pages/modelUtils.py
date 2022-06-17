import pickle
import os
import sklearn
from sklearn import linear_model

def checkDir():
	return 'models' in os.listdir('../')

def makeDir():
	if not checkDir():
		os.mkdir('../models')

# will save a model at ../models and will return the location+name of saved model
def saveModel(modelClass, name = None):
	fileName = name
	if fileName is None: 
		fileName = 'model'+str(len(os.listdir('../models')))
	fileName+='.sav'
	pickle.dump(modelClass, open(f'../models/{fileName}', 'wb'))
	return f'../models/{fileName}'

# model will be loaded through the location of model that is returned from the 
def loadModel(fileName):
	return pickle.load(open(fileName, 'rb'))

### All the below tests passed
if __name__ == '__main__':
	print(checkDir())
	makeDir()
	reg = linear_model.Ridge(alpha = 0.5)
	reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
	print("og Coeff: ",reg.coef_)
	path = saveModel(reg)
	print(f"Model Name: {path}")
	model = loadModel(path)
	print("Loaded Model:", model.coef_)
