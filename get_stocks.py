symbol = lambda x : x.split()[-1]
get_vals = lambda x: x.split(" C ")


with  open('stocks.txt', 'r') as f:
    with open('new_stocks.csv', 'wb') as nf:
        nf.write("Symbol,Shares\n")
        for line in f:
            vals = get_vals(line)
            if len(vals)==2:
                sym = symbol(vals[-2])
                res = vals[-1]
                res.split(' ')
                shares = res[0]
                nf.write(sym + ',' + shares + '\n')


