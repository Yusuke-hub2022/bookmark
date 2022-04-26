# Bookmark
htmlのリンク集を作る

ブックマークをwebページとして作るためのツール。テキストファイルにリンクを入力した後、ツールを実行してhtmlファイルを生成します。

## 準備

リンクをテキストファイルに入力する。

```
title---リンク集

>>> SNS
YouTube---https://www.youtube.com/
Twitter---https://twitter.com/
Instagram---https://www.instagram.com/

>>> Google
メール---https://www.youtube.com/
カレンダー---https://calendar.google.com/calendar/
ドライブ---https://drive.google.com/drive/
```

## 使い方

コマンドラインで以下を実行

```
python bookmark.py テキストファイル [保存先ディレクトリ]
```

## その他機能

- 「;;」に続けてコメントの入力ができる。
- htmlファイルはローカルに置いても使える。Vue.jsではできなかった。
- CSSの編集可。（css/style.css）
- CSS内で、FontAwsome 使用可。
