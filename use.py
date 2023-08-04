
import gzip
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from annoy import AnnoyIndex

class VectorDatabase:
    def __init__(self, n_trees=10):
        self.entries = []
        self.vectorizer = CountVectorizer()
        self.n_trees = n_trees
        self.index = None

    def add_entries(self, entries):
        self._update_vectorizer(entries)
        # Create the Annoy index with the correct dimensionality
        self.index = AnnoyIndex(len(self.vectorizer.vocabulary_))
        for i, entry in enumerate(entries):
            compressed_entry = gzip.compress(pickle.dumps(entry))
            vector = self.vectorizer.transform([entry]).toarray()[0]
            self.entries.append((compressed_entry, vector))
            self.index.add_item(i, vector)
        self.index.build(self.n_trees)


    def _update_vectorizer(self, entries):
        self.vectorizer.fit(entries)

    def _decompress_entry(self, entry):
        decompressed_entry = pickle.loads(gzip.decompress(entry))
        return decompressed_entry

    def search(self, query, n):
        query_vector = self.vectorizer.transform([query]).toarray()[0]
        nearest_indices = self.index.get_nns_by_vector(query_vector, n)
        return [self._decompress_entry(self.entries[i][0]) for i in nearest_indices]
