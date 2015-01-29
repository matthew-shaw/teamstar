VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :shell, :path => 'provision.sh'

  config.vm.network :forwarded_port, host: 27017, guest: 27017
  config.vm.network :forwarded_port, host: 27018, guest: 27018
  config.vm.network :forwarded_port, host: 27019, guest: 27019
  config.vm.network :forwarded_port, host: 28017, guest: 28017
end
