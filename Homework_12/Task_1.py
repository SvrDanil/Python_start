from sympy import *
x = Symbol("x")
fx = x**3 - 50*x
gx = -x**4 + 88*x**2 - 241
fgx = fx - gx

roots = solve(fgx)
roots

cross_dict = {}
c = 1 
for z in roots:
    cross_dict[c] = {"x": round(N(z),5), "y": round(N(-1*z**4 - 88*z**2-241),5)}
    c+=1
cross_dict


plot(fx,gx,x)

plot(fgx,x)

p = plot(fx,gx,fgx,show = false)
p[2].line_color = 'r'
p.show()