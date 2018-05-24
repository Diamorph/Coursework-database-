from connect_db import *
import random
import pandas as pd

PARTY_CHOICES = [
    ('Democrat','Democrat'),
    ('Republican','Republican')
]

CANDIDATE_DEMOCRAT_CHOICES = [
    ('Bernie Sanders','Bernie Sanders'),
    ("Martin O'Malley","Martin O'Malley"),
    ("Hillary Clinton","Hillary Clinton")
]

CANDIDATE_REPUBLICAN_CHOICES = [
    ("Mike Huckabee","Mike Huckabee"),
    ("Rand Paul","Rand Paul"),
    ("John Kasich","John Kasich"),
    ("Donald Trump","Donald Trump"),
    ("Carly Fiorina","Carly Fiorina"),
    ("Ted Cruz","Ted Cruz"),
    ("Ben Carson","Ben Carson"),
    ("Chris Christie","Chris Christie"),
    ("Jeb Bush","Jeb Bush"),
    ("Rick Santorum","Rick Santorum"),
    ("Marco Rubio","Marco Rubio"),
]

STATE_CHOICES = [
    ("Utah","UT"),
    ("Maryland","MD"),
    ("Oklahoma","OK"),
    ("Montana","MT"),
    ("Wisconsin","WI"),
    ("Virginia","VA"),
    ("Arizona","AZ"),
    ("Colorado","CO"),
    ("Louisiana","LA"),
    ("Maine","ME"),
    ("Delaware","DE"),
    ("Oregon","OR"),
    ("Wyoming","WY"),
    ("Michigan","MI"),
    ("Georgia","GA"),
    ("New York","NY"),
    ("Tennessee","TN"),
    ("Florida","FL"),
    ("Mississippi","MS"),
    ("California","CA"),
    ("Iowa","IA"),
    ("Alabama","AL"),
    ("Missouri","MO"),
    ("Vermont","VT"),
    ("North Dakota","ND"),
    ("Arkansas","AR"),
    ("Indiana","IN"),
    ("Nebraska","NE"),
    ("Nevada","NV"),
    ("Illinois","IL"),
    ("Alaska","AK"),
    ("Pennsylvania","PA"),
    ("Washington","WA"),
    ("New Mexico","NM"),
    ("Massachusetts","MA"),
    ("Kentucky","KY"),
    ("Rhode Island","RI"),
    ("South Carolina","SC"),
    ("Texas","TX"),
    ("New Jersey","NJ"),
    ("South Dakota","SD"),
    ("Kansas","KS"),
    ("Hawaii","HI"),
    ("North Carolina","NC"),
    ("Idaho","ID"),
    ("West Virginia","WV"),
    ("Connecticut","CT"),
]


def generate_data(count):
    conn = connect_db()
    cursor = conn.cursor()
    for i in range(count):
        party = random.choice(PARTY_CHOICES)[0]
        if party == 'Democrat':
            candidate = random.choice(CANDIDATE_DEMOCRAT_CHOICES)[0]
        else :
            candidate = random.choice(CANDIDATE_REPUBLICAN_CHOICES)[0]
        state_unpars = random.choice(STATE_CHOICES)
        state = state_unpars[0]
        st_abbr = state_unpars[1]
        votes = random.randrange(100,10000)
        country = 'country'
        fips = 1011
        fraction_votes = 0.5
        print(state,st_abbr,country,fips,party, candidate, votes,fraction_votes)
        cursor.execute('INSERT INTO public.data_election(state, st_abbr, country, fips, party, candidate, votes, fraction_votes) '
                        'VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', (state,st_abbr,country,fips,party,candidate,votes,fraction_votes))
        conn.commit()

def read_data():
    df = pd.read_csv('primary_results.csv', escapechar='`', low_memory=True)
    #print(df)
    # print(df.loc[1,'state'])
    # print(df.loc[1, 'state_abbreviation'])
    conn = connect_db()
    cursor = conn.cursor()
    for i in range(0,len(df)-1):
        try:
            state = df.loc[i, 'state']
            st_abbr = df.loc[i, 'state_abbreviation']
            country = df.loc[i, 'county']
            fips = int(df.loc[i, 'fips'])
            party = df.loc[i, 'party']
            candidate = df.loc[i, 'candidate']
            votes = str(df.loc[i, 'votes'])
            fraction_votes = str(df.loc[i, 'fraction_votes'])
            cursor.execute(
                'INSERT INTO public.data_election(state, st_abbr, country, fips, party, candidate, votes, fraction_votes) '
                'VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', (state, st_abbr, country, fips, party, candidate, votes, fraction_votes))
            conn.commit()
        except ValueError:
             continue


    print("done")
    # for i in range(0, len(df) - 1):
    #     try:
    #         Election.objects.create(state=df.loc[i, 'state'],
    #                                 st_abbr=df.loc[i, 'state_abbreviation'],
    #                                 country=df.loc[i, 'county'],
    #                                 fips=df.loc[i, 'fips'],
    #                                 party=df.loc[i, 'party'],
    #                                 candidate=df.loc[i, 'candidate'],
    #                                 votes=df.loc[i, 'votes'],
    #                                 fraction_votes=df.loc[i, 'fraction_votes']
    #                                 )
    #     except ValueError:
    #         continue