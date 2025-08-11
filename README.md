# Simple Notifier - Modular Notification API Server Which Integrates To Different Services

## Getting Started

1. Install and set up Simple Notifier using the [installation instructions](#installation) below
2. Deploy it on a server or run it temporarily as needed: [See Deployment Instructions](#Deployment)

## Installation

### Prerequisites:

- `git`
- `python >= 3.13`

### With `uv` (recommended):

- Clone this repository
- Move into cloned repository root directory
- Enable wanted modules moving `.py` files from `modules/available` to `modules/active`
    - On Windows use `\` instead of `/`
- Configure these modules in their respective files

### With `pip`

- Clone this repository
- Move into the cloned repository's root directory
- Create virtual environment with `python -m venv venv`
- Source virtual environment using:
	- `source venv/bin/activate` on Unix based OS
	- `source.\venv\Scripts\activate` on Windows.
- Install necessary packages with `pip install -r requirements.txt`
- Enable wanted modules moving `.py` files from `modules/available` to `modules/active`
    - On Windows use `\` instead of `/`
- Configure these modules in their respective files

## Deployment

### Temporary Launch

- With `uv`: `uv run fastapi run main.py`
- With `pip`: `fastapi run main.py`

The server will then be launched on port 8080
Visit `http://IP:8080/docs` to see available endpoints an their arguments

### Persistant Deploy

**Comming soon ...**

## Contributing

To contribute to this repository:

- Fork the repository
- Clone the forked repository to your local machine
- Create a new branch for your contribution
- Make changes, commit, and push to your fork
- Create a pull request to the original repository

Please:
- Follow the existing coding style
- Test new features
- Use commit messages that are meaningful and consistent in style with existing ones
- For new modules, utilize `template.py` and embed configuration instructions directly in the file

## License
Simple Notifier is a free software and it's released under the terms of the MIT [LICENSE file](LICENSE)
