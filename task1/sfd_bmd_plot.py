import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('SFS_Screening_SFDBMD.csv')
x = df["Distance (m)"].to_numpy()
shear = df["SF (kN)"].to_numpy()
moment = df["BM (kN-m)"].to_numpy()

fig, (ax_bmd, ax_sfd) = plt.subplots(1, 2, figsize=(14, 6))

ax_bmd.plot(x, moment, color='red')
ax_bmd.fill_between(x, moment, alpha=0.1, color='red', hatch='|||', edgecolor='red')
ax_bmd.set_title("Bending Moment Diagram")
ax_bmd.set_xlabel("Length (m)")
ax_bmd.set_ylabel("Moment (kN-m)")
ax_bmd.grid(True)

min_m_idx = np.argmin(moment)
max_m_idx = np.argmax(moment)
ax_bmd.annotate(f"Min: {moment[min_m_idx]:.2f} kN-m", 
                (x[min_m_idx], moment[min_m_idx]),
                textcoords="offset points", xytext=(0, -30), ha='center')
ax_bmd.annotate(f"Max: {moment[max_m_idx]:.2f} kN-m", 
                (x[max_m_idx], moment[max_m_idx]),
                textcoords="offset points", xytext=(0, 15), ha='center')

ax_sfd.plot(x, shear, color='blue')
ax_sfd.fill_between(x, shear, alpha=0.1, color='blue', hatch='|||', edgecolor='blue')
ax_sfd.set_title("Shear Force Diagram")
ax_sfd.set_xlabel("Length (m)")
ax_sfd.set_ylabel("Shear (kN)")
ax_sfd.grid(True)

min_s_idx = np.argmin(shear)
max_s_idx = np.argmax(shear)
ax_sfd.annotate(f"Min: {shear[min_s_idx]:.2f} kN", 
                (x[min_s_idx], shear[min_s_idx]),
                textcoords="offset points", xytext=(0, -30), ha='center')
ax_sfd.annotate(f"Max: {shear[max_s_idx]:.2f} kN", 
                (x[max_s_idx], shear[max_s_idx]),
                textcoords="offset points", xytext=(0, 15), ha='center')


plt.tight_layout()
plt.savefig("sfd_bmd_diagram.png", dpi=300)
plt.show()
