class DNA:#chromosome is a long strand of Dna containing many gene, why we have to start with DNA
    def __init__(self, number=10, mutation):
        self.mutation=[]

class Chromosome (DNA):
    pass

class Genes(Chromosome, DNA):

    def mutation(x, Muta):
        DNA.__init__(muta):
        muta = 0.5
        CHROMO_LEN = 10
        x = ""
        for i in range(CHROMO_LEN):
            if (random.random() < MUTATION_RATE):
             if (x[i] == 1):
                x += 0
            else:
                x += 1
        else:
            x += x[i]
        return x

mutation(.5, 10) 
print(x)