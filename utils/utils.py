from scipy.stats import shapiro, spearmanr
import scipy.stats as stats

def normality_check(data, features):
    normality_results = {}
    
    for feature in features:
        stat, p = stats.shapiro(data[feature])
        normality_results[feature] = 'Normal' if p >= 0.05 else 'Not Normal'
    
    return normality_results

def bootstrap_spearman(data, n_iterations, n_size):
    spearman_coefficients = []
    for _ in range(n_iterations):
        sample = data.sample(n=n_size, replace=True)
        corr, _ = spearmanr(sample['sulphates'], sample['quality_good_bad'])
        spearman_coefficients.append(corr)
    return spearman_coefficients