===============================
Drug Design Data Resource BlastNFilter
===============================

.. image:: https://img.shields.io/travis/rvswift/BlastNFilter.svg
        :target: https://travis-ci.org/rvswift/BlastNFilter

.. image:: https://img.shields.io/pypi/v/BlastNFilter.svg
        :target: https://pypi.python.org/pypi/BlastNFilter


BlastNFilter processes the  weekly PDB prerelease files, new_release_structure_nonpolymer.tsv and
new_release_structure_sequence.tsv, removes entries bound to undesirable ligands, and BLASTS the remaining sequences.
Those wwpdb structures whose sequences are sufficiently similar to the input sequence are returned, sorted by
resolution, and stored in an csv file for later processing

* Free software: BSD license
* Documentation: https://BlastNFilter.readthedocs.org.

Features
--------

* TODO

Installation
------------

Pip install is coming, but in the meantime:

.. code:: bash

  git clone https://github.com/nbcrrolls/BlastNFilter
  cd BlastNFilter
  make install

Usage
-----


