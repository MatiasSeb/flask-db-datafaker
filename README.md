<p align="center">
  <h1 align="center">Flask Database Data Faker</h3>

  <p align="center">
     Data faker based on desired fake data for developing ambients.
    <br/>
    <br/>
    <a href="https://github.com/MatiasSeb/flask-db-datafaker"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/MatiasSeb/flask-db-datafaker">View Demo</a>
    .
    <a href="https://github.com/MatiasSeb/flask-db-datafaker/issues">Report Bug</a>
    .
    <a href="https://github.com/MatiasSeb/flask-db-datafaker/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/MatiasSeb/flask-db-datafaker/total) ![Contributors](https://img.shields.io/github/contributors/MatiasSeb/flask-db-datafaker?color=dark-green) ![Forks](https://img.shields.io/github/forks/MatiasSeb/flask-db-datafaker?style=social) ![Stargazers](https://img.shields.io/github/stars/MatiasSeb/flask-db-datafaker?style=social) ![Issues](https://img.shields.io/github/issues/MatiasSeb/flask-db-datafaker) ![License](https://img.shields.io/github/license/MatiasSeb/flask-db-datafaker) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

This app was made based on the premise that i was working in a industrial data visualizer, and i didn't have data to lookup to, while working on the development of it, so i decided to create a fakedata motor (so i don't have to integrate faker to every project), where i can connect to multiple databases and fill them with the necessary data.

Features :

* You can connect to your desired database using the SQLAlchemy db object, so it doesn't have problems connecting to distinct prefix databases (ex: MySQL, and then connecting to a MSSQL db.)
* It will reflect the actual state of you chosen database and table to fill with the fake data.
* You can ONLY connect to one database at a time, and the app will start once you chosen the table you want to fill with fake data, and it will stop once you finish or close it.

## Built With

Made with Python Flask, SQLAlchemy (and db prefix connectors), WTForms & JavaScript. Using PipEnv as a environment and package manager.

## Getting Started

First, you'll need Python installed in your OS or System. Thats the only prerequisite.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

PipEnv

```sh
python -m pip install pipenv
```

### Installation

1. Clone the repo in the folder you want to use it, but if you use SQLite i suggest you install or clone it inside your project folder.

```sh
git clone https://github.com/MatiasSeb/flask-db-datafaker.git
```

2. Install the app, and run it within the env from pipenv.
```sh
pipenv shell
pipenv install
flask run
```

## Usage

The app is actually based on the premise that i needed a database datafaker motor to make real-time tests on multiple dashboards with industrial-oriented data, like temperatures, the velocity or the m/s that the wind is hitting a sensor, or RPM that the machines have.

All of this data is supposed to come from a PLC or an industrial tool that gives real-time data streaming to a database, as my use case was it.

The use i want this app to give or be given, is to be used inside development 

## Roadmap

See the [open issues](https://github.com/MatiasSeb/flask-db-datafaker/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/MatiasSeb/flask-db-datafaker/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/MatiasSeb/flask-db-datafaker/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/MatiasSeb/flask-db-datafaker/blob/main/LICENSE.md) for more information.

## Authors

* **Matias Bustos Lagos** - *Software Developer* - [Matias Bustos Lagos](https://github.com/MatiasSeb) - *Project managing and developing.*

## Acknowledgements

* [ShaanCoding](https://github.com/ShaanCoding/) - README Tool
* [Othneil Drew](https://github.com/othneildrew/Best-README-Template) - Readme template for tool
* [ImgShields](https://shields.io/) README Shields and Images
