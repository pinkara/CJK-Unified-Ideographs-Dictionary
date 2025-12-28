import urllib.request
import zipfile
import io
import re
import os

# --- CONFIGURATION --- 
UNIHAN_URL = "https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip"

# Liste des 214 Radicaux Kangxi (Kangxi Radicals)
KANGXI_RADICALS = [
    "一", "丨", "丶", "丿", "乙", "亅", "二", "亠", "人", "儿", "入", "八", "冂", "冖", "冫", "几", "凵", "刀", "力", "勹", "匕", "匚", "匸", "十", "卜", "卩", "厂", "厶", "又",
    "口", "囗", "土", "士", "夂", "夊", "夕", "大", "女", "子", "宀", "寸", "小", "尢", "尸", "屮", "山", "巛", "工", "己", "巾", "干", "幺", "广", "廴", "廾", "弋", "弓", "彐", "彡", "彳",
    "心", "戈", "戶", "手", "支", "攴", "文", "斗", "斤", "方", "无", "日", "曰", "月", "木", "欠", "止", "歹", "殳", "毋", "比", "毛", "氏", "气", "水", "火", "爪", "父", "爻", "爿", "片", "牙", "牛", "犬",
    "玄", "玉", "瓜", "瓦", "甘", "生", "用", "田", "疋", "疒", "癶", "白", "皮", "皿", "目", "矛", "矢", "石", "示", "禸", "禾", "穴", "立", "竹", "米", "糸", "缶", "网", "羊", "羽", "老", "而", "耒", "耳", "聿", "肉", "臣", "自", "至", "臼", "舌", "舛", "舟", "艮", "色", "艸", "虍", "虫", "血", "行", "衣", "襾",
    "見", "角", "言", "谷", "豆", "豕", "豸", "貝", "赤", "走", "足", "身", "車", "辛", "辰", "辵", "邑", "酉", "釆", "里",
    "金", "長", "門", "阜", "隶", "隹", "雨", "青", "非",
    "面", "革", "韋", "韭", "音", "頁", "風", "飛", "食", "首", "香",
    "馬", "骨", "高", "髟", "鬥", "鬯", "鬲", "鬼",
    "魚", "鳥", "鹵", "鹿", "麥", "麻",
    "黃", "黍", "黑", "黹",
    "黽", "鼎", "鼓", "鼠",
    "鼻", "齊",
    "齒",
    "龍", "龜",
    "龠"
]

def download_and_extract():
    print(f"1. Downloading {UNIHAN_URL}...")
    try:
        req = urllib.request.Request(
            UNIHAN_URL,
            data=None,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        response = urllib.request.urlopen(req)
        zip_data = response.read()
        print(f"   Download complete ({len(zip_data)/1024/1024:.2f} MB).")
        return zip_data
    except Exception as e:
        print(f"   CRITICAL ERROR: Cannot download Unihan. {e}")
        return None

def parse_unihan(zip_bytes):
    print("2. Scanning ALL files in ZIP...")
    cjk_map = []

    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
        # On liste tous les fichiers qui pourraient contenir du texte
        file_list = [n for n in z.namelist() if not n.endswith('/') and not n.startswith('__MACOSX') and not '/.' in n]

        print(f"   {len(file_list)} files found in archive.")

        for filename in file_list:
            if "ReadMe" in filename or "History" in filename:
                continue

            print(f"   -> Inspecting: {filename}")

            with z.open(filename) as f:
                krs_in_this_file = 0
                debug_lines = []

                for line in f:
                    try:
                        line_str = line.decode('utf-8').strip()
                    except:
                        continue

                    if not line_str or line_str.startswith('#'):
                        continue

                    if len(debug_lines) < 3:
                        debug_lines.append(line_str)

                    # Recherche de la propriété kRSUnicode
                    if 'kRSUnicode' in line_str:
                        krs_in_this_file += 1

                        parts = line_str.split()
                        try:
                            idx = parts.index('kRSUnicode')

                            code_str = parts[0].replace('U+', '')
                            code_point = int(code_str, 16)
                            char = chr(code_point)

                            if len(parts) > idx + 1:
                                rs_data = parts[idx + 1]
                                match = re.match(r"(\d+)'?\.(-?\d+)", rs_data)
                                if match:
                                    radical = int(match.group(1))
                                    strokes = int(match.group(2))

                                    cjk_map.append({
                                        'rad': radical,
                                        'str': strokes,
                                        'cp': code_point,
                                        'char': char
                                    })
                        except:
                            continue

                if krs_in_this_file > 0:
                    print(f"      SUCCESS! {krs_in_this_file} entries found in {filename}.")

    print(f"   TOTAL: {len(cjk_map)} characters extracted.")
    return cjk_map

def get_cjk_data():
    zip_data = download_and_extract()
    if zip_data:
        return parse_unihan(zip_data)
    return None
