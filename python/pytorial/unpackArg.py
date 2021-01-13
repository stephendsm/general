#Unpacking the arguments

def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

stephens_data = [37, 20, 0]
health_calculator(stephens_data[0], stephens_data[1], stephens_data[2])#Old fashin ways, it works but
                                                                       #If you have 100 persons, wasting time
#Quicker ways
health_calculator(*stephens_data)#'*' before variable is 'unpacking an argument list'

