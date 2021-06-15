# Julia Cuellar
# DSC 530
# Final project

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import math


def read_file():
    arb = pd.read_csv("At-risk behaviors.csv")
    print(arb.head(5))


def showBar_Date():
    arb = pd.read_csv("At-risk behaviors.csv")
    arb['Date'].value_counts().plot(kind = 'barh').invert_yaxis()
    plt.title('Date')
    plt.show()


def showBar_Week():
    arb = pd.read_csv("At-risk behaviors.csv")
    arb['Week'].value_counts().plot(kind = 'barh').invert_yaxis()
    plt.title('Week')
    plt.show()


def showBar_Shift():
    arb = pd.read_csv("At-risk behaviors.csv")
    arb['Shift'].value_counts().plot(kind = 'barh').invert_yaxis()
    plt.title('Shift')
    plt.show()


def showBar_Arb():
    arb = pd.read_csv("At-risk behaviors.csv")
    arb['At-risk behavior'].value_counts().plot(kind = 'barh').invert_yaxis()
    plt.title('At-risk behavior')
    plt.show()


def showBar_Employment():
    arb = pd.read_csv("At-risk behaviors.csv")
    arb['Employment'].value_counts().plot(kind = 'barh').invert_yaxis()
    plt.title('Employment')
    plt.show()


def showBar_JobFunc():
    arb = pd.read_csv("At-risk behaviors.csv")
    arb['Job Function'].value_counts().plot(kind = 'barh').invert_yaxis()
    plt.title('Job Function')
    plt.show()


def desChar_Date():
    arb = pd.read_csv("At-risk behaviors.csv")
    desChar_d = arb['Date'].describe
    print(desChar_d)
    count_d = arb['Date'].value_counts()
    print(count_d)


def desChar_Week():
    arb = pd.read_csv("At-risk behaviors.csv")
    desChar_w = arb['Week'].describe
    print(desChar_w)
    count_w = arb['Week'].value_counts()
    print(count_w)


def desChar_Shift():
    arb = pd.read_csv("At-risk behaviors.csv")
    desChar_s = arb['Shift'].describe
    print(desChar_s)
    count_s = arb['Shift'].value_counts()
    print(count_s)


def desChar_Arb():
    arb = pd.read_csv("At-risk behaviors.csv")
    desChar_b = arb['At-risk behavior'].describe
    print(desChar_b)
    count_b = arb['At-risk behavior'].value_counts()
    print(count_b)


def desChar_Employment():
    arb = pd.read_csv("At-risk behaviors.csv")
    desChar_e = arb['Employment'].describe
    print(desChar_e)
    count_e = arb['Employment'].value_counts()
    print(count_e)


def desChar_JobFunc():
    arb = pd.read_csv("At-risk behaviors.csv")
    desChar_jf = arb['Job Function'].describe
    print(desChar_jf)
    count_jf = arb['Job Function'].value_counts()
    print(count_jf)


def pmf_Employment():
    arb = pd.read_csv("At-risk behaviors.csv")
    sns.set()
    sns.countplot(arb['Employment'], color = 'orange')
    plt.title('Pmf Employment')
    plt.show()


def cdf_Week():
    arb = pd.read_csv("At-risk behaviors.csv")
    sns.set()
    sns.countplot(arb['Week'], color = 'yellow')
    plt.title('Cdf Week')
    plt.show()


def norm():
    mu = 0
    variance = 1
    sigma = math.sqrt(variance)
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma))
    plt.title('Norm Dist')
    plt.show()


def norm_Arb():
    arb = pd.read_csv("At-risk behaviors.csv")
    sns.set()
    sns.countplot(arb['At-risk behavior'], color = 'purple')
    plt.title('Norm Dist At-risk behavior')
    plt.show()


def showScatter_ArbShift():
    arb = pd.read_csv("At-risk behaviors.csv")
    sns.set()
    sns.swarmplot('Shift', 'At-risk behavior', data = arb, palette = 'rainbow')
    plt.title('Scatter Arb vs Shift')
    plt.show()


def showScatter_ArbEmployment():
    arb = pd.read_csv("At-risk behaviors.csv")
    sns.set()
    sns.swarmplot('Employment', 'At-risk behavior', data = arb, palette = 'rainbow')
    plt.title('Scatter Arb vs Employment')
    plt.show()


if __name__ == "__main__":
    read_file()
    showBar_Date()
    showBar_Week()
    showBar_Shift()
    showBar_Arb()
    showBar_Employment()
    showBar_JobFunc()
    desChar_Date()
    desChar_Week()
    desChar_Shift()
    desChar_Arb()
    desChar_Employment()
    desChar_JobFunc()
    pmf_Employment()
    cdf_Week()
    norm()
    norm_Arb()
    showScatter_ArbShift()
    showScatter_ArbEmployment()
