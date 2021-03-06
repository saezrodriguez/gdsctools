GDSCTools documentation
===========================

|version|, |today|


.. image:: https://badge.fury.io/py/gdsctools.svg
    :target: https://pypi.python.org/pypi/gdsctools

.. image:: https://secure.travis-ci.org/CancerRxGene/gdsctools.png
    :target: http://travis-ci.org/CancerRxGene/gdsctools

.. image::  https://coveralls.io/repos/CancerRxGene/gdsctools/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/CancerRxGene/gdsctools?branch=master

.. image:: https://badge.waffle.io/CancerRxGene/gdsctools.png?label=Done
   :target: https://waffle.io/CancerRxGene/gdsctools

.. image:: https://readthedocs.io/projects/gdsctools/badge/?version=master
    :target: http://gdsctools.readthedocs.org/en/latest/?badge=master
    :alt: Documentation Status


:Note: tested for Python 2.7, 3.3, 3.4, 3.5
:Source: https://github.com/CancerRxGene/gdsctools


**GDSCTools** is a Python library dedicated to the study of drug responses in the context of the `GDSC (Genomics of Drug Sensitivity in Cancer) <http://www.cancerrxgene.org/>`_ project. It contains utilities to find significant associations between drugs and genomic features (e.g., gene mutation), however, it should be also of interest to a wider community involved in cancer projects.

.. index:: installation

**GDSCTools** is written in Python. If you are a developer and/or knows
already about the Python ecosystem and the **pip** command, just type the following command in a :term:`Terminal` to install **GDSCTools**::

    pip install gdsctools

If you are not familiar with this command, please see the :ref:`Installation` section for further details. Note that some releases of **GDSCTools** are available on `bioconda <bioconda.github.io>`_.

In the following example, we provide a short Python snippet on how to use **GDSCTools** (from a programmer point of view). You can either copy and paste the code in a file, and execute it or type the commands in an IPython shell. With this example we investigate the associations between the :term:`IC50` of a given drug (across 52 breast cancer cell lines) and a genomic feature (here, TP53 mutation):


.. doctest::

    from gdsctools import ANOVA, ic50_test
    gdsc = ANOVA(ic50_test)
    gdsc.set_cancer_type('breast')
    df = gdsc.anova_one_drug_one_feature('Drug_1047_IC50',
        'TP53_mut', show=True)


.. plot::
    :width: 80%

    from gdsctools import ANOVA, ic50_test
    gdsc = ANOVA(ic50_test)
    gdsc.set_cancer_type('breast')
    df = gdsc.anova_one_drug_one_feature('Drug_1047_IC50',
        'TP53_mut', show=True)

The :attr:`df` is a dataframe that contains information explained in :ref:`regression`.


.. seealso:: For more examples and explanations, please visit
    the :ref:`quickstart` section.


.. index:: warnings

The previous example may be verbose with comments and warnings. You may
set the verbose option to False and ignore warnings as follows::

    import warnings
    warnings.simplefilter("ignore","exceptions.Warning")
    gdsc = ANOVA(ic50_test, verbose=False)


.. index:: standalone

The snippets above should be typed within an IPython shell. Although
the code remains simple, nevertheless, we also provide a standalone
application called **gdsctools_anova**, which can be used within a
standard :term:`Terminal` (same output as in the previous example)::

    gdsctools_anova
        --input-ic50 <ic50 filename>
        --drug Drug_1047_IC50
        --feature TP53_mut --onweb


If you want to have a go, please download this
:download:`IC50 example <../../gdsctools/data/test_IC50.csv>`, which is required as an input.

Another data set is required for this analysis, which is a genomic feature file (see :ref:`data`) but it can be replaced by yours. The default data set contains only a small set of genomic features and can be downloaded:
:download:`GenomicFeature example <../../gdsctools/data/genomic_features.tsv.gz>`, and adapted to your needs.


.. seealso:: See :ref:`standalone` section for more details about the
    standalone application and the :ref:`data` section to learn more
    about the expected input data formats.


Contents
============


.. toctree::
    :numbered:
    :maxdepth: 1

    installation.rst
    quickstart.rst
    data.rst
    html.rst
    settings.rst
    results.rst
    data_packages.rst
    notebooks.rst
    standalone.rst
    references.rst
    developers.rst

Issues
===========

Please fill bug report in https://github.com/CancerRxGene/gdsctools/issues

Contributions
================

Please join https://github.com/CancerRxGene/gdsctools

.. toctree::
    :hidden:

    ChangeLog.rst
    faqs
    glossary

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
