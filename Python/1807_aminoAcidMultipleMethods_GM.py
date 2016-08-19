#one way

rna_strand = [["UAA"], ["GCU"], ["GAC"], ["UGU"], ["CGC"]]

leucine = ["UAA"]
cysteine = ["UGU"]
alanine = ["GCU"]
aspartic_acid = ["GAC"]
arginine = ["CGC"]

for n in rna_strand:
	if n == leucine:
		print "leucine"
	elif n == cysteine:
		print "cysteine"
	elif n == alanine:
		print "alanine"
	elif n == aspartic_acid:
		print "aspartic acid"
	elif n == arginine:
		print "arginine"

#another way

def rna_to_amino (rna_strand):
	for n in range (0, len(rna_strand), 3):
		codon = rna_strand[n:n+3]
		if codon == "UAA":
			print "leucine"
		elif codon == "UGU":
			print "cysteine"
		elif codon == "GCU":
			print "alanine"
		elif codon == "GAC":
			print "aspartic acid"
		elif codon == "CGC":
			print "arginine"
		else:
			print "error"

rna_to_amino(raw_input("Input RNA strand"))



#another way 


rna_strand = [["UAA"], ["GCU"], ["GAC"], ["UGU"], ["CGC"]]
for n in rna_strand:
	for triplet in n:
		if triplet[0] == "U":
			if triplet[1] == "A":
				if triplet[2] == "A":
					print "leucine"
			elif triplet[1] == "G":
				if triplet [2] == "U":
					print "cysteine"

		elif triplet[0] == "G":
			if triplet[1] == "C":
				if triplet[2] == "U":
					print "alanine"
			elif triplet[1] == "A":
				if triplet[2] == "C":
					print "aspartic acid"


		elif triplet[0] == "C":
			if triplet[1] == "G":
				if triplet[2] == "C":
					print "arginine"
		else:
			print "error"


#another way


RNA = raw_input("Please enter an RNA strand: ")  # prompts user for RNA strand input (example strand: CUCGAACCUUGCAAC )
​
codonList = []  # initializes empty list
​
AminoAcids = [] # initializes empty amino acid list
​
#lists below for each Amino Acid that corresponds to its various potential codons
Leucine_list = ["UUA","UUG", "CUC", "CUU", "CUA", "CUG"]
Phenylalanine_list = ["UUU", "UUC"]
Isoleucine_list = ["AUU", "AUC", "AUA"]
Methionine_list = ["AUG"]
Valine_list = ["GUU", "GUC", "GUA", "GUG"]
Serine_list = ["UCU", "UCC", "UCA", "UCG"]
Proline_list = ["CCU", "CCC", "CCA", "CCG"]
Threonine_list = ["ACU", "ACC", "ACA", "ACG"]
Alanine_list = ["GCU", "GCC", "GCA", "GCG"]
Tyrosine_list = ["UAU", "UAC"]
Stop_list = ["UAA", "UAG"]
Histidine_list = ["CAU", "CAC"]
Gluatmine_list = ["CAA", "CAG"]
Asparagine_list = ["AAU", "AAC"]
Lysine_list = ["AAA", "AAG"]
AsparticAcid_list = ["GAU", "GAC"]
GlutamicAcid_list = ["GAA", "GAC"]
Cysteine_list = ["UGU", "UGC"]
Tryptophan_list = ["UGA", "UGG"]
Arginine_list = ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"]
Serine_list = ["AGU", "AGC"]
Glycine_list = ["GGU", "GGC", "GGA", "GGG"]
​
for i in range(0,len(RNA),3):    # iterating through the length of the RNA strand, in sets of 3
	codon = RNA[i:i+3]   # this will split up the RNA to sets of codons
	if codon in Leucine_list: # conditional statements to check what Amino Acids correspond to the user's codons
		AminoAcids == AminoAcids.append("Leucine") # appends to the empty AminoAcids string
	elif codon in Phenylalanine_list:
		AminoAcids == AminoAcids.append("Phenylalanine")
	elif codon in Isoleucine_list:
		AminoAcids == AminoAcids.append("Isoleucine")
	elif codon in Methionine_list:
		AminoAcids == AminoAcids.append("Methionine")
	elif codon in Valine_list:
		AminoAcids == AminoAcids.append("Valine")
	elif codon in Serine_list:
		AminoAcids == AminoAcids.append("Serine")
	elif codon in Proline_list:
		AminoAcids == AminoAcids.append("Proline")
	elif codon in Threonine_list:
		AminoAcids == AminoAcids.append("Threonine")
	elif codon in Alanine_list:
		AminoAcids == AminoAcids.append("Alanine")
	elif codon in Tyrosine_list:
		AminoAcids == AminoAcids.append("Tyrosine")
	elif codon in Stop_list:
		AminoAcids == AminoAcids.append("Stop")
	elif codon in Histidine_list:
		AminoAcids == AminoAcids.append("Histidine")
	elif codon in Gluatmine_list:
		AminoAcids == AminoAcids.append("Gluatmine")
	elif codon in Asparagine_list:
		AminoAcids == AminoAcids.append("Asparagine")
	elif codon in Lysine_list:
		AminoAcids == AminoAcids.append("Lysine")
	elif codon in AsparticAcid_list:
		AminoAcids == AminoAcids.append("Aspartic Acid")
	elif codon in GlutamicAcid_list:
		AminoAcids == AminoAcids.append("Glutamic Acid")
	elif codon in Cysteine_list:	
		AminoAcids == AminoAcids.append("Cysteine")
	elif codon in Tryptophan_list:
		AminoAcids == AminoAcids.append("Tryptophan")
	elif codon in Arginine_list:
		AminoAcids == AminoAcids.append("Arginine")
	elif codon in Serine_list:	
		AminoAcids == AminoAcids.append("Serine")
	elif codon in Glycine_list:
		AminoAcids == AminoAcids.append("Glycine")
	else: 
		print "invalid codon"  # error check; this will print out if the user enters a nonexistent codon (ex: AAT)
	
print AminoAcids  # prints the final list of the user's corresponding Amino Acids to the screen





