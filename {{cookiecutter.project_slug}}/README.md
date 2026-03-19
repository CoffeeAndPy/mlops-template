# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

**Autor:** {{cookiecutter.author_name}}  
**Licencia:** {{cookiecutter.open_source_license}}

---

## Project Structure

```
{{cookiecutter.project_slug}}/
    ├── .github/                        # GitHub Actions workflows
    │   ├── workflows/
    │   │   ├── ci.yml                  # Lint + tests + build on each PR
    │   │   └── cd.yml                  # Train + publish + deploy
    ├── api/                            # FastAPI application code
    │   └── __init__.py 
    ├── data/                           # Data storage
    │   ├── processed/                  # Processed datasets
    |   └── raw/                        # Raw datasets
    ├── notebooks/                      # Jupyter notebooks for EDA and prototyping
    │   └── 01_exploration.ipynb        # Initial exploration notebook
    ├── src/                            # Source code for training, evaluation, and utilities
    │   ├── data/                       # Data loading and processing
    │   ├── models/                     # Model definition and training
    │   └── __init__.py
    ├── tests/                          # Unit and integration tests
    │   └── __init__.py
    ├── .env.example                    # example environment variables
    ├── .gitignore                      # git ignore rules    
    ├── Dockerfile                      # multi-stage build
    ├── docker-compose.yml              # local development stack with hot-reload
    ├── Makefile                        # operation interface (make help)
    ├── params.yaml                     # versioned hyperparameters
    ├── README.md                       # project documentation
    └── requirements.txt                # project dependencies

```

