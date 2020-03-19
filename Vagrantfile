# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'libvirt'

Vagrant.configure("2") do |config|

  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
  
  Vagrant.configure("2") do |config|
    config.vm.define :test_vm do |test_vm|
      test_vm.vm.box = "debian/stretch64"
    end
  end


  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  #config.vm.define :whonix_vm do |whonix_vm|
  #  whonix_vm.vm.box =  "debian/jessie64"
  #  whonix_vm.machine_type =  "debian/jessie64"
  #  whonix_vm.machine_arch =  "x86_64"
  #end
  #
  #config.vm.provider :libvirt do |domain|
  #  domain.default_prefix = config.vm.box
  #  domain.driver = 'kvm'
  #  domain.management_network_guest_ipv6 = 'no'
  #  domain.connect_via_ssh = false
  #  domain.machine_arch = 'x86_64'
  #  if ENV['TAILS_BUILD_MACHINE_TYPE']
  #    domain.machine_type = ENV['TAILS_BUILD_MACHINE_TYPE']
  #  else
  #    domain.machine_type = 'q35'
  #  end
  #  if ENV['TAILS_BUILD_CPU_MODEL']
  #    domain.cpu_mode  = 'custom'
  #    domain.cpu_model = ENV['TAILS_BUILD_CPU_MODEL']
  #  else
  #    domain.cpu_mode = 'host-passthrough'
  #  end
  #  domain.emulator_path = '/usr/bin/qemu-system-x86_64'
  #  domain.memory = ENV['TAILS_RAM_BUILD'] ? VM_MEMORY_FOR_RAM_BUILDS :
  #                                           VM_MEMORY_FOR_DISK_BUILDS
  #  cpus = ENV['TAILS_BUILD_CPUS']
  #  domain.cpus = cpus unless cpus.nil?
  #  if ENV['TAILS_PROXY_TYPE' ] == 'vmproxy'
  #    domain.storage(
  #      :file, size: '15G', allow_existing: true,
  #      path: 'apt-cacher-ng-data.qcow2'
  #    )
  #  end
  #  if ENV['TAILS_WEBSITE_CACHE' ] == '1'
  #    domain.storage(
  #      :file, size: '5G', allow_existing: true,
  #      path: 'tails-website-cache.qcow2'
  #    )
  #  end
  #end
  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false
  
  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  
  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  
  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"
   
  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"
  
  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"
  
  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.
   
  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end
