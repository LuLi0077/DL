# Translation_Chatbot

Train a sequence to sequence model on a dataset of English and French sentences that can translate new sentences from English to French.


A primer - `sequence_to_sequence/sequence_to_sequence.ipynb`: build a model that takes in a sequence of letters, and outputs a sorted version of that sequence.

* Dataset
* Preprocess
* Model
* Train
* Prediction

`language_translation.ipynb`:

* Get the data
* Explore the data
* Preprocess
* Build the Neural Network
	- `model_inputs`
	- `process_decoding_input`
	- `encoding_layer`
	- `decoding_layer_train`
	- `decoding_layer_infer`
	- `decoding_layer`
	- `seq2seq_model`
* Model training
* Translate