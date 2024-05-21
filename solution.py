import pandas as pd
import numpy as np
import scipy.stats as sps


chat_id = 1260358058 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.06
    pvalue = sps.epps_singleton_2samp(x, y).pvalue
    return pvalue < alpha
