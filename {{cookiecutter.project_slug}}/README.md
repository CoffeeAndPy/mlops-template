# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

**Autor:** {{cookiecutter.author_name}}  
**Licencia:** {{cookiecutter.open_source_license}}

---

## Project Structure

```
{{cookiecutter.project_slug}}/
    ├── .github/                    # GitHub Actions workflows
    │   ├── workflows/
    │   │   ├── ci.yml              # Lint + tests + build on each PR
    │   │   └── cd.yml              # Train + publish + deploy
    ├── notebooks/                   # Jupyter notebooks for EDA and prototyping
    │   └── 01_exploration.ipynb     # Initial exploration notebook
    ├── .env.example                # example environment variables
    ├── .gitignore                  # git ignore rules    
    ├── Dockerfile                  # multi-stage build
    ├── docker-compose.yml          # local development stack with hot-reload
    ├── Makefile                    # operation interface (make help)
    ├── params.yaml                 # versioned hyperparameters
    ├── README.md                   # project documentation
    └── requirements.txt            # project dependencies

```

