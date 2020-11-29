import random

import numpy as np


def save_test_labels(labels, dev_acc):
    labels = labels.astype(np.float32) + 1.0
    np.savetxt('output' + str(dev_acc) + '.txt', labels, fmt="%1.1f")
