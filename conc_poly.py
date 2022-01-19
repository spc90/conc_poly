import numpy as np
import matplotlib.pyplot as plt

def poly_circ(n, r, ax):
  t = np.arange(0, 2*np.pi, 0.01)
  x = r * np.sin(t)
  y = r * np.cos(t)
  ax.plot(x, y, 'r', solid_capstyle='round')
  
  r *= 1./np.cos(np.pi/n)
  
  x = np.empty(n+1)
  y = np.empty(n+1)
  x[0], y[0] = 0, r
  for i in range(n):
    x[i+1] = r * np.sin(2.*np.pi*(i+1.)/n)
    y[i+1] = r * np.cos(2.*np.pi*(i+1.)/n)
  ax.plot(x, y, 'k', solid_capstyle='round')
  
  return r

# Make a content only 
fig = plt.figure(frameon=False, figsize=(6., 6.))
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

# Plot the polygons and circles
rad = 1.
start_i = 3
end_i = 100
for i in range(start_i,end_i+1):
  rad = poly_circ(i,rad,ax)

# Save to file...
ax.autoscale(tight=True)
fig.savefig('conc_poly_{}-{}.svg'.format(start_i,end_i),
  transparent=True)

# ...and also show
plt.show()
