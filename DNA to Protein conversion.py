#user enters a nucleotide sequence
seq=(input("Enter a DNA sequence: "))

#nucleotide sequence will be converted as list 
dna=list(seq)
print("DNA sequence: ",dna)

#converts the 'T' in the sequence to 'U'
for i in range(len(dna)):
    if dna[i]=='T':
        dna[i]='U'
print("RNA sequence: ",dna)

#joins individual nucleotides together
dna=''.join(dna)

#dna sequence is converted as rna sequence
rna=dna
print("DNA sequence converted as RNA sequence: ",rna)

#defining a dictionary for codons
codon={'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
       'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',}

#splices three nucleotides from the rna sequence and returns the codon value 
for a in range(0,len(rna),3):
    n=rna[a:a+3]
    print(codon[n],end='')