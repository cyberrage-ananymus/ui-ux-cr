#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI UX CR Search - Enhanced BM25 search engine with fuzzy matching
Cyber-Rage Design Intelligence Engine

Usage: python search.py "<query>" [--domain <domain>] [--stack <stack>] [--max-results 3]
       python search.py "<query>" --design-system [-p "Project Name"]
       python search.py "<query>" --design-system --persist [-p "Project Name"] [--page "dashboard"]
       python search.py "<query>" --multi-domains style,color,typography
       python search.py "<query>" --analyze
"""

import argparse
import sys
import io
import json
from core import CSV_CONFIG, AVAILABLE_STACKS, MAX_RESULTS, search, search_stack, multi_search
from design_system import generate_design_system, persist_design_system

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def format_output(result):
    """Format results for Claude consumption (token-optimized)"""
    if "error" in result:
        return f"Error: {result['error']}"

    output = []
    if result.get("stack"):
        output.append(f"## UI UX CR Stack Guidelines")
        output.append(f"**Stack:** {result['stack']} | **Query:** {result['query']}")
    elif result.get("domains"):
        output.append(f"## UI UX CR Multi-Domain Search")
        output.append(f"**Domains:** {', '.join(result['domains'])} | **Query:** {result.get('query', 'N/A')}")
    else:
        output.append(f"## UI UX CR Search Results")
        output.append(f"**Domain:** {result['domain']} | **Query:** {result['query']}")
    output.append(f"**Source:** {result.get('file', 'multiple')} | **Found:** {result.get('count', 0)} results\n")

    if "domains" in result:
        for domain, domain_result in result.get("results", {}).items():
            output.append(f"### Domain: {domain}")
            for i, row in enumerate(domain_result.get("results", []), 1):
                output.append(f"#### Result {i}")
                for key, value in row.items():
                    value_str = str(value)
                    if len(value_str) > 300:
                        value_str = value_str[:300] + "..."
                    output.append(f"- **{key}:** {value_str}")
                output.append("")
    else:
        for i, row in enumerate(result.get('results', []), 1):
            output.append(f"### Result {i}")
            for key, value in row.items():
                value_str = str(value)
                if len(value_str) > 300:
                    value_str = value_str[:300] + "..."
                output.append(f"- **{key}:** {value_str}")
            output.append("")

    return "\n".join(output)


def analyze_project(query):
    """Comprehensive project analysis with recommendations across all domains"""
    domains = ["product", "style", "color", "typography", "landing", "ux", "component", "animation", "responsive"]
    results = multi_search(query, domains, max_results=3)

    output = []
    output.append("## UI UX CR - Project Analysis")
    output.append(f"**Query:** {query}")
    output.append("")

    search_results = results.get("results", {})
    for domain, result in search_results.items():
        results_list = result.get("results", [])
        if results_list:
            output.append(f"### {domain.upper()} Recommendations")
            for i, row in enumerate(results_list, 1):
                output.append(f"**{i}.** {json.dumps(row, ensure_ascii=False)[:200]}")
            output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UI UX CR Search - Cyber-Rage Design Intelligence Engine")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="Search domain")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help="Stack-specific search")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="Max results (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--design-system", "-ds", action="store_true", help="Generate complete design system")
    parser.add_argument("--project-name", "-p", type=str, default=None, help="Project name")
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"], default="ascii", help="Output format")
    parser.add_argument("--persist", action="store_true", help="Save design system to design-system/")
    parser.add_argument("--page", type=str, default=None, help="Create page-specific override file")
    parser.add_argument("--output-dir", "-o", type=str, default=None, help="Output directory")
    parser.add_argument("--multi-domains", "-md", type=str, default=None, help="Comma-separated domains to search")
    parser.add_argument("--analyze", "-a", action="store_true", help="Comprehensive project analysis")

    args = parser.parse_args()

    if args.analyze:
        print(analyze_project(args.query))
    elif args.design_system:
        result = generate_design_system(
            args.query,
            args.project_name,
            args.format,
            persist=args.persist,
            page=args.page,
            output_dir=args.output_dir
        )
        print(result)

        if args.persist:
            project_slug = args.project_name.lower().replace(' ', '-') if args.project_name else "default"
            print("\n" + "=" * 60)
            print(f"Design system persisted to design-system/{project_slug}/")
            print(f"   design-system/{project_slug}/MASTER.md")
            if args.page:
                page_filename = args.page.lower().replace(' ', '-')
                print(f"   design-system/{project_slug}/pages/{page_filename}.md")
            print("=" * 60)
    elif args.multi_domains:
        domains = [d.strip() for d in args.multi_domains.split(",")]
        result = multi_search(args.query, domains, args.max_results)
        result["domains"] = domains
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
    elif args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
    else:
        result = search(args.query, args.domain, args.max_results)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
