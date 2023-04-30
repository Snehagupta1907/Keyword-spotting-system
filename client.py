import requests

# server url
URL = "http://127.0.0.1:5001/predict"


# audio file we'd like to send for predicting keyword
FILE_PATH = r"C:\Users\win10\Downloads\speech_commands_test_set_v0.02\down\0c40e715_nohash_0.wav"


if __name__ == "__main__":
    file = open(FILE_PATH, "rb")
    values = {"file": (FILE_PATH, file, "audio/wav")}
    response = requests.post(URL, files=values)
    data = response.json()

    print("Predicted keyword: {}".format(data["keyword"]))

