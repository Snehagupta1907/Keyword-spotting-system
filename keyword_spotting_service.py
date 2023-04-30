import librosa
import tensorflow as tf
import numpy as np

SAVED_MODEL_PATH = r"C:\Users\win10\Desktop\mlscv-project\model.h5"
SAMPLES_TO_CONSIDER = 22050

class _Keyword_Spotting_Service:
    model = None
    _mapping = [
        "no",
        "right",
        "off",
        "yes",
        "dog",
        "left",
        "bird",
        "go",
        "tree",
        "down",
        "stop",
        "up",
        "happy",
        "cat"
    ]
    _instance = None


    def predict(self, file_path):
        # extract MFCC
        MFCCs = self.preprocess(file_path)
        MFCCs = MFCCs[np.newaxis, ..., np.newaxis]
        # get the predicted label
        predictions = self.model.predict(MFCCs)
        predicted_index = np.argmax(predictions)
        predicted_keyword = self._mapping[predicted_index]
        return predicted_keyword


    def preprocess(self, file_path, num_mfcc=13, n_fft=2048, hop_length=512):

        # load audio file
        signal, sample_rate = librosa.load(file_path)

        if len(signal) >= SAMPLES_TO_CONSIDER:
            # ensure consistency of the length of the signal
            signal = signal[:SAMPLES_TO_CONSIDER]

            # extract MFCCs
            MFCCs = librosa.feature.mfcc(y=signal, sr=sample_rate, n_mfcc=num_mfcc, n_fft=n_fft,
                                        hop_length=hop_length)
        return MFCCs.T


def Keyword_Spotting_Service():
    # ensure an instance is created only the first time the factory function is called
    if _Keyword_Spotting_Service._instance is None:
        _Keyword_Spotting_Service._instance = _Keyword_Spotting_Service()
        _Keyword_Spotting_Service.model = tf.keras.models.load_model(SAVED_MODEL_PATH)
    return _Keyword_Spotting_Service._instance


if __name__ == "__main__":

    # create 2 instances of the keyword spotting service
    kss = Keyword_Spotting_Service()
    kss1 = Keyword_Spotting_Service()

    # check that different instances of the keyword spotting service point back to the same object (singleton)
    assert kss is kss1

    # make a prediction
    keyword = kss.predict(r"C:\Users\win10\Desktop\keyword-spotting-\mlscv-project\speech_commands_test_set_v0.02\down\0c40e715_nohash_0.wav")
    print(keyword)