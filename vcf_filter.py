# MIT License

# Copyright (c) 2024 Hyunwoo Ryu

import os
import argparse

parser = argparse.ArgumentParser(prog='vcf_filter.py')

parser.add_argument('vcf_loc', type=os.path.abspath)
parser.add_argument('-d', '--diff_len_range', type=str)
parser.add_argument('-a', '--max_alt_len_range', type=str)

arg = parser.parse_args()

mind, maxd = arg.diff_len_range.split(':')
mina, maxa = arg.max_alt_len_range.split(':')

min_diff_len_unlimit = mind == ''
min_diff_len = -1 if mind == '' else int(mind)

max_diff_len_unlimit = maxd == ''
max_diff_len = -1 if maxd == '' else int(maxd)

min_max_alt_len_unlimit = mina == ''
min_max_alt_len = -1 if mina == '' else int(mina)

max_max_alt_len_unlimit = maxa == ''
max_max_alt_len = -1 if maxa == '' else int(maxa)

cnt = 0
with open(arg.vcf_loc, 'r') as f:
    for vcf_line in f:
        if (vcf_line.split('\t')[0] == '#CHROM'):
            break
    
    for vcf_line in f:
        vcf_data = vcf_line.split('\t')

        ref_len = len(vcf_data[3])
        max_alt_len = max(map(len, vcf_data[4].split(',')))
        diff_len = max([abs(ref_len - alt) for alt in map(len, vcf_data[4].split(','))])

        if ((max_max_alt_len_unlimit or max_alt_len <= max_max_alt_len) and ((min_max_alt_len_unlimit or max_alt_len >= min_max_alt_len)) and (max_diff_len_unlimit or diff_len <= max_diff_len) and (min_diff_len_unlimit or diff_len >= min_diff_len)):
            cnt += 1

print(cnt)