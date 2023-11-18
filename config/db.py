from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MSSQL = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'basedb',
        'USER': 'sa',
        'PASSWORD': 'Password123.',
        'HOST': 'DESKTOP-RTR90I9',
        'PORT': '1433',
        'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server',
                    },
    }
}