import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 253630223 # Ваш chat ID, не меняйте название переменной

def solution(x: int, y: int) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.01
    stat, pval = mannwhitneyu(x, y, alternative='less')
    return pval < alpha
