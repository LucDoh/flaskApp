import sys
import os.path
import subprocess
from V_Flask.scripts import analyzePosts, clHousingScraper
from V_Flask.utils import makePdf

def run(prefix, zip, dist, n):
    #= str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4])
    stringDB = 'clHousing_' + zip + "_" + dist + "_" + str(n) + ".db"
    b = os.path.isfile('V_Flask/dbs/' + stringDB)

    #1 Scrape if data doesn't exist yet
    if b == False: stringDB = clHousingScraper.scrapeRentals(prefix, zip, dist, n)
    #2 Analyze
    analyzePosts.analyze(stringDB)

    #3 Generate report in pdf form.
    makePdf.generateReport('static/plots/facts.txt','static/plots/distPlots.png', 'static/plots/relPlot.png')

def main():
    return
if __name__== "__main__":
  main()













    #stringDB = 'clHousing_20740_5_240.db'
