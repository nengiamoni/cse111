import math

# Function to calculate the height of a water column in the tank
def water_column_height(tower_height, tank_height):
    h = tower_height + (3 * tank_height / 4)
    return h

# Function to calculate pressure gain from water height
def pressure_gain_from_water_height(height):
    rho = 998.2  # Density of water in kg/m^3
    g = 9.80665  # Acceleration due to gravity in m/s^2
    P = (rho * g * height) / 1000
    return P

# Function to calculate pressure loss from friction in a pipe
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    rho = 998.2  # Density of water in kg/m^3
    d = pipe_diameter
    L = pipe_length
    f = friction_factor
    v = fluid_velocity
    P = -(f * L * rho * v**2) / (2000 * d)
    return P
import math

# Function to calculate the water pressure lost due to fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    rho = 998.2  # Density of water in kg/m^3
    v = fluid_velocity
    n = quantity_fittings
    P = (-0.04 * rho * v**2 * n) / 2000
    return P

# Function to calculate the Reynolds number for water flow in a pipe
def reynolds_number(hydraulic_diameter, fluid_velocity):
    rho = 998.2  # Density of water in kg/m^3
    d = hydraulic_diameter
    v = fluid_velocity
    mu = 0.0010016  # Dynamic viscosity of water in Pascal seconds
    R = (rho * d * v) / mu
    return R

# Function to calculate pressure loss due to a pipe diameter reduction
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    R = reynolds_number
    D = larger_diameter
    d = smaller_diameter
    k = 0.1 + (50 / R) * (D / d)**4 - 1
    rho = 998.2  # Density of water in kg/m^3
    v = fluid_velocity
    P = (-k * rho * v**2) / 2000
    return P
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()