import random
from items import Item

ITEMS=[Item(random.randint(0,20),random.randint(0,20))for x in range(0,20)]

CAPACITY= 10*len(ITEMS)  #bag capacity
POP_SIZE= 30    #solution populaton size
ITER= 1
FITNESS_VALUES={}

def fitness(target):
    total_value=0
    total_weight=0
    index=0
    
    for i in target:
        if index >= len(ITEMS):
            break
        if(i==1):
            total_value +=ITEMS[index].value
            total_weight +=ITEMS[index].weight
        index += 1
        
    if total_weight > CAPACITY:
        return 0
    else:
        return total_value

def mutate(individual):
    r=random.randint(0,len(individual)-1)
    
    if individual[r]==0:
        individual[r]=1
        
    elif individual[r]==1:
        individual[r]=0

def crossover(pop):
    parent_elitizm=0.2
    parent_lenght=int(parent_elitizm*len(pop))

    
#choose best individual
    parents=pop[:parent_lenght]  #chosen
    noparents=pop[parent_lenght:] #not chosen

#choose best individual for roulette
    parents = roulette(FITNESS_VALUES,parent_lenght)
   
#mutation
    mutate(parents[random.randint(0,len(parents)-1)])
    
#new individuals
    children=[]
    desired_lenght=len(pop)-len(parents)
    
    while len(children)<desired_lenght:
        p1=pop[random.randint(0,len(parents)-1)]
        p2=pop[random.randint(0,len(parents)-1)]
        half=len(p1)/2
        child=p1[:int(half)]+p2[:int(half)]
        children.append(child)
    parents.extend(children
    
    return parents    

def roulette(fit_values,parent_L):
    PERCENTS={}
    total_fitness=0
    for i in fit_values:
        total_fitness+=fit_values[i]
    #Percent : fit_values[i]*100/total_fitness
    #best percents for 20 individual
    for i in fit_values:
        PERCENTS[fit_values[i]]=(fit_values[i]*100/total_fitness)
    return choose_parent(PERCENTS,parent_L)

def choose_parent(percents,parent_L):
    PARENTS=[] 
    CHOSEN=[]
    random_number=random.randint(0,100)
    top=100.0
    
    for j in range(0,parent_L): 
        for i in percents:
            if(top-i<random_number):
                PARENTS.append(i)
                percents.pop(i)   
                break
                
            elif(top-i > random_number):
                top-=i
                
    for i in range (0,parent_L):
        for individuals, fit in FITNESS_VALUES.items():  
            if fit == PARENTS[i]:
                CHOSEN.append(individuals)
                
    return CHOSEN   
    

def create_starting_population(amount):

    return [create_individuals()for x in range(0,amount)]

def create_individuals():

    return [random.randint(0,1) for x in range(0,len(ITEMS))]

if __name__ == '__main__':
    population=create_starting_population(POP_SIZE)
    generation=1
    
    for j in range(0,ITER):
        population=sorted(population,key=lambda x:fitness(x),reverse=True)
        for i in population:
                fitness_value = fitness(i)
                print("%s, fit: %s"%(str(i),fitness_value))
                if(j==ITER-1):
                    FITNESS_VALUES[str(i)]=fitness_value   
                    
    population=crossover(population)
    generation +=1
