TFnet
=====

There are several notebooks in this folder. They were created to do preliminary 
studies on the transciptor factor (TF) binding site data of the Uniprobe 
database. Uniprobe contains data on 21 species (with different kinds of 
coverage). This data consists of the binding streght of a TF to all kmers of 
length 8. The data is available as a mySQL dump (complete dataset) or as zipped 
files containing partial dataset (including only specific species and/or TFs).

## uniprobe_data.ipynb

The SQL dump is provided without any ER diagram or documentation. This notebook 
imports the database (after conversion into a SQLite database) for exploratory 
discovery and conversion to a more intelligible format. Some preprocessing is 
done directly in SQL (stuff like merging identical tables and such). Data which 
does not fit our needs (e.g. TF complexed with proteins) was also selected and 
discarded.

## uniprobe_data.py

Python library that makes the database available to other programs. Use with
```python
from uniprobe_data import *
```

## Other notebooks

Additionally, other notebooks are dedicated to more detailed analysis.

#### bind_graphs.ipynb

Study the TF binding sites per TF. Create binding sites networks for each of
the TFs. Do TF pair-wise comparisons of the sets of binding sites.

#### uniprot_seq.ipynb

For the TF in the Uniprobe database, mine Uniprot and PFAM for sequence and 
domain data and add it to the database. Make TF pair-wise comparisons.

#### clustering.ipynb

Cluster TFs according to pairwise comparison statistics: binding site sets
similarity, sequence similarity and BLAST score and domain content.

## Notes

What is shown here is the exploratory phase of the project. Looking into the 
data, understanding what is and what is not usable and making it available for 
further analysis.
