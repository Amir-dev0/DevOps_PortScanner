terraform {
  required_providers {
    proxmox = {
      source  = "bpg/proxmox"
      version = "~> 0.90"
    }
  }
}

provider "proxmox" {
  alias    = "root"
  endpoint = var.proxmox_endpoint
  username = var.proxmox_username
  password = var.proxmox_root_password
  insecure = true
}

resource "proxmox_virtual_environment_container" "test" {
  provider = proxmox.root
  node_name = var.proxmox_node
  vm_id     = 136 # Based on my Proxmox server, the number 136 has been assigned.
  features {
    nesting = true
    keyctl  = true
  }

  initialization {
    hostname = var.proxmox_hostname

    ip_config {
      ipv4 {
        address = var.proxmox_ip_address
        gateway = var.proxmox_gateway
      }
    }
  }

  operating_system {
    template_file_id = var.proxmox_template_file
    type             = var.proxmox_type_template
  }

  cpu {
    cores = 1
  }

  memory {
    dedicated = 512
  }

  disk {
    datastore_id = "hdd"
    size         = 8
  }

  network_interface {
    name   = "eth0"
    bridge = "vmbr0"
  }
}