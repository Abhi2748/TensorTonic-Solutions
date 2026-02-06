import math
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    dot_product = sum(a*b for a,b in zip(x1,x2))

    norm_x1 = math.sqrt(sum(a*a for a in x1))
    norm_x2 = math.sqrt(sum(a*a for a in x2))

    cosine_similarity = dot_product/(norm_x1 * norm_x2)

    if label == 1:
        return 1- cosine_similarity
    elif label == -1:
        return max(0,cosine_similarity - margin)