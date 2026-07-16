# Skill: ui-ux-cr

# UI UX CR - Cyber-Rage Design Intelligence Engine

Ultra-premium design intelligence system with enhanced BM25 search, fuzzy matching, synonym expansion, color theory engine, component library, animation database, responsive patterns, and design tokens. Supports 30+ product types, 100+ styles, 50+ color palettes, 30+ font pairings, and 16+ tech stacks.

## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

If Python is not installed, install it based on user's OS:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## How to Use This Skill

When user requests UI/UX work (design, build, create, implement, review, fix, improve), follow this workflow:

### Step 1: Analyze User Requirements

Extract key information from user request:
- **Product type**: SaaS, e-commerce, portfolio, dashboard, landing page, etc.
- **Style keywords**: minimal, playful, professional, elegant, dark mode, etc.
- **Industry**: healthcare, fintech, gaming, education, etc.
- **Stack**: React, Vue, Next.js, or default to `html-tailwind`

### Step 2: Generate Design System (REQUIRED)

**Always start with `--design-system`** to get comprehensive recommendations with reasoning:

```bash
python3 scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

This command:
1. Searches 10 domains in parallel (product, style, color, landing, typography, component, animation, responsive, design_token, ux)
2. Applies reasoning rules from `ui-reasoning.csv` to select best matches
3. Generates extended color palette using color theory engine
4. Returns complete design system: pattern, style, colors, typography, effects, components, animations, responsive patterns
5. Includes anti-patterns to avoid and pre-delivery checklist

**Example:**
```bash
python3 scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

### Step 2b: Persist Design System (Master + Overrides Pattern)

To save the design system for hierarchical retrieval across sessions, add `--persist`:

```bash
python3 scripts/search.py "<query>" --design-system --persist -p "Project Name"
```

This creates:
- `design-system/MASTER.md` — Global Source of Truth with all design rules
- `design-system/pages/` — Folder for page-specific overrides

**With page-specific override:**
```bash
python3 scripts/search.py "<query>" --design-system --persist -p "Project Name" --page "dashboard"
```

### Step 2c: Comprehensive Project Analysis

For a complete analysis across all domains:

```bash
python3 scripts/search.py "<query>" --analyze
```

This returns recommendations across all 10 domains simultaneously.

### Step 3: Supplement with Detailed Searches (as needed)

After getting the design system, use domain searches to get additional details:

```bash
python3 scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**Available Domains:**

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `style` | UI styles, colors, effects | glassmorphism, minimalism, dark mode |
| `color` | Color palettes by product type | saas, ecommerce, healthcare |
| `typography` | Font pairings, Google Fonts | elegant, playful, professional |
| `landing` | Page structure, CTA strategies | hero, testimonial, pricing |
| `chart` | Chart types, library recommendations | trend, comparison, funnel |
| `ux` | Best practices, anti-patterns | animation, accessibility, loading |
| `component` | Component recommendations | button, card, modal, form |
| `animation` | Animation patterns | hover, entrance, scroll, loading |
| `responsive` | Responsive design patterns | mobile-first, grid, typography |
| `design_token` | Design tokens and variables | color, spacing, typography, shadow |
| `product` | Product type recommendations | SaaS, e-commerce, healthcare |
| `icons` | Icon recommendations | lucide, heroicons, symbol |
| `react` | React/Next.js performance | memo, suspense, bundle |
| `web` | Web interface guidelines | aria, focus, keyboard |

### Step 4: Stack Guidelines (Default: html-tailwind)

Get implementation-specific best practices. If user doesn't specify a stack, **default to `html-tailwind`**.

```bash
python3 scripts/search.py "<keyword>" --stack html-tailwind
```

**Available Stacks:**

| Stack | Focus |
|-------|-------|
| `html-tailwind` | Tailwind utilities, responsive, a11y (DEFAULT) |
| `react` | State, hooks, performance, patterns |
| `nextjs` | SSR, routing, images, API routes |
| `vue` | Composition API, Pinia, Vue Router |
| `nuxtjs` | Nuxt.js specific patterns |
| `svelte` | Runes, stores, SvelteKit |
| `swiftui` | Views, State, Navigation, Animation |
| `react-native` | Components, Navigation, Lists |
| `flutter` | Widgets, State, Layout, Theming |
| `shadcn` | shadcn/ui components, theming |
| `jetpack-compose` | Composables, Modifiers, State |
| `angular` | Components, Services, RxJS |
| `laravel` | Blade, Livewire, Inertia.js |
| `threejs` | Three.js, WebGL, 3D |
| `astro` | Islands, Content Collections |
| `nuxt-ui` | Nuxt UI components |

### Step 5: Multi-Domain Search

Search across multiple domains simultaneously:

```bash
python3 scripts/search.py "<query>" --multi-domains style,color,typography
```

---

## Output Formats

The `--design-system` flag supports two output formats:

```bash
# ASCII box (default) - best for terminal display
python3 scripts/search.py "fintech crypto" --design-system

# Markdown - best for documentation
python3 scripts/search.py "fintech crypto" --design-system -f markdown
```

---

## Example Workflow

**User request:** "Build a landing page for my SaaS product"

### Step 1: Analyze Requirements
- Product type: SaaS
- Style keywords: modern, clean, professional
- Industry: Technology/SaaS
- Stack: html-tailwind (default)

### Step 2: Generate Design System

```bash
python3 scripts/search.py "SaaS landing page modern" --design-system -p "My SaaS"
```

**Output:** Complete design system with pattern, style, colors, typography, effects, components, animations, responsive patterns.

### Step 3: Supplement with Detailed Searches

```bash
# Get UX guidelines for animation and accessibility
python3 scripts/search.py "animation accessibility" --domain ux

# Get component recommendations
python3 scripts/search.py "button card modal" --domain component

# Get responsive patterns
python3 scripts/search.py "mobile-first grid" --domain responsive
```

### Step 4: Stack Guidelines

```bash
python3 scripts/search.py "layout responsive form" --stack html-tailwind
```

### Step 5: Implement the Design

Using the design system output, implement the UI with proper colors, fonts, spacing, components, animations, and responsive patterns.

---

## Key Features

### Enhanced BM25 Search Engine
- Fuzzy matching for partial word matches
- Synonym expansion for semantic understanding
- Priority-based ranking for better results

### Color Theory Engine
- Extended palette generation (50-900 shades)
- Complementary, analogous, triadic color harmonies
- HSL-based color manipulation

### Component Library
- 25+ pre-built component recommendations
- CSS and Tailwind code snippets
- Accessibility guidelines for each component

### Animation Database
- 20+ animation patterns
- CSS code with duration, easing, GPU optimization
- Reduced motion support

### Responsive Patterns
- 15+ responsive design patterns
- Mobile-first approach
- Container queries support

### Design Tokens
- 50+ design token categories
- CSS variables and Tailwind classes
- Light and dark mode values

---

## Common Rules for Professional UI

### Icons & Visual Elements

| Rule | Do | Don't |
|------|----|-----|
| **No emoji icons** | Use SVG icons (Heroicons, Lucide, Simple Icons) | Use emojis as UI icons |
| **Stable hover states** | Use color/opacity transitions on hover | Use scale transforms that shift layout |
| **Correct brand logos** | Research official SVG from Simple Icons | Guess or use incorrect logo paths |
| **Consistent icon sizing** | Use fixed viewBox (24x24) with w-6 h-6 | Mix different icon sizes randomly |

### Interaction & Cursor

| Rule | Do | Don't |
|------|----|-----|
| **Cursor pointer** | Add `cursor-pointer` to all clickable elements | Leave default cursor on interactive elements |
| **Hover feedback** | Provide visual feedback (color, shadow, border) | No indication element is interactive |
| **Smooth transitions** | Use `transition-colors duration-200` | Instant state changes or too slow (>500ms) |

### Light/Dark Mode Contrast

| Rule | Do | Don't |
|------|----|-----|
| **Glass card light mode** | Use `bg-white/80` or higher opacity | Use `bg-white/10` (too transparent) |
| **Text contrast light** | Use `#0F172A` (slate-900) for text | Use `#94A3B8` (slate-400) for body text |
| **Muted text light** | Use `#475569` (slate-600) minimum | Use gray-400 or lighter |
| **Border visibility** | Use `border-gray-200` in light mode | Use `border-white/10` (invisible) |

---

## Pre-Delivery Checklist

Before delivering UI code, verify:

### Visual Quality
- [ ] No emojis used as icons (use SVG instead)
- [ ] All icons from consistent icon set (Heroicons/Lucide)
- [ ] Brand logos are correct
- [ ] Hover states don't cause layout shift

### Interaction
- [ ] All clickable elements have `cursor-pointer`
- [ ] Hover states provide clear visual feedback
- [ ] Transitions are smooth (150-300ms)
- [ ] Focus states visible for keyboard navigation

### Light/Dark Mode
- [ ] Light mode text has sufficient contrast (4.5:1 minimum)
- [ ] Glass/transparent elements visible in light mode
- [ ] Borders visible in both modes
- [ ] Test both modes before delivery

### Layout
- [ ] Floating elements have proper spacing from edges
- [ ] No content hidden behind fixed navbars
- [ ] Responsive at 375px, 768px, 1024px, 1440px
- [ ] No horizontal scroll on mobile

### Accessibility
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Color is not the only indicator
- [ ] `prefers-reduced-motion` respected

### Components
- [ ] All interactive elements keyboard accessible
- [ ] Loading states implemented
- [ ] Error states handled
- [ ] Empty states designed

---

## Tips for Better Results

1. **Be specific with keywords** - "healthcare SaaS dashboard" > "app"
2. **Use `--analyze`** - Get comprehensive analysis across all domains
3. **Search multiple times** - Different keywords reveal different insights
4. **Combine domains** - Style + Typography + Color = Complete design system
5. **Use `--multi-domains`** - Search across multiple domains simultaneously
6. **Check components** - Get component recommendations for your design
7. **Use animations** - Add polish with recommended animations
8. **Follow responsive patterns** - Ensure mobile-first design
9. **Use design tokens** - Maintain consistency with token system
10. **Iterate** - If first search doesn't match, try different keywords
