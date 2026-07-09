# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ar
%define go_import_path  github.com/blakesmith/ar
%define commit_id       809d4375e1fb4a5a860357fe7f06d00ca8236f3e

Name:           go-github-blakesmith-ar
Version:        0+git20190502.809d437
Release:        %autorelease
Summary:        Go library for reading and writing ar archives
License:        MIT
URL:            https://github.com/blakesmith/ar
#!RemoteAsset
Source0:        %{url}/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/blakesmith/ar) = %{version}

%description
This is a simple library for reading and writing ar files in common format.

%files
%license COPYING
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
