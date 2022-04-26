# Bookmark
リンク集のhtmlページ

リンクを入力したテキストファイルから、htmlファイルを生成します。

## デモ

リンクを入力したテキストファイルの例

```
title---リンク集

;;グループに分けることができる。'>>>'に続けてグループ名

>>> SNS
YouTube---https://www.youtube.com/  ;;タイトルとURLを'---' で区切る
Twitter---https://twitter.com/
Instagram---https://www.instagram.com/

>>> Google
メール---https://www.youtube.com/
カレンダー---https://calendar.google.com/calendar/
ドライブ---https://drive.google.com/drive/

;;  ';;'でコメント可
```

## 使い方

コマンドラインで以下を実行

```
python bookmark.py テキストファイル [保存先ディレクトリ]
```

## 特徴

- htmlファイルはローカルに置いても使える。Vue.jsではできなかった。
- CSSの編集可。（css/style.css）
- CSS内に限り、FontAwsome を使うことができる。
