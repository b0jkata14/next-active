# NextActive

NextActive is a platform that connects users with certified personal trainers. Whether you're looking to improve in your favorite activity, train for a competition, or simply stay active, NextActive helps you find the perfect trainer to meet your needs – across a wide range of sports and disciplines.

## Installation

### 1. Clone the repo

```bash
  git clone https://github.com/b0jkata14/next-active.git
```
   
### 2. Install dependencies
```bash
  pip install -r requirements.txt
```

### 3. Create the `.env` file in the root of your project.

#### Example `.env`

```python
# Development settings
SECRET_KEY=your_secret_key_here
DEBUG=True
```

### 4. Run the migrations

```bash
  python manage.py migrate
```

### 5. Run the project

```bash
  python manage.py runserver
```
