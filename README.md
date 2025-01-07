<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/GWCustom/bfabric-web-app-template">
    <img src="logo.png" alt="Logo" width="80" height="50.6">
  </a>

<h3 align="center">B-Fabric Web App Template</h3>

<p align="center">
    A fully functional template app to demonstrate the usage of the 
    <a href="https://pypi.org/project/bfabric-web-apps/"><strong>bfabric-web-app</strong></a> Python library.
    <br />
    <br />
    <a href="https://github.com/GWCustom/bfabric-web-app-template">View Demo</a>
    ·
    <a href="https://github.com/GWCustom/bfabric-web-app-template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/GWCustom/bfabric-web-app-template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
## Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Deployment](#deployment)
  - [1. Fork and Clone the Repository](#1-fork-and-clone-the-repository)
  - [2. Set Up a Virtual Environment](#2-set-up-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Configure Your Application](#4-configure-your-application)
  - [5. Set Up .bfabricpy.yml Configuration File](#5-set-up-bfabricpyyml-configuration-file)
  - [6. Run the Application](#6-run-the-application)
  - [7. Check It Out](#7-check-it-out)
- [What Is B-Fabric?](#what-is-bfabric)
- [What Is BfabricPy?](#what-is-bfabricpy)
- [What Is Dash?](#what-is-dash)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)




## About The Project

The `bfabric-web-app-template` serves as an example project built using the [`bfabric-web-app`](https://github.com/GWCustom/bfabric-web-apps) Python library. This template demonstrates how to quickly set up a web app that integrates with the B-Fabric Laboratory Information Management System (LIMS). It provides a starting point for developers to build their custom applications.

Key Features:
- **Preconfigured Setup**: Easily adapt the template to your use case.
- **Integrated API Connection**: Demonstrates how to connect to B-Fabric via the `bfabric-web-app` library.
- **Dash Dashboard Integration**: Includes examples of data visualization with Plotly Dash.
- **Fully Documented Code**: Explore the codebase for learning and extension.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Python][Python.js]][Python-url]
* [![Dash][Dash.js]][Dash-url]
* [![Plotly][Plotly.js]][Plotly-url]
* [![Flask][Flask.js]][Flask-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Deployment

Follow these steps to set up and deploy the B-Fabric Web App Template locally:

### 1. Fork and Clone the Repository

1. **Fork** the repository to your GitHub account.
2. Clone the forked repository to your local machine:
   
   ```sh
   git clone https://github.com/GWCustom/bfabric-web-app-template.git
   cd bfabric-web-app-template
   ```


### 2. Set Up a Virtual Environment

Choose one of the following options to create and activate a virtual environment:

#### Using `virtualenv`:
**For Linux/Mac:**
```sh
python3 -m venv my_app_1
source my_app_1/bin/activate
```

**For Windows:**
```sh
python -m venv my_app_1
my_app_1\Scripts\activate
```

#### Using `conda`:
   ```sh
   conda create -n my_app_1 pip
   conda activate my_app_1
   ```

#### Using `mamba`:
   ```sh
   mamba create -n my_app_1 pip
   mamba activate my_app_1
   ```


### 3. Install Dependencies

Once the virtual environment is active, install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```


### 4. Configure Your Application

Create a file named `PARAMS.py` in the project root directory to define configuration parameters for the app.

**Example `PARAMS.py`**:
   ```python
   # PARAMS.py
   HOST = "0.0.0.0"  # Host to run the app (default: localhost)
   PORT = 8050       # Port to serve the application
   DEV = False       # Enable/disable debug mode
   CONFIG_FILE_PATH = "~/.bfabricpy.yml"  # Path to the configuration file for credentials
   ```

### 5. Set Up `.bfabricpy.yml` Configuration File

The `.bfabricpy.yml` file is **essential for the power user configuration**. It provides the credentials needed for interacting with the B-Fabric API and is used for functionalities like the logger and API access. Without this file, certain backend features may not work.

Create a `.bfabricpy.yml` file in your home directory (e.g., `~/.bfabricpy.yml`) and format it as follows:

**Example `.bfabricpy.yml`**:
   ```yaml
   GENERAL:
     default_config: PRODUCTION

   PRODUCTION:
     login: your_username
     password: your_password
     base_url: https://your-bfabric-api-endpoint
   ```

- **`login`**: The B-Fabric user login.
- **`password`**: The corresponding password for the user.
- **`base_url`**: The base API endpoint for your B-Fabric instance.

Ensure the file is saved in the specified path and accessible by the application.

If you encounter any issues, please refer to the [bfabricPy documentation](https://fgcz.github.io/bfabricPy/) for further guidance.

### 6. Run the Application

Start the development server by running:
   ```sh
   python3 index.py
   ```


### 7. Check It Out

Visit the following URL to see your application in action:
   ```sh
   http://localhost:8050
   ```

## What Is B-Fabric?

B-Fabric is a Laboratory Information Management System (LIMS) used for managing scientific experiments and their associated data in laboratories. It provides a platform for tracking samples, analyzing results, and organizing workflows efficiently. 

For more details, visit the [Bfabric official website](https://fgcz-bfabric.uzh.ch/bfabric/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## What Is BfabricPy?

BfabricPy is a Python library that provides a programmatic interface to interact with the B-Fabric API. It allows developers to integrate B-Fabric functionalities into custom Python applications. This library simplifies tasks like querying samples, uploading results, and interacting with the LIMS programmatically.

BfabricPy is a dependency of this project and is fetched directly from its GitHub repository during installation.

For more details, visit the [bfabricPy official documentation](https://github.com/fgcz/bfabricPy/tree/main).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## What Is Dash?

Dash is a Python framework for building interactive web applications. It combines the power of Plotly for data visualization and Flask for backend support, making it ideal for scientific and analytical dashboards.

For more details, visit the [Dash official documentation](https://dash.plotly.com/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

See the [open issues](https://github.com/GWCustom/bfabric-web-apps/issues) for a full list of planned features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Add feature: YourFeature"
   ```
4. Push to your branch:
   ```sh
   git push origin feature/YourFeature
   ```
5. Open a Pull Request.

### Top contributors:

<a href="https://github.com/GWCustom/bfabric-web-app-template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=GWCustom/bfabric-web-app-template" alt="Top contributors" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## License

Distributed under the MIT License. See `LICENSE` for more details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

GWC GmbH - [GitHub](https://github.com/GWCustom) - [LinkedIn](https://www.linkedin.com/company/gwc-gmbh/posts/?feedView=all)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Acknowledgments

- [Plotly Dash](https://dash.plotly.com/)
- [Flask Framework](https://flask.palletsprojects.com/)
- [Python.org](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/GWCustom/bfabric-web-apps.svg?style=for-the-badge
[contributors-url]: https://github.com/GWCustom/bfabric-web-apps/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/GWCustom/bfabric-web-apps.svg?style=for-the-badge
[forks-url]: https://github.com/GWCustom/bfabric-web-apps/network/members
[stars-shield]: https://img.shields.io/github/stars/GWCustom/bfabric-web-apps.svg?style=for-the-badge
[stars-url]: https://github.com/GWCustom/bfabric-web-apps/stargazers
[issues-shield]: https://img.shields.io/github/issues/GWCustom/bfabric-web-apps.svg?style=for-the-badge
[issues-url]: https://github.com/GWCustom/bfabric-web-apps/issues
[license-shield]: https://img.shields.io/github/license/GWCustom/bfabric-web-apps.svg?style=for-the-badge
[license-url]: https://github.com/GWCustom/bfabric-web-apps/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/gwc-gmbh/posts/?feedView=all
[product-screenshot]: images/screenshot.png
[Python.js]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Dash.js]: https://img.shields.io/badge/dash-20232A?style=for-the-badge&logo=dash&logoColor=61DAFB
[Dash-url]: https://dash.plotly.com/
[Plotly.js]: https://img.shields.io/badge/plotly-563D7C?style=for-the-badge&logo=plotly&logoColor=white
[Plotly-url]: https://plotly.com/
[Flask.js]: https://img.shields.io/badge/flask-0769AD?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/stable/
