# Bookmark
リンク集のhtmlページ

リンクを入力したテキストファイルから、htmlファイルを生成します。

## デモ

リンクを入力したテキストファイルの例

```
title---リンク集

;;グループに分けることができる。'>>>'に続けてグループ名

>>> SNS
YouTube---https://www.youtube.com/  ;;タイトルとリンクを'---' で区切る
Twitter---https://twitter.com/
Instagram---https://www.instagram.com/

>>> Google
メール---https://www.youtube.com/
カレンダー---https://calendar.google.com/calendar/
ドライブ---https://drive.google.com/drive/

;;  ';;'でコメント可
```

## 使い方

コマンドライン

```
python bookmark.py テキストファイル [保存先ディレクトリ]
```

GUI

```
python bookmark
```
