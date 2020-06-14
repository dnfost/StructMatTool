def strain(elongation, original_length, new_length, sigma, elastic_modulus):

    if(elongation and original_length):

        return elongation/original_length

    elif(elongation and new_length):

        return elongation/(new_length - elongation)

    elif(original_length and new_length):

        return (new_length - original_length)/original_length

    elif(sigma and elastic_modulus):

        return sigma/elastic_modulus

    elif(stress):

        strain(None, None, None, stress, elastic_modulus)

    else:

        print("Not enough information provided to calculate strain.")
        return None

if __name__ == "__main__":

    print(strain(None, 2, 2.02, None, None))
