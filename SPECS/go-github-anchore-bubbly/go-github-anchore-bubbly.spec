# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bubbly
%define go_import_path  github.com/anchore/bubbly

Name:           go-github-anchore-bubbly
Version:        0.2.1
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        Apache-2.0
URL:            https://github.com/anchore/bubbly
#!RemoteAsset
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/anchore/bubbly) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
