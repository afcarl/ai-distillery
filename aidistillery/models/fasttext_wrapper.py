import logging
from gensim.models import fasttext
from aidistillery import file_handling

class FastTextWrapper:
    def __init__(self, sentences, use_bf = True, dimension=100, window=5, min_count=5, workers=4, sg=0, iterations=5,
                 type="fasttext", dataset = ""):
        logging.info("FastText Wrapper Initialized")
        self.sentences = sentences
        self.type = type
        self.dataset = dataset
        self.use_bf = use_bf
        self.dimension = dimension
        self.window = window
        self.min_count = min_count
        self.workers = workers
        self.sg = sg
        self.iterations = iterations

    def fit(self):
        model = fasttext.FastText(self.sentences,
            size=self.dimension,
            window=self.window,
            min_count=self.min_count,
            workers=self.workers,
            sg=self.sg,
            iter=self.iterations)

        if not self.use_bf:
            return model
        else:
            bf_format = file_handling.BF().load_from_gensim(model)
            return bf_format


