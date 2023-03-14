<!--
*** Template auto-generated
-->

<!-- PROJECT SHIELDS -->
<!-- START templates/header.md -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- END templates/header.md -->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Johansmm/PyRAT-RL">
    <img src="/images/logo.png" alt="Logo">
  </a>

  <h2 align="center"><b> Pyrat Rl </h2></b>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/Johansmm/PyRAT-RL"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Johansmm/PyRAT-RL">View Demo</a>
    ·
    <a href="https://github.com/Johansmm/PyRAT-RL/issues">Report Bug</a>
    ·
    <a href="https://github.com/Johansmm/PyRAT-RL/issues">Request Feature</a>
  </p>
</p>


<!-- START templates/02-table_contents.md -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>
<!-- END templates/02-table_contents.md -->

<!-- ABOUT THE PROJECT -->
## About The Project
<a href="https://github.com/Johansmm/PyRAT-RL"> <img src="/images/screenshot.png"></a>

There are many great README templates available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should element DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have have contributed to expanding this template!

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With
The main frameworks and libraries used in the project.
* [python](https://rasa.com/)
* [networkx](https://networkx.org/)
* [matplotlib](https://matplotlib.org/)
* [opencv](https://opencv.org/)


<!-- GETTING STARTED -->
## Getting Started
Clone the repository as first step:

```sh
git clone https://github.com/Johansmm/PyRAT-RL
```

### Prerequisites
Nothing to do

### Installation
1. Install the list of requirements

```sh
python -m pip install -r requirements.txt
```


<!-- USAGE EXAMPLES -->
## Usage
Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

Another example to use:
```python
from libraries.dynamics import spread_zombie_dynamics as szd
from libraries.dynamics import graph_by_default
import datetime as dt
import tqdm

G = graph_by_default(nodes = 20)
ini_date = dt.datetime(year = 2019, month = 8, day = 18)
dynamic = szd(graph = G, INTIAL_DATE = ini_date)
```


<!-- START templates/06-roadmap.md -->
## Roadmap
See the [open issues](https://github.com/Johansmm/PyRAT-RL/issues) for a list of proposed features (and known issues).
<!-- END templates/06-roadmap.md -->

<!-- START templates/07-contribution.md -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
<!-- END templates/07-contribution.md -->

<!-- START templates/08-license.md -->
## License
Distributed under the MIT License. See [`LICENSE`](https://github.com/Johansmm/PyRAT-RL/blob/main/LICENSE) for more information.
<!-- END templates/08-license.md -->

<!-- START templates/09-contact.md -->
## Contact
**Johan Mejia:** [![LinkedIn][linkedin-shield]][linkedin-url]  [![Email][email-shield]][email-url] [![GitHub][github-shield]][github-url]

**Project Link:** https://github.com/Johansmm/PyRAT-RL
<!-- END templates/09-contact.md -->

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Action dynamic readme](https://github.com/varunsridharan/action-dynamic-readme)
* [Shields](https://shields.io)


<!-- MARKDOWNS AND LINKS -->
<!-- START templates/links.md -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- URLS -->
[contributors-url]: https://github.com/Johansmm/PyRAT-RL/graphs/contributors
[forks-url]: https://github.com/Johansmm/PyRAT-RL/network/members
[stars-url]: https://github.com/Johansmm/PyRAT-RL/stargazers
[issues-url]: https://github.com/Johansmm/PyRAT-RL/issues
[license-url]: https://github.com/Johansmm/PyRAT-RL/blob/main/LICENSE
[linkedin-url]: https://www.linkedin.com/in/Johansmm
[email-url]: mailto:josmejiam@correo.udistrital.edu.co
[github-url]: https://github.com/Johansmm

<!-- Shield -->
[contributors-shield]: https://img.shields.io/github/contributors/Johansmm/PyRAT-RL.svg?style=plastic
[forks-shield]: https://img.shields.io/github/forks/Johansmm/PyRAT-RL.svg?style=plastic
[stars-shield]: https://img.shields.io/github/stars/Johansmm/PyRAT-RL.svg?style=plastic
[issues-shield]: https://img.shields.io/github/issues/Johansmm/PyRAT-RL.svg?style=plastic
[license-shield]: https://img.shields.io/github/license/Johansmm/PyRAT-RL.svg?style=plastic
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-e74c3c.svg?logo=linkedin&style=social
[email-shield]: https://img.shields.io/badge/-Email-e74c3c.svg?logo=gmail&style=social
[github-shield]: https://img.shields.io/badge/-GitHub-e74c3c.svg?logo=github&style=social
<!-- END templates/links.md -->
