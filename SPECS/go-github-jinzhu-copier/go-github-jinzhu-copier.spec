# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           copier
%define go_import_path  github.com/jinzhu/copier

Name:           go-github-jinzhu-copier
Version:        0.4.0
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        MIT
URL:            https://github.com/jinzhu/copier
#!RemoteAsset
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/jinzhu/copier) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license License*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
