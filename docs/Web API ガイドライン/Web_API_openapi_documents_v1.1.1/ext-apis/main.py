import json

def validate_json(data):
  """
  引数として与えられたJSONデータに対して、以下のルールに適合しない行とその内容を表示する関数

  Args:
    data: 検証対象のJSONデータ (dict形式)

  Returns:
    None
  """

  errors = []

  # "properties" キーが存在する場合
  if "properties" in data:
    for i, property_data in enumerate(data["properties"], start=1):
      # "descriptions" キーが存在する場合
      if "descriptions" in property_data:
        for lang, description in property_data["descriptions"].items():
          # "en" キーが存在し、かつ英語の文章形式ではない場合
          if lang == "en" and is_english_sentence(description):
            errors.append(f"行 {get_line_number(data, i)}: {property_data['name']} の 'en' 説明が英語の文章形式ではありません: {description}")

  # "actions" キーが存在する場合
  if "actions" in data:
    for action_data in data["actions"]:
      # "descriptions" キーが存在する場合
      if "descriptions" in action_data:
        for lang, description in action_data["descriptions"].items():
          # "en" キーが存在し、かつ英語の文章形式ではない場合
          if lang == "en" and not is_english_sentence(description):
            errors.append(f"行 {get_line_number(data, i)}: {action_data['name']} の 'en' 説明が英語の文章形式ではありません: {description}")

  if errors:
    print("以下の行がルールに違反しています:")
    for error in errors:
      print(error)
  else:
    print("すべての行がルールに適合しています。")

def is_english_sentence(text):
  """
  引数として与えられた文字列が英語の文章形式かどうかを判定する関数

  Args:
    text: 判定対象の文字列

  Returns:
    True: 英語の文章形式である場合
    False: 英語の文章形式ではない場合
  """

  # 頭文字が小文字で、文末にピリオドがない場合は英語の文章形式ではないと判定
  if text[0].islower():
    return False
  if not text.endswith("."):
    return False
  return True

def get_line_number(data, index):
  """
  JSONデータとインデックスに基づいて、該当する行番号を取得する関数

  Args:
    data: 検証対象のJSONデータ (dict形式)
    index: 行番号を取得したい要素のインデックス

  Returns:
    該当する行番号
  """

  # データを文字列に変換
  data_str = json.dumps(data, indent=4)

  # 行番号を取得
  lines = data_str.splitlines()
  for i, line in enumerate(lines):
    if str(index) in line:  # Convert index to string before checking
      return i + 1

# 検証対象のJSONデータを用意
json_data = {
  "properties": [
    {
      "name": "商品A",
      "descriptions": {
        "ja": "これは商品Aの説明です。",
        "en": "a description of product A"
      }
    },
    {
      "name": "商品B",
      "descriptions": {
        "ja": "これは商品Bの説明です。",
        "en": "A description. Not a sentence."
      }
    }
  ],
  "actions": [
    {
      "name": "アクションA",
      "descriptions": {
        "ja": "これはアクションAの説明です。",
        "en": "Perform action A."
      }
    },
    {
      "name": "アクションB",
      "descriptions": {
        "ja": "これはアクションBの説明です。",
        "en": "This is a description of action B."
      }
    }
  ]
}

# JSONデータの検証を実行
validate_json(json_data)
