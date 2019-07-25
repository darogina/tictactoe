# -*- mode: ruby -*-
# vi: set ft=ruby :

$motd = <<-'MOTD'
************************************************************
*   _____ _          _____               _____             *
*  /__   (_) ___    /__   \__ _  ___    /__   \___   ___   *
*    / /\/ |/ __|____ / /\/ _` |/ __|____ / /\/ _ \ / _ \  *
*   / /  | | (_|_____/ / | (_| | (_|_____/ / | (_) |  __/  *
*   \/   |_|\___|    \/   \__,_|\___|    \/   \___/ \___|  *
*                                                          *
*             github.com/darogina/tictactoe                *
*                                                          *
* To start the game simply run `tictactoe`                 *
* Source code and other options can be found in /tictactoe *
*                                                          *
************************************************************
MOTD

$setupscript = <<SCRIPT
cat <<'EOF' > /etc/motd
#{$motd}
EOF

dnf --refresh install -y python3 make rpm rpm-build podman
cd /tictactoe
make rpm-install
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "fedora/30-cloud-base"
  config.vm.box_version = "30.20190425.0"
  config.vm.synced_folder ".", "/tictactoe", type: "rsync"

  config.vm.provision "shell", inline: $setupscript

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 2
  end
end
