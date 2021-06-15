# Imports
import pandas as pd
from pandas.io import parsers

data_file = input("Input a data file using PATH (eg: /folder/filename.txt): ")

gene_code = pd.read_csv(str(data_file))

gene_code = list(gene_code)

inp_new = []


# Find mutation functions
def find_mutations_DNA(codon_list):
    item_count = 0
    data_count = 0
    mutation_type = ''

    DNA_codon_p = {'Adenine': 'A', 'Thymine': 'T', 'Guanine': 'G', 'Cytosine': 'C'}

    for i in codon_list:
        data_count = data_count + 1
        length = len(i)
        if length > 6:
            mutation_type = f'Insertion instance detected! Codon Pair {data_count} has been affected.'
            print(mutation_type)
            item_count = item_count+1
        elif length < 3:
            mutation_type = f'Deletion instance detected! Codon pair {data_count} has been affected.'
            print(mutation_type)
            item_count = item_count + 1
        if i in DNA_codon_p.items():
            item_count = item_count+1
        elif 'U' in i:
            mutation_type = f'mRNA constituent base "Uracil" found! Codon Pair {data_count} has been affected.'
            print(mutation_type)
            item_count = item_count+1
        else:
            return 'No Issues Found'


def find_mutations_mRNA(codon_list):
    item_count = 0
    data_count = 0
    mutation_type = ''

    mRNA_codon_p = {'Adenine': 'A', 'Uracil': 'U', 'Guanine': 'G', 'Cytosine': 'C'}

    for i in codon_list:
        data_count = data_count + 1
        length = len(i)
        if length > 6:
            mutation_type = f'Extra constituent base found! Codon Pair: {data_count} has been affected.'
            print(mutation_type)
            item_count = item_count+1
        elif length < 3:
            mutation_type = f'Deletion instance detected! Codon pair {data_count} has been affected.'
            print(mutation_type)
            item_count = item_count + 1
        if i in mRNA_codon_p.items():
            item_count = item_count+1
        elif 'T' in i:
            mutation_type = f'DNA constituent base "Thymine" found! Codon Pair: {data_count} has been affected.'
            print(mutation_type)
            item_count = item_count+1
        else:
            return 'No Issues Found'


def parse_code_DNA():
    global inp_new
    input = gene_code
    input = str(input[0])
    inp_new = []
    for index in range(0, len(str(input)), 1):
        inp_new.append(str(input)[index : index + 1])
    print(transcribe_Info('d_m'))


def parse_code_mRNA():
    global inp_new
    input = gene_code
    input = str(input[0])
    inp_new = []
    for index in range(0, len(str(input)), 1):
        inp_new.append(str(input)[index : index + 1])
    print(transcribe_Info('m_d'))


# Transcription functions
def transcribe_Info(type):
    new_info = []
    info = inp_new
    if type == 'm_d':

        data_types = {'A': 'A', 'U': 'T', 'C': 'C', 'G': 'G'}
            
        for i in info:
            i = data_types[i]
            new_info.append(i)

        print(''.join([i for i in new_info]))

    elif type == 'd_m':

        data_types = {'A': 'A', 'T': 'U', 'C': 'C', 'G': 'G'}

        for i in info:
            i = data_types[i]
            new_info.append(i)

        print(''.join([i for i in new_info]))

    return 0


# Process chosing code
processing_type = input('Input codon key name: ')

if processing_type == 'DNA':
    print(find_mutations_DNA(gene_code))
elif processing_type == 'mRNA':
    print(find_mutations_mRNA(gene_code))
elif processing_type == 'DNA_C':
    print(parse_code_DNA())
elif processing_type == 'mRNA_C':
    print(parse_code_mRNA())
