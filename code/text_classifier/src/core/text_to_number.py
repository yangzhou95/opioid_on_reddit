from core.preprocessor import processor
import dill as dpickle
import numpy as np


class TextToNumber:

    @staticmethod
    def create_number_vector(raw_text_array, append_indicators=True, max_uniqie_words_size=8000, padding_maxlen=70, padding_position='post', output_file='nummerical_text'):
        body_pp = processor(append_indicators=append_indicators, keep_n=max_uniqie_words_size, padding_maxlen=padding_maxlen, padding=padding_position)
        vecs = body_pp.fit_transform(raw_text_array)

        if output_file is not None:
            # Save the preprocessor
            with open(output_file + '_pp.dpkl', 'wb') as f:
                dpickle.dump(body_pp, f)

            # Save the processed data
            np.save(output_file + '_vecs.npy', vecs)

        return vecs

    @staticmethod
    def load_text_processor(fname='title_pp.dpkl'):
        """
        Load preprocessors from disk.
        Parameters
        ----------
        fname: str
            file name of ktext.proccessor object
        Returns
        -------
        num_tokens : int
            size of vocabulary loaded into ktext.processor
        pp : ktext.processor
            the processor you are trying to load
        Typical Usage:
        -------------
        num_decoder_tokens, title_pp = load_text_processor(fname='title_pp.dpkl')
        num_encoder_tokens, body_pp = load_text_processor(fname='body_pp.dpkl')
        """
        # Load files from disk
        with open(fname, 'rb') as f:
            pp = dpickle.load(f)

        num_tokens = max(pp.id2token.keys()) + 1
        # print(f'Size of vocabulary for {fname}: {num_tokens:,}')
        return num_tokens, pp

    @staticmethod
    def load_decoder_inputs(decoder_np_vecs='train_title_vecs.npy'):
        """
        Load decoder inputs.
        Parameters
        ----------
        decoder_np_vecs : str
            filename of serialized numpy.array of decoder input (issue title)
        Returns
        -------
        decoder_input_data : numpy.array
            The data fed to the decoder as input during training for teacher forcing.
            This is the same as `decoder_np_vecs` except the last position.
        decoder_target_data : numpy.array
            The data that the decoder data is trained to generate (issue title).
            Calculated by sliding `decoder_np_vecs` one position forward.
        """
        vectorized_text = np.load(decoder_np_vecs)
        # For Decoder Input, you don't need the last word as that is only for prediction
        # when we are training using Teacher Forcing.
        decoder_input_data = vectorized_text[:, :-1]

        # Decoder Target Data Is Ahead By 1 Time Step From Decoder Input Data (Teacher Forcing)
        decoder_target_data = vectorized_text[:, 1:]

        # print(f'Shape of decoder input: {decoder_input_data.shape}')
        # print(f'Shape of decoder target: {decoder_target_data.shape}')
        return decoder_input_data, decoder_target_data

    @staticmethod
    def load_encoder_inputs(encoder_np_vecs='train_body_vecs.npy'):
        """
        Load variables & data that are inputs to encoder.
        Parameters
        ----------
        encoder_np_vecs : str
            filename of serialized numpy.array of encoder input (issue title)
        Returns
        -------
        encoder_input_data : numpy.array
            The issue body
        doc_length : int
            The standard document length of the input for the encoder after padding
            the shape of this array will be (num_examples, doc_length)
        """
        vectorized_body = np.load(encoder_np_vecs)
        # Encoder input is simply the body of the issue text
        encoder_input_data = vectorized_body
        doc_length = encoder_input_data.shape[1]
        # print(f'Shape of encoder input: {encoder_input_data.shape}')
        return encoder_input_data, doc_length
