# pyfeat-from-camera
A sample program of recognizing an emotion from an image using a camera device.

## 動作環境
- Windows
- Python3.11

※Python3.12ではPyfeatのインストールでエラーが出る

## 事前準備
- Pyfeatの依存モジュールが使用するDLLをインストールするために、Visual Studioをインストールする。
  - [公式サイト](https://visualstudio.microsoft.com/ja/downloads/)から「コミュニティ」を選んでダウンロード
  - インストールの際には、「C＋＋によるデスクトップ開発」にチェックを入れてインストールする。

## 仮想環境の作成
- `py -3.11 -m venv myenv`

## モジュールのインストール
- `myenv\Script\activate`
- `pip install opencv-python py-feat`
- `pip install scipy==1.13.0`

※scipyのバージョンは1.13.0にしないとエラーが出る。

## プログラムの実行
- `myenv\Script\activate`
- `python sample.py`

## その他
- 12th Gen Intel(R) Core(TM) i7-1265U で処理にかかる時間は1フレーム約1秒。
