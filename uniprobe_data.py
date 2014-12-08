# coding: utf-8

from sqlalchemy import create_engine
engine = create_engine('sqlite:///uniprobe_data.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship, backref

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
            raise 'invalid value %s' % value


class Gene(Base):
    __tablename__ = 'gene_ids'

    gene_id = Column(Integer, primary_key=True)
    gene_name = Column(String)
    species = Column(String)
    publication_id = Column(Integer)
    type = Column(String)
    is_complex = Column(Boolean)
    gene_id_name = Column(String)
    has_pbm_data = Column(StrIntBoolean)

    def __repr__(self):
        return '<Gene(gene_id=%s, gene_name=%s, species=%s, publication_id=%s)>' \
            % (self.gene_id, self.gene_name, self.species, self.publication_id)


class Contig(Base):
    __tablename__ = 'contig_8mers_0'

    gene_id = Column(Integer, ForeignKey('gene_ids.gene_id'), primary_key=True)
    kmer = Column(Integer, primary_key=True)
    enrichment_score = Column(Float)

    gene = relationship('Gene', backref=backref('contigs'))

    def __repr__(self):
        return '<Contig(gene_id=%s, kmer=%s, enrichment_score=%s)>' \
            % (self.gene_id, self.kmer, self.enrichment_score)


class Publication(Base):
    __tablename__ = 'publication_ids'

    publication_id = Column(Integer, ForeignKey('gene_ids.publication_id'),
                            primary_key=True)
    small_ref = Column(String)
    full_ref = Column(String)
    folder_name = Column(String)
    is_bulyklab = Column(String)
    in_TFBSshape = Column(String)

    gene = relationship('Gene', backref=backref('publication'))

    def __repr__(self):
        return '<Publication(publication_id=%s, small_ref=%s)>' %\
            (self.publication_id, self.small_ref)


class GeneInfo(Base):
    __tablename__ = 'genomic_info'

    gene_name = Column(String, ForeignKey('gene_ids.gene_name'), primary_key=True)
    name = Column(String)
    synonyms = Column(String)
    species = Column(String, ForeignKey('gene_ids.species'), primary_key=True)
    ihop = Column(String)
    uniprot = Column(String)
    refseq_id = Column(String)
    uniq_id = Column(String)
    uniq_id_2 = Column(String)
    jaspar = Column(String)
    description = Column(String)
    domain = Column(String)

    gene = relationship('Gene', backref=backref('gene_info'),
                        primaryjoin='(GeneInfo.gene_name == Gene.gene_name) & (GeneInfo.species == Gene.species)')

    def __repr__(self):
        return '<GeneInfo(gene_name=%s, synonyms=%s, species=%s)>' %\
            (self.gene_name, self.synonyms, self.species)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
