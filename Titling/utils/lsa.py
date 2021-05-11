import numpy as np
from collections import Counter

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import LatentDirichletAllocation
from nltk import tokenize


def modelTopics(data):
   
    l = tokenize.sent_tokenize(data)
    l = np.array(l)
    small_count_vectorizer = CountVectorizer(stop_words='english', max_features=40000)
    # small_text_sample = reindexed_data.sample(n=10000, random_state=0).values
    # small_text_sample = data
#     print('Headline before vectorization: {}'.format(l[1]))
    # print('Headline before vectorization: {}'.format(small_text_sample[1]))

    small_document_term_matrix = small_count_vectorizer.fit_transform(l)

#     print('Headline after vectorization: \n{}'.format(small_document_term_matrix[1]))
    n_topics = 8
    lsa_model = TruncatedSVD(n_components=n_topics)
    lsa_topic_matrix = lsa_model.fit_transform(small_document_term_matrix)

    # Define helper functions
    def get_keys(topic_matrix):
        '''
        returns an integer list of predicted topic 
        categories for a given topic matrix
        '''
        keys = topic_matrix.argmax(axis=1).tolist()
        return keys

    def keys_to_counts(keys):
        '''
        returns a tuple of topic categories and their 
        accompanying magnitudes for a given list of keys
        '''
        count_pairs = Counter(keys).items()
        categories = [pair[0] for pair in count_pairs]
        counts = [pair[1] for pair in count_pairs]
        return (categories, counts)

    lsa_keys = get_keys(lsa_topic_matrix)
    lsa_categories, lsa_counts = keys_to_counts(lsa_keys)

    # Define helper functions
    def get_top_n_words(n, keys, document_term_matrix, count_vectorizer):
        '''
        returns a list of n_topic strings, where each string contains the n most common 
        words in a predicted category, in order
        '''
        top_word_indices = []
        for topic in range(n_topics):
            temp_vector_sum = 0
            for i in range(len(keys)):
                if keys[i] == topic:
                    temp_vector_sum += document_term_matrix[i]
            temp_vector_sum = temp_vector_sum.toarray()
            top_n_word_indices = np.flip(np.argsort(temp_vector_sum)[0][-n:],0)
            top_word_indices.append(top_n_word_indices)   
        top_words = []
        for topic in top_word_indices:
            topic_words = []
            for index in topic:
                temp_word_vector = np.zeros((1,document_term_matrix.shape[1]))
                temp_word_vector[:,index] = 1
                the_word = count_vectorizer.inverse_transform(temp_word_vector)[0][0]
                topic_words.append(the_word.encode('ascii').decode('utf-8'))
            top_words.append(" ".join(topic_words))         
        return top_words
    
    top_n_words_lsa = get_top_n_words(10, lsa_keys, small_document_term_matrix, small_count_vectorizer)

    return top_n_words_lsa
