# ui-ux-cr
<p align="center">
  <img src="https://img.shields.io/badge/UI_UX_CR-Cyber--Rage-FF006E?style=for-the-badge&logo=cyber&logoColor=white" alt="UI UX CR">
</p>

<h1 align="center">UI UX CR - Cyber-Rage Design Intelligence Engine</h1>

<p align="center">
  <strong>Ultra-premium design intelligence system for AI assistants</strong><br>
  Enhanced BM25 search, fuzzy matching, color theory engine, component library, animations, responsive patterns, and design tokens.
</p>

<p align="center">
  <a href="https://github.com/cyberrage-ananymus/ui-ux-cr/releases"><img src="https://img.shields.io/badge/version-1.0.0-blue?style=flat-square" alt="Version"></a>
  <a href="https://github.com/cyberrage-ananymus/ui-ux-cr/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="License"></a>
  <img src="https://img.shields.io/badge/python-3.x-yellow?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/styles-25+-purple?style=flat-square" alt="Styles">
  <img src="https://img.shields.io/badge/colors-30+-orange?style=flat-square" alt="Colors">
  <img src="https://img.shields.io/badge/components-25+-cyan?style=flat-square" alt="Components">
  <img src="https://img.shields.io/badge/animations-20+-pink?style=flat-square" alt="Animations">
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#domains">Domains</a> •
  <a href="#stacks">Stacks</a> •
  <a href="#examples">Examples</a>
</p>

---

## What is UI UX CR?

**UI UX CR** (Cyber-Rage) is an advanced AI skill that provides comprehensive design intelligence for building professional UI/UX across multiple platforms and frameworks. It goes beyond traditional design systems by incorporating:

- **Enhanced BM25 Search Engine** with fuzzy matching and synonym expansion
- **Color Theory Engine** for generating harmonious palettes
- **Component Library** with 25+ pre-built recommendations
- **Animation Database** with 20+ patterns and CSS code
- **Responsive Patterns** for mobile-first design
- **Design Tokens** for consistent theming

## Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **Enhanced BM25 Search** | Fuzzy matching, synonym expansion, semantic understanding |
| **Design System Generator** | Complete design systems with pattern, style, colors, typography |
| **Color Theory Engine** | Extended palette generation (50-900 shades), color harmonies |
| **Component Library** | 25+ components with CSS/Tailwind code and accessibility |
| **Animation Database** | 20+ animations with duration, easing, GPU optimization |
| **Responsive Patterns** | 15+ mobile-first responsive design patterns |
| **Design Tokens** | 50+ token categories for consistent theming |

### Data Coverage

| Category | Count | Description |
|----------|-------|-------------|
| UI Styles | 25+ | Glassmorphism, Minimalism, Dark Mode, Cyberpunk, etc. |
| Product Types | 30 | SaaS, E-commerce, Healthcare, Gaming, etc. |
| Color Palettes | 30 | Industry-specific palettes with hex values |
| Font Pairings | 20 | Curated typography combinations |
| Chart Types | 20 | Data visualization recommendations |
| Landing Page Patterns | 20 | Conversion-optimized page structures |
| Components | 25+ | Buttons, Cards, Modals, Forms, etc. |
| Animations | 20 | Hover, Entrance, Scroll, Loading, etc. |
| Responsive Patterns | 15 | Mobile-first, Grid, Typography, etc. |
| Design Tokens | 50+ | Colors, Spacing, Typography, Shadows, etc. |
| Tech Stacks | 16 | React, Next.js, Vue, Flutter, SwiftUI, etc. |

## Installation

### Option 1: Direct Copy (Recommended)

```bash
# Clone the repository
git clone https://github.com/cyberrage-ananymus/ui-ux-cr.git

# Copy to your project
cp -r ui-ux-cr/.claude/skills/ui-ux-cr /path/to/your/project/.claude/skills/
```

### Option 2: Manual Installation

```bash
# Create skill directory
mkdir -p .claude/skills/ui-ux-cr

# Copy files
cp -r ui-ux-cr/scripts .claude/skills/ui-ux-cr/
cp -r ui-ux-cr/data .claude/skills/ui-ux-cr/
cp ui-ux-cr/SKILL.md .claude/skills/ui-ux-cr/
```

### Prerequisites

Python 3.x is required for the search scripts:

```bash
python3 --version
```

If not installed:
- **macOS:** `brew install python3`
- **Ubuntu/Debian:** `sudo apt update && sudo apt install python3`
- **Windows:** `winget install Python.Python.3.12`

## Usage

### Design System Generation (Primary Feature)

Generate a complete design system with one command:

```bash
python3 scripts/search.py "SaaS landing page" --design-system -p "My SaaS App"
```

**Output includes:**
- Pattern (Landing page structure)
- Style (UI style recommendations)
- Colors (Primary, Secondary, CTA, Background, Text, Border + Extended Palette)
- Typography (Heading + Body fonts with Google Fonts link)
- Effects (Animation recommendations)
- Components (Recommended components with CSS/Tailwind)
- Animations (Recommended animations with code)
- Responsive Patterns (Mobile-first patterns)
- Anti-patterns (What to avoid)
- Pre-delivery Checklist

### Save Design System to File

```bash
python3 scripts/search.py "ecommerce" --design-system --persist -p "MyShop"
```

Creates:
```
design-system/myshop/
├── MASTER.md           # Global Source of Truth
└── pages/              # Page-specific overrides
```

### Comprehensive Project Analysis

```bash
python3 scripts/search.py "fintech dashboard" --analyze
```

Returns recommendations across all domains simultaneously.

### Domain-Specific Search

```bash
# Search for styles
python3 scripts/search.py "glassmorphism dark" --domain style

# Search for colors
python3 scripts/search.py "healthcare" --domain color

# Search for typography
python3 scripts/search.py "elegant luxury" --domain typography

# Search for components
python3 scripts/search.py "button card modal" --domain component

# Search for animations
python3 scripts/search.py "hover entrance scroll" --domain animation

# Search for responsive patterns
python3 scripts/search.py "mobile-first grid" --domain responsive
```

### Multi-Domain Search

```bash
python3 scripts/search.py "modern dark" --multi-domains style,color,typography
```

### Stack-Specific Guidelines

```bash
python3 scripts/search.py "form validation" --stack react
python3 scripts/search.py "responsive layout" --stack html-tailwind
python3 scripts/search.py "composition" --stack vue
```

### Output Formats

```bash
# ASCII box (default) - best for terminal
python3 scripts/search.py "fintech" --design-system

# Markdown - best for documentation
python3 scripts/search.py "fintech" --design-system -f markdown

# JSON - for programmatic use
python3 scripts/search.py "glassmorphism" --domain style --json
```

## Available Domains

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `style` | UI styles, colors, effects | glassmorphism, minimalism, dark mode |
| `color` | Color palettes | saas, ecommerce, healthcare |
| `typography` | Font pairings | elegant, playful, professional |
| `landing` | Page structure | hero, testimonial, pricing |
| `chart` | Chart types | trend, comparison, funnel |
| `ux` | Best practices | animation, accessibility |
| `component` | Components | button, card, modal |
| `animation` | Animations | hover, entrance, scroll |
| `responsive` | Responsive patterns | mobile-first, grid |
| `design_token` | Design tokens | color, spacing, shadow |
| `product` | Product types | SaaS, e-commerce |
| `icons` | Icons | lucide, heroicons |
| `react` | React performance | memo, suspense |
| `web` | Web guidelines | aria, focus |

## Available Stacks

| Stack | Focus |
|-------|-------|
| `html-tailwind` | Tailwind utilities (DEFAULT) |
| `react` | State, hooks, performance |
| `nextjs` | SSR, routing, images |
| `vue` | Composition API, Pinia |
| `nuxtjs` | Nuxt.js patterns |
| `svelte` | Runes, stores, SvelteKit |
| `swiftui` | Views, State, Navigation |
| `react-native` | Components, Navigation |
| `flutter` | Widgets, State, Layout |
| `shadcn` | shadcn/ui components |
| `jetpack-compose` | Composables, Modifiers |
| `angular` | Components, Services |
| `laravel` | Blade, Livewire |
| `threejs` | Three.js, WebGL |
| `astro` | Islands, Content |
| `nuxt-ui` | Nuxt UI components |

## Examples

### Example 1: SaaS Landing Page

```bash
python3 scripts/search.py "SaaS landing page modern" --design-system -p "My SaaS"
```

**Recommended:**
- **Pattern:** Hero-Centric with social proof
- **Style:** Glassmorphism + Flat Design
- **Colors:** Trust blue (#2563EB) + Orange CTA (#F97316)
- **Typography:** Poppins (headings) + Inter (body)
- **Effects:** Subtle hover transitions, scroll reveal

### Example 2: Healthcare Dashboard

```bash
python3 scripts/search.py "healthcare dashboard" --design-system -p "Health App"
```

**Recommended:**
- **Pattern:** Data-Dense Dashboard
- **Style:** Dark Mode (OLED) + Accessible
- **Colors:** Dark bg (#0F172A) + Health green (#22C55E)
- **Typography:** Merriweather (headings) + Open Sans (body)
- **Effects:** Real-time data updates, smooth transitions

### Example 3: E-commerce Store

```bash
python3 scripts/search.py "ecommerce luxury" --design-system -p "Luxury Shop"
```

**Recommended:**
- **Pattern:** Feature-Rich Showcase
- **Style:** Liquid Glass + Glassmorphism
- **Colors:** Premium dark (#1C1917) + Gold accent (#CA8A04)
- **Typography:** Cormorant Garamond (headings) + Montserrat (body)
- **Effects:** Chromatic aberration, fluid animations

## Pre-Delivery Checklist

Before delivering UI code, verify:

- [ ] No emojis used as icons (use SVG instead)
- [ ] All icons from consistent icon set (Heroicons/Lucide)
- [ ] `cursor-pointer` on all clickable elements
- [ ] Hover states with smooth transitions (150-300ms)
- [ ] Light mode: text contrast 4.5:1 minimum
- [ ] Focus states visible for keyboard navigation
- [ ] `prefers-reduced-motion` respected
- [ ] Responsive: 375px, 768px, 1024px, 1440px
- [ ] Dark mode tested
- [ ] Loading states implemented
- [ ] Error states handled
- [ ] Empty states designed

## Why UI UX CR is Better

| Feature | ui-ux-pro-max | UI UX CR |
|---------|---------------|----------|
| Search Engine | Basic BM25 | Enhanced BM25 + Fuzzy + Synonyms |
| Color Theory | Basic palettes | Extended palette generation (50-900) |
| Components | None | 25+ with CSS/Tailwind |
| Animations | None | 20+ with code |
| Responsive | Basic | 15+ patterns |
| Design Tokens | Basic | 50+ categories |
| Analysis | Single domain | Multi-domain analysis |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Cyber-Rage**

- **GitHub:** [cyberrage-ananymus](https://github.com/cyberrage-ananymus)
- **LinkedIn:** [Cyber Rage](https://www.linkedin.com/in/cyber-rage-green-eyes-801656416)
- **Session:** `05fd51ac639edc257133f9364529eff3af1d69c5c18b31f321ba466b3823a0a805`

---

<p align="center">
  <strong>Built with passion by Cyber-Rage</strong><br>
  <em>Making AI-powered design accessible to everyone</em>
</p>
