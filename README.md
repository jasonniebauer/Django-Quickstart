# Django Quickstart
Template for Django projects.

## Project Structure
```
Django-Quickstart
├── app/
│   ├── media/
│   ├── static/
│   ├── templates/
|   ├── __init__.py
|   ├── admin.py
|   ├── apps.py
|   ├── models.py
│   ├── tests.py
│   └── views.py
├── config/
│   ├── __init.py__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docs/
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

### Repository Root Files and Directories
| File or Directory | Purpose |
|:------------------|:--------|
| .gitignore        | Lists the files and directories Git should ignore. |
| app/              | The root directory of the project. |
| config/           | Project-wide configuration settings for the project. |
| README.md and docs/ | Developer-facing project documentation. |
| requirements.txt  | A list of Python packages required by the project, including the Django package. |

### Django Project Files and Directories
| File or Directory | Purpose |
|:------------------|:--------|
| media/            | For use in development only: User-generated static media assets such as photos uploaded by users. |
| static/           | Non-user-generated static media assets including CSS, JavaScript, and images. |
| templates/        | Where you put your site-wide Django templates. |