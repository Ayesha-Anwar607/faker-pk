# Changelog

All notable changes to the `faker-pk` project will be documented in this file.

## [v2.0.0] 

### Added
- **SQLite Database Architecture**: Migrated data storage from static Python dictionaries to an optimized SQLite database backend (`faker_pk.db`) for faster, maintainable queries.
- **Education Module (`education.py`)**: Added support for generating localized Pakistani education data, including degree levels, majors, universities, grading metrics, and complete student profiles.
- **15 Industry Sectors**: Expanded company and job generation across 15 distinct industry sectors (IT/Software, Banking, Healthcare, Textile, Agriculture, Telecommunications, FMCG, Petroleum, Logistics, Media, etc.).
- **Industry-Aware Financial Data**: Added realistic job-level salary ranges (PKR), bank names, and valid formatted IBAN generation.
- **Faker Provider Integration**: Custom provider class `FakerPKProvider` for seamless integration into the standard `faker` library ecosystem.
- **GitHub Actions CI/CD Pipeline**: Configured automated test suites, pytest execution, and coverage tracking workflow.

### Changed
- **Modularized Test Suite**: Split test scripts into 26+ focused unit test modules in `tests/` covering personal, address, company, education, and provider interfaces.
- **Packaging & Build System**: Standardized package setup using `pyproject.toml` and setuptools configuration.
- **Documentation**: Overhauled `README.md` with complete API reference tables, installation instructions, usage examples, and author/maintainer metadata.

### Improved
- **Test Coverage**: Increased code coverage from unmonitored baseline to **>90%**.
- **CNIC & Gender Parity Validation**: Ensured strict formatting (`xxxxx-xxxxxxx-x`) and accurate gender matching based on CNIC last digit rules.

---

## [v1.0.0] - Initial Legacy Release

### Added
- Initial Pakistani personal data generation (male/female names, CNIC numbers, mobile numbers, network providers).
- Basic address generation (cities, provinces, full addresses).
- Basic company names and job titles.
- Initial package structure for PyPI distribution.
