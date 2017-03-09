import random

from abc import ABCMeta
from population import *

class Chromosome(metaclass=ABCMeta):
    """A generic chromosome class for genetic algorithms.
    The population is made up of these. These, in turn, are made up of genes, which can be in a series of different
    states, or alleles. The genes are actually stored as a bignum for efficiency reasons, but there are plenty
    of functions to abstract that away if you don't want to deal with it.
    """
    
    # The bignum containing the allelles for the chromosome.
    _genes = 0

    # The population the chromosome belongs to.
    parent = None

    def __init__(self, new_parent: Population, new_genes: int = 0) -> Chromosome:
        """Creates a new chromosome object.

        :param new_parent: The population the chromosome should belong to.
        :param gene_set: The set of genes to initialize the chromosome with. Can be omitted.
        """

        self.parent = new_parent
        self.set_genes(gene_set)

    def set_genes(self, gene_set: int):
        """Sets the genes of the chromosome.

        :param geneSet: A mutable bitSet representing the genes of the chromosome.
        :throws IllegalArgumentException: if the new gene set is too high for the gene count dictated by the population.
        """
        if len(gene_set) > parent.gene_count:
            raise ValueError("Invalid gene set for chromosome.")
        self._genes = gene_set

    def get_genes(self) -> int:
        """Returns the genes as an integer."""
        return self._genes

    def gene_at(self, index: int) -> bool:
        """Returns the allele of the gene at the specified index.

        :param index: The index of the gene to be returned.
        :return: The allele of the gene at the specified index.
        """
        
        return bool(genes & (1 << index))

    def ux(self, other: Chromosome) -> (Chromosome, Chromosome):
        #TODO
        pass

    def mutate(self):
        """Mutates the chromosome according to the parent population's mutation chance."""

        newGenes = self.genes
        for i in range(parent.gene_count):
            if (random.random() > parent.mutate_chance):
                self.genes ^= 1 << i
                