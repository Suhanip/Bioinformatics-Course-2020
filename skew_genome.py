Genome = "CATGGC"

def Skew(genome):
    skewi = [0]

    for i in range(1, len(genome)):
        skewi.append(skewi[-1])

        if genome[i-1] == 'G':
            skewi[i] = skewi[i-1] + 1
        elif genome[i-1] == 'C':
            skewi[i] = skewi[i-1] - 1
        else:
            skewi[i] = skewi[i-1]
        
    return skewi

print(Skew(Genome))