# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           chardet
%define go_import_path  github.com/saintfish/chardet
%define commit_id       5e3ef4b5456d

Name:           go-github-saintfish-chardet
Version:        0.0.0+git20230101.5e3ef4b
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        MIT
URL:            https://github.com/saintfish/chardet
#!RemoteAsset
Source0:        %{url}/archive/5e3ef4b5456d.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-5e3ef4b5456d

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/saintfish/chardet) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
