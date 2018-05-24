from connect_db import *

def filter_data(column,value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.data_election WHERE %s=$$%s$$" % (column,value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_votes_ls(value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.data_election WHERE votes<=%s" % (value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_votes_gt(value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.data_election WHERE votes>=%s" % (value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_state(value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.data_election WHERE state=$$%s$$" % (value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_st_abbr(value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.data_election WHERE st_abbr=$$%s$$" % (value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_candidate(value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.data_election WHERE candidate=$$%s$$" % (value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_party(value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.data_election WHERE party=$$%s$$" % (value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)
