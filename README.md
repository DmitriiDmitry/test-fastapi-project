# FastAPI Test Project

This is a learning project built with [FastAPI](https://fastapi.tiangolo.com/), showcasing various modern Python tools and libraries used in real-world web backend development. The goal of this project was to get hands-on experience with asynchronous frameworks, background task processing, dependency injection, ORM, caching, and testing.

## 🚀 Stack Overview

### Core Framework
- **FastAPI**: Main web framework for building high-performance APIs with Python.
- **Uvicorn** + **Gunicorn**: ASGI servers for running the app in both development and production.

### ORM and Database
- **SQLAlchemy**: ORM for database models and interactions.
- **AsyncPG**: Asynchronous PostgreSQL driver.
- **Alembic**: For handling database migrations.

### Auth and Security
- **python-jose**, **passlib**: Used for handling JWT authentication and password hashing.
- **python-dotenv**: Manage environment variables securely.

### Background Tasks
- **Celery**: For managing background tasks.
- **Redis**: As a message broker for Celery.
- **Flower**: Monitoring Celery workers.

### Caching & Monitoring
- **fastapi-cache2**: Provides response-level caching.
- **prometheus-fastapi-instrumentator** + **prometheus_client**: Metrics and performance monitoring.

### Admin Panel
- **SQLAdmin**: Auto-generated admin interface for SQLAlchemy models.

### Linting & Code Formatting
- **Black**, **Isort**, **Autoflake**: Code formatting and cleanup.
- **Flake8**, **Pyflakes**, **Mypy**, **Pyright**: Static code analysis and type checking.

### Testing
- **Pytest**, **pytest-asyncio**: For unit and async integration testing.

### Containerization
- **Docker**: Used to package the service into an isolated container.
- **Docker Compose**: Manages a multi-container setup, allowing the service to run alongside all required dependencies (e.g., database, redis, etc.) with a single command.

### Others
- **HTTPX**, **httpcore**, **orjson**: For high-performance HTTP operations and JSON serialization.
- **logging**, **python-json-logger**: Used for logging.


# 🚀 Running Locally

1. **Clone the repo:**

    ```bash
    git clone https://github.com/DmitriiDmitry/test-fastapi-project.git
    cd test-fastapi-project
    ```

2. **Create and activate virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app (development mode):**

    ```bash
    uvicorn main:app --reload
    ```

---

## 📂 Environment Variables

Use `.env` or `.env-non-dev` to manage configuration secrets.

**Example `.env.example`:**

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
SECRET_KEY=your-secret-key
DEBUG=True
```



✨ What I Learned
	•	Structuring FastAPI projects for scalability
	•	Handling async database operations with SQLAlchemy 2.0
	•	Implementing JWT-based authentication
	•	Running and monitoring background tasks with Celery and Redis
	•	Applying linters, formatters, and type checkers for clean, safe code
	•	Writing async tests with pytest
	•	Configuring observability with Prometheus
	•	Using auto-generated admin panels with SQLAdmin

⸻

📜 License

This project is for educational purposes and does not include a license. Use it as a reference or a base for your own experiments.

