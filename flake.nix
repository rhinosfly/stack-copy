{
  description = "My Python CLI tool packaged with Nix";

  inputs = { nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable"; };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux"; # or builtins.currentSystem
      pkgs = import nixpkgs { inherit system; };
      program_name = "stack_copy";
      bin_name = "scp";
      version = "0.0.0";
    in {
      packages.${system}.default = pkgs.python3Packages.buildPythonPackage {
        pname = program_name;
        version = version;
        format = "pyproject";
        src = ./.;

        # Needed for PEP 517/518 projects
        nativeBuildInputs =
          [ pkgs.python3Packages.setuptools pkgs.python3Packages.wheel ];
      };

      # Make it runnable via `nix run github:you/mytool`
      apps.${system}.default = {
        type = "app";
        program = "${self.packages.${system}.default}/bin/${bin_name}";
      };

      # Development shell with your program installed
      devShells.${system}.default =
        pkgs.mkShell { buildInputs = [ self.packages.${system}.default ]; };
    };
}
