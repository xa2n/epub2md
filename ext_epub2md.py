import pypandoc
import os

# epub ファイルがあるディレクトリと markdown ファイルを保存するディレクトリ
epub_dir = "/volumes/ct1tb/books/epub"
markdown_dir = "/volumes/ct1tb/books/markdown"

# epub ディレクトリ内のすべての epub ファイルを取得
for filename in os.listdir(epub_dir):
    if filename.endswith(".epub"):
        epub_file = os.path.join(epub_dir, filename)
        markdown_file = os.path.join(markdown_dir, filename.replace(".epub", ".md"))

        # 例外処理を追加
        try:
            # pypandoc を使って変換を実行
            pypandoc.convert_file(
                epub_file,
                "md",
                outputfile=markdown_file,
                extra_args=["--extract-media=."],
            )

            print(f"{epub_file} を {markdown_file} に変換しました。")
        except Exception as e:
            # エラーが発生した場合、エラーメッセージを出力
            print(f"{epub_file} の変換中にエラーが発生しました: {e}")
