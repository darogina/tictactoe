# Tic-Tac-Toe (the unbeatable version)

A friendly game of Tic-Tac-Toe with a twist... You can't win! The game is set up such that the computer will always win or force a draw. This script is fully compatible with both python 2 & 3.

**NOTE**: This project is tailored for Fedora 30. Results on different platforms may vary.

## How to play
There are several different ways to start the game. A `Makefile` has been added to make all these ways simpler.

### Python directly (easiest)
Start the application directly from the command line.
#### Requirements
- [python (2 or 3)](https://developer.fedoraproject.org/tech/languages/python/python-installation.html)
- make

```bash
dnf install -y python3 make
python3 tictactoe.py
# OR
make run
```

### RPM
Either build the RPM or use the prebuilt package in the `/dist` directory. Leverages python [setuptools](https://docs.python.org/2.0/dist/creating-rpms.html) to create the spec file and build the RPM.

#### Requirements
- [python (2 or 3)](https://developer.fedoraproject.org/tech/languages/python/python-installation.html)
- make
- rpm
- rpm-build

```bash
dnf install -y python3 make rpm rpm-build
make rpm-install
tictactoe
```

### Container
The game has also been packaged up as a container.  Both Podman and Docker are supported.

#### Requirements
- [python (2 or 3)](https://developer.fedoraproject.org/tech/languages/python/python-installation.html)
- podman
- docker

```bash
dnf install -y python3 make podman
make podman-run
# OR
dnf install -y python3 make docker
make docker-run
```

### Vagrant
A simple Fedora 30 virtual machine can be spun up which is baked with the source code and RPM already installed.

#### Requirements
- [Vagrant](https://developer.fedoraproject.org/tools/vagrant/vagrant-virtualbox.html)
- [VirtualBox](https://www.virtualbox.org/wiki/Linux_Downloads#RPM-basedLinuxdistributions_)

```bash
vagrant up
vagrant ssh -t -c tictactoe
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
