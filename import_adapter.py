#!/usr/bin/python

import pypinyin
import pandas as pd
import sys
import csv


class ImportAdapter:
    def process(self, input_filename, output_filename):
        print("Reading input file: {}..".format(input_filename))
        df = pd.read_csv(input_filename,
                         header=None,
                         names=['Vocabulary'])
        if df.shape[1] != 1:
            raise ValueError("Invalid input file")
        df.drop_duplicates(inplace=True)
        df['zhuyin'] = df['Vocabulary'].apply(
            lambda x: self.to_zhuyin(x))
        with open(output_filename, "w", encoding='utf-16le') as txt:
            txt.write('\ufeff')
            for index, row in df.iterrows():
                txt.write("{}  {}\n".format(row['Vocabulary'],
                                     row['zhuyin']))
            print("Result is written to {}".format(output_filename))

    def to_zhuyin(self, astr):
        zhuyin_list = pypinyin.pinyin(astr, style=pypinyin.Style.BOPOMOFO)
        zhuyin_list = [self.adapt_format(pin[0]) for pin in zhuyin_list]
        zhuyin = " ".join(zhuyin_list)
        return zhuyin

    def adapt_format(self, zhuyin_compact):
        zhuyin_formatted = ["　", "　", "　", "　"]
        for i, pin in enumerate(zhuyin_compact):
            if pin in ['ㄅ','ㄆ','ㄇ','ㄈ','ㄉ','ㄊ','ㄋ','ㄌ',
                       'ㄍ','ㄎ','ㄏ','ㄐ','ㄑ','ㄒ',
                       'ㄓ','ㄔ','ㄕ','ㄖ','ㄗ','ㄘ','ㄙ']:
                zhuyin_formatted[0] = pin
            elif pin in ['ㄧ','ㄨ','ㄩ']:
                zhuyin_formatted[1] = pin
            elif pin in ['ㄚ','ㄛ','ㄜ','ㄝ','ㄞ','ㄟ','ㄠ','ㄡ',
                         'ㄢ','ㄣ','ㄤ','ㄥ','ㄦ']:
                zhuyin_formatted[2] = pin
            elif pin in ['ˋ', 'ˊ', 'ˇ','˙']:
                zhuyin_formatted[3] = pin
            else:
                raise ValueError('Illegal character found: {}'.format(pin))
        if zhuyin_formatted[3] == '　':
            zhuyin_formatted[3] = 'ˉ'
        return ''.join(zhuyin_formatted)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python import_adapter.py <input.txt> <output.txt>")
        sys.exit(1)
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    import_adapter = ImportAdapter()
    import_adapter.process(input_filename, output_filename)
