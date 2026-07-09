# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-nix
%define go_import_path  github.com/nix-community/go-nix
%define commit_id       4bdde671e0a1

Name:           go-github-nix-community-go-nix
Version:        0.0.0+git20250101.4bdde67
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        Apache-2.0
URL:            https://github.com/nix-community/go-nix
#!RemoteAsset
Source0:        %{url}/archive/4bdde671e0a1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-4bdde671e0a1

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/nix-community/go-nix) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
