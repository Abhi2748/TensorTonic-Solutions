def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size-overlap
    gl = []
    for i in range(0,len(tokens),step):
    #     # ll = []
    #     # end = min(i + chunk_size, len(tokens))
    #     # for j in range(i, end):
    #     #     ll.append(tokens[j])
    #     # gl.append(ll)
        
        gl.append(list(tokens[i:i+chunk_size]))
        if i+chunk_size >= len(tokens):
            break
    
    return gl
