# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-version
%define go_import_path  github.com/bitnami/go-version
%define commit_id       b1f57a8634ef

Name:           go-github-bitnami-go-version
Version:        0.0.0+git20250131.b1f57a8
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        Apache-2.0
URL:            https://github.com/bitnami/go-version
#!RemoteAsset
Source0:        %{url}/archive/b1f57a8634ef.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-b1f57a8634ef

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bitnami/go-version) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
