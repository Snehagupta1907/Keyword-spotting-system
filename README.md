# Keyword Spotting System

This project involves building a Convolutional Neural Network (CNN) architecture for Keyword Spotting, specifically trained on the Google Speech Commands dataset with an impressive Test Accuracy of 90%. Additionally, the model has been deployed as an API using Flask, and the API has been integrated into a frontend built in ReactJS.

## CNN Architecture

The Convolutional Neural Network is a deep learning model well-suited for audio-related tasks. For keyword spotting, it has proven to be effective in recognizing specific words or phrases within audio clips.

The architecture of the CNN used for this project is as follows:

<img width="334" alt="image" src="https://github.com/Snehagupta1907/Keyword-spotting-system/assets/96808735/7513d568-a67b-44ab-98dd-eb8a071c80cf">

The CNN architecture is designed to extract relevant features from the audio input and learn to differentiate between different keywords.

## Model Performance

The trained CNN has achieved an impressive Test Accuracy of 90% on the Google Speech Commands dataset. The high accuracy is a testament to the effectiveness of the chosen architecture and the quality of the training data.

## API Deployment with Flask

To make the trained model accessible and usable, it has been deployed as an API using Flask. Flask is a popular web framework in Python that allows us to create a simple and efficient API for serving predictions from the model.

With the API, users can send audio clips as requests to the server, and the server will respond with predictions regarding the presence of the specific keyword in the audio.

## Integration with ReactJS Frontend

To provide a user-friendly interface, the API has been integrated with a frontend built in ReactJS. ReactJS is a popular JavaScript library for building interactive user interfaces.

Users can interact with the frontend, record or upload audio clips, and send them to the Flask API for keyword spotting predictions. The results are then displayed back to the user in a user-friendly manner.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the authors of the Google Speech Commands dataset and the open-source community for their contributions to the tools used in this project.
