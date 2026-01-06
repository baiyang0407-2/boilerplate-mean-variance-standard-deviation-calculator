import numpy as np

def calculate(list):
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    matrix=np.array(list)
    matrix.shape=(3,3)

    
    sol=dict()
    sol['mean'] = [matrix.mean(0).tolist(),matrix.mean(1).tolist(),np.array(list).mean().tolist()]
    sol['variance'] = [matrix.var(0).tolist(),matrix.var(1).tolist(),np.array(list).var().tolist()]
    sol['standard deviation'] = [matrix.std(0).tolist(),matrix.std(1).tolist(),np.array(list).std().tolist()]
    sol['max'] =[ matrix.max(0).tolist(),matrix.max(1).tolist(),np.array(list).max().tolist()]
    sol['min'] = [matrix.min(0).tolist(),matrix.min(1).tolist(), np.array(list).min().tolist()]
    sol['sum'] = [matrix.sum(0).tolist(),matrix.sum(1).tolist(),np.array(list).sum().tolist()]

    return sol




    




    