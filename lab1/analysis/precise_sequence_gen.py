from mpmath import mp

# 1. Set precision to 100 digits 
mp.dps = 100

def get_reference_sequence(x0, k_max):
    seq = [mp.mpf(x0)]
    for _ in range(k_max):
        x = seq[-1]
        next_x = x + mp.mpf(3) * x * (mp.mpf(1) - x)
        seq.append(next_x)
    return [float(val) for val in seq]
