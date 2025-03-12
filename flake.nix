{
  description = "Python development environment with numpy";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }: flake-utils.lib.eachSystem [
    "x86_64-linux"
  ] (system: let
    pkgs = import nixpkgs { inherit system; };
  in {
    devShell = pkgs.mkShell {
      buildInputs = [
        pkgs.python310
        pkgs.python310Packages.numpy
	pkgs.python310Packages.psycopg2
        pkgs.postgresql  # PostgreSQL development libraries
        pkgs.zlib  # Ensure zlib is included in your environment
      ];

      shellHook = ''
        echo "Welcome to your Python environment with numpy!"
      '';
    };
  });
}

