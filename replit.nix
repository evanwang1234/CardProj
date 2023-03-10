{ pkgs }: {
  deps = [
    pkgs.systemdMinimal
    pkgs.sudo
    pkgs.docker
    pkgs.sqlite.bin
    pkgs.python38Full
    pkgs.postgresql
    pkgs.postgresql
  ];
  env = {
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}
