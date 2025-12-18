# WorkTrack（工数管理アプリ）

## 概要

**WorkTrack** は、Django を用いて作成したシンプルな業務管理・学習用 Web アプリケーションです。
業務系システムを想定した工数管理アプリです。
日次の工数入力、月次集計、管理者確認を行うことを目的としています。
ログイン認証、ダッシュボード表示など、Web アプリ開発の基礎構成を一通り実装しています。

本リポジトリは **ポートフォリオ提出用** として整理しています。

---

## 主な機能

- ユーザー認証（ログイン / ログアウト）
- ログイン後のダッシュボード表示
- Django 標準認証機能の利用
- テンプレート継承（base.html）による共通レイアウト

---

## 使用技術

- Python 3.12
- Django 6.0
- SQLite3（開発用）
- HTML / Bootstrap（UI）

---

## ディレクトリ構成（主要部分）

```
worktrack/
├── backend/        # Django プロジェクト設定
├── core/           # メインアプリ
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   └── dashboard.html
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── db.sqlite3      # 開発用DB（※GitHubには含めていません）
├── manage.py
└── requirements.txt
```

---

## セットアップ手順

### 1. リポジトリをクローン

```bash
git clone https://github.com/＜ユーザー名＞/＜リポジトリ名＞.git
cd worktrack
```

### 2. 仮想環境を作成・有効化

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. 必要パッケージをインストール

```bash
pip install -r requirements.txt
```

### 4. マイグレーション

```bash
python manage.py migrate
```

### 5. 管理ユーザー作成（任意）

```bash
python manage.py createsuperuser
```

### 6. サーバー起動

```bash
python manage.py runserver
```

ブラウザで以下にアクセス：

```
http://127.0.0.1:8000/
```

---

## ポートフォリオとしてのポイント

- Django の基本構成（settings / urls / views / templates）を理解して構築
- テンプレート探索エラーなどのトラブルを自己解決し、構成を整理
- ログイン制御・リダイレクト処理の実装
- GitHub によるバージョン管理

---

## 今後の改善予定

- CRUD 機能の追加
- モデル設計の拡張
- UI の改善
- Docker 化

---

## 補足

- `SECRET_KEY` や `venv`、`db.sqlite3` は `.gitignore` により除外しています
- 本番運用を想定した設定ではありません

---

## 作成者

浦島 啓

---

※ 本リポジトリは学習・ポートフォリオ目的で作成しています。
