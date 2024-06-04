import numpy as np


START_FLANK = 500
END_FLANK = 100

def get_tss_start(gene_row):
    if gene_row['strand'] == '+':
        return gene_row['start'] - START_FLANK
    else:
        return gene_row['end'] - END_FLANK # (1) replaced with (2) to make  it ordered

def get_tss_end(gene_row):
    if gene_row['strand'] == '+':
        return gene_row['start'] + END_FLANK
    else:
        return gene_row['end'] + START_FLANK # (2) replaced with (1) to make it ordered

def get_genes_list(xs):
    xs = list(xs)
    return list(set([x for x in xs if x is not None]))

def impute_nans(matrix):
    '''
    This function is used to impute some NaNs for 
    a bit more pretty Hi-C maps visualization

    ::warning:: Only for visualization!!
    '''
    for i in range(matrix.shape[0]):
        raw_matrix = matrix.copy()
        for j in range(matrix.shape[1]):
            if np.isnan(matrix[i,j]):
                neighbors = []
                for x in range(max(0,i-1), min(matrix.shape[0],i+2)):
                    for y in range(max(0,j-1), min(matrix.shape[1],j+2)):
                        if not np.isnan(matrix[x,y]) and (x,y) != (i,j):
                            neighbors.append(matrix[x,y])
                if len(neighbors) == 8:
                    matrix[i,j] = np.mean(neighbors)
                elif not (np.all(np.isnan(raw_matrix[:, i])) or np.all(np.isnan(raw_matrix[:, i]))):
                    matrix[i,j] = 0
                    
    return matrix