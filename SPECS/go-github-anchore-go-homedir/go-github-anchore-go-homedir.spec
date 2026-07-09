# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-homedir
%define go_import_path  github.com/anchore/go-homedir

Name:           go-github-anchore-go-homedir
Version:        0.1.1
Release:        %autorelease
Summary:        Go library for detecting user home directories
License:        MIT
URL:            https://github.com/anchore/go-homedir
#!RemoteAsset
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/anchore/go-homedir) = %{version}

%description
Go library for detecting the user's home directory without the use of cgo.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
