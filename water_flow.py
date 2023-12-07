# water_flow.py

def water_column_height(tower_height, tank_height):
    h = tower_height + (3 * tank_height / 4)
    return h

def pressure_gain_from_water_height(height):
    density_water = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    pressure = (density_water * gravity * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density_water = 998.2  # kg/m^3
    pressure_loss = (-friction_factor * pipe_length * density_water * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density_water = 998.2  # kg/m^3
    pressure_loss_fittings= (-0.04*density_water*fluid_velocity**2*quantity_fittings)/2000
    return pressure_loss_fittings

def reynolds_number(hydraulic_diameter, fluid_velocity):
    density_water = 998.2  # kg/m^3
    dynamic_viscosity_of_water=0.0010016 #Pascal seconds
    Reynolds_number_for_pipe=(density_water*hydraulic_diameter*fluid_velocity)/dynamic_viscosity_of_water
    return Reynolds_number_for_pipe

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k = (0.1 +(50/reynolds_number))*((larger_diameter/smaller_diameter)**4-1)
    pressure = (-k *998.2 * fluid_velocity ** 2) / 2000
    return pressure

# I exceed the requiremnt and write this new function 
#def psi_to_kpa(psi):
    return psi * 6.89476  # 1 psi = 6.89476 kPa
#pressure_psi = psi_to_kpa(pressure)
#print(f"Pressure at house: {pressure:.1f} kilopascals ({pressure_psi:.1f} psi)")

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