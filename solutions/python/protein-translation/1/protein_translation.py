CODON_TABLE = {
'AUG': 'Methionine',
'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
'UUA': 'Leucine', 'UUG': 'Leucine',
'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
'UGU': 'Cysteine', 'UGC': 'Cysteine',
'UGG': 'Tryptophan',
}
STOP_CODONS = {'UAA', 'UAG', 'UGA'}


def proteins(strand):
    rna = strand.upper().strip()
    proteins = []
    for i in range(0,len(rna)+1,3):
        if len(rna) < i:
            break
        codon = rna[i:i+3]
        if codon in STOP_CODONS:
            return proteins
        if codon in CODON_TABLE:
            proteins.append(CODON_TABLE[codon])            
    return proteins