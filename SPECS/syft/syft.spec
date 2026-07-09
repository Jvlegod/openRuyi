# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           syft
%global go_import_path  github.com/anchore/syft

Name:           syft
Version:        1.46.0
Release:        %autorelease
Summary:        CLI tool for generating a software bill of materials
License:        Apache-2.0
URL:            https://github.com/anchore/syft
#!RemoteAsset:  sha256:5545ff8d797fc14d27ae23608ec271609c9038e1732ec13d4ba8042ef542f0ea
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
# Upstream release archives do not include root vendor/, so keep vendor mode
# until all Go module dependencies are packaged as BuildRequires.
#!RemoteAsset:  sha256:a5c6c409e5930447ae8ae9e5c1d6e1b92c44e855ba0277f8767d249aca96c3ce
Source1:        https://github.com/software-vendor/go-syft-vendor/releases/download/v%{version}/syft-v%{version}-vendor.tar.gz
BuildSystem:    golang

BuildOption(prep):  -n %{name}-%{version}

BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/CycloneDX/cyclonedx-go)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/Masterminds/sprig/v3)
BuildRequires:  go(github.com/OneOfOne/xxhash)
BuildRequires:  go(github.com/acarl005/stripansi)
BuildRequires:  go(github.com/acobaugh/osrelease)
BuildRequires:  go(github.com/adrg/xdg)
BuildRequires:  go(github.com/anchore/bubbly)
BuildRequires:  go(github.com/anchore/clio)
BuildRequires:  go(github.com/anchore/fangs)
BuildRequires:  go(github.com/anchore/go-collections)
BuildRequires:  go(github.com/anchore/go-homedir)
BuildRequires:  go(github.com/anchore/go-logger)
BuildRequires:  go(github.com/anchore/go-macholibre)
BuildRequires:  go(github.com/anchore/go-rpmdb)
BuildRequires:  go(github.com/anchore/go-sync)
BuildRequires:  go(github.com/anchore/go-version)
BuildRequires:  go(github.com/anchore/packageurl-go)
BuildRequires:  go(github.com/anchore/stereoscope)
BuildRequires:  go(github.com/anmitsu/go-shlex)
BuildRequires:  go(github.com/aquasecurity/go-pep440-version)
BuildRequires:  go(github.com/bitnami/go-version)
BuildRequires:  go(github.com/blakesmith/ar)
BuildRequires:  go(github.com/bmatcuk/doublestar/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/charmbracelet/bubbles)
BuildRequires:  go(github.com/charmbracelet/bubbletea)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/dave/jennifer)
BuildRequires:  go(github.com/deitch/magic)
BuildRequires:  go(github.com/diskfs/go-diskfs)
BuildRequires:  go(github.com/distribution/reference)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/elliotchance/phpserialize)
BuildRequires:  go(github.com/facebookincubator/nvdtools)
BuildRequires:  go(github.com/github/go-spdx/v2)
BuildRequires:  go(github.com/gkampitakis/go-snaps)
BuildRequires:  go(github.com/go-git/go-billy/v5)
BuildRequires:  go(github.com/go-git/go-git/v5)
BuildRequires:  go(github.com/go-test/deep)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/goccy/go-yaml)
BuildRequires:  go(github.com/gohugoio/hashstructure)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-containerregistry)
BuildRequires:  go(github.com/google/licensecheck)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gookit/color)
BuildRequires:  go(github.com/gpustack/gguf-parser-go)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-getter)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/hcl/v2)
BuildRequires:  go(github.com/iancoleman/strcase)
BuildRequires:  go(github.com/invopop/jsonschema)
BuildRequires:  go(github.com/jedib0t/go-pretty/v6)
BuildRequires:  go(github.com/jinzhu/copier)
BuildRequires:  go(github.com/kastenhq/goversion)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/mholt/archives)
BuildRequires:  go(github.com/moby/sys/mountinfo)
BuildRequires:  go(github.com/nix-community/go-nix)
BuildRequires:  go(github.com/olekukonko/tablewriter)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/quasilyte/go-ruleguard/dsl)
BuildRequires:  go(github.com/rust-secure-code/go-rustaudit)
BuildRequires:  go(github.com/saintfish/chardet)
BuildRequires:  go(github.com/sanity-io/litter)
BuildRequires:  go(github.com/sassoftware/go-rpmutils)
BuildRequires:  go(github.com/scylladb/go-set)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(github.com/spdx/gordf)
BuildRequires:  go(github.com/spdx/tools-golang)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/ulikunitz/xz)
BuildRequires:  go(github.com/vbatts/go-mtree)
BuildRequires:  go(github.com/vifraa/gopom)
BuildRequires:  go(github.com/wagoodman/go-partybus)
BuildRequires:  go(github.com/wagoodman/go-progress)
BuildRequires:  go(github.com/xeipuuv/gojsonschema)
BuildRequires:  go(github.com/zyedidia/generic)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(modernc.org/sqlite)
BuildRequires:  go(github.com/pb33f/ordered-map/v2)
BuildRequires:  go(github.com/tailscale/hujson)
BuildRequires:  zsh

%description
Syft is a CLI tool and Go library for generating a software bill of materials
from container images and filesystems.

%prep -a
%setup -q -D -T -a 1 -n %{name}-%{version}

%build
export GO111MODULE=on
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
export GOFLAGS="-buildmode=pie -mod=vendor -trimpath -modcacherw"
go build %{go_build_flags_default} \
    -ldflags="-X main.version=%{version} -X main.gitDescription=v%{version}" \
    -o %{_name} ./cmd/syft

%install
install -D -m 0755 %{_name} %{buildroot}%{_bindir}/%{_name}
%{buildroot}%{_bindir}/%{_name} completion bash \
    > %{_name}.bash
%{buildroot}%{_bindir}/%{_name} completion fish \
    > %{_name}.fish
%{buildroot}%{_bindir}/%{_name} completion zsh \
    > _%{_name}
install -D -m 0644 %{_name}.bash %{buildroot}%{bash_completions_dir}/%{_name}
install -D -m 0644 %{_name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{_name}.fish
install -D -m 0644 _%{_name} %{buildroot}%{_datadir}/zsh/site-functions/_%{_name}

%check
export GO111MODULE=on
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
export GOFLAGS="-mod=vendor"
go test %{go_test_flags_default} ./cmd/syft

%files
%license LICENSE
%doc README.md
%{_bindir}/%{_name}
%{bash_completions_dir}/%{_name}
%{_datadir}/fish/vendor_completions.d/%{_name}.fish
%{_datadir}/zsh/site-functions/_%{_name}

%changelog
%autochangelog
