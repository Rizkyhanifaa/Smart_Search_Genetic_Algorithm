import random
import math

# Fungsi objektif yang ingin diminimalkan
def fitness(x1, x2):
    try:
        f = - (math.sin(x1) * math.cos(x2) * math.tan(x1 + x2) + (3/4) * math.exp(1 - math.sqrt(x1**2)))
        return f
    except:
        return float('inf')  # Hindari nilai tak hingga dari tan()

# Dekode kromosom biner ke nilai nyata di domain [-10, 10]
def decode(chromosome):
    mid = len(chromosome) // 2
    x1_bin = chromosome[:mid]
    x2_bin = chromosome[mid:]
    
    x1 = int(x1_bin, 2) / (2**10 - 1) * 20 - 10
    x2 = int(x2_bin, 2) / (2**10 - 1) * 20 - 10
    return x1, x2

# Inisialisasi populasi awal*
def initialize_population(size):
    population = []
    for _ in range(size):
        chromosome = ''.join(random.choice('01') for _ in range(20))  # Ini bagian acaknya
        population.append(chromosome)
    return population

# Evaluasi fitness dari kromosom
def evaluate(chromosome):
    x1, x2 = decode(chromosome)
    return fitness(x1, x2)

# Pemilihan Orangtua - Metode Tournament selection dengan ukuran 3
def select_parent(population):
    tournament = random.sample(population, 3)  # Ini bagian acaknya
    best = min(tournament, key=evaluate)
    return best

# Crossover satu titik*
def crossover(parent1, parent2, pc):
    if random.random() < pc:
        point = random.randint(1, len(parent1) - 1) # ← Titik crossover acak
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    else:
        return parent1, parent2

# Mutasi flip bit dengan probabilitas pm = 0.1*
def mutate(chromosome, pm):
    mutated = ''
    for bit in chromosome:
        if random.random() < pm: # ← Setiap bit punya peluang 10% diubah (acak)
            mutated += '1' if bit == '0' else '0'
        else:
            mutated += bit
    return mutated

# Algoritma Genetika utama
def genetic_algorithm():
    pop_size = 20
    generations = 100
    pc = 0.8
    pm = 0.1  # Probabilitas mutasi dinaikkan

    population = initialize_population(pop_size)
    best_chrom = min(population, key=evaluate)

    for gen in range(generations):
        new_population = []

        # Elitism: simpan individu terbaik
        new_population.append(best_chrom)

        while len(new_population) < pop_size:
            p1 = select_parent(population)
            p2 = select_parent(population)
            c1, c2 = crossover(p1, p2, pc)
            c1 = mutate(c1, pm)
            c2 = mutate(c2, pm)
            new_population.extend([c1, c2])

        # Hanya ambil jumlah populasi yang sesuai
        population = new_population[:pop_size]

        # Update kromosom terbaik
        current_best = min(population, key=evaluate)
        if evaluate(current_best) < evaluate(best_chrom):
            best_chrom = current_best

    # Decode dan tampilkan hasil terbaik
    x1, x2 = decode(best_chrom)
    print("----- Tugas Searching - Genetic Algorithm -----")
    print("\nKromosom Terbaik:", best_chrom)
    print("\nx1 =", x1, "\nx2 =", x2)
    print("\nFitness =", evaluate(best_chrom))

# Jalankan
genetic_algorithm()
