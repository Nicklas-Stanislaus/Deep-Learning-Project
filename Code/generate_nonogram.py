import numpy as np
def generate_nonogram(d_i = 0.2, d_v = 0.3, d_h = 0.3, columns=5, rows = 5, sim_number = 1):
    '''
    generate fixed size nonograms
    
    d_i  = overall accept rate
    d_h = extra acceptrate if left cell is occupied.
    d_v = extra acceptrate if above cell is occupied.
    '''
    n_nonograms = []
    for _ in range(sim_number):
        nonogram = []
        for i in range(rows):
            row = []
            left = False
            for j in range(columns):
                r = d_i
                if i != 0 and last_row[j] == 1:
                    r += d_v  
                if left:
                    r += d_h
                var = np.random.rand()
                
                if var < r: 
                    row.append(1)
                    left = True 
                else:
                    row.append(0)
                    left = False
                    
            nonogram.append(row)
            last_row = row
        n_nonograms.append(nonogram)
    return np.array(n_nonograms)