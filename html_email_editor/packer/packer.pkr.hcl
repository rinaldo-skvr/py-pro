packer {
  required_plugins {
    ansible = {
      version = ">= 1.0.0"
      source  = "github.com/hashicorp/ansible"
    }
  }
}

source "file" "orangepi" {
  source_file = "../base_img/Orangepizero2w_1.0.2_ubuntu_jammy_desktop_xfce_linux6.1.31.img"
  destination = "output-image/Orangepizero2w_custom.img"
}

build {
  sources = ["source.file.orangepi"]

  # Note: The file builder only copies the image. To provision inside the image, use a shell script or QEMU.
}
