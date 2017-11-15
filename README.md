# IME-phonetic-importer
A helper tool for importing custom vocabularies into Microsoft New Phonetic IME

微軟新注音輸入法[使用者造詞](https://www.techbang.com/posts/19800-how-to-win-7-related-term-editing-tools-pchome224drj)的匯入幫助工具

For more information about 使用者造詞: https://www.google.com.tw/search?q=使用者造詞


## Motivation
微軟新注音的使用者造詞除了手動輸入外，還有匯入功能，但其匯入功能要求單詞要附加注音並遵守一定格式，
這個script可以將一份新詞清單轉換成使用者造詞工具接受的格式。

The Custom Vocabulary Tool in Microsoft New Phonetic IME supports importing, but it only accepts an odd format.
This script is used to transform a list of custom vocabularies into proper format accepted by Microsoft New Phonetic IME.


## Prerequisites:
- Python 3
- [pypinyin](https://github.com/mozillazg/python-pinyin)
- [pandas](http://pandas.pydata.org/)


## Usage
Putting custom vocabularies into a text file (single vocabulary for each line), and then use the script to transform it by the following command:

`python import_adapter.py <input.txt> <output.txt>`


## Example
```
python import_adapter.py test_input.txt test_output.txt`

// test_input.txt
小確幸
過譽
銅鋰鋅
已知用火

// test_output.txt
小確幸  ㄒㄧㄠˇ ㄑㄩㄝˋ ㄒㄧㄥˋ
過譽  ㄍㄨㄛˋ 　ㄩ　ˋ
銅鋰鋅  ㄊㄨㄥˊ ㄌㄧ　ˇ ㄒㄧㄣˉ
已知用火  　ㄧ　ˇ ㄓ　　ˉ 　ㄩㄥˋ ㄏㄨㄛˇ
```

## Contributing
Any thougt or feedback is welcome :)
