# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-progress
%define go_import_path  github.com/wagoodman/go-progress
%define commit_id       10176f79b2c0

Name:           go-github-wagoodman-go-progress
Version:        0.0.0+git20260303.10176f7
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        MIT
URL:            https://github.com/wagoodman/go-progress
#!RemoteAsset
Source0:        %{url}/archive/10176f79b2c0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-10176f79b2c0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/wagoodman/go-progress) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
