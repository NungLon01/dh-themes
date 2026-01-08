# DESIGN INTELLIGENCE PROTOCOL

Searchable database of UI styles, color palettes, and stack-specific best practices.

## Workflow Execution

### Step 1: Analyze Requirements
Extract: **Product type** (SaaS, E-com), **Style** (Glass, Minimal), **Stack** (React, HTML-Tailwind).

### Step 2: Intelligence Search (Run these commands)
Use the shared `search.py` script to gather context.

```bash
# 1. Product Style
python3 .shared/ui-ux-pro-max/scripts/search.py "<keyword>" --domain product

# 2. Visual Style & Colors
python3 .shared/ui-ux-pro-max/scripts/search.py "<keyword>" --domain style
python3 .shared/ui-ux-pro-max/scripts/search.py "<keyword>" --domain color

# 3. Typography
python3 .shared/ui-ux-pro-max/scripts/search.py "<keyword>" --domain typography

# 4. Tech Stack Patterns (IMPORTANT)
python3 .shared/ui-ux-pro-max/scripts/search.py "<keyword>" --stack html-tailwind
```
*(Note: If `html-tailwind` is not the target, replace with `react`, `vue`, etc.)*

### Step 3: Implementation Rules
1.  **Icons**: Use SVG only (Lucide/Heroicons). No Emojis.
2.  **Interaction**: `cursor-pointer` on all clickables. Smooth `transition-all`.
3.  **Contrast**: Ensure text is legible in both Light/Dark modes.
4.  **Spacing**: Use consistent padding/margin scales (Tailwind standard).

### Step 4: Verification
Before finishing, verify:
- [ ] Hover states active and visible?
- [ ] Mobile responsive (No horizontal scroll)?
- [ ] Dark mode colors balanced?

---
*This file is synced from Remote Repository.*
