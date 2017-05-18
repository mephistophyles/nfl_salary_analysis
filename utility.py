from __future__ import division
import csv
from os.path import join
from os import getcwd
import pprint

import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np

style.use('ggplot')


# source, profootballfocus
rb_rankings_teams = {'Eagles':24, 'Redskins':27, 'Cowboys':5, 'Giants':31,
             'Falcons':8, 'Saints':21, 'Panthers':15, 'Buccaneers':3,
             'Seahawks':11, '49ers':22, 'Cardinals':2, 'Rams':16,
             'Bears':17, 'Packers':30, 'Lions':26, 'Vikings':32,
             'Steelers':1, 'Ravens':19, 'Bengals':9, 'Browns':13,
             'Chargers':12, 'Broncos':28, 'Raiders':20, 'Chiefs':14,
             'Colts':25, 'Texans':10, 'Jaguars':23, 'Titans':6,
             'Patriots':18, 'Bills':4, 'Dolphins':7, 'Jets':29}

# source, profootballfocus
dl_rankings_teams = {'Eagles':2, 'Redskins':21, 'Cowboys':22, 'Giants':11,
             'Falcons':24, 'Saints':28, 'Panthers':3, 'Buccaneers':25,
             'Seahawks':1, '49ers':31, 'Cardinals':5, 'Rams':4,
             'Bears':23, 'Packers':9, 'Lions':30, 'Vikings':6,
             'Steelers':16, 'Ravens':17, 'Bengals':19, 'Browns':29,
             'Chargers':14, 'Broncos':7, 'Raiders':15, 'Chiefs':8,
             'Colts':32, 'Texans':10, 'Jaguars':26, 'Titans':13,
             'Patriots':18, 'Bills':20, 'Dolphins':12, 'Jets':27}

# source, profootballfocus
ol_rankings_teams = {'Eagles':8, 'Redskins':7, 'Cowboys':2, 'Giants':20,
             'Falcons':6, 'Saints':12, 'Panthers':17, 'Buccaneers':23,
             'Seahawks':32, '49ers':28, 'Cardinals':26, 'Rams':27,
             'Bears':15, 'Packers':5, 'Lions':19, 'Vikings':29,
             'Steelers':3, 'Ravens':9, 'Bengals':13, 'Browns':16,
             'Chargers':31, 'Broncos':24, 'Raiders':4, 'Chiefs':14,
             'Colts':25, 'Texans':18, 'Jaguars':22, 'Titans':1,
             'Patriots':10, 'Bills':11, 'Dolphins':30, 'Jets':21}

# source, profootballfocus
secondary_rankings_teams = {'Eagles':32, 'Redskins':26, 'Cowboys':1, 'Giants':2,
             'Falcons':6, 'Saints':29, 'Panthers':27, 'Buccaneers':15,
             'Seahawks':5, '49ers':21, 'Cardinals':9, 'Rams':22,
             'Bears':30, 'Packers':19, 'Lions':18, 'Vikings':7,
             'Steelers':11, 'Ravens':10, 'Bengals':16, 'Browns':28,
             'Chargers':14, 'Broncos':4, 'Raiders':17, 'Chiefs':12,
             'Colts':31, 'Texans':8, 'Jaguars':13, 'Titans':25,
             'Patriots':3, 'Bills':24, 'Dolphins':20, 'Jets':23}

# source, profootballfocus only through week 6 though
wr_rankings_teams = {'Eagles':29, 'Redskins':3, 'Cowboys':2, 'Giants':10,
             'Falcons':6, 'Saints':8, 'Panthers':16, 'Buccaneers':24,
             'Seahawks':12, '49ers':32, 'Cardinals':7, 'Rams':30,
             'Bears':28, 'Packers':19, 'Lions':18, 'Vikings':25,
             'Steelers':9, 'Ravens':23, 'Bengals':31, 'Browns':20,
             'Chargers':21, 'Broncos':5, 'Raiders':4, 'Chiefs':17,
             'Colts':11, 'Texans':15, 'Jaguars':13, 'Titans':27,
             'Patriots':1, 'Bills':26, 'Dolphins':14, 'Jets':22}


def check_dictionary(d):
    v = d.values()
    for i in range(1,33):
        if i not in v:
            print 'missing {}'.format(i)
            return False
    return True


def csv_to_dict(csv_target):
    csv_file = join(getcwd(), 'data/{}'.format(csv_target))
    header_names = ["Team", "QB", "RB", "WR", "TE", "OL", "Offense", "DL", "LB", "S", "CB", "Defense"]
    teams = ['Eagles', 'Redskins', 'Cowboys', 'Giants',
             'Falcons', 'Saints', 'Panthers', 'Buccaneers',
             'Seahawks', '49ers', 'Cardinals', 'Rams',
             'Bears', 'Packers', 'Lions', 'Vikings',
             'Steelers', 'Ravens', 'Bengals', 'Browns',
             'Chargers', 'Broncos', 'Raiders', 'Chiefs',
             'Colts', 'Texans', 'Jaguars', 'Titans',
             'Patriots', 'Bills', 'Dolphins', 'Jets']

    csvfile = open(csv_file, 'r')
    reader = csv.DictReader(csvfile)
    data_dict = {}
    index = 0
    for line in reader:
        data_dict[line['Team']]=line
    return data_dict


def clean_salary_text(input_file, output_file):
    data_file = join(getcwd(), 'data/{}'.format(input_file))
    with open(data_file) as f:
        data = f.readlines()
    data = [x.replace('\t\t', '\t') for x in data]
    data = [x.replace(',', '') for x in data]
    data = [x.replace('$', '') for x in data]
    data = [x.replace('\t', ', ') for x in data]
    data = [x.split('\n') for x in data]
    output_file = join(getcwd(), 'data/{}'.format(output_file))
    f = open(output_file, 'w')
    print output_file

    for line in data:
        f.write(line[0]+'\n')
    f.close()


def import_team_rankings(stat_file):
    f = open(stat_file)
    keys = f.readline().split("\t")
    data = {}
    for k in keys:
        data[k] = []
    for i in xrange(32):
        line = f.readline().split("\t")
        for j in xrange(len(keys)):
            data[keys[j]].append(line[j])
    f.close()
    return data

def plot_overview(csv_file):
    # folder_location = join(getcwd(), "data")
    # pickle_location = join(folder_location, 'cap_dataframe.pkl')
    # pos_dataframe = get_salary_data()
    # pos_dataframe.to_pickle(pickle_location)
    # clean_salary_text()
    TOTAL_CAPSPSACE = 155270000
    x = csv_to_dict(csv_file)
    # pprint.pprint(x)
    teams = ['Eagles', 'Redskins', 'Cowboys', 'Giants',
             'Falcons', 'Saints', 'Panthers', 'Buccaneers',
             'Seahawks', '49ers', 'Cardinals', 'Rams',
             'Bears', 'Packers', 'Lions', 'Vikings',
             'Steelers', 'Ravens', 'Bengals', 'Browns',
             'Chargers', 'Broncos', 'Raiders', 'Chiefs',
             'Colts', 'Texans', 'Jaguars', 'Titans',
             'Patriots', 'Bills', 'Dolphins', 'Jets']
    offense_spending = []
    defense_spending = []
    cb_spending = []
    s_spending = []
    lb_spending = []
    dl_spending = []
    qb_spending = []
    rb_spending = []
    wr_spending = []
    te_spending = []
    ol_spending = []
    position_specific_headers = [" QB", " RB", " WR", " TE", " OL", " DL", " LB", " S", " CB"]

    plt.subplot(111)
    for team in teams:
        offense_spending.append(int(x[team][" Offense"]))
        defense_spending.append(int(x[team][" Defense"]))
        cb_spending.append(int(x[team][" CB"]))
        s_spending.append(int(x[team][" S"]))
        lb_spending.append(int(x[team][" LB"]))
        dl_spending.append(int(x[team][" DL"]))
        qb_spending.append(int(x[team][" QB"]))
        rb_spending.append(int(x[team][" RB"]))
        wr_spending.append(int(x[team][" WR"]))
        te_spending.append(int(x[team][" TE"]))
        ol_spending.append(int(x[team][" OL"]))
    ind = np.arange(32)
    p1 = plt.barh(ind, offense_spending, height=0.25, color='r')
    p2 = plt.barh(ind, defense_spending, height=0.25, color='b', left=offense_spending)
    p3 = plt.barh(32, TOTAL_CAPSPSACE, color='black')
    plt.yticks(ind, teams)
    plt.xlabel("Contract cost [$]")
    plt.legend((p1[0], p2[0], p3[0]), ('Offense', 'Defense', 'Salary Cap for 2016'), bbox_to_anchor=(0., 1.02, 1., .102),
               loc=3, ncol=5, mode="expand", borderaxespad=0.)
    plt.figure()
    plt.subplot(121)
    p1 = plt.barh(ind, qb_spending, height=0.25, color='red')
    p2 = plt.barh(ind, wr_spending, height=0.25, color='blue', left=qb_spending)
    p3 = plt.barh(ind, rb_spending, height=0.25, color='black', left=[sum(x) for x in zip(qb_spending, wr_spending)])
    p4 = plt.barh(ind, te_spending, height=0.25, color='green', left=[sum(x) for x in zip(qb_spending, wr_spending, rb_spending)])
    p5 = plt.barh(ind, ol_spending, height=0.25, color='yellow', left=[sum(x) for x in zip(qb_spending, wr_spending, rb_spending, te_spending)])
    plt.yticks(ind, teams)
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ("QB", "WR", "RB", "TE", "OL"), bbox_to_anchor=(0., 1.02, 1., .102),
               loc=3, ncol=5, mode="expand", borderaxespad=0.)
    plt.subplot(122)
    p1 = plt.barh(ind, s_spending, height=0.25, color='red')
    p2 = plt.barh(ind, cb_spending, height=0.25, color='blue', left=s_spending)
    p3 = plt.barh(ind, lb_spending, height=0.25, color='black', left=[sum(x) for x in zip(s_spending, cb_spending)])
    p4 = plt.barh(ind, dl_spending, height=0.25, color='green', left=[sum(x) for x in zip(s_spending, cb_spending, lb_spending)])
    plt.yticks(ind, teams)
    plt.legend((p1[0], p2[0], p3[0], p4[0]), ("DL", "LB", "S", "CB"), bbox_to_anchor=(0., 1.02, 1., .102),
               loc=3, ncol=4, mode="expand", borderaxespad=0.)
    plt.show()


def offense_defense_stats(pos = "Offense"):
    if pos == "Offense":
        stats_file = 'offensive_stats.txt'
    else:
        stats_file = 'defensive_stats.txt'
    ranking_dict = import_team_rankings(stats_file)
    # we now have all the data we need to create offensive rankings
    yards = [int(yardage) for yardage in ranking_dict["TotYds"]]
    mean_yards = sum(yards) / 32.0
    points = [int(pts) for pts in ranking_dict["Tot Pts"]]
    mean_points = sum(points) / 32.0
    # points_ratio depends on position too
    if pos == "Offense":
        points_ratio = [pt / mean_points for pt in points]
        yards_ratio = [yd / mean_yards for yd in yards]
    else:
        points_ratio = [mean_points / pt for pt in points]
        yards_ratio = [mean_yards / yd for yd in yards]
    # needed to preserve team relation to the ratios
    teams = ranking_dict['Team']
    # homoginizing names over both datasets
    teams = [team.split(" ")[-1] for team in teams]
    salary = csv_to_dict('2016_cap_hits.csv')
    salaries = []
    for t in teams:
        # that space is a bit of a quirk in the dictionary cleaning
        salaries.append(int(salary[t][" {}".format(pos)]))
    mean_salary = sum(salaries) / 32.0
    salary_ratio = [sal / mean_salary for sal in salaries]
    yards_efficiency = [x / y for x, y in zip(yards_ratio, salary_ratio)]
    points_efficiency = [x / y for x, y in zip(points_ratio, salary_ratio)]
    plt.figure()
    p1 = plt.scatter(xrange(32), yards_ratio, color='r')
    p2 = plt.scatter(xrange(32), points_ratio, color='blue')
    plt.xticks(np.arange(32), teams, rotation='vertical')
    plt.legend((p1, p2), ('yards ratio', 'points ratio'))
    plt.figure()
    p3 = plt.scatter(xrange(32), yards_efficiency, color='r')
    p4 = plt.scatter(xrange(32), points_efficiency, color='blue')
    plt.xticks(np.arange(32), teams, rotation='vertical')
    plt.legend((p3, p4), ('yard/salary efficiency', 'point/salary efficiency'))
    plt.show()
    print "*" * 50


if __name__ == "__main__":
    print "*"*50
    plot_overview('2016_cap_hits.csv')