import numpy as np

def effective_hp (protections, hp, percent_mitigation):
    return (hp * (100 + protections)) / (100 * (1 - percent_mitigation))

def effective_hp_per_protection (hp, percent_mitigation):
    return hp / (100 * (1 - percent_mitigation))
v_e_hp = np.vectorize(effective_hp_per_protection)