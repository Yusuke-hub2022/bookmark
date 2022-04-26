# Bookmark
htmlのリンク集を作る

ブックマークをwebページにしたいときに使えるツールです。
テキストファイルにリンクを入力した後、ツールを実行してhtmlファイルを生成します。

## デモ

例えば links.txt に次のように入力します。

```
title: リンク集

>>> SNS
YouTube---https://www.youtube.com/
Twitter---https://twitter.com/
Instagram---https://www.instagram.com/

>>> Google
メール---https://www.youtube.com/
カレンダー---https://calendar.google.com/calendar/
ドライブ---https://drive.google.com/drive/
```

そしてコマンドラインでプログラムを実行します。

```
$ python bookmark.py links.txt
```

すると、下記の inks.html が生成されます。

```
<!doctype html>
<html>
<head>
<title>リンク集</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link href="css/style.css" rel="stylesheet" type="text/css">
<link href="https://use.fontawesome.com/releases/v6.1.1/css/all.css" rel="stylesheet">
</head>
<body>
<div id="contents">
  <div id="head"><h1>リンク集</h1></div>
  <div id="groups">

    <div class="group">
      <h2>SNS</h2>
      <ul class="links">
        <li><a href="https://www.youtube.com/">YouTube</a></li>
        <li><a href="https://twitter.com/">Twitter</a></li>
        <li><a href="https://www.instagram.com/">Instagram</a></li>
      </ul>
    </div>
    <div class="group">
      <h2>Google</h2>
      <ul class="links">
        <li><a href="https://www.youtube.com/">メール</a></li>
        <li><a href="https://calendar.google.com/calendar/">カレンダー</a></li>
        <li><a href="https://drive.google.com/drive/">ドライブ</a></li>
      </ul>
    </div>

  </div>
</div>
</body>
</html>
```

## 使い方

コマンドラインで以下を実行します。

```
$ python bookmark.py テキストファイル [保存先ディレクトリ]
```

## その他機能

- テキストファイルには「;;」に続けてコメントを入力することができます。
- もしも css/style.css がなければ自動で作られます。
- CSS内で、FontAwsome を使うことができます。
- htmlファイルはローカルに置いても使えます。Vue.jsではできませんでした。
