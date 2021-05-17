# Imports
import pandas as pd

# Gather data and convert to list
data_file = input("Input a data file using PATH (eg: /folder/filename.txt): ")

gene_code = pd.read_csv(str(data_file))

gene_code = list(gene_code)


# Data cleaning function
def clean_data():
    for i in gene_code:
        if len(i) > 3:
            i = i[:-2]


# Finds mutatuions in DNA codon list
def find_mutations_DNA(codon_list):
    item_count = 0
    data_count = 0
    mutation_type = ''

    DNA_codon_p = {'Adenine': 'A', 'Thymine': 'T', 'Guanine': 'G', 'Cytosine': 'C'} # DNA bases
    mRNA_codon_p = {'Uracil': 'U'} # mRNA extra base

    for i in codon_list: # Find abnormalities/mutations
        data_count = data_count + 1
        length = len(i)
        if length > 6:
            mutation_type = f'Extra constituent base found! Codon Pair: {data_count}'
            print(mutation_type)
            item_count = item_count+1
        if i in DNA_codon_p.items():
            item_count = item_count+1
        elif 'U' in i:
            mutation_type = f'mRNA constituent base "Uracil" found! Codon Pair: {data_count}'
            print(mutation_type)
            item_count = item_count+1


# Finds mutatations in mRNA codon list (imported)
def find_mutations_mRNA(codon_list):
    item_count = 0
    data_count = 0
    mutation_type = ''

    DNA_codon_p = {'Thymine': 'T'}
    mRNA_codon_p = {'Adenine': 'A', 'Uracil': 'U', 'Guanine': 'G', 'Cytosine': 'C'} # Reversed DNA codon list minus thymine for uracil as mRNA does not posess thymine

    for i in codon_list: # Find abnormalities/mutations
        data_count = data_count + 1
        length = len(i)
        if length > 6:
            mutation_type = f'Extra constituent base found! Codon Pair: {data_count}'
            print(mutation_type)
            item_count = item_count+1
        if i in mRNA_codon_p.items():
            item_count = item_count+1
        elif 'T' in i:
            mutation_type = f'DNA constituent base "Thymine" found! Codon Pair: {data_count}'
            print(mutation_type)
            item_count = item_count+1


# Run data cleaning
print('Cleaning Data')
clean_data()

processing_type = input('Input codon key name: ') # Ask which function to use based on import

# Find which function to use based on user input
if processing_type == 'DNA':
    print(find_mutations_DNA(gene_code))
elif processing_type == 'mRNA':
    print(find_mutations_mRNA(gene_code))
