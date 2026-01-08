#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design Intelligence Core - BM25 search engine for UI/UX style guides
"""

import csv
import re
from pathlib import Path
from math import log
from collections import defaultdict

# ============ CONFIGURATION ============
# Data directory relative to this script: ../data
DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3

CSV_CONFIG = {
    "style": {
        "file": "styles.csv",
        "search_cols": ["Style Category", "Keywords", "Best For", "Type"],
        "output_cols": ["Style Category", "Keywords", "Primary Colors", "Secondary Colors", "Effects & Animation", "Best For"]
    },
    "typography": {
        "file": "typography.csv",
        "search_cols": ["Pairing Name", "Keywords", "Vibe"],
        "output_cols": ["Pairing Name", "Header Font", "Body Font", "Google Fonts Import", "Usage Context"]
    },
    "color": {
        "file": "colors.csv",
        "search_cols": ["Palette Name", "Keywords", "Industry"],
        "output_cols": ["Palette Name", "Primary", "Secondary", "Accent", "Background", "Surface", "Description"]
    },
    "chart": {
        "file": "charts.csv",
        "search_cols": ["Chart Type", "Keywords", "Use Case", "Accessibility Notes"],
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
        "output_cols": ["Category", "Issue", "Best Practice", "Anti-Pattern", "Accessibility Impact", "Platform"]
    }
}

# Add Stack Support
AVAILABLE_STACKS = {
    "html-tailwind", "react", "nextjs", "vue", "svelte", "swiftui", "react-native", "flutter"
}

def load_data(domain):
    """Load CSV data for a domain"""
    if domain not in CSV_CONFIG:
        return []
    
    config = CSV_CONFIG[domain]
    file_path = DATA_DIR / config["file"]
    
    if not file_path.exists():
        return []
        
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Create a searchable text blob
                search_text = " ".join([row.get(col, "") for col in config["search_cols"]]).lower()
                row["_search_text"] = search_text
                data.append(row)
    except Exception as e:
        print(f"Error loading {domain}: {e}")
        
    return data

def load_stack_data(stack):
    """Load CSV data for a specific stack"""
    file_path = DATA_DIR / "stacks" / f"{stack}.csv"
    
    if not file_path.exists():
        return []
        
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Searchable text
                search_text = (row.get("Category", "") + " " + row.get("Keywords", "")).lower()
                row["_search_text"] = search_text
                data.append(row)
    except Exception as e:
        print(f"Error loading stack {stack}: {e}")
        
    return data

def bm25_score(query, documents):
    """
    Simple ranking algorithm
    """
    query_terms = query.lower().split()
    scored_results = []
    
    for doc in documents:
        score = 0
        doc_text = doc.get("_search_text", "")
        
        # Simple term matching weight
        matches = 0
        for term in query_terms:
            if term in doc_text:
                score += 10 # Exact match bonus
                matches += 1
                
        # Fuzzy partial match
        if matches > 0:
            scored_results.append((score, doc))
            
    # Sort by score desc
    scored_results.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored_results]

def search(query, domain, limit=MAX_RESULTS):
    data = load_data(domain)
    if not data:
        return [{"error": f"No data found for domain: {domain}"}]
        
    results = bm25_score(query, data)
    
    # Format output based on config
    formatted = []
    config = CSV_CONFIG[domain]
    
    for item in results[:limit]:
        entry = {k: item.get(k, "N/A") for k in config["output_cols"]}
        formatted.append(entry)
        
    return formatted

def search_stack(query, stack, limit=MAX_RESULTS):
    if stack not in AVAILABLE_STACKS:
        return [{"error": f"Stack not supported: {stack}"}]
        
    data = load_stack_data(stack)
    if not data:
        return [{"error": f"No data found for stack: {stack}"}]
        
    results = bm25_score(query, data)
    
    formatted = []
    for item in results[:limit]:
        # Intelligent Output for Stacks
        entry = {
            "Category": item.get("Category", "General"),
            "Pattern": item.get("Pattern Name", "N/A"),
            "Code/Rule": item.get("Code Snippet / Rule", "N/A"),
            "Explanation": item.get("Explanation", "N/A")
        }
        formatted.append(entry)
        
    return formatted
