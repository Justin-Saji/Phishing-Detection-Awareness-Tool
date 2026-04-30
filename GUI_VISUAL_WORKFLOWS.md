# GUI Enhancement - Visual Workflow Guide

## 🎯 Overall Analysis Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                   START: Open GUI Tool                           │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────────┐
        │  1. Paste Content Into Text Area     │
        │  • Email address                     │
        │  • URL                               │
        │  • Full email message                │
        │  • Mixed content                     │
        └──────────────┬───────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────┐
        │  2. Select Analysis Mode             │
        │  ✓ 🤖 Auto-Detect (Recommended)      │
        │  ✓ 📧 Email Only                     │
        │  ✓ 🔗 URL Only                       │
        └──────────────┬───────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────┐
        │  3. Click "🔍 ANALYZE"               │
        └──────────────┬───────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────┐
        │  4. Tool Processes Content           │
        │  • Extracts emails/URLs (if Auto)    │
        │  • Validates format                  │
        │  • Checks for threats                │
        └──────────────┬───────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────┐
        │  5. View Results                     │
        │  • Risk Level (Low/Med/High)        │
        │  • Risk Score (0-100)               │
        │  • Detected Issues                   │
        │  • Explanations                      │
        └──────────────┬───────────────────────┘
                       │
               ┌───────┴────────┐
               │                │
               ▼                ▼
    ┌─────────────────┐  ┌──────────────────┐
    │ Save Report? 💾 │  │ Clear & Analyze  │
    │ YES → Save File │  │ Again? 🗑️ Clear  │
    │ NO → Next Step  │  │ YES → Clear      │
    └─────────────────┘  │ NO → Done        │
               │          └──────────────────┘
               │
               ▼
        ┌──────────────────────────────────────┐
        │           END: Done                  │
        └──────────────────────────────────────┘
```

---

## 🤖 Auto-Detect Mode Flow

```
┌─────────────────────────────────────┐
│    Paste Any Content                │
│  (Email, URL, Full message, etc.)   │
└──────────────────┬──────────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │  Extract Emails              │
    │  Pattern: .*@.*\..+          │
    │  Found: [ ]                  │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │  Extract URLs                │
    │  Pattern: http(s)://... or   │
    │           www\..+            │
    │  Found: [ ]                  │
    └──────────────┬───────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
    Items Found?          No Items?
        YES                  │
        │               Show Error:
        │          "Please paste email
        │            address, URL, or
        ▼            email content"
    ┌──────────────────────┐
    │ Create Analysis List │
    │ [                    │
    │  (type, content),    │
    │  (type, content),    │
    │  ...                 │
    │ ]                    │
    └──────────┬───────────┘
               │
        ┌──────▼──────────┐
        │ For Each Item:  │
        │ 1. Analyze      │
        │ 2. Score        │
        │ 3. Explain      │
        └──────┬──────────┘
               │
               ▼
    ┌──────────────────────────────┐
    │  Display Results             │
    │  Show: Item #X of Y          │
    │        Type: EMAIL/URL       │
    │        Content: [...]        │
    │        Risk Level: HIGH      │
    │        Score: 75/100         │
    │        Issues: [...]         │
    └──────────────────────────────┘
```

---

## 📧 Email Analysis Path

```
                 ┌─ Email Address ─┐
                 │  user@domain.com │
                 └────────┬─────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │ Extract Domain Part  │
              │ domain.com           │
              └──────────┬───────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
  ┌──────────┐  ┌──────────────┐  ┌──────────┐
  │Check     │  │Check         │  │Check     │
  │Phishing  │  │Spoofing      │  │Known     │
  │Keywords  │  │Domain        │  │Threats   │
  │(verify,  │  │(bank vs      │  │(look up  │
  │confirm,  │  │domain bank)  │  │database) │
  │secure)   │  │              │  │          │
  └────┬─────┘  └──────┬───────┘  └────┬─────┘
       │                │               │
       └────────────────┼───────────────┘
                        │
                        ▼
           ┌──────────────────────────┐
           │ Calculate Risk Score     │
           │ Based on Issues Found    │
           │ 0-100                    │
           └──────────┬───────────────┘
                      │
                      ▼
           ┌──────────────────────────┐
           │ Determine Risk Level     │
           │ Low (0-33)               │
           │ Medium (34-66)           │
           │ High (67-100)            │
           └──────────────────────────┘
```

---

## 🔗 URL Analysis Path

```
              ┌─────────────────────┐
              │  https://google.com  │
              └──────────┬──────────┘
                         │
        ┌────────────────┼─────────────────┐
        │                │                 │
        ▼                ▼                 ▼
  ┌──────────────┐ ┌─────────────┐ ┌──────────┐
  │Check         │ │Check        │ │Check     │
  │Protocol      │ │Domain       │ │Special   │
  │HTTP? HTTPS?  │ │Legitimate?  │ │Chars     │
  │https://= ✓   │ │Real IP? @   │ │Hyphens?  │
  │http:// = ❌  │ │symbol?      │ │Encoding? │
  └──────┬───────┘ └──────┬──────┘ └────┬─────┘
         │                │             │
         └────────────────┼─────────────┘
                          │
                          ▼
           ┌──────────────────────────┐
           │ Calculate Risk Score     │
           │ - Each issue: +25 points │
           │ Total: 0-100             │
           └──────────┬───────────────┘
                      │
                      ▼
           ┌──────────────────────────┐
           │ Determine Risk Level     │
           │ Low (0-33)               │
           │ Medium (34-66)           │
           │ High (67-100)            │
           └──────────────────────────┘
```

---

## 🎨 GUI Layout Diagram

```
╔════════════════════════════════════════════════════════════════╗
║  🔒 PHISHING DETECTION AWARENESS TOOL                          ║
║  Protect yourself from phishing attacks | Analyze emails and   ║
║  URLs                                                          ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║ 📋 INPUT & ANALYSIS OPTIONS                                   ║
║ ┌─ Radio Buttons ─────────────────────────────────────────┐  ║
║ │ ◉ 🤖 Auto-Detect (Recommended)                          │  ║
║ │ ○ 📧 Email Only      ○ 🔗 URL Only                      │  ║
║ └────────────────────────────────────────────────────────┘  ║
║                                                                ║
║ 💡 Paste email content, URLs, or full email messages...      ║
║                                                                ║
║ Paste your content here:                                      ║
║ ┌──────────────────────────────────────────────────────────┐ ║
║ │  [Text Input Area - 8 lines tall]                        │ ║
║ │  [User can paste emails, URLs, full content here]       │ ║
║ │                                                           │ ║
║ │                                                           │ ║
║ └──────────────────────────────────────────────────────────┘ ║
║                                                                ║
║          ┌─────────────────────────────┐                      ║
║          │ 🔍 ANALYZE                  │                      ║
║          └─────────────────────────────┘                      ║
║                                                                ║
║ 📊 ANALYSIS RESULTS                                           ║
║ ┌────────────────────────────────────────────────────────┐   ║
║ │ Risk Level: ⚠️ HIGH     Score: 75 / 100               │   ║
║ │ Risk Meter: [████████░░░░] 75%                         │   ║
║ │                                                        │   ║
║ │ Detected Issues & Explanations:                        │   ║
║ │ ┌─────────────────────────────────────────────────┐   │   ║
║ │ │ 📌 Analyzed EMAIL:                              │   │   ║
║ │ │ admin@suspicious-bank.com                       │   │   ║
║ │ │                                                  │   │   ║
║ │ │ • Contains "verify account" keyword             │   │   ║
║ │ │ • Domain spoofing detected...                   │   │   ║
║ │ └─────────────────────────────────────────────────┘   │   ║
║ └────────────────────────────────────────────────────────┘   ║
║                                                                ║
║ ┌──────────────────┐  ┌──────────────┐  ┌────────────────┐   ║
║ │ 💾 Save Report   │  │ 🗑️  Clear    │  │ [Info Label]   │   ║
║ └──────────────────┘  └──────────────┘  └────────────────┘   ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

---

## 📊 Decision Tree

```
                    ┌─── Start ───┐
                    │  User Paste │
                    └──────┬──────┘
                           │
                ┌──────────┴──────────┐
                │                    │
            Mode Selected?        No Items
                │                 Shown?
         ┌──────┴──────┐              │
         │             │          Show Error
    Auto-Detect   Manual Mode
         │             │
         │      ┌──────┴──────┐
         │      │             │
         │    Email          URL
         │      │             │
         │  ┌───┴───┐     ┌───┴───┐
         │  │       │     │       │
    Extract Val.   Val. Check Check
    Email & idates idates Domain Proto
    URL   Format  Format        Port
         │      │       │       │
         └──────┼───────┼───────┘
                │
                ▼
    ┌──────────────────────┐
    │  Analyze Item(s)     │
    │  Check for Issues    │
    └─────────┬────────────┘
              │
              ▼
    ┌──────────────────────┐
    │  Calculate Score     │
    │  Determine Level     │
    └─────────┬────────────┘
              │
              ▼
    ┌──────────────────────┐
    │  Display Results     │
    │  Show Findings       │
    └─────────┬────────────┘
              │
         ┌────┴────┐
         │         │
      Save?      Done?
         │         │
         ▼         ▼
      [File]    [End]
```

---

## 🔄 Input Type Detection

```
User Paste
    │
    ├─ Contains @ and .
    │  ├─ Single line? → EMAIL
    │  └─ Multiple contexts? → Check further
    │
    ├─ Starts with http://
    │  └─ → URL
    │
    ├─ Starts with https://
    │  └─ → URL
    │
    ├─ Starts with www.
    │  └─ → URL
    │
    └─ Contains both @ and http?
       └─ → MIXED (Auto-detect extracts all)
```

---

## 📈 Risk Score Calculation

```
Email Phishing Keywords Found:
    Each keyword = +25 points
    Examples: "verify", "confirm", "urgent", "action required"
    Max Score from keywords: +100

URL Security Issues Found:
    HTTP instead of HTTPS = +30 points
    IP address found = +30 points
    @ symbol found = +25 points
    Excessive hyphens = +15 points
    Max Score from URL: +100

Final Score = Min(Total Points, 100)

Score Mapping to Risk Level:
    0-33   → 🟢 LOW
    34-66  → 🟡 MEDIUM
    67-100 → 🔴 HIGH
```

---

## 🎯 User Journey Map

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  Journey: How Users Interact with Enhanced GUI              │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  START: Open Application                                    │
│    ↓                                                         │
│  AWARENESS: Read instructions (new users)                   │
│    ↓                                                         │
│  ACTION: Copy suspicious content                            │
│    ↓                                                         │
│  INPUT: Paste into text area                                │
│    ↓                                                         │
│  CHOICE: Select mode (Default: Auto-Detect)                 │
│    ↓                                                         │
│  ANALYZE: Click analyze button                              │
│    ↓                                                         │
│  INSIGHT: Review results and risk level                     │
│    ↓                                                         │
│  ├─ Confused? → Try Auto-Detect                             │
│  ├─ Need More? → Read explanations                          │
│  ├─ Want to Save? → Click Save Report                       │
│  └─ Ready Again? → Click Clear                              │
│    ↓                                                         │
│  REPEAT or END                                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 💾 Report Generation Flow

```
┌─ Analyze Content ──┐
│  Get Results       │
└────────┬───────────┘
         │
         ▼
   ┌──────────────┐
   │Save Report?  │
   │ Click Button │
   └────────┬─────┘
            │
            ▼
   ┌──────────────────────────┐
   │ Save Dialog Opens        │
   │ Default: phishing_report_ │
   │          YYYYMMDD_HHMMSS │
   └────────┬─────────────────┘
            │
            ▼
   ┌──────────────────────────┐
   │ Choose Save Location     │
   │ (User's Downloads, etc)  │
   └────────┬─────────────────┘
            │
            ▼
   ┌──────────────────────────┐
   │ Generate Report Content: │
   │ • Header                 │
   │ • Timestamp              │
   │ • Analysis Type          │
   │ • Risk Assessment        │
   │ • Detected Issues        │
   │ • Explanations           │
   │ • Safety Tips            │
   └────────┬─────────────────┘
            │
            ▼
   ┌──────────────────────────┐
   │ Write to File (.txt)     │
   └────────┬─────────────────┘
            │
            ▼
   ┌──────────────────────────┐
   │ Show Success Message     │
   │ with File Path           │
   └──────────────────────────┘
```

---

*These visual guides help users understand the analysis flow and make informed decisions about their email and URL security.*
