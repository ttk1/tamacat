# tamacat

Python で cat コマンドを雑に実装。

## インストール

```sh
pip install git+https://github.com/ttk1/tamacat.git

# もしくは
git clone https://github.com/ttk1/tamacat.git
cd tamacat
pip install .
```

## 使い方

### ファイル一つ

```sh
$ echo 'hello!' > hoge
$ tamacat hoge
hello!
```

### ファイル複数

```sh
$ echo 'hello!' > hoge2
$ tamacat hoge*
hello!
hello!
```

### 標準出力

```sh
$ echo 'hello!' | tamacat
hello!
```

### help

```sh
tamacat -h
```
