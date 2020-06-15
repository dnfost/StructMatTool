# Want to add classes for a "material" with attributes of all variables in equations below

def strain(elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio):

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

def stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio):

    if(sigma):

        return sigma
    
    elif(elongation and original_length and elastic_modulus):

        return elastic_modulus * strain(elongation, original_length, None, None, None, None, None, None)

    elif(elongation and new_length and elastic_modulus):

        return elastic_modulus * strain(elongation, None, new_length, None, None, None, None, None)

    elif(original_length and new_length and elastic_modulus):

        return elastic_modulus * strain(None, original_length, new_length, None, None, None, None, None)

    elif(force and area):

        return (force / area)

    else:

        print("Not enough information provided to calculate stress.")
        return None

def yield_strength(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio):

    if (elastic_modulus):

        return elastic_modulus * 0.02

    else:

       print("Not enough information provided to calculate yield strength.")
       return None 

def transverse_strain(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio):

    if not poissons_ratio:
        
       print("Not enough information provided to calculate transverse strain.")
       return None

    else:

        if (strain(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio)):

            return -1 * strain(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio) * poissons_ratio

        elif (stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio)):

            return -1 * (1 / stress(epsilon, elongation, original_length, new_length, sigma, force, area, elastic_modulus, poissons_ratio)) * poissons_ratio

if __name__ == "__main__":

    print(yield_strength(None, None, 5, None, None, 30000 * 9.81, 3, 20000000000, None))
