# coding: utf-8

from sqlalchemy import create_engine
engine = create_engine('sqlite:///uniprobe.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)
metadata = Base.metadata

from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship, backref

from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)()

import sqlalchemy.types as types


class StrIntBoolean(types.TypeDecorator):

    impl = types.Integer

    def process_bind_param(self, value, dialect):
        return '1' if value else '0'

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        elif value == '1':
            return True
        elif value == '0':
            return False
        else:
            raise None


class Gene(Base):
    __tablename__ = 'genes'

    gene_id = Column(Integer, primary_key=True)
    gene_name = Column(String, ForeignKey('genomic_info.gene_name'))
    species = Column(String, ForeignKey('genomic_info.species'))
    publication_id = Column(Integer, ForeignKey('publications.publication_id'))
    type = Column(String)
    extended_name = Column('gene_id_name', String)

    publication = relationship('Publication', backref=backref('genes'))
    gene_info = relationship('GeneInfo', backref=backref('genes'),
                             primaryjoin='(GeneInfo.gene_name == Gene.gene_name) &\
                                          (GeneInfo.species == Gene.species)')

    def __repr__(self):
        return '<Gene(gene_id=%s, gene_name=%s, species=%s, publication_id=%s)>' %\
            (self.gene_id, self.gene_name, self.species, self.publication_id)


class Contig(Base):
    __tablename__ = 'contigs'

    gene_id = Column(Integer, ForeignKey('genes.gene_id'), primary_key=True)
    kmer = Column(Integer, primary_key=True)
    enrichment_score = Column(Float)

    gene = relationship('Gene', backref=backref('contigs'))

    def __repr__(self):
        return '<Contig(gene_id=%s, kmer=%s, enrichment_score=%s)>' %\
            (self.gene_id, self.kmer, self.enrichment_score)


class Publication(Base):
    __tablename__ = 'publications'

    publication_id = Column(Integer, primary_key=True)
    short_ref = Column('small_ref', String)
    full_ref = Column(String)

    def __repr__(self):
        return '<Publication(publication_id=%s, short_ref=%s)>' %\
            (self.publication_id, self.short_ref)


class GeneInfo(Base):
    __tablename__ = 'genomic_info'

    gene_name = Column(String, primary_key=True)
    name = Column(String)
    synonyms = Column(String)
    species = Column(String, primary_key=True)
    ihop = Column(String)
    uniprot = Column(String)
    refseq_id = Column(String)
    uniq_id = Column(String)
    uniq_id_2 = Column(String)
    jaspar = Column(String)
    description = Column(String)
    domain = Column(String)

    def __repr__(self):
        return '<GeneInfo(gene_name=%s, synonyms=%s, species=%s)>' %\
            (self.gene_name, self.synonyms, self.species)


class GeneData(Base):
    __tablename__ = 'gene_data'

    gene_name = Column(String, primary_key=True)
    species = Column(String, primary_key=True)
    name = Column(String)
    synonyms = Column(String)
    uniprot = Column(String, ForeignKey('genomic_info.uniprot'), index=True)
    fasta = Column(String)
    xdom = Column(String)

    gene_info = relationship('GeneInfo', backref=backref('gene_data',
                                                         uselist=False))

    def __repr__(self):
        return '<GeneData(gene_name=%s, synonyms=%s, species=%s)>' %\
            (self.gene_name, self.synonyms, self.species)
