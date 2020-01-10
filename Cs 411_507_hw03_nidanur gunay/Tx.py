import DS
import Phase1_Test
import random
#Transaction informations
q,p,g=Param_Generator(224,2048)


def gen_random_tx(q,p,g):
    serialno = random.randrange(2 ** (7 - 1), 2 ** 7 - 1)
    a = int(input("Pick a random secret key between 0 - " + str(q - 1) + ":\n"))
    payerbeta = Key_generation(g, a, p)
