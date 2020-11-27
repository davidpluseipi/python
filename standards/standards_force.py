# Coding Standards - Force Calculation

# Without Coding Standards
mass = 1  # kg
acceleration = 9.81  # m/s^2
print(mass*acceleration)

print('###########################################################')

# With Coding Standards
# (Note: All units are S.I.)
# mass                  = m (kg)
# gravitational const.  = g (m/s^2)
# force                 = F (N)

# Known quantities
m = 1
a = 9.81

# Force calculation
F = m * a

# Results
print("Resultant force (N):")
print(F)
