#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI UX CR Core - Enhanced BM25 search engine with fuzzy matching & semantic ranking
Cyber-Rage Design Intelligence Engine
"""

import csv
import re
import json
from pathlib import Path
from math import log, sqrt
from collections import defaultdict

DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3

CSV_CONFIG = {
    "style": {
        "file": "styles.csv",
        "search_cols": ["Style Category", "Keywords", "Best For", "Type", "AI Prompt Keywords"],
        "output_cols": ["Style Category", "Type", "Keywords", "Primary Colors", "Effects & Animation", "Best For", "Performance", "Accessibility", "Framework Compatibility", "Complexity", "AI Prompt Keywords", "CSS/Technical Keywords", "Implementation Checklist", "Design System Variables"]
    },
    "color": {
        "file": "colors.csv",
        "search_cols": ["Product Type", "Notes"],
        "output_cols": ["Product Type", "Primary (Hex)", "Secondary (Hex)", "CTA (Hex)", "Background (Hex)", "Text (Hex)", "Border (Hex)", "Notes"]
    },
    "chart": {
        "file": "charts.csv",
        "search_cols": ["Data Type", "Keywords", "Best Chart Type", "Accessibility Notes"],
        "output_cols": ["Data Type", "Keywords", "Best Chart Type", "Secondary Options", "Color Guidance", "Accessibility Notes", "Library Recommendation", "Interactive Level"]
    },
    "landing": {
        "file": "landing.csv",
        "search_cols": ["Pattern Name", "Keywords", "Conversion Optimization", "Section Order"],
        "output_cols": ["Pattern Name", "Keywords", "Section Order", "Primary CTA Placement", "Color Strategy", "Conversion Optimization"]
    },
    "product": {
        "file": "products.csv",
        "search_cols": ["Product Type", "Keywords", "Primary Style Recommendation", "Key Considerations"],
        "output_cols": ["Product Type", "Keywords", "Primary Style Recommendation", "Secondary Styles", "Landing Page Pattern", "Dashboard Style (if applicable)", "Color Palette Focus"]
    },
    "ux": {
        "file": "ux-guidelines.csv",
        "search_cols": ["Category", "Issue", "Description", "Platform"],
        "output_cols": ["Category", "Issue", "Platform", "Description", "Do", "Don't", "Code Example Good", "Code Example Bad", "Severity"]
    },
    "typography": {
        "file": "typography.csv",
        "search_cols": ["Font Pairing Name", "Category", "Mood/Style Keywords", "Best For", "Heading Font", "Body Font"],
        "output_cols": ["Font Pairing Name", "Category", "Heading Font", "Body Font", "Mood/Style Keywords", "Best For", "Google Fonts URL", "CSS Import", "Tailwind Config", "Notes"]
    },
    "icons": {
        "file": "icons.csv",
        "search_cols": ["Category", "Icon Name", "Keywords", "Best For"],
        "output_cols": ["Category", "Icon Name", "Keywords", "Library", "Import Code", "Usage", "Best For", "Style"]
    },
    "react": {
        "file": "react-performance.csv",
        "search_cols": ["Category", "Issue", "Keywords", "Description"],
        "output_cols": ["Category", "Issue", "Platform", "Description", "Do", "Don't", "Code Example Good", "Code Example Bad", "Severity"]
    },
    "web": {
        "file": "web-interface.csv",
        "search_cols": ["Category", "Issue", "Keywords", "Description"],
        "output_cols": ["Category", "Issue", "Platform", "Description", "Do", "Don't", "Code Example Good", "Code Example Bad", "Severity"]
    },
    "component": {
        "file": "components.csv",
        "search_cols": ["Component", "Category", "Keywords", "Best For"],
        "output_cols": ["Component", "Category", "Keywords", "Variants", "CSS/Code", "Tailwind", "Accessibility", "Best For"]
    },
    "animation": {
        "file": "animations.csv",
        "search_cols": ["Animation", "Category", "Keywords", "Best For"],
        "output_cols": ["Animation", "Category", "Keywords", "CSS Code", "Duration", "Easing", "GPU Friendly", "Reduced Motion", "Best For"]
    },
    "responsive": {
        "file": "responsive.csv",
        "search_cols": ["Pattern", "Category", "Keywords", "Best For"],
        "output_cols": ["Pattern", "Category", "Keywords", "Breakpoints", "CSS", "Tailwind", "Best For"]
    },
    "design_token": {
        "file": "design_tokens.csv",
        "search_cols": ["Token Category", "Token Name", "Keywords", "Usage"],
        "output_cols": ["Token Category", "Token Name", "Keywords", "Usage", "CSS Variable", "Tailwind", "Value Light", "Value Dark"]
    }
}

STACK_CONFIG = {
    "html-tailwind": {"file": "stacks/html-tailwind.csv"},
    "react": {"file": "stacks/react.csv"},
    "nextjs": {"file": "stacks/nextjs.csv"},
    "astro": {"file": "stacks/astro.csv"},
    "vue": {"file": "stacks/vue.csv"},
    "nuxtjs": {"file": "stacks/nuxtjs.csv"},
    "nuxt-ui": {"file": "stacks/nuxt-ui.csv"},
    "svelte": {"file": "stacks/svelte.csv"},
    "swiftui": {"file": "stacks/swiftui.csv"},
    "react-native": {"file": "stacks/react-native.csv"},
    "flutter": {"file": "stacks/flutter.csv"},
    "shadcn": {"file": "stacks/shadcn.csv"},
    "jetpack-compose": {"file": "stacks/jetpack-compose.csv"},
    "angular": {"file": "stacks/angular.csv"},
    "laravel": {"file": "stacks/laravel.csv"},
    "threejs": {"file": "stacks/threejs.csv"}
}

_STACK_COLS = {
    "search_cols": ["Category", "Guideline", "Description", "Do", "Don't"],
    "output_cols": ["Category", "Guideline", "Description", "Do", "Don't", "Code Good", "Code Bad", "Severity", "Docs URL"]
}

AVAILABLE_STACKS = list(STACK_CONFIG.keys())


# ============ ENHANCED BM25 WITH FUZZY MATCHING ============
class EnhancedBM25:
    """BM25 ranking with fuzzy matching, synonym support, and semantic boosting"""

    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus = []
        self.raw_docs = []
        self.doc_lengths = []
        self.avgdl = 0
        self.idf = {}
        self.doc_freqs = defaultdict(int)
        self.N = 0
        self.vocabulary = set()
        self.synonym_map = self._build_synonym_map()

    def _build_synonym_map(self):
        """Build synonym map for semantic matching"""
        return {
            "modern": ["contemporary", "current", "latest", "new", "futuristic", "cutting-edge"],
            "minimal": ["minimalist", "clean", "simple", "basic", "essential", "stripped"],
            "dark": ["night", "midnight", "dim", "shadow", "noir", "obsidian"],
            "elegant": ["sophisticated", "refined", "graceful", "classy", "premium", "luxury"],
            "bold": ["strong", "powerful", "striking", "vibrant", "dynamic", "impactful"],
            "soft": ["gentle", "smooth", "subtle", "muted", "calm", "peaceful"],
            "tech": ["technology", "digital", "cyber", "electronic", "smart", "advanced"],
            "creative": ["artistic", "innovative", "imaginative", "original", "unique", "experimental"],
            "professional": ["business", "corporate", "formal", "enterprise", "serious", "commercial"],
            "playful": ["fun", "colorful", "vibrant", "energetic", "lively", "dynamic"],
            "warm": ["cozy", "comfortable", "inviting", "friendly", "approachable", "welcoming"],
            "cool": ["fresh", "crisp", "clean", "icy", "frosty", "chill"],
            "trust": ["reliable", "secure", "safe", "credible", "dependable", "stable"],
            "fast": ["quick", "rapid", "speedy", "instant", "immediate", "swift"],
            "smooth": ["fluid", "seamless", "polished", "refined", "flowing", "silk"],
            "gradient": ["transition", "blend", "fade", "shift", "morph", "flow"],
            "animation": ["motion", "movement", "transition", "effect", "dynamic", "kinetic"],
            "responsive": ["adaptive", "flexible", "fluid", "mobile-first", "adaptive", "progressive"],
            "accessible": ["inclusive", "usable", "a11y", "universal", "barrier-free", "compliant"],
            "ux": ["user experience", "usability", "interaction", "interface", "user-centered"],
            "ui": ["user interface", "visual", "design", "graphical", "front-end"],
            "saas": ["software as a service", "cloud", "subscription", "platform", "app"],
            "ecommerce": ["e-commerce", "shop", "store", "retail", "marketplace", "commerce"],
            "dashboard": ["admin", "panel", "control", "analytics", "overview", "monitor"],
            "landing": ["homepage", "hero", "front page", "main page", "start page"],
            "mobile": ["phone", "app", "responsive", "touch", "handheld", "portable"],
            "dark mode": ["night mode", "dark theme", "dark UI", "noir", "obsidian theme"],
            "glassmorphism": ["glass", "frosted", "blur", "transparent", "glassy"],
            "neumorphism": ["soft ui", "embossed", "debossed", "soft 3D", "soft shadow"],
            "brutalism": ["raw", "stark", "bold", "industrial", "anti-design"],
            "cyberpunk": ["cyber", "futuristic", "neon", "sci-fi", "tech-noir"],
            "organic": ["natural", "biophilic", "eco", "sustainable", "green", "earthy"],
        }

    def _expand_query(self, query):
        """Expand query with synonyms for better matching"""
        tokens = self.tokenize(query)
        expanded = list(tokens)
        for token in tokens:
            for key, synonyms in self.synonym_map.items():
                if token == key or token in synonyms:
                    expanded.extend([key] + synonyms)
                    break
        return expanded

    def tokenize(self, text):
        """Lowercase, split, remove punctuation, filter short words"""
        text = re.sub(r'[^\w\s]', ' ', str(text).lower())
        return [w for w in text.split() if len(w) > 2]

    def fit(self, documents):
        """Build BM25 index from documents"""
        self.raw_docs = documents
        self.corpus = [self.tokenize(doc) for doc in documents]
        self.N = len(self.corpus)
        if self.N == 0:
            return
        self.doc_lengths = [len(doc) for doc in self.corpus]
        self.avgdl = sum(self.doc_lengths) / self.N

        for doc in self.corpus:
            self.vocabulary.update(doc)
            seen = set()
            for word in doc:
                if word not in seen:
                    self.doc_freqs[word] += 1
                    seen.add(word)

        for word, freq in self.doc_freqs.items():
            self.idf[word] = log((self.N - freq + 0.5) / (freq + 0.5) + 1)

    def _fuzzy_score(self, token, doc_tokens):
        """Calculate fuzzy match score between token and document tokens"""
        score = 0
        for doc_token in doc_tokens:
            # Exact match
            if token == doc_token:
                score += 3.0
            # Prefix match (e.g., "minimal" matches "minimalism")
            elif doc_token.startswith(token) or token.startswith(doc_token):
                score += 2.0
            # Contains match
            elif token in doc_token or doc_token in token:
                score += 1.5
        return score

    def score(self, query, use_synonyms=True):
        """Score all documents against query with fuzzy matching and synonym expansion"""
        query_tokens = self.tokenize(query)
        expanded_tokens = self._expand_query(query) if use_synonyms else query_tokens
        scores = []

        for idx, doc in enumerate(self.corpus):
            score = 0
            doc_len = self.doc_lengths[idx]
            term_freqs = defaultdict(int)
            for word in doc:
                term_freqs[word] += 1

            # Exact BM25 scoring
            for token in query_tokens:
                if token in self.idf:
                    tf = term_freqs[token]
                    idf = self.idf[token]
                    numerator = tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                    score += idf * numerator / denominator

            # Fuzzy matching for expanded tokens
            for token in expanded_tokens:
                if token not in query_tokens:  # Only for expanded tokens
                    score += self._fuzzy_score(token, doc) * 0.5

            scores.append((idx, score))

        return sorted(scores, key=lambda x: x[1], reverse=True)


# ============ SEARCH FUNCTIONS ============
def _load_csv(filepath):
    """Load CSV and return list of dicts"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    """Core search function using Enhanced BM25"""
    if not filepath.exists():
        return []

    data = _load_csv(filepath)
    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

    bm25 = EnhancedBM25()
    bm25.fit(documents)
    ranked = bm25.score(query)

    results = []
    for idx, score in ranked[:max_results]:
        if score > 0:
            row = data[idx]
            results.append({col: row.get(col, "") for col in output_cols if col in row})

    return results


def detect_domain(query):
    """Auto-detect the most relevant domain from query"""
    query_lower = query.lower()

    domain_keywords = {
        "color": ["color", "palette", "hex", "#", "rgb", "hsl", "scheme"],
        "chart": ["chart", "graph", "visualization", "trend", "bar", "pie", "scatter", "heatmap", "funnel", "data viz"],
        "landing": ["landing", "page", "cta", "conversion", "hero", "testimonial", "pricing", "section", "above fold"],
        "product": ["saas", "ecommerce", "e-commerce", "fintech", "healthcare", "gaming", "portfolio", "crypto", "dashboard", "app", "platform"],
        "style": ["style", "design", "ui", "minimalism", "glassmorphism", "neumorphism", "brutalism", "dark mode", "flat", "aurora", "prompt", "css", "implementation", "variable", "checklist", "tailwind", "theme", "visual"],
        "ux": ["ux", "usability", "accessibility", "wcag", "touch", "scroll", "animation", "keyboard", "navigation", "mobile", "interaction", "user experience"],
        "typography": ["font", "typography", "heading", "serif", "sans", "typeface", "lettering", "text"],
        "icons": ["icon", "icons", "lucide", "heroicons", "symbol", "glyph", "pictogram", "svg icon"],
        "react": ["react", "next.js", "nextjs", "suspense", "memo", "usecallback", "useeffect", "rerender", "bundle", "waterfall", "barrel", "dynamic import", "rsc", "server component"],
        "web": ["aria", "focus", "outline", "semantic", "virtualize", "autocomplete", "form", "input type", "preconnect"],
        "component": ["component", "button", "card", "modal", "dropdown", "input", "form", "widget", "element", "building block"],
        "animation": ["animation", "transition", "motion", "keyframe", "easing", "spring", "parallax", "scroll reveal"],
        "responsive": ["responsive", "breakpoint", "mobile", "tablet", "grid", "flex", "adaptive", "fluid"],
        "design_token": ["token", "design system", "variable", "css variable", "spacing", "shadow", "border radius", "color token"]
    }

    scores = {domain: sum(1 for kw in keywords if kw in query_lower) for domain, keywords in domain_keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "style"


def search(query, domain=None, max_results=MAX_RESULTS):
    """Main search function with auto-domain detection"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["style"])
    filepath = DATA_DIR / config["file"]

    if not filepath.exists():
        return {"error": f"File not found: {filepath}", "domain": domain}

    results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)

    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results
    }


def search_stack(query, stack, max_results=MAX_RESULTS):
    """Search stack-specific guidelines"""
    if stack not in STACK_CONFIG:
        return {"error": f"Unknown stack: {stack}. Available: {', '.join(AVAILABLE_STACKS)}"}

    filepath = DATA_DIR / STACK_CONFIG[stack]["file"]

    if not filepath.exists():
        return {"error": f"Stack file not found: {filepath}", "stack": stack}

    results = _search_csv(filepath, _STACK_COLS["search_cols"], _STACK_COLS["output_cols"], query, max_results)

    return {
        "domain": "stack",
        "stack": stack,
        "query": query,
        "file": STACK_CONFIG[stack]["file"],
        "count": len(results),
        "results": results
    }


def multi_search(query, domains=None, max_results=MAX_RESULTS):
    """Search across multiple domains simultaneously"""
    if domains is None:
        domains = ["style", "color", "typography", "product", "landing"]

    results = {}
    for domain in domains:
        results[domain] = search(query, domain, max_results)
    return {"query": query, "results": results}
