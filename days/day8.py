from .day import Day
import json

mapping = {
    '3': 7,
    '2': 1,
    '4': 4,
    '7': 8
}
k_mapping = {
    'bcdefg': 9,
    'abcdefg': 8,
    'bfg': 7,
    'acdefg': 6,
    'bcdef': 5,
    'cefg': 4,
    'abefg': 3,
    'abcdg': 2,
    'bc': 1,
}
 
def update(o,k):
    if k in o:
        v = o[k]
        v['freq'] = v['freq'] + 1
    else:
        o[k] = {
            'freq': 1,
            'digits': mapping[str(len(k))] 
        }
def calc_num(a):
    mx = pow(10, len(a))
    v = 0
    for idx, m in enumerate(a):
        dg = k_mapping.get(m,0)
        if dg ==0:
            print(m)
        v = v + (dg * (mx - pow(10,idx)))
    return v

class Day8(Day):
    def quiz1(self):
        ks = [1,4,7,8]
        return sum([self.ofreq[x] for x in ks])
    def quiz2(self):
        for dg in self.digits:
            v = calc_num(dg)
            print(v)
        print()

    def load(self):
        input = {}
        output = {}
        ofreq = [0 for x in range(10)]
        ifreq = [0 for x in range(10)]
        digits = []
        # normalize the mapping
        
        for line in self.dfile.readlines():
            left,right = [x.strip() for x in line.split("|")]
            for l in left.split():
                k = "".join(sorted(l))
                ix = mapping.get(str(len(k)), -1)
                if ix >= 0:
                    ifreq[ix] = ifreq[ix] + 1
                # update(input,k)
            dg = []
            for r in right.split():
                k = "".join(sorted(r))
                dg.append(k)
                ix = mapping.get(str(len(k)), -1)
                if ix >= 0:
                    ofreq[ix] = ofreq[ix] + 1
                # update(output,k)
            digits.append(dg)   

        self.ifreq = ifreq
        self.ofreq = ofreq
        self.digits = digits
            
           
