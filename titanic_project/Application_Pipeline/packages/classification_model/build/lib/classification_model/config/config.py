import pathlib
import classification_model
import pandas as pd
# ====   PATHS ===================
PACKAGE_ROOT = pathlib.Path(classification_model.__file__).resolve().parent
#print('HEYYYYYYYYY'+ str(PACKAGE_ROOT))
#TRAINING_DATA_FILE = PACKAGE_ROOT/"datasets/titanic.csv"
PIPELINE_NAME = 'classification_model'
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"

TESTING_DATA_FILE = "test.csv"
TRAINING_DATA_FILE = "train.csv"
#TRAINING_DATA_FILE = "titanic.csv"
# ======= FEATURE GROUPS =============

TARGET = 'Survived'

CATEGORICAL_VARS = ['Sex', 'Cabin', 'Embarked', 'Title']

NUMERICAL_VARS = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

CABIN = 'Cabin'

RANDOM_SEED = 0


#OTHER

pd.options.display.max_rows = 10
pd.options.display.max_columns = 10


PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"