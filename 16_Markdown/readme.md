# 📘 Markdown — wprowadzenie

## 🧾 Co to jest Markdown?

**Markdown** to lekki język znaczników (lightweight markup language), którego celem jest umożliwienie **łatwego formatowania tekstu** w sposób czytelny zarówno dla człowieka, jak i maszyny.

Został stworzony przez **Johna Grubera** i **Aarona Swartza** w 2004 roku, aby uprościć proces pisania tekstów, które potem są konwertowane do HTML.

Markdown jest:
- prosty i intuicyjny,
- czytelny jako zwykły tekst (bez renderowania),
- kompatybilny z wieloma narzędziami.

---

## ✍️ Składnia Markdown — podstawy

| Cel | Składnia | Przykład | Efekt |
|-----|----------|----------|-------|
| **Nagłówki** | `#`, `##`, `###` itd. | `## Tytuł` | Tytuł |
| **Pogrubienie** | `**tekst**` lub `__tekst__` | `**ważne**` | **ważne** |
| **Kursywa** | `*tekst*` lub `_tekst_` | `*pochylony*` | *pochylony* |
| **Lista nieuporządkowana** | `-`, `*` lub `+` | `- punkt` | • punkt |
| **Lista uporządkowana** | `1.`, `2.` itd. | `1. Start` | 1. Start |
| **Kod w linii** | `` `kod` `` | `` `print("hi")` `` | `print("hi")` |
| **Blok kodu** | \`\`\`python <br> kod <br> \`\`\` | patrz niżej | zobacz poniżej |
| **Link** | `[tekst](adres)` | `[Google](https://google.com)` | [Google](https://google.com) |
| **Obrazek** | `![alt](url)` | `![logo](logo.png)` | ![logo](logo.png) |
| **Cytat** | `> cytat` | `> mądrość` | > mądrość |
| **Linia pozioma** | `---` lub `***` | `---` | ———— |

### Przykład bloku kodu:
````python
```python
def hello():
    print("Hello, world!")
```
