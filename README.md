# **CJK Unified Ideographs Dictionary**

### **全訳CJK統合漢字辞典プロジェクト**

Documentation for the Python Generator and the resulting HTML Dictionary.

Pythonジェネレーターと生成されるHTML辞書のためのドキュメント。

## **Part 1: The Code**

### **Python Generator Script (Pythonジェネレーター・スクリプト)**

The core of this project is a robust Python script named `generate_cjk_full.py`. Its sole purpose is to fetch raw data and transform it into a usable format.

このプロジェクトの核となるのは、`generate_cjk_full.py` という堅牢なPythonスクリプトです。その目的は、生データを取得し、使用可能な形式に変換することです。

#### **🔧 Functionality / 機能**

* **Automated Download:** Connects to the official Unicode.org servers and downloads the latest `Unihan.zip` database (\~8MB).  
  **自動ダウンロード:** 公式Unicode.orgサーバーに接続し、最新の`Unihan.zip`データベース（約8MB）をダウンロードします。  
* **Intelligent Parsing:** Scans the ZIP archive to find the `RadicalStrokeCounts` file, regardless of folder structure changes or hidden files.  
  **インテリジェント解析:** ZIPアーカイブをスキャンして、フォルダ構成の変更や隠しファイルに関係なく、正しい`RadicalStrokeCounts`ファイルを見つけ出します。  
* **Data Sorting:** Sorts over 100,000 characters by Radical (Busyu), then by Stroke Count, then by Unicode Code Point.  
  **データソート:** 10万文字以上の漢字を、部首（Busyu）→ 画数 → Unicodeコードポイントの順にソートします。

#### **💻 How to Run / 実行方法**

No external libraries are required. Simply run the script with Python 3\.

外部ライブラリは不要です。Python 3でスクリプトを実行するだけです。

python `generate_cjk_full.py`

**Terminal Output Example:**
```bash
1. Downloading https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip...
   Download complete (8.12 MB).
2. Scanning ALL files in ZIP...
   8 files found in archive.
   -> Inspecting: Unihan_DictionaryIndices.txt
   -> Inspecting: Unihan_DictionaryLikeData.txt
   -> Inspecting: Unihan_IRGSources.txt
      SUCCESS! 102998 entries found in Unihan_IRGSources.txt.
   -> Inspecting: Unihan_NumericValues.txt
   -> Inspecting: Unihan_OtherMappings.txt
   -> Inspecting: Unihan_RadicalStrokeCounts.txt
   -> Inspecting: Unihan_Readings.txt
   -> Inspecting: Unihan_Variants.txt
   TOTAL: 102944 characters extracted.
3. Sorting data...
4. Generating cjk_full_busyu_ja_en.html...
Finished! Open 'cjk_full_busyu_ja_en.html' to see the result.

```

## **Part 2: The Output**

### **The Generated Dictionary (生成された辞書ファイル \- HTML)**

Upon successful execution, the script generates a standalone file named `cjk_full_busyu_ja_en.html`. This is the final product.

実行が成功すると、スクリプトは`cjk_full_busyu_ja_en.html`というスタンドアロンファイルを生成します。これが最終成果物です。

#### **📄 Interface Features / インターフェースの特徴**

* **Sidebar Navigation:** A fixed sidebar on the left lists all 214 Kangxi Radicals for quick jumping.  
  **サイドバーナビゲーション:** 左側の固定サイドバーには、全214の康熙部首がリストアップされており、素早くジャンプできます。  
* **Radical Sections:** The main view is divided into clear sections for each radical, displaying the radical number and character (e.g., R1 一).  
  **部首セクション:** メインビューは部首ごとに明確に区分され、部首番号と文字（例：R1 一）が表示されます。  
* **Stroke Grouping:** Within each radical, characters are grouped by their additional stroke count (e.g., +0 Strokes, +1 Stroke).  
  **画数グルーピング:** 各部首内で、文字は追加画数ごとにグループ化されます（例：+0画、+1画）。  
* **Extensions Included:** Unlike standard web fonts, this dictionary allows browsing of Extensions A, B, C, D, E, F, G, H, I, and J seamlessly.  
  **全拡張対応:** 標準的なWebフォントとは異なり、この辞書では拡張A〜Jまでの文字をシームレスに閲覧できます。

#### **🌍 Localization / ローカライズ**

The HTML interface is fully bilingual. All headers, labels, and descriptions are provided in both English and Japanese.

HTMLインターフェースは完全なバイリンガル対応です。すべての見出し、ラベル、説明文は英語と日本語の両方で提供されます。

**Project maintained by PINKARA / プロジェクト管理者: PINKARA** *Data Source: The Unicode Consortium*
