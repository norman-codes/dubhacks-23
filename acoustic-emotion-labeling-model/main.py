# # IMPORT MODULES
# import pandas as pd
# import numpy as np
# import os
# import librosa
# import librosa.display
# from sklearn.preprocessing import OneHotEncoder
# from keras.models import Sequential
# from keras.layers import Dense, LSTM, Dropout
# import warnings
# warnings.filterwarnings('ignore')
#
# # Get the current directory of the script
# script_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Specify the relative paths to the dataset directories
# tess_dataset_relative_path = 'datasets/TESS'
# cremad_dataset_relative_path = 'datasets/CREMA-D/AudioWAV'
# ravdess_dataset_relative_path = 'datasets/RAVDESS'
# savee_dataset_relative_path = 'datasets/SAVEE'
#
# # Construct the absolute paths to the dataset directories
# tess_dataset_path = os.path.join(script_dir, tess_dataset_relative_path)
# cremad_dataset_path = os.path.join(script_dir, cremad_dataset_relative_path)
# ravdess_dataset_path = os.path.join(script_dir, ravdess_dataset_relative_path)
# savee_dataset_path = os.path.join(script_dir, savee_dataset_relative_path)
#
# # Create the paths and labels lists
# paths = []
# labels = []
#
# # LOAD THE TESS DATASET
# for dirname, _, filenames in os.walk(tess_dataset_path):
#     for filename in filenames:
#         paths.append(os.path.join(dirname, filename))
#         label = filename.split('_')[-1]
#         label = label.split('.')[0]
#         if label == 'ps':
#             label = 'surprise'
#         labels.append(label)
#     if len(paths) == 2800:
#         break
# print('TESS dataset is loaded.')
#
# # Dictionary for mapping the CREMA-D dataset to the same labels as the TESS dataset.
# cremad_emotion_dict = {
#     "ANG": "angry",
#     "DIS": "disgust",
#     "FEA": "fear",
#     "HAP": "happy",
#     "NEU": "neutral",
#     "SAD": "sad"
# }
#
# # LOAD THE CREMA-D DATASET
# for dirname, _, filenames in os.walk(cremad_dataset_path):
#     for filename in filenames:
#         paths.append(os.path.join(dirname, filename))
#         label = filename.split('_')[2]
#         label = cremad_emotion_dict[label]
#         labels.append(label)
#     if len(paths) == 7442:
#         break
# print('CREMA-D dataset is loaded.')
#
# # Dictionary for mapping the RAVDESS dataset to the same labels as the TESS dataset.
# ravdess_emotion_dict = {
#     "01": "neutral",
#     "02": "neutral",  # originally "calm"
#     "03": "happy",
#     "04": "sad",
#     "05": "angry",
#     "06": "fear",
#     "07": "disgust",
#     "08": "surprise"
# }
#
# # LOAD THE RAVDESS DATASET
# for dirname, _, filenames in os.walk(ravdess_dataset_path):
#     for filename in filenames:
#         paths.append(os.path.join(dirname, filename))
#         label = filename.split('-')[2]
#         label = ravdess_emotion_dict[label]
#         labels.append(label)
#     if len(paths) == 1440:
#         break
# print('RAVDESS dataset is loaded.')
#
# # Dictionary for mapping the RAVDESS dataset to the same labels as the TESS dataset.
# savee_emotion_dict = {
#     "KL": "angry",
#     "JK": "happy",
#     "JE": "sad",
#     "DC": "neutral"
# }
#
# # LOAD THE SAVEE DATASET
# for dirname, _, filenames in os.walk(savee_dataset_path):
#     for filename in filenames:
#         paths.append(os.path.join(dirname, filename))
#         label = filename.split('_')[0]
#         label = savee_emotion_dict[label]
#         labels.append(label)
#     if len(paths) == 480:
#         break
# print('SAVEE dataset is loaded.')
#
# print(len(paths))
# print(len(labels))
#
# ## Create a dataframe
# df = pd.DataFrame()
# df['speech'] = paths
# df['label'] = labels
# print(df.head())
#
# print(df['label'].value_counts())
#
# ## Feature Extraction
# def extract_mfcc(filename):
#     y, sr = librosa.load(filename, duration=3, offset=0.5)
#     mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
#     return mfcc
#
# X_mfcc = df['speech'].apply(lambda x: extract_mfcc(x))
#
# X = [x for x in X_mfcc]
# X = np.array(X)
# print(X.shape)
#
# ## Input Split
# X = np.expand_dims(X, -1)
# print(X.shape)
#
# enc = OneHotEncoder()
# y = enc.fit_transform(df[['label']])
# y = y.toarray()
# print(y.shape)
#
# ## Create the LSTM Model
# model = Sequential([
#     LSTM(256, return_sequences=False, input_shape=(40,1)),
#     Dropout(0.2),
#     Dense(128, activation='relu'),
#     Dropout(0.2),
#     Dense(64, activation='relu'),
#     Dropout(0.2),
#     Dense(7, activation='softmax')
# ])
#
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# print(model.summary())
#
# ## Train the model
# history = model.fit(X, y, validation_split=0.2, epochs=50, batch_size=64)
#
