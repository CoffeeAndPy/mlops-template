# mlops-template

Cookiecutter template for MLOps projects with production-ready.

## Use

```bash
# Install cookiecutter (only the first time)
pip install cookiecutter

# Generate a new project from GitHub
cookiecutter gh:{{cookiecutter.github_username}}/mlops-template

# Or from local (for template development)
cookiecutter ./mlops-template
```

Cookiecutter will ask you:

```
project_name [My MLOps Project]: Housing Price Predictor
project_description [A machine learning project...]: Predicts housing prices
author_name [Your Name]: Your Name
github_username [your-github-username]: Your GitHub Username
python_version [3.11]:
mlflow_port [5000]:
api_port [8000]:
Select open_source_license:
1 - MIT
2 - Apache-2.0
3 - None
```

And it will generate the project folder with everything set up.

## What it includes

| File | Purpose |
|---|---|
| `.github/workflows/` | GitHub Actions workflows for CI/CD |
| `notebooks/` | Jupyter notebooks for EDA and prototyping |
| `.env.example` | Example environment variables |
| `.gitignore` | Git ignore rules |
| `Dockerfile` | Multi-stage build (builder + runtime) |
| `docker-compose.yml` | Local development stack with hot-reload |
| `Makefile` | Operation interface (`make help`) |
| `params.yaml` | Versioned hyperparameters |
| `README.md` | Project documentation |
| `requirements.txt` | Project dependencies |

