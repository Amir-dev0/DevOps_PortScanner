variable "proxmox_endpoint" {
  type = string
}
variable "proxmox_username" {
  type        = string
}
variable "proxmox_api_token" {
  type      = string
  sensitive = true
}
variable "proxmox_root_password" {
  type        = string
  sensitive   = true
}
variable proxmox_node {
  type        = string
}

variable "proxmox_hostname" {
  type        = string
  default     = "terraform-test"
}
variable "proxmox_ip_address" {
  type        = string
}
variable "proxmox_gateway" {
  type        = string
}
variable "proxmox_template_file" {
  type        = string
}
variable "proxmox_type_template" {
  type        = string
}
