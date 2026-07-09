# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stripansi
%define go_import_path  github.com/acarl005/stripansi
%define commit_id       5a71ef0e047d9cb3dcdac7c3a46327b6aef99b7b

Name:           go-github-acarl005-stripansi
Version:        0+git20180116.5a71ef0
Release:        %autorelease
Summary:        Go package for removing ANSI escape codes from strings
License:        MIT
URL:            https://github.com/acarl005/stripansi
#!RemoteAsset
Source0:        %{url}/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/acarl005/stripansi) = %{version}

%description
This Go package removes ANSI escape codes from strings.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
