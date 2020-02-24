# AUTOGENERATED! DO NOT EDIT! File to edit: dev/00_data.preprocessing.ipynb (unless otherwise specified).

__all__ = ['jsonl_list_to_dataframe', 'get_dfs', 'df_to_txt_file', 'gen_sp_model', 'gen_hugface_model']

# Cell
# Imports
import pandas as pd
import sentencepiece as sp

from pathlib import Path
from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing

# Cell
def jsonl_list_to_dataframe(file_list, columns=None):
    """Load a list of jsonl.gz files into a pandas DataFrame."""
    return pd.concat([pd.read_json(f,
                                   orient='records',
                                   compression='gzip',
                                   lines=True)[columns]
                      for f in file_list], sort=False)

# Cell
def get_dfs(path):
    """
        Grabs the different data splits and converts them into dataframes.
        Expects format from Code Search Net Challenge.
    """
    dfs = []
    for split in ["train", "valid", "test"]:
        files = sorted((path/split).glob("**/*.gz"))
        df = jsonl_list_to_dataframe(files, ["code", "docstring"])
        dfs.append(df)

    return dfs

# Cell
def df_to_txt_file(df, output, cols):
    """Converts a dataframe and converts it into a text file that SentencePiece can use to train a BPE model"""
    if cols is None: cols = list(df.columns)
    merged_df = pd.concat([df[col] for col in cols])

    with open(output/'text.txt', 'w') as f:
        f.write('\n'.join(list(merged_df)))
    return output/'text.txt'

# Cell
def gen_sp_model(df, output, model_name, cols = None):
    """Trains a SentencePiece BPE model from a pandas dataframe"""
    fname = df_to_txt_file(df, output, cols)
    sp.SentencePieceTrainer.train(f'--input={fname} --model_prefix={output / model_name} --hard_vocab_limit=false')

# Cell
def gen_hugface_model(df, output, tokenizer = ByteLevelBPETokenizer(), vocab_sz = 30_000, min_freq = 3, cols = None):
    fname = df_to_txt_file(df, output, cols)
    tokenizer.train(files = [str(fname)], vocab_size = vocab_sz, min_frequency = min_freq, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>",
    ])

    return tokenizer