# Changelog

All notable changes to the `faker-pk` project will be documented in this file.

## [v0.2.0] - Aug 4, 2026

### Added
- **SQLite Database Architecture**: Migrated data storage from static Python dictionaries to an optimized SQLite database backend (`faker_pk.db`) for faster, maintainable queries.
- **Education Module (`education.py`)**: Added support for generating localized Pakistani education data, including degree levels, universities and complete student profiles.
- **15 Industry Sectors**: Expanded company and job generation across 15 distinct industry sectors (IT/Software, Banking, Healthcare, Textile, Agriculture, Telecommunications, Media, etc.).
- **Industry-Aware Financial Data**: Added realistic job-level salary ranges (PKR), bank names, and valid formatted IBAN generation.
- **Faker Provider Integration**: Custom provider class `FakerPKProvider` for seamless integration into the standard `faker` library ecosystem.
- **GitHub Actions CI/CD Pipeline**: Configured automated test suites, pytest execution, and coverage tracking workflow.

### Changed
- **Modularized Test Suite**: Split test scripts into 26+ focused unit test modules in `tests/` covering personal, address, company, education, and provider interfaces.
- **Packaging & Build System**: Standardized package setup using `pyproject.toml` and setuptools configuration.

### Improved
- **Test Coverage**: Increased code coverage from unmonitored baseline to **>90%**.
- **CNIC & Gender Parity Validation**: Ensured strict formatting (`xxxxx-xxxxxxx-x`) and accurate gender matching based on CNIC last digit rules.

---
## [v0.1.9] - Sep 18, 2025

### Added
- Industry-aware salary generation with refined distributions aligned to actual industry tiers across entry, mid, and senior levels.
- Provider API standardization — all provider methods follow `pk_*` naming convention for parity with core Faker.

### Changed
- Improved city–province mappings for more consistent address generation.
- Cleaner formatting for `full_address()` output across urban and regional locations.
- Updated datasets for names, companies, and industries with reduced edge-case repeats.

### Improved
- More stable CNIC and phone number generation with fewer duplicates.
- Salary variation across experience levels within each industry.
- Internal codebase cleanup, minor fixes, and optimization across modules.