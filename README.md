# Image2pdf
画像をpdfに変換する

## 使い方
```
> python Image2pdf.py < hogehoge
```
※hogehogeは画像の入ったディレクトリ

hogehoge.pdfがカレントに作成されます。
hogehogeは相対パス、絶対パスも可能です。
その際は、指定したパスにpdfが生成されます。

## ライブラリ
reportlabを使用しています。
pipがインストールされている環境では、以下のコマンドでインストールできます。
```
> pip install rlextra -i https://www.reportlab.com/pypi/
```

## 動作確認
Windows 7 + python 2.7 で確認しました。
ほかの環境ではまだ確認していません...。
