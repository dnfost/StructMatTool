def strain(elongation, original_length, sigma, elastic_modulus):

    if(elongation and original_length):

        return elongation/original_length

    else if(sigma and elastic_modulus):

        return sigma/elastic_modulus

    else:

        print("Not enough information provided to calculate strain.")
