# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/3.4_facade.ipynb (unless otherwise specified).

__all__ = ['TraceLinkValue', 'NumDoc', 'VocabSize', 'AverageToken', 'Vocab', 'VocabShared', 'SharedVocabSize',
           'MutualInformation', 'CrossEntropy', 'KLDivergence']

# Cell
import random

# Cell
def TraceLinkValue(filename, source, technique):
    value = random.randint(0,1)
    return value

#export
def NumDoc(source, target):
    source_doc = random.randint(100,200)
    target_doc = random.randint(100,200)
    difference = source_doc - target_doc
    return [source_doc, target_doc, difference, -difference]

#export
def VocabSize(source, target):
    source_size = random.randint(100,200)
    target_size = random.randint(100,200)
    difference = source_size - target_size
    return [source_size, target_size, difference, -difference]

#export
def AverageToken(source, target):
    source_token = random.randint(100,200)
    target_token = random.randint(100,200)
    difference = source_token - target_token
    return [source_token, target_token, difference, -difference]

#export
def Vocab(filename):
    total = 1000
    vocab_dict = dict()
    tmp1 = random.randint(100,200)
    tmp2 = random.randint(100,200)
    tmp3 = random.randint(100,200)
    vocab_dict["est"] = [tmp1, tmp1/total]
    vocab_dict["http"] = [tmp2, tmp2/total]
    vocab_dict["frequnecy"] = [tmp3, tmp3/total]
    return vocab_dict


#export
def VocabShared(source, target):
    total = 1000
    vocab_dict = dict()
    tmp1 = random.randint(100,200)
    tmp2 = random.randint(100,200)
    tmp3 = random.randint(100,200)
    vocab_dict["est"] = [tmp1, tmp1/total]
    vocab_dict["http"] = [tmp2, tmp2/total]
    vocab_dict["frequnecy"] = [tmp3, tmp3/total]
    return vocab_dict

#export
def SharedVocabSize(source, target):
    shared_size = random.randint(100,200)
    return shared_size

#export
def MutualInformation(source, target):
    mutual_information = random.randint(100,200)
    return mutual_information

#export
def CrossEntropy(source, target):
    cross_entropy = random.randint(100,200)
    return cross_entropy

#export
def KLDivergence(source, target):
    divergence = random.randint(100,200)
    return divergence