import sympy
import sympy.vector


R = sympy.vector.CoordSysCartesian('R')

scalar = R.x + R.y + R.z

grad_scalar = sympy.vector.gradient(scalar, R)

print("grad(scalar) = " + str(grad_scalar))

vector = grad_scalar

grad_vector = sympy.vector.gradient(vector, R)

print("grad(vector) = " + str(grad_vector))
