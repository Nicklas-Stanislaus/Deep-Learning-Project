#import numpy as np

def generate_inputs(nonogram_picture):  
    """Function for generating the inputs of a given nonogram. 
    Input can be either numpy array or list.  
    """
    out = []
    for mode in ("rows", "columns"): 
        #If working with columns transpose nonogram picture
        if mode == "columns": 
            nonogram_picture = list(map(list, zip(*nonogram_picture)))
        
        inputs = []
        for line in nonogram_picture:  
            # Create the input for each line
            one_seqs = filter(None, "".join(map(str,line)).split("0"))
            line_input = [len(x) for x in list(one_seqs)]
            
            # Add padding
            inputs.append([0]*(len(line)-len(line_input)) + line_input)
        
        #If working with columns transpose the input back to right dimensions
        if mode == "columns": 
            inputs = list(map(list, zip(*inputs)))
        
        out.append(inputs)
    return np.array(out)