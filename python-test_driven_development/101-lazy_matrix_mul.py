#!/usr/bin/python3
"""matrix multiplication module"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiply two matrices"""
    return np.matmul(m_a, m_b)
