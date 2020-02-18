

import aerosandbox as ae
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import csv



def geo2W_WingCoord(theta1,theta2,L1,L2): #assuming same ratio RADIANS

    z_1 = ((L1)/(L1 + L2))*(np.cos(theta1)) if L1*(np.cos(theta1)) > 0.01 else 0

    y_1 = ((L1)/(L1 + L2))*(np.sin(theta1)) if L1*(np.sin(theta1)) < 0.99 else 1

    z_2 = ((L2)/(L1 + L2))*(np.sin(theta2)) if  L2*(np.sin(theta2)) > 0.01 else 0

    dfW = np.array([z_1 , y_1, z_2])
    return dfW

# 30 < t1 < 90
# 0 t2 < 60



# t1 = np.linspace(0.5236, 1.56,5)
#
# t2 = np.linspace(0,1.04,5)
#
# # t1,t2, cl, cdi, cl/cdi
#
# sol = pd.DataFrame(columns=['t1','t2','cl','cdi','cl/cdi'])
#
#
# print(sol)


# for i in t1:
#     for j in t2:
#         L1 = 1
#         L2 = 1
#         x_trans = geo2W_WingCoord(i, j, L1, L2)
#         print(x_trans)
#         testPlane = ae.Airplane(
#             name='ju87',
#             xyz_ref=[0, 0, 0],  # CG location
#             wings=[
#                 ae.Wing(
#                     name="Main Wing",
#                     xyz_le=[0, 0, 0],  # Coordinates of the wing's leading edge
#                     symmetric=True,
#                     xsecs=[  # The wing's cross ("X") sections
#                         ae.WingXSec(  # Root
#                             xyz_le=[0, 0, x_trans[0]],
#                             # Coordinates of the XSec's leading edge, relative to the wing's leading edge.
#                             chord=0.2,
#                             twist=0,  # degrees
#                             airfoil=ae.Airfoil(name="naca0003"),
#                             control_surface_type='symmetric',
#                             # Flap # Control surfaces are applied between a given XSec and the next one.
#                             control_surface_deflection=0,  # degrees
#                             control_surface_hinge_point=0.75  # as chord fraction
#                         ),
#                         ae.WingXSec(  # Mid
#                             xyz_le=[0, x_trans[1] / (L1 + L2), 0],
#                             chord=0.2,
#                             twist=0,
#                             airfoil=ae.Airfoil(name="naca0003"),
#                             control_surface_type='asymmetric',  # Aileron
#                             control_surface_deflection=0,
#                             control_surface_hinge_point=0.75
#                         ),
#                         ae.WingXSec(  # Tip
#                             xyz_le=[0, 1, x_trans[2]],
#                             chord=0.2,
#                             twist=0,
#                             airfoil=ae.Airfoil(name="naca0003"),
#                         )
#                     ]
#
#                 )
#             ]
#         )
#
#         aero_problem = ae.vlm3(  # Analysis type: Vortex Lattice Method, version 3
#             airplane=testPlane,
#             op_point=ae.OperatingPoint(
#                 velocity=5,
#                 alpha=5,
#                 beta=0,
#                 p=0,
#                 q=0,
#                 r=0,
#             ),
#         )
#         aero_problem.run()
#         sol = sol.append({'t1' : i, 't2' : j, 'cl' : aero_problem.Cl , 'cdi' : aero_problem.CDi, 'cl/cdi' : (aero_problem.Cl/aero_problem.CDi) }, ignore_index=True)
#         print(aero_problem.Cl)
#         #aero_problem.draw()
#
#
#
#
# print(sol)
#
#
# plt.figure()
# plt.points(sol[t1])

#'t1','t2','cl','cdi','cl/cdi'

CHORD = (0.150/0.300)
x_trans = np.array([0.0669, 0.25,0.1322])
print(CHORD)
print(x_trans)
#
#
testPlane = ae.Airplane(
    name='ju87',
    xyz_ref=[0, 0, 0], # CG location
    wings=[
        ae.Wing(
            name="Main Wing",
            xyz_le=[0, 0, 0], # Coordinates of the wing's leading edge
            symmetric=True,
            xsecs=[# The wing's cross ("X") sections
                ae.WingXSec(  # Root
                    xyz_le=[0, 0, x_trans[0]],  # Coordinates of the XSec's leading edge, relative to the wing's leading edge.
                    chord=CHORD,
                    twist=0,  # degrees
                    airfoil=ae.Airfoil(name="naca4412"),
                    control_surface_type='symmetric',
                    # Flap # Control surfaces are applied between a given XSec and the next one.
                    control_surface_deflection=0,  # degrees
                    control_surface_hinge_point=0.75  # as chord fraction
                ),
                ae.WingXSec(  # Mid
                    xyz_le=[0, x_trans[1], 0],
                    chord=CHORD,
                    twist=0,
                    airfoil=ae.Airfoil(name="naca4412"),
                    control_surface_type='asymmetric',  # Aileron
                    control_surface_deflection=0,
                    control_surface_hinge_point=0.75
                ),
                ae.WingXSec(  # Tip
                    xyz_le=[0, 1, x_trans[2]],
                    chord=CHORD,
                    twist=0,
                    airfoil=ae.Airfoil(name="naca4412"),
                )
            ]


        )
    ]
)


# aero_problem = ae.vlm3( # Analysis type: Vortex Lattice Method, version 3
#     airplane=testPlane,
#     op_point= ae.OperatingPoint(
#         velocity=4.5,
#         alpha=5,
#         beta=0,
#         p=0,
#         q=0,
#         r=0,
#     ),
# )
#
#
#
#
# aero_problem.run()


aleph = np.linspace(0,15,16)
sol = pd.DataFrame(columns=['alpha', 'cl', 'cdi', 'cl/cdi'])

for a in aleph:
    aero_problem = ae.vlm3(  # Analysis type: Vortex Lattice Method, version 3
        airplane=testPlane,
        op_point=ae.OperatingPoint(
            velocity=4.5,
            alpha=a,
            beta=0,
            p=0,
            q=0,
            r=0,
        ),
    )
    aero_problem.run()
    sol = sol.append({'alpha': a, 'cl': aero_problem.Cl, 'cdi': aero_problem.CDi,
                      'cl/cdi': (aero_problem.Cl / aero_problem.CDi)}, ignore_index=True)



print(sol)

plt.figure()

plt.plot(sol['alpha'],sol['cl'])

plt.show()

#aero_problem.draw()


