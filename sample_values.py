import numpy as np
from effective_hp_per_protections import v_e_hp_30

HEALTH_FLOOR = 850 # A level 5 sol with death's toll
HEALTH_CEIL = 3250 # A level 20 ymir with almost 700 health from items

health_axis = np.linspace(HEALTH_FLOOR, HEALTH_CEIL, 24)

PERCENT_MIT = [0.0,0.02,0.04,0.12]

e_hp_per_prot = []
e_hp_per_prot.append(v_e_hp_30(health_axis, PERCENT_MIT[0]))
e_hp_per_prot.append(v_e_hp_30(health_axis, PERCENT_MIT[1]))
e_hp_per_prot.append(v_e_hp_30(health_axis, PERCENT_MIT[2]))
e_hp_per_prot.append(v_e_hp_30(health_axis, PERCENT_MIT[3]))

# print(e_hp_per_prot)