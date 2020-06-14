def strain(elongation, original_length, sigma, elastic_modulus):

    if(elongation and original_length):

        return elongation/original_length

    elif(sigma and elastic_modulus):

        return sigma/elastic_modulus

    elif(stress):

        return stress/elastic_modulus

    else:

        print("Not enough information provided to calculate strain.")
        return 0

if __name__ == "__main__":

    print(strain(2, 1000, None, None))
