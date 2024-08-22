import numpy as np
 
def compare_vectors(reference_vector, *other_vectors):
...     common_elements_counts = []
...     for vector in other_vectors:
...         common_elements = np.intersect1d(reference_vector, vector)
...         common_elements_counts.append(len(common_elements))
...     return common_elements_counts
common_counts = compare_vectors(x, nonregress_0, nonregress_1, regress_0, regress_1)
