# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-rustaudit
%define go_import_path  github.com/rust-secure-code/go-rustaudit
%define commit_id       e20ec32e963c

Name:           go-github-rust-secure-code-go-rustaudit
Version:        0.0.0+git20250226.e20ec32
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        MIT
URL:            https://github.com/rust-secure-code/go-rustaudit
#!RemoteAsset
Source0:        %{url}/archive/e20ec32e963c.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-e20ec32e963c

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/rust-secure-code/go-rustaudit) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
