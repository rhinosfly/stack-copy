{
  description = "My Python CLI tool packaged with Nix";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux"; # or builtins.currentSystem
      pkgs = import nixpkgs { inherit system; };
    in {
      packages.${system}.default = pkgs.python3Packages.buildPythonPackage {
        pname = "mytool";
        version = "0.1.0";
        format = "pyproject";
        src = ./.;

        # Needed for PEP 517/518 projects
        nativeBuildInputs = [
          pkgs.python3Packages.setuptools
          pkgs.python3Packages.wheel
        ];
      };

      # Make it runnable via `nix run github:you/mytool`
      apps.${system}.default = {
        type = "app";
        program = "${self.packages.${system}.default}/bin/mytool";
      };
    };
}
