import keras
import librosa
import numpy as np

# Load the trained model
model = keras.models.load_model('aelm.keras')

def extract_mfcc(filename):
    y, sr = librosa.load(filename, duration=3, offset=0.5)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
    return mfcc

def predict_emotion(filename):
    mfcc_features = extract_mfcc(filename)
    mfcc_features = mfcc_features.reshape(1, 40, 1)
    prediction = model.predict(mfcc_features)
    emotion_label = np.argmax(prediction)
    return emotion_label

# Usage
filename = 'testing/neutral.wav'
predicted_emotion = predict_emotion(filename)
print(predicted_emotion)
