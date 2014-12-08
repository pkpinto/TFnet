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

Python library that makes the data available to other programs.

## TFnet_MOUSE.ipynb and TFnet_CELEGANS.ipynb

These two notebooks create statistics and TF binding site networks respectivelly
for the mouse and the worm. From the zipped datasets, data is imported into 
pandas DataFrames and number of binding sites studied under different binding 
cutoff values. The specificity of the TF binding site (how many TFs it can bind)
and its average binding strenght are some of the quantities studied.

Additionally, TF binding site networks are created for each of the available 
TFs. Nodes in said network are the binding sites (the kmers) and edges are 
placed between nodes which differ by a single letter. The intention here is to 
understand how TFs can continue to work (binding to something) even when their 
prefered binding site is mutated.

## TFnet_MOUSE_SNP+INDEL.ipynb

Here different binding site mutation processes are compared.

### HTML folder

In the html folder one can find the html version of the notebooks, complete 
with produced figures. Without the database (which is 1.4Gb) there is no way
to reproduce the results currently in all ipython notebooks, hence the html
versions. The individual species notebooks have the code to download zipped
files which contain smaller datasets relative to particular species, but these
files are also quite large (~300Mb).

### Notes

The analysis shown in species notebooks have been automated in independent 
Python programs to accelerate and scale the analysis here introduced.

What is shown here is the exploratory phase of the project. Looking into the 
data, understanding what is and what is not usable and making it available for 
further analysis.
