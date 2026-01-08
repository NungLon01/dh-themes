# DESIGN INTELLIGENCE PROTOCOL

Searchable database of UI styles, color palettes, and stack-specific best practices.

## Workflow Execution

### Step 1: Analyze Requirements
Extract: Product type, Style, Stack.

### Step 2: Intelligence Search
python3 scripts/search.py ""<keyword>"" --domain product
python3 scripts/search.py ""<keyword>"" --domain style
python3 scripts/search.py ""<keyword>"" --domain color
python3 scripts/search.py ""<keyword>"" --domain typography
python3 scripts/search.py ""<keyword>"" --stack html-tailwind

### Step 3: Implementation Rules
1. Icons: SVG only.
2. Interaction: cursor-pointer.
3. Contrast: Light/Dark mode.
