# atlas-live-codes
Danielle's public repository of live codes at Atlas School

## Description
Each immediate subdirectory contains a live code with its own `README` with additional context for the code, compilation instructions, usage examples, etc.

## General Usage (Students)
This repository has a dev container defined in `.devcontainer/devcontainer.json`. To avoid the portability hassles with the lower-level languages (i.e., running on Windows, MacOS, a Linux distro, etc.), I recommend working with the examples locally via VSCode with the `Dev Containers` extension installed. (You may need to install Docker Engine on your system first...consult Docker docs for installation on your OS.)

### Setup/Use Dev Containers (VSCode)
- Install VSCode on your machine
    - Inside VSCode, find the `Extensions` tab on the left and search for "dev containers"
    - Install the official `Dev Containers` extension
- Clone this repository in your terminal
- Open the root folder of the repository in VSCode
    - If you have `Dev Containers` installed, it should prompt you with something like "Folder contains a Dev Container configuration file. Reopen folder to develop in a container."
    - Click `Reopen in Container`
    - VSCode will then reopen inside the dev container

## Live Codes in this Repository

### `c-signal-handling/`
Contains examples of working with the `signal` and `sigaction` system calls in C (GNU libc/Linux)

### `red-black-trees/`
Contains an example of implementing a Red-Black tree in Python. Includes code to generate diagrams of the current state of the tree using the `graphviz` package.

