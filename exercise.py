import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt

dev = qml.device('default.qubit', wires=1)
@qml.qnode(dev)
def circuit(phi, theta, omega):
    qml.Rot(phi, theta, omega, wires=0)
    return qml.expval(qml.Hadamard(wires=0))

x_angles = np.linspace(0, 1, 201)
y_angles = np.linspace(0, 2, 401)
data=[]
for x in x_angles:
    for y in y_angles:
        phi=0
        theta=np.pi*x
        omega=np.pi*y
        data.append([circuit(phi,theta,omega), x, y])

data_fig=np.array(data).T
exp=data_fig[0]
x_axis=data_fig[1]
y_axis=data_fig[2]

minimum=min(exp)
print("Ground State Energy: ", minimum)
print("x -> ", x_axis[exp.tolist().index(minimum)],
       " ,  y -> ", y_axis[exp.tolist().index(minimum)])