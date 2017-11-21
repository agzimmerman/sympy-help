import sympy
import sympy.physics
import sympy.physics.vector


R = sympy.physics.vector.ReferenceFrame('R')

scalar = R[0] + R[1] + R[2]

grad_scalar = sympy.physics.vector.gradient(scalar, R)

print("grad(scalar) = " + str(grad_scalar))

vector = grad_scalar

grad_vector = sympy.physics.vector.gradient(vector, R)

print("grad(vector) = " + str(grad_vector))
