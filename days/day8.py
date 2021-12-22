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
def calc_digits(disp_map, outputs):
    ret = ""
    for digit in ["".join(sorted(x)) for x in outputs]:
        ret = ret + disp_map[digit]

    return int(ret)

def decode_segments(sigs):
    disp_map=[0 for x in range(10)]
    ret = {}
    lt = []
    rt = []

    # build mapping
    for i in sigs:
        l = len(i)
        match l:
            case 2: disp_map[1] = set(i)
            case 3: disp_map[7] = set(i)
            case 4: disp_map[4] = set(i)
            case 5: lt.append(set(i)) # could be a few 
            case 6: rt.append(set(i)) # could be the other few (0, 6 or 9)
            case 7: disp_map[8] = set(i)
    for x in rt:
        if disp_map[4].issubset(set(x)):
            disp_map[9] = set(x)
        elif disp_map[7].issubset(set(x)):
            disp_map[0] = set(x)
        else:
            disp_map[6] = set(x)
    for y in lt:
        if disp_map[7].issubset(set(y)):
            disp_map[3] = set(y)
        elif len(set(y).intersection(disp_map[4])) == 3:
            disp_map[5] = set(y)
        else:
            disp_map[2] = set(y)
    for idx,s in enumerate(disp_map):
        k = "".join(sorted(s))
        ret[k] = str(idx)
  
    return ret,disp_map

class Day8(Day):
    def quiz1(self):
        ret = 0
        ks = [1,4,7,8]
        for l in [len(x[1]) for x in self.data]:
            if l in ks:
                ret = ret + 1
        return ret

    def quiz2(self):
        ret = 0
        for sigs,outputs in self.data:
            disp_map,set_map = decode_segments(sigs)
            ret = ret + calc_digits(disp_map, outputs)
        return ret

    def load(self):
        self.data = []
        for i,o in [x.split('|') for x in self.dfile]:
           i = i.split()
           o = o.split()
           self.data.append((i,o))

        
            
           
