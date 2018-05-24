from connect_db import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PLOT_LABEL_FONT_SIZE = 8

def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS

def dict_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
    for k, v in my_dict:
        keys.append(k)
        values.append(v)
    return (keys,values)


def candidates_votes():
    conn = connect_db()
    df = pd.read_sql("SELECT candidate, SUM(votes) AS votes FROM public.data_election Group BY candidate", conn)
    dict = {}
    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys,dict_values = dict_sort(dict)
    top_keys = len(dict_keys)

    plt.title('Кандидати', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість голосів', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()


def party_votes():
    conn = connect_db()
    df = pd.read_sql("SELECT  party,SUM(votes) AS votes FROM public.data_election Group BY party;",conn)
    dict = {}
    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)
    plt.title('Партії', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=0, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість голосів', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()

def candidate_votes_democrat():
    conn = connect_db()
    df = pd.read_sql("SELECT candidate, SUM(votes) AS votes FROM public.data_election WHERE party='Democrat' Group BY candidate", conn)
    dict = {}
    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)
    plt.title('Кандидати від демократів', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість голосів', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()

def candidate_votes_republican():
    conn = connect_db()
    df = pd.read_sql("SELECT candidate, SUM(votes) AS votes FROM public.data_election WHERE party='Republican' Group BY candidate", conn)
    dict = {}
    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)
    plt.title('Кандидати від республіканців', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість голосів', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()

def state_votes_democrat():
    conn = connect_db()
    df = pd.read_sql(
        "SELECT st_abbr, SUM(votes) AS votes FROM public.data_election WHERE party='Democrat' Group BY st_abbr",
        conn)
    dict = {}
    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)
    plt.title('Голоси по штатам(демократи)', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість голосів', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()

def state_votes_republican():
    conn = connect_db()
    df = pd.read_sql(
        "SELECT st_abbr, SUM(votes) AS votes FROM public.data_election WHERE party='Republican' Group BY st_abbr",
        conn)
    dict = {}
    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)
    plt.title('Голоси по штатам(демократи)', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість голосів', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()