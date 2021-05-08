import pandas as pd

gene_code = pd.read_csv('Genetics\Genetic Codes\Code-mRNA.txt', engine='python', delimiter=', ')

gene_code = list(gene_code)


def clean_data():
    for i in gene_code:
        if len(i) > 3:
            i = i[:-2]


def find_mutations_DNA(codon_list):
    item_count = 0
    data_count = 0
    mutation_type = ''

    DNA_codon_p = {'Adenine': 'A', 'Thymine': 'T', 'Guanine': 'G', 'Cytosine': 'C'}
    mRNA_codon_p = {'Uracil': 'U'}

    for i in codon_list:
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


def find_mutations_mRNA(codon_list):
    item_count = 0
    data_count = 0
    mutation_type = ''

    DNA_codon_p = {'Thymine': 'T'}
    mRNA_codon_p = {'Adenine': 'A', 'Uracil': 'U', 'Guanine': 'G', 'Cytosine': 'C'}

    for i in codon_list:
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

print('Cleaning Data')
clean_data()

processing_type = input('Input codon key name: ')

if processing_type == 'DNA':
    print(find_mutations_DNA(gene_code))
elif processing_type == 'mRNA':
    print(find_mutations_mRNA(gene_code))
