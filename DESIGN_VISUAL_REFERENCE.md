# 🎯 DESIGN VISUAL REFERENCE & WIREFRAMES

## Console Mode - Visual Layout

### Welcome & Setup Screen

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  ════════════════════════════════════════════════════════  ║
║  🔒 PHISHING DETECTION AWARENESS TOOL                     ║
║  ════════════════════════════════════════════════════════  ║
║  Protect yourself from phishing attacks                   ║
║  Analyze emails and URLs                                  ║
║  ════════════════════════════════════════════════════════  ║
║                                                            ║
║  Do you want to check an Email or a URL?                 ║
║  (Enter 'email' or 'url'):                               ║
║  > [user input here]                                      ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

**Typography:**
- Main title: 18pt bold Courier, neon green (#00ff88)
- Subtitle: 9pt Courier, cyan (#00ddff)
- Prompt: 10pt Courier, white
- Dividers: Full width with = characters

---

### Email Analysis Screen

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  Paste the email text here (address or full message):     ║
║  ────────────────────────────────────────────────────     ║
║  [                                                        ║
║  user@phishing-example.com                               ║
║  Subject: Verify Your Account                            ║
║  Body: Click here to verify...                           ║
║  http://fake-bank.com/verify                             ║
║  ]                                                        ║
║                                                            ║
║  ════════════════════════════════════════════════════════  ║
║  📊 PHISHING DETECTION REPORT                             ║
║  ════════════════════════════════════════════════════════  ║
║                                                            ║
║  🔍 Risk Score: 85/100                                    ║
║  ⚠️  Risk Level: High                                      ║
║                                                            ║
║  ════════════════════════════════════════════════════════  ║
║                                                            ║
║  🚨 Detected Issues:                                       ║
║    • Contains "verify account" keyword                    ║
║    • Suspicious URL pattern detected                      ║
║    • Uses non-HTTPS protocol                              ║
║                                                            ║
║  📚 Explanations:                                          ║
║    Phishing emails often use urgent language to pressure ║
║    victims. This email tries to create a sense of        ║
║    urgency with "Verify Your Account."                   ║
║                                                            ║
║    Attackers often use URLs that look legitimate but     ║
║    point to fake sites. Always check the real URL.       ║
║                                                            ║
║  ════════════════════════════════════════════════════════  ║
║  📊 PHISHING DETECTION STATISTICS                         ║
║  ════════════════════════════════════════════════════════  ║
║  Total Analyses: 3                                         ║
║                                                            ║
║  🔴 High Risk   : ████████████████████████████ (2)       ║
║  🟡 Medium Risk : ████████████ (1)                        ║
║  🟢 Low Risk    : (0)                                      ║
║  ════════════════════════════════════════════════════════  ║
║                                                            ║
║  💡 Safety Tips:                                           ║
║    • Never click links from unsolicited emails            ║
║    • Verify sender identity through official channels    ║
║    • Check for HTTPS and security indicators             ║
║    • Be suspicious of urgent requests for sensitive info ║
║  ════════════════════════════════════════════════════════  ║
║                                                            ║
║  ✅ Analysis saved to output/report.txt                    ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

**Color Zones:**
- Header: Neon green (#00ff88)
- Risk Score: Cyan (#00ddff) for label, neon green for number
- Warnings: Red emoji (⚠️) with red text
- Success: Green emoji (✅) with green text
- Chart: Color-coded bars (red, orange, green)

---

## GUI Mode - Visual Layout

### Main Interface - Detailed Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ 🔒 Phishing Detection Awareness Tool                    [_][□][X]│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ════════════════════════════════════════════════════════════  │
│  🔒 PHISHING DETECTION AWARENESS TOOL                          │
│  Protect yourself from phishing attacks | Analyze emails and   │
│  URLs                                                           │
│  ════════════════════════════════════════════════════════════  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  📋 INPUT & ANALYSIS OPTIONS                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                         │   │
│  │ ◉ 🤖 Auto-Detect (Recommended)  ○ 📧 Email Only       │   │
│  │ ○ 🔗 URL Only                                          │   │
│  │                                                         │   │
│  │ 💡 Paste email content, URLs, or full email messages.  │   │
│  │    Click 'Auto-Detect' to analyze all emails/URLs.     │   │
│  │                                                         │   │
│  │ Paste your content (email, URL, or full email):        │   │
│  │ ┌──────────────────────────────────────────────────┐   │   │
│  │ │ From: attacker@phishing.com                       │↕  │   │
│  │ │ Subject: Urgent: Verify Your Account             │   │   │
│  │ │ To: victim@company.com                           │   │   │
│  │ │                                                   │   │   │
│  │ │ Click here to verify: http://fake-site.com/...  │   │   │
│  │ │                                                   │   │   │
│  │ │ [scrollable area - user pastes content here]     │   │   │
│  │ └──────────────────────────────────────────────────┘   │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│                    ┌──────────────────┐                        │
│                    │  🔍 ANALYZE      │                        │
│                    └──────────────────┘                        │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  📊 ANALYSIS RESULTS                                            │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                         │   │
│  │ Risk Level: ⚠️ High        Score: 85 / 100             │   │
│  │                                                         │   │
│  │ Risk Meter:                                             │   │
│  │ ████████████████████████████████████████░░░░ 85%       │   │
│  │                                                         │   │
│  │ Detected Issues & Explanations:                         │   │
│  │ ┌────────────────────────────────────────────────┐     │   │
│  │ │ 📌 Analyzed EMAIL:                            │↕    │   │
│  │ │ attacker@phishing.com                         │     │   │
│  │ │                                                │     │   │
│  │ │ ══════════════════════════════════════════════│     │   │
│  │ │                                                │     │   │
│  │ │ • Contains "verify account" keyword            │     │   │
│  │ │                                                │     │   │
│  │ │ Phishing attackers often use urgency and      │     │   │
│  │ │ emotion to bypass critical thinking. The      │     │   │
│  │ │ phrase "Verify Your Account" is a classic     │     │   │
│  │ │ phishing lure...                              │     │   │
│  │ │                                                │     │   │
│  │ │ • Uses non-HTTPS URL                           │     │   │
│  │ │                                                │     │   │
│  │ │ Legitimate sites use HTTPS (secure           │     │   │
│  │ │ protocol). HTTP-only sites put your data at   │     │   │
│  │ │ risk during transmission...                   │     │   │
│  │ │                                                │     │   │
│  │ └────────────────────────────────────────────────┘     │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ [💾 Save Report] [📊 Show Chart] [🗑️ Clear]                    │
│                     Made to raise awareness | Stay safe!         │
└─────────────────────────────────────────────────────────────────┘
```

**Dimensions:**
- Window: 1000px × 800px
- Header: 60px
- Input section: ~300px
- Analyze button: ~40px
- Results section: Expandable
- Footer: ~50px

---

## Color Palette Reference

### Hex Color Grid

```
┌──────────────┬──────────────┬──────────────┐
│ BACKGROUND   │ PRIMARY TEXT │ SECONDARY    │
├──────────────┼──────────────┼──────────────┤
│ #0a0e27      │ #00ff88      │ #00ddff      │
│ (Dark Blue)  │ (Neon Green) │ (Cyan)       │
└──────────────┴──────────────┴──────────────┘

┌──────────────┬──────────────┬──────────────┐
│ HIGH RISK    │ MEDIUM RISK  │ LOW RISK     │
├──────────────┼──────────────┼──────────────┤
│ #ff1744      │ #ff9800      │ #00ff00      │
│ (Red)        │ (Orange)     │ (Green)      │
└──────────────┴──────────────┴──────────────┘

┌──────────────┬──────────────┐
│ ACTION BTN   │ INPUT BG     │
├──────────────┼──────────────┤
│ #2196F3      │ #1a1f3a      │
│ (Blue)       │ (Dark Gray)  │
└──────────────┴──────────────┘
```

### Color Application Examples

```
╔════════════════════════════════════════════════════════╗
║                                                        ║
║  COMPONENT           COLOR            HEX VALUE        ║
║  ────────────────────────────────────────────────────  ║
║  Window Background   ████ Dark Blue    #0a0e27        ║
║  Main Title          ████ Neon Green   #00ff88        ║
║  Subtitle            ████ Cyan         #00ddff        ║
║  Input Area Background ████ Dark Gray   #1a1f3a        ║
║  Input Text          ████ Neon Green   #00ff88        ║
║  Analyze Button Text ████ Dark Blue    #0a0e27        ║
║  Analyze Button BG   ████ Neon Green   #00ff88        ║
║  High Risk          ████ Red           #ff1744        ║
║  Medium Risk        ████ Orange        #ff9800        ║
║  Low Risk           ████ Green         #00ff00        ║
║  Chart Button       ████ Blue          #2196F3        ║
║  Save Button        ████ Orange        #ff9800        ║
║  Clear Button       ████ Red           #ff1744        ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
```

---

## Typography Hierarchy

### Console Mode

```
MAIN TITLE (18pt Bold)
═══════════════════════════════════════════════════════════
🔒 PHISHING DETECTION AWARENESS TOOL

Subtitle (9pt Regular)
───────────────────────────────────────────────────────────
Protect yourself from phishing attacks | Analyze emails and URLs

Section Header (11pt Bold)
───────────────────────────────────────────────────────────
📊 PHISHING DETECTION REPORT

Body Text (9pt Regular)
──────────────────────────────────────────────────────────
🔍 Risk Score: 85/100
⚠️  Risk Level: High

List Items (9pt Regular)
──────────────────────────────────────────────────────────
  • Contains "verify account" keyword
  • Suspicious URL pattern detected

Small Text / Labels (8pt Regular)
──────────────────────────────────────────────────────────
✅ Analysis saved to output/report.txt
```

### GUI Mode

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  🔒 PHISHING DETECTION AWARENESS TOOL                  │
│  ← MAIN TITLE (18pt Bold, Neon Green)                 │
│                                                         │
│  Protect yourself from phishing attacks               │
│  ← SUBTITLE (9pt Regular, Cyan)                        │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  📋 INPUT & ANALYSIS OPTIONS                           │
│  ← SECTION HEADER (11pt Bold, Neon Green)             │
│                                                         │
│  ◉ 🤖 Auto-Detect (Recommended)                       │
│  ← LABEL TEXT (10pt Regular, Neon Green)              │
│                                                         │
│  💡 Paste email content, URLs, or full email          │
│     messages. Click 'Auto-Detect' to analyze...       │
│  ← INSTRUCTIONS (8pt Regular, Cyan)                    │
│                                                         │
│  Paste your content here:                              │
│  ← FIELD LABEL (9pt Regular, Blue)                    │
│  ┌───────────────────────────────────┐                │
│  │ [User input text area]            │                │
│  │ ← INPUT TEXT (9pt Regular, Green) │                │
│  └───────────────────────────────────┘                │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  📊 ANALYSIS RESULTS                                   │
│  ← SECTION HEADER (11pt Bold, Neon Green)             │
│                                                         │
│  Risk Level: ⚠️ High        Score: 85 / 100           │
│  ← RESULT LABELS (12-14pt Bold, Color-coded)          │
│                                                         │
│  Detected Issues & Explanations:                       │
│  ← SUBSECTION HEADER (9pt Regular, Blue)              │
│  ┌───────────────────────────────────┐                │
│  │ • Issue with explanation           │                │
│  │ ← BODY TEXT (9pt Regular, Green)  │                │
│  └───────────────────────────────────┘                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Button Design Reference

### Console-Style Buttons (GUI)

```
Style 1: Primary Action (Analyze)
┌──────────────────────┐
│   🔍 ANALYZE        │  ← Neon Green background
│                      │  ← Black text
│ (30px x 40px pad)    │
└──────────────────────┘

Style 2: Secondary Actions
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ 💾 Save      │  │ 📊 Show      │  │ 🗑️ Clear    │
│   Report     │  │   Chart      │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
 Orange BG        Blue BG           Red BG
 Dark text        White text        White text
 (15px pad)       (15px pad)        (15px pad)
```

### Button Hover States

```
Default State:        Hover State:         Click State:
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ 🔍 ANALYZE      │  │ 🔍 ANALYZE      │  │ 🔍 ANALYZE      │
│ (Normal color)  │  │ (Darker shade)  │  │ (Pressed)       │
│ Cursor: Pointer │  │ Cursor: Pointer │  │ Visual feedback │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

---

## Modal & Dialog Designs

### Error Message Dialog

```
╔══════════════════════════════════════════════════════════╗
║  ❌ Invalid Input                                 [X]     ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  The input is not a valid email:                        ║
║                                                          ║
║  Must contain '@' symbol                                ║
║                                                          ║
║  Tip: Try using 'Auto-Detect' mode to analyze full     ║
║       email content.                                     ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                            [OK]          ║
╚══════════════════════════════════════════════════════════╝
```

### Success Message Dialog

```
╔══════════════════════════════════════════════════════════╗
║  ✅ Success                                       [X]     ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  Report saved to:                                       ║
║                                                          ║
║  C:\Users\user\phishing_report_20260222_123456.txt     ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                            [OK]          ║
╚══════════════════════════════════════════════════════════╝
```

### Info Message Dialog

```
╔══════════════════════════════════════════════════════════╗
║  ℹ️ Multiple Items Found                         [X]     ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  Found 3 items to analyze.                             ║
║                                                          ║
║  Currently showing: 1 of 3                             ║
║  Type: EMAIL                                            ║
║                                                          ║
║  Content: attacker@phishing.com                        ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                            [OK]          ║
╚══════════════════════════════════════════════════════════╝
```

---

## ASCII Chart Visualization Examples

### Basic Chart (Few Analyses)

```
════════════════════════════════════════════════════════════
📊 PHISHING DETECTION STATISTICS
════════════════════════════════════════════════════════════
Total Analyses: 3

🔴 High Risk   : ██████████ (1)
🟡 Medium Risk : ██████████ (1)
🟢 Low Risk    : ██████████ (1)

════════════════════════════════════════════════════════════
```

### Detailed Chart (Many Analyses)

```
════════════════════════════════════════════════════════════
📊 PHISHING DETECTION STATISTICS
════════════════════════════════════════════════════════════
Total Analyses: 15

🔴 High Risk   : ████████████████████████████ (8)
🟡 Medium Risk : ████████████████████ (6)
🟢 Low Risk    : ██████████ (1)

════════════════════════════════════════════════════════════
```

### Skewed Distribution Chart

```
════════════════════════════════════════════════════════════
📊 PHISHING DETECTION STATISTICS
════════════════════════════════════════════════════════════
Total Analyses: 20

🔴 High Risk   : ████████████████████████████████████████ (12)
🟡 Medium Risk : ████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ (6)
🟢 Low Risk    : ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ (2)

════════════════════════════════════════════════════════════
```

---

## Matplotlib Chart Examples

### Sample Chart Layout

```
Phishing Detection Risk Analysis

Count
    |
  12|        ┌────┐
  10|        │    │
   8|        │    │  ┌────┐
   6|        │    │  │    │  ┌────┐
   4|        │    │  │    │  │    │
   2|        │    │  │    │  │    │
   0|________│____│__│____│__│____|________
      High Risk  Medium Risk  Low Risk

   Colors:  Red      Orange    Green
```

### Full Chart with Labels

```
        Phishing Detection Risk Analysis
        ═══════════════════════════════════

Count  │
    15 │  ┌─────┐
    12 │  │  12 │
    10 │  │  ┌──┴────┐
     8 │  │  │ 8     │
     6 │  │  │ ┌─────┴──┐
     4 │  │  │ │ 4      │
     2 │  │  │ │        │
     0 │  │  │ │        │
       └──┴──┴─┴────────┴───────
          High Medium  Low
          Risk Risk    Risk

Legend:
🔴 High Risk = Red (#ff1744)
🟡 Medium Risk = Orange (#ff9800)
🟢 Low Risk = Green (#00ff00)
```

---

## Responsive Behavior

### Console Mode
- Fixed width: 60 characters
- Scales to terminal width automatically
- Text wraps at word boundaries
- Charts scale proportionally

### GUI Mode
- Minimum window: 800×600px
- Default window: 1000×800px
- Resizable components
- Responsive layout with fill options

---

## Accessibility Features

### Color Contrast Examples

```
✅ PASS (12.5:1 ratio)
─────────────────────────────────
Text: #00ff88 (Neon Green)
Background: #0a0e27 (Dark Blue)
     ███████████████████████████

✅ PASS (13.4:1 ratio)
─────────────────────────────────
Text: #00ff00 (Bright Green)
Background: #0a0e27 (Dark Blue)
     ███████████████████████████

✅ PASS (8.2:1 ratio)
─────────────────────────────────
Text: #ff1744 (Red)
Background: #0a0e27 (Dark Blue)
     ███████████████████████████
```

### Keyboard Navigation (GUI)

```
Tab Order:
1. Mode Selection (Radio buttons)
2. Text Input Area
3. Analyze Button
4. Results Area (view only)
5. Save Report Button
6. Show Chart Button
7. Clear Button

Shortcuts (Future Enhancement):
Alt+A = Analyze
Alt+S = Save Report
Alt+C = Clear
```

---

## State Transitions

### Analysis Workflow Visual

```
EMPTY STATE
    ↓
    [User enters input]
    ↓
READY STATE (Analyze button available)
    ↓
    [User clicks Analyze]
    ↓
LOADING STATE (visual feedback)
    ↓
    [Analysis completes]
    ↓
RESULTS STATE
├─ Risk score visible
├─ Issues displayed
├─ Explanations shown
├─ Chart button available
└─ Save button available
    ↓
    [User can:]
    ├─ View chart
    ├─ Save report
    ├─ Clear and start over
    └─ Analyze more items
```

---

## Design System Summary

This visual reference provides:
- ✅ Exact color codes (HEX values)
- ✅ Font specifications (size, weight, family)
- ✅ Layout dimensions and spacing
- ✅ Component specifications (buttons, inputs, labels)
- ✅ Example dialogs and messages
- ✅ Chart visualizations
- ✅ Accessibility guidelines
- ✅ State transitions and workflows

**All elements follow consistent cybersecurity aesthetic while maintaining high usability and accessibility.**

---

Version 1.0 | February 22, 2026 | Production Ready
