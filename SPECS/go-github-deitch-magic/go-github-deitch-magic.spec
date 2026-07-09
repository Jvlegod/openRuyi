# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           magic
%define go_import_path  github.com/deitch/magic
%define commit_id       1ff89d7342da

Name:           go-github-deitch-magic
Version:        0.0.0+git20230404.1ff89d7
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        Apache-2.0
URL:            https://github.com/deitch/magic
#!RemoteAsset
Source0:        %{url}/archive/1ff89d7342da.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-1ff89d7342da

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/deitch/magic) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
