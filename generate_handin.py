with open(f"result-enzh.txt", "w") as fout:
    # news
    with open(f"data/newstest2021.en-zh.src.en", "r") as fsrc, open(f"data/newstest2021.en-zh.ref.A.zh", "r") as fref, open(f"data/en-zh.out", "r") as f6x6, open(f"data/en-zh_24x6.out", "r") as f24x6:
        src = fsrc.readlines()
        ref = fref.readlines()
        h6x6 = f6x6.readlines()
        h24x6 = f24x6.readlines()

        assert(len(src) == len(ref) and len(ref) == len(h6x6) and len(h6x6) == len(h24x6))

        length = len(src)
        for i in range(length):
            string = src[i].strip() + '\t' + ref[i].strip() + '\t' + h6x6[i].strip() + '\t' + h24x6[i].strip() + '\n'
            fout.write(string)

    # biomedical
    with open(f"data/medline_en2zh_en.txt", "r") as fsrc, open(f"data/med_en-zh_ref.out", "r") as fref, open(f"data/med_en-zh.out", "r") as f6x6, open(f"data/med_en-zh_24x6.out", "r") as f24x6:
        src1 = fsrc.readlines()
        ref = fref.readlines()
        h6x6 = f6x6.readlines()
        h24x6 = f24x6.readlines()

        src1 = [string.split('\t') for string in src1]
        src = []

        doc = src1[0][0]

        string = str()
        for i in src1:
            if doc != i[0]:
                src.append(string)
                string = str()
                doc = i[0]
            string += i[2].strip()

        src.append(string)

        assert(len(src) == len(ref) and len(ref) == len(h6x6) and len(h6x6) == len(h24x6))

        length = len(src)
        for i in range(length):
            string = src[i].strip() + '\t' + ref[i].strip() + '\t' + h6x6[i].strip() + '\t' + h24x6[i].strip() + '\n'
            fout.write(string)

with open(f"result-zhen.txt", "w") as fout:
    # news
    with open(f"data/newstest2021.zh-en.src.zh", "r") as fsrc, open(f"data/newstest2021.zh-en.ref.A.en", "r") as fref, open(f"data/zh-en.out", "r") as f6x6, open(f"data/zh-en_24x6.out", "r") as f24x6:
        src = fsrc.readlines()
        ref = fref.readlines()
        h6x6 = f6x6.readlines()
        h24x6 = f24x6.readlines()

        assert(len(src) == len(ref) and len(ref) == len(h6x6) and len(h6x6) == len(h24x6))

        length = len(src)
        for i in range(length):
            string = src[i].strip() + '\t' + ref[i].strip() + '\t' + h6x6[i].strip() + '\t' + h24x6[i].strip() + '\n'
            fout.write(string)

    # biomedical
    with open(f"data/medline_zh2en_zh.txt", "r") as fsrc, open(f"data/med_zh-en_ref.out", "r") as fref, open(f"data/med_zh-en.out", "r") as f6x6, open(f"data/med_zh-en_24x6.out", "r") as f24x6:
        src1 = fsrc.readlines()
        ref = fref.readlines()
        h6x6 = f6x6.readlines()
        h24x6 = f24x6.readlines()

        src1 = [string.split('\t') for string in src1]
        src = []

        doc = src1[0][0]

        string = str()
        for i in src1:
            if doc != i[0]:
                src.append(string)
                string = str()
                doc = i[0]
            string += i[2].strip()

        src.append(string)

        assert(len(src) == len(ref) and len(ref) == len(h6x6) and len(h6x6) == len(h24x6))

        length = len(src)
        for i in range(length):
            string = src[i].strip() + '\t' + ref[i].strip() + '\t' + h6x6[i].strip() + '\t' + h24x6[i].strip() + '\n'
            fout.write(string)