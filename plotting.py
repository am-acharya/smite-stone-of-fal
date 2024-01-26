import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from sample_values import health_axis, e_hp_per_prot

x = health_axis
a = e_hp_per_prot[0] # effective hp gained per protection and no %mitigation
b = e_hp_per_prot[1] # effective hp gained per protection after 1 basic attack
C = e_hp_per_prot[2] # effective hp gained per protection after 2 basic attacks
D = e_hp_per_prot[3] # effective hp gained per protection after 3 basic attacks

plt.plot(x,a, 'm-.', x, b, 'c:', x, C, 'b--', x, D, 'r-')
plt.xlabel('Total Current HP', color='#1e8bc3')
plt.ylabel('Effective HP gained per 30 Protections', color='#e74c3c')
plt.title('Impact of Stone of Fal on the Efficiency of Protections Purchased', color='#34495e')
legends = [
    mpatches.Patch(color='magenta', label='0% Mitigation'),
    mpatches.Patch(color='cyan', label='One Basic'),
    mpatches.Patch(color='blue', label='Two Basics'),
    mpatches.Patch(color='red', label='Three Basics'),
    ]
plt.legend(handles=legends)
plt.show()
