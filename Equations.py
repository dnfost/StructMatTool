# Want to add classes for a "material" with attributes of all variables in equations below

def strain(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal):

    if(epsilon):

        return epsilon

    elif(elongation and original_length):

        return elongation/original_length

    elif(elongation and new_length):

        return elongation/(new_length - elongation)

    elif(original_length and new_length):

        return (new_length - original_length)/original_length

    elif(sigma and elastic_modulus):

        return sigma/elastic_modulus

    elif(force and area and elastic_modulus):

        return force/(area * elastic_modulus)

    elif(stress):

        return stress/elastic_modulus

    else:

        print("Not enough information provided to calculate strain.")
        return None

def stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal):

    if(sigma):

        return sigma
    
    elif(elongation and original_length and elastic_modulus):

        return elastic_modulus * strain(elongation, original_length, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

    elif(elongation and new_length and elastic_modulus):

        return elastic_modulus * strain(elongation, None, new_length, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

    elif(original_length and new_length and elastic_modulus):

        return elastic_modulus * strain(None, original_length, new_length, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

    elif(force and area):

        return (force / area)

    else:

        print("Not enough information provided to calculate stress.")
        return None

def yield_strength(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal):

    if (elastic_modulus):

        return elastic_modulus * 0.02

    else:

       print("Not enough information provided to calculate yield strength.")
       return None 

def transverse_strain(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal):

    if not poissons_ratio:
        
       print("Not enough information provided to calculate transverse strain.")
       return None

    else:

        if (strain(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal)):

            return -1 * strain(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal) * poissons_ratio

        elif (stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal)):

            return -1 * (1 / stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal)) * poissons_ratio

        else:

            print("Not enough information provided to calculate transverse strain.")
            return None

def shear_stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal): 

    if (tau):

        return tau
    
    elif (shear_force and area):

        return shear_force / area

    elif (gamma and shear_modulus):

        return gamma * shear_modulus

    else:

       print("Not enough information provided to calculate shear stress.")
       return None

def shear_modulus_isotropic(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal):

    if not (if_isotropic):

        print("No data currently available to calculate shear modulus.")

    else:

        if (elastic_modulus and poissons_ratio):

            return elastic_modulus / (2 * (1 + poissons_ratio))

        else:

            print("Not enough information provided to calculate shear modulus.")
            return None

def biaxial_strain_x(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal):

    if not poissons_ratio:

        print("Not enough information provided to calculate biaxial strain in loading direction.")
        return None

    else:

        if (elastic_modulus and strain(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal)):

            return (strain(epsilon, elongation, original_length, new_length, sigma_x, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal) - transverse_strain(epsilon, elongation, original_length, new_length, sigma_y, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal))

        else:

            print("Not enough information provided to calculate biaxial strain in loading direction.")
            return None

def biaxial_strain_y(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal):

    if not poissons_ratio:

        print("Not enough information provided to calculate biaxial strain in tranverse direction.")
        return None

    else:

        if (elastic_modulus and strain(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal)):

            return (strain(epsilon, elongation, original_length, new_length, sigma_y, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal) - transverse_strain(epsilon, elongation, original_length, new_length, sigma_x, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal))

        else:

            print("Not enough information provided to calculate biaxial strain in loading direction.")
            return None

def thermal_strain(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal, delta_temp):

    if not (coeff_thermal and delta_temp):

        print("Not enough information provided to calculate thermal strain.")
        return None

    else:

        return coeff_thermal * delta_temp

def rho_of_mixtures(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal, delta_temp, rho_fibre, vol_fibre, rho_matrix, vol_matrix):

    if not (rho_fibre and vol_fibre and rho_matrix and vol_matrix):

        print("Not enough information provided to calculate density of composite.")
        return None

    else:

        return (rho_fibre * vol_fibre + rho_matrix * rho_matrix)

def mod_of_mixtures(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal, delta_temp, rho_fibre, vol_fibre, mod_fibre, rho_matrix, vol_matrix, mod_matrix):

    if not (mod_fibre and mod_matrix and vol_fibre):

        print("Not enough information provided to calculate elastic modulus of composite.")
        return None

    else:

        return (mod_fibre * vol_fibre + (1 - vol_fibre) * mod_matrix)

def hoop_stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal, delta_pressure, radius, thickness):

    if not (delta_pressure and radius and thickness):

        print("Not enough information provided to calculate hoop stress.")
        return None

    else:

        return (delta_pressure * radius) / thickness

def long_stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal, delta_pressure, radius, thickness):

    if not (hoop_stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal, delta_pressure, radius, thickness)):

        print("Not enough information provided to calculate hoop stress.")
        return None

    else:

        return (hoop_stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio, tau, shear_force, gamma, shear_modulus, if_isotropic, sigma_x, sigma_y, coeff_thermal, delta_pressure, radius, thickness) * 0.5)       