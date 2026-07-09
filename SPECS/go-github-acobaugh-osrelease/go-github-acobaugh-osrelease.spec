# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           osrelease
%define go_import_path  github.com/acobaugh/osrelease

Name:           go-github-acobaugh-osrelease
Version:        0.1.0
Release:        %autorelease
Summary:        Go package for reading os-release files
License:        BSD-3-Clause
URL:            https://github.com/acobaugh/osrelease
#!RemoteAsset
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/acobaugh/osrelease) = %{version}

%description
A Go package to make reading os-release files easy.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
