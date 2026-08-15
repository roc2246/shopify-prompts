---
name: shopify-test-quality
description: Audit Shopify theme quality checks and test coverage, including Theme Check, lint/build validation, storefront interaction tests, and unit tests for nontrivial JS/TS when a test framework exists. Use for test/quality-gate requests.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Use the shared workflow/output. Do not demand unit tests for static Liquid markup by default. Match tests to failure risk: Theme Check for Liquid/JSON, browser/interaction coverage for storefront behavior, and unit tests for nontrivial pure JS/TS logic when the project supports them.

# Workflow

See `.agents/skills/_base/common-workflow.md`.

# Output

See `.agents/skills/_base/common-output.md`.
