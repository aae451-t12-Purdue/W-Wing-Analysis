

import aerosandbox as ae
import numpy as np


def geo2W_WingCoord(theta1,theta2,L): #assuming same ratio RADIANS
    z_1 = L*(np.cos(theta1))

    y_1 = L*(np.sin(theta1))

    z_2 = L*(np.sin(theta2))

    dfW = np.array([z_1,y_1,z_2])
    return dfW

# 30 < t1 < 90
# 0 t2 < 60

x_trans = geo2W_WingCoord(np.pi/2,np.pi/30, 1)





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
                    chord=0.18,
                    twist=2,  # degrees
                    airfoil=ae.Airfoil(name="naca0003"),
                    control_surface_type='symmetric',
                    # Flap # Control surfaces are applied between a given XSec and the next one.
                    control_surface_deflection=0,  # degrees
                    control_surface_hinge_point=0.75  # as chord fraction
                ),
                ae.WingXSec(  # Mid
                    xyz_le=[0, x_trans[1], 0],
                    chord=0.16,
                    twist=0,
                    airfoil=ae.Airfoil(name="naca0003"),
                    control_surface_type='asymmetric',  # Aileron
                    control_surface_deflection=0,
                    control_surface_hinge_point=0.75
                ),
                ae.WingXSec(  # Tip
                    xyz_le=[0, 1, x_trans[2]],
                    chord=0.08,
                    twist=-2,
                    airfoil=ae.Airfoil(name="naca0003"),
                )
            ]


        )
    ]
)


aero_problem = ae.vlm3( # Analysis type: Vortex Lattice Method, version 3
    airplane=testPlane,
    op_point= ae.OperatingPoint(
        velocity=10,
        alpha=5,
        beta=0,
        p=0,
        q=0,
        r=0,
    ),
)

aero_problem.run()

aero_problem.draw()


