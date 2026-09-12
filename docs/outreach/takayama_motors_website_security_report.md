<!-- Version: v1.1 | Last modified: 2026-09-12 -->

<style>
  html { font-size: 9.5px !important; }
  body { line-height: 1.25 !important; }
  p, blockquote, ul, ol, dl, table { margin: 4px 0 !important; }
  h1, h2, h3 { margin-top: 5px !important; margin-bottom: 3px !important; }
  hr { margin: 5px 0 !important; }
  code { font-size: 0.95em !important; }
  pre { margin: 4px 0 !important; padding: 4px 6px !important; }
  .page-break { page-break-after: always; break-after: page; height: 0; margin: 0; padding: 0; }
</style>

# 株式会社髙山自動車 様 ウェブサイト診断報告

**診断対象:** takayama-motors.com　**診断ツール:** internet.nl（オランダ政府後援の公的Web診断サービス）　**総合スコア:** 45%

---

### 診断結果サマリー

| 項目 | 結果 | 内容 |
|---|---|---|
| IPv6対応 | ✕ 未対応 | Webサーバー・DNSともにIPv6アドレスなし |
| DNSSEC | ✕ 未対応 | ドメインの署名検証が無効。DNS改ざんに脆弱 |
| HTTPS強制転送 | ✕ なし | http://のアクセスが自動でhttps://へ転送されない |
| HSTS設定 | ✕ なし | ブラウザにHTTPS常時使用を指示するヘッダーが未設定 |
| 暗号化強度 | △ 弱い | 古い暗号方式（SHA1、弱いDH鍵）が使用可能 |
| セキュリティヘッダー | ✕ 未設定 | クリックジャッキング・XSS対策ヘッダーが欠如 |
| security.txt | ✕ なし | 脆弱性報告窓口ファイル未設置（小規模事業者では省略可） |
| RPKI（経路保護） | ✓ 有効 | 通信経路の乗っ取り対策は適切に機能 |

なぜ重要か：これらはサイトを見ただけでは分からない技術的な項目ですが、①お客様が入力する情報（見積依頼・車検予約など）の保護、②Googleなど検索エンジンでの評価・検索順位、③「このサイトは安全です」というブラウザ表示に関わります。特に上位2項目は対応の効果が高く、作業も比較的簡単です。

### 対応方法（優先度順）

**1. HTTPS強制転送 + HSTS設定（最優先・効果大）**
現状、`http://takayama-motors.com` でアクセスした場合、暗号化なしのページがそのまま表示されてしまいます。多くのレンタルサーバー（さくら、Xserver、ロリポップ等）では管理画面に「常時SSL化」「HTTPS強制」といった設定項目があり、チェックを入れるだけで解決します。管理画面に項目が見当たらない場合は、サーバー会社のサポート窓口へ以下のように問い合わせてください：

> 「httpでアクセスした際にhttpsへ自動転送されるよう設定し、あわせてHSTSヘッダー（Strict-Transport-Security）を有効にしてください」

自社でサーバー設定ファイル（.htaccess）を編集できる場合は、以下を追記します：
```
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
```

**2. セキュリティヘッダーの追加（作業は簡単）**
同じ.htaccessファイルに以下を追記するだけで、クリックジャッキングやXSS攻撃への基本的な防御が有効になります：
```
Header set X-Frame-Options "SAMEORIGIN"
Header set X-Content-Type-Options "nosniff"
Header set Referrer-Policy "strict-origin-when-cross-origin"
```
自社での編集が難しい場合は、上記コードをそのままサーバー会社のサポートに渡せば設定してもらえます。

**3. 暗号化設定の見直し（サーバー会社対応が必要）**
古い暗号方式（SHA1、弱いDH鍵、TLS1.0/1.1）が有効なままです。自社での変更は難しいため、サーバー会社に以下のように伝えてください：

> 「internet.nlの診断でSHA1・弱いDiffie-Hellmanパラメータの使用を指摘されました。TLS1.2/1.3のみを許可し、古い暗号方式を無効化してください」

**4. DNSSEC（ドメイン管理会社への依頼）**
ドメインを購入した会社（お名前.com、ムームードメイン等）の管理画面に「DNSSEC」の設定項目があるか確認し、有効化を依頼してください。ドメインとサーバーの会社が異なる場合は両社への確認が必要です。

**5. IPv6対応（優先度は低い・中長期）**
現在のホスティングプランがIPv6に対応していない可能性があります。急ぎではありませんが、サーバー乗り換えや契約更新のタイミングで確認すると良い項目です。

### 対応後の確認方法
すべて対応後、再度 https://internet.nl でtakayama-motors.comを診断すると、スコアの改善が確認できます（無料・登録不要）。

**ご報告者:** Rob Oudendijk（御杖村 AIデータセンタープロジェクト）

<div class="page-break"></div>

# Website Security Report — Takayama Motors Co., Ltd.

**Site tested:** takayama-motors.com　**Tool:** internet.nl (Dutch government-backed public web diagnostic service)　**Overall score:** 45%

---

### Summary of Findings

| Category | Result | Details |
|---|---|---|
| IPv6 support | ✕ Fail | No IPv6 address on the web server or DNS |
| DNSSEC | ✕ Fail | Domain is not signed; vulnerable to DNS spoofing |
| HTTPS redirect | ✕ Fail | http:// does not automatically redirect to https:// |
| HSTS header | ✕ Fail | No header instructing browsers to always use HTTPS |
| Cipher strength | △ Weak | Outdated ciphers available (SHA1, weak Diffie-Hellman) |
| Security headers | ✕ Fail | Clickjacking and XSS protection headers all missing |
| security.txt | ✕ Missing | No vulnerability-disclosure contact file (fine to skip for a small business) |
| RPKI (route protection) | ✓ Pass | Route hijack protection is correctly in place |

Why it matters: these items are invisible to a casual visitor, but affect (1) protection of data customers submit (quote requests, inspection bookings), (2) how search engines like Google rank the site, and (3) the browser's "this site is secure" indicator. The top two items below give the biggest improvement for the least effort.

### How to Fix Each Issue (in priority order)

**1. Enable HTTPS redirect + HSTS (highest priority, biggest impact)**
Right now, visiting `http://takayama-motors.com` serves the unencrypted page directly instead of redirecting. Most Japanese hosting providers (Sakura, Xserver, Lolipop, etc.) have a control-panel toggle for "force SSL" / "always use HTTPS" — enabling it solves this. If no such option is visible, ask the hosting provider's support team:

> "Please configure automatic redirection from http to https, and enable the HSTS header (Strict-Transport-Security)."

If you or a developer can edit the server's `.htaccess` file directly, add:
```
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
```

**2. Add security headers (simple, low effort)**
Add the following to the same `.htaccess` file to enable basic protection against clickjacking and cross-site scripting attacks:
```
Header set X-Frame-Options "SAMEORIGIN"
Header set X-Content-Type-Options "nosniff"
Header set Referrer-Policy "strict-origin-when-cross-origin"
```
If self-editing isn't practical, this snippet can simply be forwarded to the hosting provider's support team to apply.

**3. Review cipher/TLS settings (requires hosting provider)**
Outdated cryptographic settings (SHA1, weak Diffie-Hellman parameters, TLS 1.0/1.1) are still enabled. This typically can't be changed by the site owner directly — ask the hosting provider:

> "internet.nl flagged SHA1 and weak Diffie-Hellman parameters on our TLS configuration. Please restrict the server to TLS 1.2/1.3 only and disable outdated ciphers."

**4. DNSSEC (requires the domain registrar)**
Check the control panel of the company where the domain was registered for a "DNSSEC" option and ask them to enable it. If the domain registrar and hosting provider are different companies, both may need to be involved.

**5. IPv6 support (lower priority, medium-term)**
The current hosting plan may not support IPv6 addressing. Not urgent, but worth checking next time the hosting plan is renewed or migrated.

### Verifying the Fixes
After making changes, re-run the free test at https://internet.nl on takayama-motors.com (no signup required) to confirm the score has improved.

**Reported by:** Rob Oudendijk (Mitsue Village AI Data Center Project)
