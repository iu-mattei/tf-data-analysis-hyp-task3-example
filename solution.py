import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 253630223 # Ваш chat ID, не меняйте название переменной

def solution(x: int, y: int) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.01
    stats, pval = stats.ttest_ind(x, y)
    return pval <= alpha
