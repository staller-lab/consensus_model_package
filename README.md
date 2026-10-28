This is a Python package that is based off of the MADRIGAL consensus activation-domain predictor model developed at Staller Lab.

Credits to Holehouse Lab for development and use of the Parrot package to analyze amino acid data in protein sequences: github.com/idptools/parrot

Developed by Staller Lab. Credits to Claire Josephine LeBlanc, Marissa Ann Zintel, Sanjana R. Kotha, Rishaan J. Bansal. 
https://www.stallerlab.com/

Example Usage:
```
import madrigal_predictor as mp # import the madrigal predictor
import os 

path_fasta = os.path.expanduser("~/Documents/example_fasta.fasta")

# Example: Read a string sequence - outputs likely ADs, unlikely ADs, list of start coordinates, list of end coordinates
ADs, not_ADs, starts, ends = mp.read_sequence("MSEYQPSLFALNPMGFSPLDGSKSTNENVSASTSTAKPMVGQLIFDKFIKTEEDPIIKQDTPSNLDFDFALPQTATAPDAKTVLPIPELDDAVVESFFSSSTDSTPMFEYENLEDNSKEWTSLFDNDIPVTTDDVSLADKAIESTEEVSLVPSNLEVSTTSFLPTPVLEDAKLTQTRKVKKPNSVVKKSHHVGKDDESRLDHLGVVAYNRKQRSIPLSPIVPESSDPAALKRARNTEAARRSRARKLQRMKQLEDKVEELLSKNYHLENEVARLKKLVGER", threshold=0.8)

# Example: Reads a fasta file given a path, outputs lists of titles, likely ADs
titles, all_ADs, all_nots, all_starts, all_ends = mp.analyze_fasta_file(path_fasta, threshold=0.8)
```

