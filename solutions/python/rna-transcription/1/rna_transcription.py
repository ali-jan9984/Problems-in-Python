def to_rna(dna_strand):
    mapping = {"A": "U", "G": "C", "T": "A", "C": "G"}
    return "".join(mapping[n] for n in dna_strand)
