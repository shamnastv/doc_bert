import random

import numpy as np


def save_test_labels(labels):
    labels = labels.astype(np.float32) + 1.0
    np.savetxt('output' + str(random.randint(0, 100)) + '.txt', labels, fmt="%1.1f")
