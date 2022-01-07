from nemo.collections.nlp.models import MTEncDecModel

# Get the list of pre-trained models
MTEncDecModel.list_available_models()

# Download and load pre-trained models to translate
# 6x6 transformer models
model_enzh = MTEncDecModel.from_pretrained("nmt_en_zh_transformer6x6", map_location = 'cuda:0')
model_zhen = MTEncDecModel.from_pretrained("nmt_zh_en_transformer6x6", map_location = 'cuda:0')
# 24x6 transformer models
# model_enzh = MTEncDecModel.from_pretrained("nmt_en_zh_transformer24x6", map_location = 'cuda:0')
# model_zhen = MTEncDecModel.from_pretrained("nmt_zh_en_transformer24x6", map_location = 'cuda:0')

# Translate
# news
with open(f"data/newstest2021.en-zh.src.en", "r") as enzh_in, open(f"data/en-zh_24x6.out", "w") as enzh_out:
    src_text = enzh_in.readlines()
    src_text = [string.strip() for string in src_text]

    for i in src_text:
        translations_enzh = model_enzh.translate([i], source_lang="en", target_lang="zh")
        enzh_out.write(translations_enzh[0] + '\n')

with open(f"data/newstest2021.zh-en.src.zh", "r") as zhen_in, open(f"data/zh-en_24x6.out", "w") as zhen_out:
    src_text = zhen_in.readlines()
    src_text = [string.strip() for string in src_text]

    for i in src_text:
        translations_zhen = model_zhen.translate([i], source_lang="zh", target_lang="en")
        zhen_out.write(translations_zhen[0] + '\n')

# biomedical
with open(f"data/medline_en2zh_en.txt", "r") as enzh_in, open(f"data/med_en-zh.out", "w") as enzh_out:
    src_text = enzh_in.readlines()
    src_text = [string.split('\t') for string in src_text]

    doc = src_text[0][0]

    for i in src_text:
        if doc != i[0]:
            enzh_out.write('\n')
            doc = i[0]
        translations_enzh = model_enzh.translate([i[2].strip()], source_lang="en", target_lang="zh")
        enzh_out.write(translations_enzh[0])

with open(f"data/medline_zh2en_zh.txt", "r") as zhen_in, open(f"data/med_zh-en.out", "w") as zhen_out:
    src_text = zhen_in.readlines()
    src_text = [string.split('\t') for string in src_text]

    doc = src_text[0][0]
    
    for i in src_text:
        if doc != i[0]:
            zhen_out.write('\n')
            doc = i[0]
        translations_zhen = model_zhen.translate([i[2].strip()], source_lang="zh", target_lang="en")
        zhen_out.write(translations_zhen[0])