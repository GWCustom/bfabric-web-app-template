
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
    <img src="https://drive.google.com/uc?export=view&id=1_RekqDx9tOY-4ziZLn7cG9sozMXIhrfE" alt="Logo" width="80" height="50.6">
  </a>

<h3 align="center">B-Fabric Web App Template</h3>

<p align="center">
    Two fully functional template apps to demonstrate the usage of the  
    <a href="https://pypi.org/project/bfabric-web-apps/"><strong>bfabric-web-apps</strong></a> Python library.
    <br />
    <br />
    <a href="https://template-d12.bfabric.org/">View Demo</a>
    ·
    <a href="https://github.com/GWCustom/bfabric-web-app-template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/GWCustom/bfabric-web-app-template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>


> **Version Compatibility Notice**  
> To ensure proper functionality, the `bfabric_web_apps` library and the `bfabric_web_app_template` must have the **same version**.  
> For example, if `bfabric_web_apps` is version `0.1.3`, then `bfabric_web_app_template` must also be `0.1.3`.  
> Please verify and update the versions accordingly before running the application.


<!-- TABLE OF CONTENTS -->
## Table of Contents

- [About The Project](#about-the-project)
  - [Key Features](#Key-Features)
  - [Built With](#built-with)
- [Quickstart & Deployment](#quickstart--deployment)
  - [1. Fork and Clone the Repository](#1-fork-and-clone-the-repository)
  - [2. Set Up a Virtual Environment](#2-set-up-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Set Up .bfabricpy.yml Configuration File](#4-set-up-bfabricpyyml-configuration-file-as-described-in-bfabricpy)
  - [5. Run the Application](#5-run-the-application)
  - [6. Check It Out](#6-check-it-out)
- [What Is B-Fabric?](#what-is-bfabric)
- [What Is BfabricPy?](#what-is-bfabricpy)
- [What Is Dash?](#what-is-dash)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## About The Project

The `bfabric_web_app_template` serves as an example project built using the [`bfabric-web-app`](https://github.com/GWCustom/bfabric-web-apps) Python library. These templates demonstrate how to quickly set up web apps that integrate with the B-Fabric Laboratory Information Management System (LIMS). They provide a starting point for developers to build their custom applications.

We offer **two templates**:

- **Basic Template (`basic_index.py`)**: A minimal setup for simple applications. [`View Demo`](https://small-template-d12.bfabric.org/)
- **Advanced Template (`index.py`)**: A more feature-rich version with additional integrations and functionalities. [`View Demo`](https://template-d12.bfabric.org/)

These templates allow developers to choose the level of complexity that best suits their project needs.


### Key Features:

#### Shared Features:
- **API Connection**: Easily connect to B-Fabric using the `bfabric-web-app` library, including URL parameter handling and authentication management.
- **Preconfigured Template**: Streamlines development with a ready-to-use setup.
- **Dash Integration**: Includes example layouts and callbacks.
- **Logger Example**: Demonstrates logging functionality for tracking application events.

#### Advanced Template Only:
- **Interactive Sidebar**: Features sliders, dropdowns, and inputs for enhanced user interaction.
- **Power User Wrapper**: Provides additional functionality for power users.
- **Sophisticated Layout**: Includes a more advanced app specific layout template.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Python][Python.js]][Python-url]
* [![Dash][Dash.js]][Dash-url]
* [![Plotly][Plotly.js]][Plotly-url]
* [![Flask][Flask.js]][Flask-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Quickstart & Deployment

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


### 4. Set Up `.bfabricpy.yml` Configuration File as Described in [bfabricPy](https://fgcz.github.io/bfabricPy)

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

As mentioned above, if you encounter any issues, please refer to the [bfabricPy documentation](https://fgcz.github.io/bfabricPy/) for further guidance.

### 5. Run the Application

Start the development server by running:
   ```sh
   python3 index.py
   ```


### 6. Check It Out

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

See the [open issues](https://github.com/GWCustom/bfabric-web-app-template/issues) for a full list of planned features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

`bfabric_web_apps` is an open-source project, and therefore any contributions you make are greatly appreciated. If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

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

Distributed under the MIT License. See [`LICENSE`](https://github.com/GWCustom/bfabric-web-app-template/blob/main/LICENSE) for more details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

GWC GmbH - [GitHub](https://github.com/GWCustom) - [LinkedIn](https://www.linkedin.com/company/gwc-gmbh/posts/?feedView=all)  
Griffin White - [GitHub](https://github.com/grawfin) - [LinkedIn](https://www.linkedin.com/in/griffin-white-3aa20918a/)  
Marc Zuber - [GitHub](https://github.com/MarcZuberGWC) - [LinkedIn](https://www.linkedin.com/in/marc-zuber-1161b3305/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Acknowledgments

- [Plotly Dash](https://dash.plotly.com/)
- [Flask Framework](https://flask.palletsprojects.com/)
- [Python.org](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/GWCustom/bfabric-web-app-template.svg?style=for-the-badge
[contributors-url]: https://github.com/GWCustom/bfabric-web-app-template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/GWCustom/bfabric-web-app-template.svg?style=for-the-badge
[forks-url]: https://github.com/GWCustom/bfabric-web-app-template/network/members
[stars-shield]: https://img.shields.io/github/stars/GWCustom/bfabric-web-app-template.svg?style=for-the-badge
[stars-url]: https://github.com/GWCustom/bfabric-web-app-template/stargazers
[issues-shield]: https://img.shields.io/github/issues/GWCustom/bfabric-web-app-template.svg?style=for-the-badge
[issues-url]: https://github.com/GWCustom/bfabric-web-app-template/issues
[license-shield]: https://img.shields.io/github/license/GWCustom/bfabric-web-app-template.svg?style=for-the-badge
[license-url]: https://github.com/GWCustom/bfabric-web-app-template/blob/main/LICENSE
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

