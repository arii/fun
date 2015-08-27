#!/usr/bin/env python
import urllib2, urllib, json


def get_query(stocks):
    start_date = "2015-03-02"
    hist_select = "select Close from yahoo.finance.historicaldata where symbol in "
    curr_select = "select LastTradePriceOnly from yahoo.finance.quote where symbol in " 
    names = "(%s)" % ','.join(['"%s"'% s for s in stocks])
    curr_query = curr_select + names
    hist_query = hist_select + names + 'and startDate = "%s" and endDate = "%s" ' % (start_date, start_date)
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    endurl = "&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
   
    def get_response(select):
        yql_url = baseurl + urllib.urlencode({'q':select}) + endurl
        result = urllib2.urlopen(yql_url).read()
        data = json.loads(result)
        return [float(d.values()[0])for d in data['query']['results']['quote']]

    
    return zip(get_response(hist_query), get_response(curr_query))

    
def main():
    stocks = ["YELP", "VA", "INTC", "F", "BABA", "BAC", "PCG", "PG", "BP", "BEBE", "ANF", "AMD", "NVAX", "GDP", "GRO", "VLTC", "EDU", "P", "RST", "GME", "FIX", "CRC", "AUMN", "APP", "REGI", "FE", "C", "BORN", "X", "AAPL", "YHOO", "ORCL", "JBLU", "HLS", "EMC", "SGMS", "DOW", "AAL", "GTIM", "ATRA", "CDXS", "GM", "BXP", "HLT", "NVDA", "M", "AMC"]
    res = get_query(stocks)

    difference = []
    perc_difference = []
    o_total = 0
    n_total = 0
    
    for (o, n) in res:
        difference.append(n-o)
        o_total += o
        n_total += n
        perc_difference.append( 100.0*(n-o)/o )
    total_change = sum(difference)
    print "previous total on march 2nd, 2015 = %.2f\ncurrent total = %.2f \ntotal net change = %.2f\n" % (o_total, n_total, total_change)
    print "\npositive percent increases"
    for i,p in enumerate(perc_difference):
        if p > 0:
            print "%s:\t%.2f,\t%.2f%%" % (stocks[i], res[i][1], p)
    print "\nnegative percent increases"
    for i,p in enumerate(perc_difference):
        if p < 0:
            print "%s:\t%.2f,\t%.2f%%" % (stocks[i], res[i][1], p)



if __name__=="__main__":
   main() 
