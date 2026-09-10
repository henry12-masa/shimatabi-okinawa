# しまたび沖縄（沖縄観光ポータルサイト）

沖縄本島（那覇・北谷・恩納村・本部北部）の観光スポット・グルメ情報を集約した静的HTMLポータルサイト。航空券は楽天トラベル／じゃらん／Skyscannerへの外部リンクで連携。

- 公開URL: https://shimatabi-okinawa.napoblog.com （旧: https://shimatabi-okinawa.pages.dev も引き続き有効）
- GitHub: https://github.com/henry12-masa/shimatabi-okinawa
- ホスティング: Cloudflare Pages（GitHub連携で自動デプロイ、main pushで反映）

## 構成

```
okinawa_portal/
├── index.html        トップページ（エリア紹介・人気スポット/グルメのピックアップ）
├── spots.html         観光スポット一覧（エリア別フィルタ付き）
├── restaurants.html   グルメ一覧（ジャンル別フィルタ付き）
├── flights.html       航空券比較・外部サイト連携ページ
├── css/style.css      共通スタイル
├── js/main.js         モバイルナビ／絞り込みフィルタ／航空券検索リンク生成
└── .claude/launch.json  ローカル確認用サーバー設定（プロジェクトルート note/ に配置）
```

## ローカルで確認する方法

`note/.claude/launch.json` に `okinawa-portal` サーバー設定を追加済み。Claude Codeのプレビュー機能、または以下で確認できる。

```bash
python -m http.server 8834 --directory okinawa_portal
```

## 航空券アフィリエイトについて

- **楽天トラベル**: 設定済み（2026-09-10）。`flights.html` 内の「楽天トラベル」リンク（partner-cardと footer）は Rakuten Affiliate で発行した `hb.afl.rakuten.co.jp` 経由の計測リンクになっている。国内航空券ページ（`travel.rakuten.co.jp/air/domestic.html`）向け、料率1.0%。動作確認済み（`scid=af_pc_etc` 付きで遷移することを確認）。
- **じゃらん**: 設定済み（2026-09-10）。A8.net経由で「【じゃらんｎｅｔ】宿泊予約」プログラムと提携済みだったため、`flights.html` 内の「じゃらん」リンクを `px.a8.net/svt/ejp?a8mat=...` の計測リンクに差し替え済み（成果報酬: 予約金額の1%）。動作確認済み。
- Skyscannerへのリンクはアフィリエイト登録不要な検索結果ディープリンク形式を使用している（対応不要）。

## 今後の拡張候補

- 掲載スポット・グルメの画像追加（著作権フリー素材 or 自前撮影）
- 楽天トラベル/じゃらんのホテル比較セクション追加
- 実際のアフィリエイトIDを設定後の効果測定（Amazon運用と同様、URLパラメータでの流入元トラッキング）
