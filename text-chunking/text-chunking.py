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
    # step = chunk_size - overlap
    # chunks = []
    # i = 0

    # while i < len(tokens):
    #     chunk = list(tokens[i:i + chunk_size])
    #     chunks.append(chunk)

    #     # once we reach (or pass) the end, stop (prevents extra tiny tail chunks)
    #     if i + chunk_size >= len(tokens):
    #         break

    #     i += step

    # return chunks
