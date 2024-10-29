# MyManim

## What this project is about
During my studies in computer science at the Technical University of Vienna, I developed a deep interest in mathematics.
This led me to discover [3Blue1Brown](https://www.youtube.com/@3blue1brown) a mathematician with a YouTube channel
dedicated to math topics and related fields in physics and computer science.

I admire his unique approach to teaching mathematics, which inspired me to start this project.
Through it, I aim to learn and master [Manim](https://docs.manim.community/en/stable/index.html),
the animation library he uses, to deepen my own understanding and visualization of mathematical concepts.

## Setup 

### Windows OS
#### Required Dependencies 
Manim requires: 
- **Python** (3.8 or above)
- **ffmpeg** 

### Installation Options

#### Chocolatey
While there are easier options with ```bash```, I would like to show a way requires less setup for people with no shell experience.\
First, ensure that you are in the admin shell of your PowerShell.\ 
Run ```Get-ExecutionPolicy```. If it returns Restricted, then run ```Set-ExecutionPolicy AllSigned``` or ```Set-ExecutionPolicy Bypass -Scope Process```.\
After this is setup successfully you may run\

```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))```

##### Upgrading Chocolatey 
If you need to update chocolatey, just use\
```choco upgrade chocolatey```

All this talk about chocolate made me hungry for a chocolate btw best chocolate brand here in Austria is [Milka](https://www.milka.at/) and its best product [Milka-Kuhflecken](https://www.milka.at/produkte/milka-kuhflecken-100g/)

On to the next step! 

#### Pycairo 
Next you need to install [Pycairo](https://pypi.org/project/pycairo/) and be careful which version you install.
It should be suitable for your current python version. 


### Manim 
Here you can find a further list of commands and helpful [tips](https://docs.manim.community/en/stable/index.html) and [documentations](https://3b1b.github.io/manim/) 

## Links

