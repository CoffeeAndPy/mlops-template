# STAGE 1: builder
#
# Objective: install and compile all Python dependencies.
# This stage does NOT end up in the final image.
FROM python:{{cookiecutter.python_version}}-slim AS builder

WORKDIR /build

# This install gcc only in the builder, not in the final runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*  

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
#                               ^^^^^^^^^^^^^^^^
#                               install in /install instead of system
#                               so we can cleanly copy it to runtime

# STAGE 2: runtime
#
# Objective: minimal final image with only what's needed to run.
# It doesn't contain pip, gcc, or any build tools.

FROM python:{{cookiecutter.python_version}}-slim AS runtime

# Image metadata
# Useful in corporate registries to know what's in each image
LABEL org.opencontainers.image.title="{{cookiecutter.project_name}}"
LABEL org.opencontainers.image.description="{{cookiecutter.project_description}}"
LABEL org.opencontainers.image.authors="{{cookiecutter.author_name}}"
LABEL org.opencontainers.image.source="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}"

WORKDIR /app

# Copy ONLY the compiled packages from the builder
# The /install directory contains site-packages with all the wheels
COPY --from=builder /install /usr/local

