__author__ = 'robswift'
__project__ = 'blastnfilter'

import os
from BlastNFilter.PreRelease import ParsePreRelease
from BlastNFilter.Blast import ParseAlignment
import OutPut


def run(options):
    non_polymer = options.non_polymer
    polymer = options.polymer
    out = options.out
    blast_dir = os.path.abspath(options.blast_db)
    pdb_db = os.path.join(blast_dir, 'pdb_db')
    fasta = os.path.join(blast_dir, 'pdb_seqres.txt')

    target_list = ParsePreRelease.add_ligands(non_polymer)
    target_list = ParsePreRelease.add_sequences(polymer, target_list)
    #new = [x for x in target_list if x.get_pdb_id().lower() == '2n02']
    target_list = ParseAlignment.blast_the_targets(target_list, pdb_db, fasta)
    target_list = ParseAlignment.remove_multiple_dockers(target_list)
    OutPut.write_csv(target_list, out)
