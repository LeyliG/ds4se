# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/3.4_facade.ipynb (unless otherwise specified).

__all__ = ['LinkType', 'get_docs', 'get_counters', 'preprocess', 'TraceLinkValue', 'NumDoc', 'VocabSize',
           'AverageToken', 'Vocab', 'VocabShared', 'SharedVocabSize', 'MutualInformation', 'CrossEntropy',
           'KLDivergence']

# Cell
import random
from nbdev.showdoc import *
import pandas as pd
import sentencepiece as sp
from pathlib import Path
from collections import Counter
from .mining.unsupervised.traceability.eval import *
from enum import Enum, unique, auto
from .exp import i
import os
import pkg_resources

# Cell
@unique
class LinkType(Enum):
    req2tc = auto()
    req2src = auto()

# Cell

#export
def get_docs(df, spm):
    #param dataframe of content that need to be processed
    #param sentence piece processor that will process the dataframe
    #return the document list
    docs = []
    for fn in df["contents"]:
        docs += spm.EncodeAsPieces(fn)
    return docs

#export
def get_counters(docs):
    #param doc list of contents that need info on tokens
    #return the counters object of tokens
    doc_cnts = []
    cnt = Counter()
    for tok in docs:
        cnt[tok] += 1
        doc_cnts.append(cnt)
    return doc_cnts

#export
#load sentence piece model and call two helper function to calculate token freqnency
def preprocess(artifacts_df):
    spm = sp.SentencePieceProcessor()
    bpe_model_path = pkg_resources.resource_filename('ds4se', 'model/test.model')
    spm.Load(bpe_model_path)
    docs = get_docs(artifacts_df,spm)
    cnts = get_counters(docs)
    return cnts

# Cell
def TraceLinkValue(source, target, technique, word2vec_metric = "WMD"):
    #param source a string of the entire source file
    #param target a string of the entire target file
    #param technique what tecchnique to use to calculate trace values
    #return a tuple: (distance, similarity)

    #TODO make the string saved and then return the path to that string
    sourcePath = "path/to/something"#this is where we save the passed in source
    targetPath = "./something"

    dummy_path = pkg_resources.resource_filename('ds4se', 'model/val.csv')


    value = random.randint(0,1)/100


    if (technique == "VSM"):
        pass
    if (technique == "LDA"):
        pass
    if (technique == "orthogonal"):
        pass
    if (technique == "LSA"):
        pass
    if (technique == "JS"):
        pass
    if (technique == "word2vec"):
        model_path = pkg_resources.resource_filename('ds4se', 'model/word2vec_libest.model')
        parameter = {
            "vectorizationType": VectorizationType.word2vec,
            "linkType": LinkType.req2tc,
            "system": 'libest',
            "path_to_trained_model": model_path,
            "source_path": dummy_path,
            "target_path": dummy_path,
            "system_path": dummy_path,
            "saving_path": 'test_data/',
            "names": ['Source','Target','Linked?']
        }

        source_df = pd.DataFrame({ "ids": ["source"],  "text":[source]})
        target_df = pd.DataFrame({ "ids": ["target"],  "text":[target]})
        word2vec = Word2VecSeqVect(parameter)
        word2vec.df_source = source_df
        word2vec.df_target = target_df
        links = [(source_df["ids"][0],target_df["ids"][0])]
        if (word2vec_metric == "SCM"):
            computeDistanceMetric = word2vec.computeDistanceMetric(links, metric_list = [DistanceMetric.SCM])
        else:
            computeDistanceMetric = word2vec.computeDistanceMetric(links, metric_list = [DistanceMetric.WMD])
        value = (computeDistanceMetric[0][0][2],computeDistanceMetric[0][0][3])

    if (technique == "doc2vec"):
        model_path = pkg_resources.resource_filename('ds4se', 'model/[word2vec-Java-Py-SK-500-20E-128k-1594873397.267055].model')
        parameter = {
            "vectorizationType": VectorizationType.doc2vec,
            "linkType": LinkType.req2tc,
            "system": 'libest',
            "path_to_trained_model": model_path,
            "source_path": 'test_data/val.csv',
            "target_path": 'test_data/val.csv',
            "system_path": 'test_data/val.csv',
            "saving_path": 'test_data/',
            "names": ['Source','Target','Linked?']
        }

        source_df = pd.DataFrame({ "ids": ["source"],  "text":[source]})
        target_df = pd.DataFrame({ "ids": ["target"],  "text":[target]})
        doc2vec = Doc2VecSeqVect(params = parameter)
        doc2vec.df_source = source_df
        doc2vec.df_target = target_df
        doc2vec.InferDoc2Vec(steps=200)
        table = doc2vec.ComputeDistanceArtifacts( sampling=True, samples = 50, metric_list = [DistanceMetric.EUC] )
        value = (table[0][0][2], table[0][0][3])
        #The bottom is here for reference -- may not need it
#         doc2vec.SaveLinks()
#         #will most likely need to change this part need to change this part to a different path
#         path_to_ground_truth = '/tf/main/benchmarking/traceability/testbeds/groundtruth/english/[libest-ground-req-to-tc].txt'
#         doc2vec.MatchWithGroundTruth(path_to_ground_truth)
#         doc2vec.SaveLinks(grtruth = True)
#         #TODO find logic to LoadLink properly and display what is needed

    return value

# Cell
def NumDoc(source, target):
    #param source a dataframe of the entire source file
    #param target a dataframe of the entire target file
    #return a list containing the the difference between the two files
    source_doc = source.shape[0]
    target_doc = target.shape[0]
    difference = source_doc - target_doc
    return [source_doc, target_doc, difference, -difference]

# Cell
def VocabSize(source, target):
    #param source a string of the entire source file
    #param target a string of the entire target file
    #return a list containing the the difference between the two files in terms of vocab
    source_list = preprocess(source)
    target_list = preprocess(target)
    source_size = len(source_list[0])
    target_size = len(target_list[0])
    difference = source_size - target_size
    return [source_size, target_size, difference, -difference]

# Cell
def AverageToken(source, target):
    #param source a dataframe of the entire source file
    #param target a dataframe of the entire target file
    #return a list containing the the difference between the two files in terms of tokens
    source_doc = source.shape[0]
    target_doc = target.shape[0]

    source_list = preprocess(source)
    target_list = preprocess(target)

    source_total_token = sum(source_list[0].values())
    target_total_token = sum(target_list[0].values())

    source_token = source_total_token/source_doc
    target_token = target_total_token/target_doc
    difference = source_token - target_token
    return [source_token, target_token, difference, -difference]

# Cell
def Vocab(artifacts_df):
    #we can add a parameter for user to specify the number of most frequent token to return
    #param a dataframe of contents that need to be processed
    #return a list containing the the difference between the two files in terms of vocab
    cnts = preprocess(artifacts_df)
    vocab_list = cnts[0].most_common(3)
    total = sum(cnts[0].values())
    vocab_dict = dict()
    vocab_dict[vocab_list[0][0]] = [vocab_list[0][1], vocab_list[0][1]/total]
    vocab_dict[vocab_list[1][0]] = [vocab_list[1][1], vocab_list[1][1]/total]
    vocab_dict[vocab_list[2][0]] = [vocab_list[2][1], vocab_list[2][1]/total]

    return vocab_dict

# Cell
def VocabShared(source, target):
    #param source a dataframe of the entire source file
    #param target a dataframe of the entire target file
    #return the similarities of vocab in the files
    df = pd.concat([source, target])
    return Vocab(df)

# Cell
def SharedVocabSize(source, target):
    #param source a dataframe of the entire source file
    #param target a dataframe of the entire target file
    #return the similarities of vocab sizes in the files
    df = pd.concat([source, target])
    df_counts = preprocess(df)
    shared_size = len(df_counts[0])
    return shared_size

# Cell
def MutualInformation(source, target):
    #param source a string of the entire source file
    #param target a string of the entire target file
    #return the mutual information
    mutual_information = random.randint(100,200)
    return mutual_information

# Cell
def CrossEntropy(source, target):
    #param source a string of the entire source file
    #param target a string of the entire target file
    #return the entropy
    cross_entropy = random.randint(100,200)
    cross_entropy = get_system_entropy_from_df(source, "col1",)
    return cross_entropy

# Cell


#export
def KLDivergence(source, target):
    #param source a string of the entire source file
    #param target a string of the entire target file
    #return the divergence
    divergence = random.randint(100,200)
    return divergence