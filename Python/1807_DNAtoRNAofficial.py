def dna_to_rna (dna_strand):
	for n in dna_strand:
		if n == "A":
			print "U"
		elif n == "T":
			print "A"
		elif n == "G":
			print "C"
		elif n == "C":
			print "G"

dna_to_rna (raw_input("Input a strand of DNA"))

