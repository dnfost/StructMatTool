def strain(elongation, original_length, new_length, sigma, force, area, elastic_modulus):

    if(elongation and original_length):

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

def stress(elongation, original_length, new_length, sigma, force, area, elastic_modulus):

    if (elongation and original_length and elastic_modulus):

        return elastic_modulus * strain(elongation, original_length, None, None, None, None, None)

if __name__ == "__main__":

    print(stress(0.02, 2, 2.02, None, None, None, 1600000000))
