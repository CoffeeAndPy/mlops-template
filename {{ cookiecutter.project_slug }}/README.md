# {{ cookiecutter.project_name }}

<!-- Project description -->
{{ cookiecutter.project_short_description }}

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── data                    <- Data sets, usually CSV files or similar.
│   ├── raw                 <- The original, immutable data dump.
│   └── processed           <- The cleaned and processed data sets.
├── models                  <- Trained and serialized models, model predictions, or model summaries.
├── notebooks               <- Jupyter notebooks for exploration and analysis.
├── src                     <- Source code for the project.
├── tests                   <- Unit tests and test data.
├── .gitignore              <- Git ignore file to exclude files from version control.
├── README.md               <- The top-level README for developers using this project.
├── requirements.txt        <- The dependencies file for reproducing the analysis environment.
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd {{ cookiecutter.project_slug }}
   ```
2. Create a virtual environment and activate it:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required packages:
    ```bash
   pip install -r requirements.txt
   ```
4. Run the main script to start the project:
   ```bash
    python src/main.py
    ```

