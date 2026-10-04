<!-- Version: v1.0 | Last modified: 2026-10-03 -->

# Outreach Email Signature Standard

How to sign project outreach emails (Gmail send, any language).

## Rules

1. **Send as HTML (`htmlBody`), never as a plain-text signature with bare URLs.** Gmail rewrites bare URLs in plain text into long `google.com/url?q=...` redirect links, which look messy (seen on the 2026-10-02 follow-ups to Sakoda, Karsten Klein and Komatsu).
2. **Show linked text, hide the real URL** behind it with an `<a href>`.
3. **Phone number as a tap-to-call link** (`tel:`).
4. **Sender:** project outreach goes from **rob@mitsue.it** when possible. The Gmail connector sends from **oudendijk.biz@gmail.com**, so check the From address before sending anything where the mitsue.it identity matters.
5. **Mascot:** Mitsue-kun image inline on the left when the mailbox/tool allows embedding it (assets are in `assets/`, for example `assets/Mitsue-kun_16-removebg-preview.png`). If it cannot be embedded, send the text block only.
6. **Do not describe the partners or the project as contracted** in the body (see the overstatement rule in the project notes).

## HTML signature block

```html
<p style="margin:0">
ロブ・アウデンダイク (Rob Oudendijk)<br>
YR-Design / Safecast ／ 御杖村 森林エネルギー事業<br>
Telephone: <a href="tel:+818022605966">+81 80-2260-5966</a><br>
Website: <a href="https://mitsue.it">mitsue.it</a><br>
Repository: <a href="https://tinyurl.com/2xv524fz">Project repository</a>
</p>
```

English-only emails can use "Rob Oudendijk (ロブ・アウデンダイク)" and "Mitsue Village forest-energy project" for the second line.

## Before sending

- Draft is shown to Rob and approved first.
- Body is HTML with the block above, and the plain-text version contains no bare tracking-prone URLs.
- Log the send in the AgentMesh Outreach tab.
