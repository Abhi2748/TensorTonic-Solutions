import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param = np.asarray(param, dtype=float)
    grad  = np.asarray(grad,  dtype=float)
    m     = np.asarray(m,     dtype=float)
    v     = np.asarray(v,     dtype=float)

    # Moment updates (elementwise)
    m_new = beta1 * m + (1.0 - beta1) * grad
    v_new = beta2 * v + (1.0 - beta2) * (grad * grad)

    # Bias correction (t is 1-based)
    beta1_t = beta1 ** t
    beta2_t = beta2 ** t
    m_hat = m_new / (1.0 - beta1_t)
    v_hat = v_new / (1.0 - beta2_t)

    # Parameter update (elementwise)
    param_new = param - lr * m_hat / (np.sqrt(v_hat) + eps)

    return param_new, m_new, v_new