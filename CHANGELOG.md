# 📦 CHANGELOG

## v0.2.0 (2025-05-25)

### ✨ New Features

- **Modular Export Architecture**:
  - Introduced `BaseExporter` for unified export behavior.
  - Added `ExporterFactory` to dynamically instantiate exporters.
  - Exporters implemented: `JSON`, `CSV`, `HTML`, `Markdown`, `PDF`, `Fancy HTML`, `Terminal`.

- **Threaded Exporting with `tqdm`**:
  - Exporters now support multithreaded file generation.
  - Unified `--workers` flag controls crawling, analysis, and exporting.
  - Progress bars added to all stages.

- **`SmartBatchSEOAnalyzer` Overhaul**:
  - Uses `ThreadPoolExecutor` for both crawling and analysis.
  - Supports progress bars and shared thread pool count.
  - Flexible crawling enabled with `follow_links`.

- **Improved CLI (`cli.py`)**:
  - `--export` format: `json`, `csv`, `pdf`, etc.
  - `--workers` applies to all threaded stages.
  - `--crawl` enables internal link discovery.
  - Uses factory + threaded exporters by default.

---

### ⚙️ Analyzer Engine Enhancements

- **Feature Flag System** for toggling individual checks using bitmasks.
- **Keyword Control for Density Analysis**:
  - `disallow_keyword()` and `allow_keyword()` for tuning ignored keywords.
  - `get_disallowed_keywords()` to inspect all exclusions.
- **Structured Logging**:
  - Centralized log to `seo_errors.log` using `logging`.

---

### 🐛 Fixes & Improvements

- Exported file naming now includes path-safe slugs to prevent overwrites.
- CLI decoupled from export logic — calls exporters via factory.
- Unicode-safe PDF export.
- General performance and concurrency improvements.

---

### 🔜 Upcoming

- CLI support for `--include` / `--exclude` using feature flags.
- `.seoignore` support to exclude paths/URLs.
- Rich HTML export dashboard for site-wide summaries.
