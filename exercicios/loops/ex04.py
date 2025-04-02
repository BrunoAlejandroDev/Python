
populacao_cidadeA = 80000
taxa_crescimento_cidadeA = 0.03

populacao_cidadeB = 200000
taxa_crescimento_cidadeB = 0.015

anos = 0

while populacao_cidadeA < populacao_cidadeB:
    populacao_cidadeA += populacao_cidadeA * taxa_crescimento_cidadeA
    populacao_cidadeB += populacao_cidadeB * taxa_crescimento_cidadeB
    anos += 1
    
print(f"Serao necessarios {anos} anos para que a populacao do pais A ultrapasse ou iguale a populacao do pais B.")